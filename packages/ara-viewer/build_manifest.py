#!/usr/bin/env python3
"""
build_manifest.py — Parse an ARA directory into manifest.json for the viewer.

Usage:
    python3 build_manifest.py <path-to-ara-dir>

Writes <ara-dir>/manifest.json with:
    { meta: {...}, nodes: [...], edges: [...] }

Recognized node kinds and provenance:
    paper       — PAPER.md root
    observation — logic/problem.md  O01..On
    claim       — logic/claims.md   C01..Cn
    experiment  — logic/experiments.md  E01..En
    concept     — logic/concepts.md  (## headings)
    heuristic   — logic/solution/heuristics.md  H01..Hn
    related     — logic/related_work.md  RW01..RWn
    solution    — logic/solution/{architecture,algorithm,constraints}.md
    trace_node  — trace/exploration_tree.yaml  N01..Nn (question/experiment/decision/dead_end/pivot)
    code        — src/**/*.py / *.md
    figure      — evidence/figures/*.md
    table       — evidence/tables/*.md

Edge kinds:
    proves          claim  → experiment   (claim.Proof: [E..])
    verifies        experiment → claim    (experiment.Verifies: C..)
    depends_on      X → Y                 (claim/experiment Dependencies)
    implements      heuristic → code      (heuristic.Code ref)
    references      claim/exp → figure|table  (mentioned in Evidence basis)
    affects         related → claim       (RW.Claims affected)
    layer           paper → layer-root, layer-root → node
    trace_edge      trace_node → trace_node (parent → child in DAG)
    trace_evidence  trace_node → claim/figure (cited in trace node evidence)
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

LAYER_COGNITIVE = "cognitive"
LAYER_PHYSICAL = "physical"
LAYER_EVIDENCE = "evidence"
LAYER_TRACE = "trace"
LAYER_ROOT = "root"


# ---------- generic helpers ----------

def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Very small YAML-ish frontmatter parser (top-level keys + list items)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    raw = text[3:end].strip("\n")
    body = text[end + 4 :].lstrip("\n")
    meta: dict[str, Any] = {}
    cur_key = None
    cur_list: list[str] | None = None
    cur_block: list[str] | None = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if cur_block is not None and (line.startswith("  ") or not line.strip().endswith(":")):
            if line.startswith("  "):
                cur_block.append(line.strip())
                continue
            else:
                meta[cur_key] = " ".join(cur_block).strip()
                cur_block = None
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m and not line.startswith(" "):
            if cur_list is not None:
                meta[cur_key] = cur_list
                cur_list = None
            cur_key, val = m.group(1), m.group(2).strip()
            if val == "" or val == "|" or val == ">":
                cur_block = []
                continue
            if val.startswith("[") or val.startswith("{"):
                try:
                    meta[cur_key] = json.loads(val.replace("'", '"'))
                except Exception:
                    meta[cur_key] = val
            else:
                meta[cur_key] = val.strip('"').strip("'")
        elif line.startswith("  - "):
            if cur_list is None:
                cur_list = []
            cur_list.append(line[4:].strip().strip('"').strip("'"))
    if cur_list is not None:
        meta[cur_key] = cur_list
    if cur_block is not None:
        meta[cur_key] = " ".join(cur_block).strip()
    return meta, body


def split_sections(body: str, level: int = 2) -> list[tuple[str, str]]:
    """Split a markdown body into (heading, content) tuples at the given heading level."""
    prefix = "#" * level + " "
    out = []
    cur_h = None
    cur_lines: list[str] = []
    for line in body.splitlines():
        if line.startswith(prefix) and not line.startswith("#" * (level + 1)):
            if cur_h is not None:
                out.append((cur_h, "\n".join(cur_lines).strip()))
            cur_h = line[len(prefix):].strip()
            cur_lines = []
        else:
            cur_lines.append(line)
    if cur_h is not None:
        out.append((cur_h, "\n".join(cur_lines).strip()))
    return out


def field(section: str, name: str) -> str:
    """Pull '**Name**: value' (single line or first line of multi-line)."""
    m = re.search(rf"\*\*{re.escape(name)}\*\*:\s*(.+)", section)
    return m.group(1).strip() if m else ""


def split_ids(text: str, pattern: str) -> list[str]:
    return re.findall(pattern, text)


def find_figures(text: str) -> list[str]:
    """Find 'Figure N' or 'Figure Na' references."""
    return list(dict.fromkeys(re.findall(r"Figure\s+(\d+[a-z]?)", text)))


def find_tables(text: str) -> list[str]:
    return list(dict.fromkeys(re.findall(r"Table\s+(\d+)", text)))


# ---------- exploration tree YAML (lightweight) ----------

def parse_exploration_tree(text: str) -> list[dict]:
    """Parse the limited YAML schema used by exploration_tree.yaml.

    Returns a flat list of node dicts with parent-id pre-computed.
    """
    nodes: list[dict] = []
    # Stack of (indent, id) for the current ancestor chain.
    stack: list[tuple[int, str]] = []
    cur: dict | None = None
    cur_indent = 0
    cur_key: str | None = None
    cur_block: list[str] | None = None

    def flush_block():
        nonlocal cur_block, cur_key
        if cur is not None and cur_key and cur_block is not None:
            cur[cur_key] = " ".join(s.strip() for s in cur_block).strip()
        cur_block = None
        cur_key = None

    def close_cur():
        nonlocal cur
        if cur is not None:
            nodes.append(cur)
            cur = None

    for raw in text.splitlines():
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        line = raw.strip()
        # New tree node
        m = re.match(r"-\s+id:\s*(\S+)", line)
        if m:
            flush_block()
            close_cur()
            # Pop ancestors with indent >= this list item's indent
            while stack and stack[-1][0] >= indent:
                stack.pop()
            parent = stack[-1][1] if stack else None
            cur = {"id": m.group(1), "parent": parent, "children_ids": []}
            cur_indent = indent
            # Register as child of parent later (after node is fully built).
            stack.append((indent, cur["id"]))
            continue
        # Within a node
        if cur is None:
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            flush_block()
            key, val = m.group(1), m.group(2)
            if val == "" or val == ">" or val == "|":
                cur_key = key
                cur_block = []
            elif val.startswith("["):
                try:
                    cur[key] = json.loads(val.replace("'", '"'))
                except Exception:
                    cur[key] = val
            else:
                cur[key] = val.strip().strip('"').strip("'")
            continue
        if line.startswith("- "):
            # list item under current key
            if cur_key not in cur:
                cur[cur_key] = []
            if not isinstance(cur.get(cur_key), list):
                cur[cur_key] = []
            cur[cur_key].append(line[2:].strip().strip('"').strip("'"))
            cur_block = None
            continue
        if cur_block is not None:
            cur_block.append(line)
    flush_block()
    close_cur()

    # Wire children
    by_id = {n["id"]: n for n in nodes}
    for n in nodes:
        if n.get("parent") and n["parent"] in by_id:
            by_id[n["parent"]]["children_ids"].append(n["id"])
    return nodes


# ---------- builder ----------

def build(ara_root: Path) -> dict:
    nodes: list[dict] = []
    edges: list[dict] = []
    seen: set[str] = set()

    def add_node(node: dict):
        if node["id"] in seen:
            return
        seen.add(node["id"])
        nodes.append(node)

    def add_edge(source: str, target: str, kind: str):
        if source == target:
            return
        edges.append({"source": source, "target": target, "kind": kind})

    # --- PAPER.md
    paper_text = read(ara_root / "PAPER.md")
    meta, _ = parse_frontmatter(paper_text)
    title = meta.get("title", ara_root.name)
    add_node({
        "id": "PAPER",
        "kind": "paper",
        "layer": LAYER_ROOT,
        "label": title,
        "file": "PAPER.md",
        "summary": meta.get("abstract", "")[:400],
    })
    # Layer root nodes
    for layer in (LAYER_COGNITIVE, LAYER_PHYSICAL, LAYER_TRACE, LAYER_EVIDENCE):
        add_node({
            "id": f"layer:{layer}",
            "kind": "layer",
            "layer": layer,
            "label": layer.capitalize(),
            "file": None,
            "summary": f"{layer} layer",
        })
        add_edge("PAPER", f"layer:{layer}", "layer")

    # --- logic/problem.md observations
    problem_text = read(ara_root / "logic/problem.md")
    for h, body in split_sections(problem_text, level=3):
        m = re.match(r"^(O\d+):\s*(.+)$", h)
        if not m:
            continue
        oid, title_ = m.group(1), m.group(2)
        add_node({
            "id": oid,
            "kind": "observation",
            "layer": LAYER_COGNITIVE,
            "label": f"{oid}: {title_}",
            "file": "logic/problem.md",
            "summary": field(body, "Statement")[:240],
        })
        add_edge(f"layer:{LAYER_COGNITIVE}", oid, "contains")

    # --- logic/claims.md
    claims_text = read(ara_root / "logic/claims.md")
    for h, body in split_sections(claims_text, level=2):
        m = re.match(r"^(C\d+):\s*(.+)$", h)
        if not m:
            continue
        cid, title_ = m.group(1), m.group(2)
        add_node({
            "id": cid,
            "kind": "claim",
            "layer": LAYER_COGNITIVE,
            "label": f"{cid}: {title_}",
            "file": "logic/claims.md",
            "summary": field(body, "Statement")[:240],
            "status": field(body, "Status"),
        })
        add_edge(f"layer:{LAYER_COGNITIVE}", cid, "contains")
        # proofs
        for eid in split_ids(field(body, "Proof"), r"E\d+"):
            add_edge(cid, eid, "proves")
        # dependencies
        for dep in split_ids(field(body, "Dependencies"), r"C\d+"):
            add_edge(cid, dep, "depends_on")
        # figure/table references from Evidence basis
        ev = field(body, "Evidence basis")
        for fnum in find_figures(ev):
            add_edge(cid, f"Fig{fnum}", "references")
        for tnum in find_tables(ev):
            add_edge(cid, f"Tab{tnum}", "references")

    # --- logic/experiments.md
    exp_text = read(ara_root / "logic/experiments.md")
    for h, body in split_sections(exp_text, level=2):
        m = re.match(r"^(E\d+):\s*(.+)$", h)
        if not m:
            continue
        eid, title_ = m.group(1), m.group(2)
        add_node({
            "id": eid,
            "kind": "experiment",
            "layer": LAYER_COGNITIVE,
            "label": f"{eid}: {title_}",
            "file": "logic/experiments.md",
            "summary": " ".join(body.split())[:240],
        })
        add_edge(f"layer:{LAYER_COGNITIVE}", eid, "contains")
        for cid in split_ids(field(body, "Verifies"), r"C\d+"):
            add_edge(eid, cid, "verifies")
        for dep in split_ids(field(body, "Dependencies"), r"E\d+"):
            add_edge(eid, dep, "depends_on")
        # Figures the experiment produces
        for fnum in find_figures(body):
            add_edge(eid, f"Fig{fnum}", "references")
        for tnum in find_tables(body):
            add_edge(eid, f"Tab{tnum}", "references")

    # --- logic/concepts.md (## headings, no ID prefix)
    concepts_text = read(ara_root / "logic/concepts.md")
    for h, body in split_sections(concepts_text, level=2):
        cid = "Concept:" + re.sub(r"\s+", "_", h.split("(")[0].strip())[:40]
        add_node({
            "id": cid,
            "kind": "concept",
            "layer": LAYER_COGNITIVE,
            "label": h,
            "file": "logic/concepts.md",
            "summary": field(body, "Definition")[:240],
        })
        add_edge(f"layer:{LAYER_COGNITIVE}", cid, "contains")

    # --- logic/solution/heuristics.md
    heur_text = read(ara_root / "logic/solution/heuristics.md")
    for h, body in split_sections(heur_text, level=2):
        m = re.match(r"^(H\d+):\s*(.+)$", h)
        if not m:
            continue
        hid, title_ = m.group(1), m.group(2)
        add_node({
            "id": hid,
            "kind": "heuristic",
            "layer": LAYER_COGNITIVE,
            "label": f"{hid}: {title_}",
            "file": "logic/solution/heuristics.md",
            "summary": field(body, "Rationale")[:240],
        })
        add_edge(f"layer:{LAYER_COGNITIVE}", hid, "contains")
        # Code ref
        coderef = field(body, "Code ref")
        for path in re.findall(r"\[([^\]]+)\]", coderef):
            # normalize: drop "src/" prefix to compare with code node ids
            code_id = "Code:" + path
            add_edge(hid, code_id, "implements")

    # --- logic/solution/*.md (architecture, algorithm, constraints)
    for fn in ("architecture", "algorithm", "constraints"):
        fp = ara_root / f"logic/solution/{fn}.md"
        if fp.exists():
            nid = f"Sol:{fn}"
            add_node({
                "id": nid,
                "kind": "solution",
                "layer": LAYER_COGNITIVE,
                "label": fn.capitalize(),
                "file": f"logic/solution/{fn}.md",
                "summary": " ".join(fp.read_text(encoding="utf-8").split())[:240],
            })
            add_edge(f"layer:{LAYER_COGNITIVE}", nid, "contains")

    # --- logic/related_work.md
    rw_text = read(ara_root / "logic/related_work.md")
    for h, body in split_sections(rw_text, level=2):
        m = re.match(r"^(RW\d+):\s*(.+)$", h)
        if not m:
            continue
        rid, title_ = m.group(1), m.group(2)
        add_node({
            "id": rid,
            "kind": "related",
            "layer": LAYER_COGNITIVE,
            "label": f"{rid}: {title_}",
            "file": "logic/related_work.md",
            "summary": title_,
        })
        add_edge(f"layer:{LAYER_COGNITIVE}", rid, "contains")
        for cid in split_ids(field(body, "Claims affected"), r"C\d+"):
            add_edge(rid, cid, "affects")

    # --- src/ code files
    src_dir = ara_root / "src"
    if src_dir.exists():
        for fp in sorted(src_dir.rglob("*")):
            if fp.is_dir() or fp.name.startswith("."):
                continue
            rel = fp.relative_to(ara_root).as_posix()
            nid = "Code:" + rel
            kind = "code" if fp.suffix == ".py" else "config"
            add_node({
                "id": nid,
                "kind": kind,
                "layer": LAYER_PHYSICAL,
                "label": rel.replace("src/", ""),
                "file": rel,
                "summary": fp.name,
            })
            add_edge(f"layer:{LAYER_PHYSICAL}", nid, "contains")

    # --- evidence/figures and evidence/tables
    fig_dir = ara_root / "evidence/figures"
    if fig_dir.exists():
        for fp in sorted(fig_dir.glob("*.md")):
            m = re.search(r"figure(\d+[a-z]?)", fp.stem, re.I)
            fid = f"Fig{m.group(1)}" if m else f"Fig:{fp.stem}"
            rel = fp.relative_to(ara_root).as_posix()
            # First non-blank line as label.
            text = fp.read_text(encoding="utf-8")
            label = next((l.lstrip("# ").strip() for l in text.splitlines() if l.strip()), fp.stem)
            add_node({
                "id": fid,
                "kind": "figure",
                "layer": LAYER_EVIDENCE,
                "label": label,
                "file": rel,
                "summary": label,
            })
            add_edge(f"layer:{LAYER_EVIDENCE}", fid, "contains")
    tbl_dir = ara_root / "evidence/tables"
    if tbl_dir.exists():
        for fp in sorted(tbl_dir.glob("*.md")):
            m = re.search(r"table(\d+)", fp.stem, re.I)
            tid = f"Tab{m.group(1)}" if m else f"Tab:{fp.stem}"
            rel = fp.relative_to(ara_root).as_posix()
            text = fp.read_text(encoding="utf-8")
            label = next((l.lstrip("# ").strip() for l in text.splitlines() if l.strip()), fp.stem)
            add_node({
                "id": tid,
                "kind": "table",
                "layer": LAYER_EVIDENCE,
                "label": label,
                "file": rel,
                "summary": label,
            })
            add_edge(f"layer:{LAYER_EVIDENCE}", tid, "contains")

    # --- trace/exploration_tree.yaml
    trace_path = ara_root / "trace/exploration_tree.yaml"
    if trace_path.exists():
        tnodes = parse_exploration_tree(read(trace_path))
        for tn in tnodes:
            nid = tn["id"]
            kind_tn = tn.get("type", "question")
            add_node({
                "id": nid,
                "kind": "trace_" + kind_tn,
                "layer": LAYER_TRACE,
                "label": f"{nid}: {tn.get('title', '')}",
                "file": "trace/exploration_tree.yaml",
                "summary": (tn.get("description") or tn.get("result") or tn.get("choice")
                            or tn.get("hypothesis") or tn.get("failure_mode") or "")[:240],
            })
            add_edge(f"layer:{LAYER_TRACE}", nid, "contains")
            if tn.get("parent"):
                add_edge(tn["parent"], nid, "trace_edge")
            # evidence references — link trace node to claims/figures it cites
            ev = tn.get("evidence")
            ev_text = " ".join(ev) if isinstance(ev, list) else str(ev or "")
            for cid in re.findall(r"C\d+", ev_text):
                add_edge(nid, cid, "trace_evidence")
            for fnum in find_figures(ev_text):
                add_edge(nid, f"Fig{fnum}", "trace_evidence")

    # Drop edges whose endpoints don't exist (e.g. unresolved Code: paths).
    edges_clean = [e for e in edges if e["source"] in seen and e["target"] in seen]

    return {
        "meta": {
            "title": title,
            "ara_dir": ara_root.name,
            "authors": meta.get("authors", []),
            "venue": meta.get("venue", ""),
            "year": meta.get("year", ""),
            "abstract": meta.get("abstract", ""),
            "claims_summary": meta.get("claims_summary", []),
        },
        "nodes": nodes,
        "edges": edges_clean,
    }


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    ara_root = Path(sys.argv[1]).resolve()
    if not (ara_root / "PAPER.md").exists():
        print(f"error: {ara_root}/PAPER.md not found", file=sys.stderr)
        sys.exit(2)
    manifest = build(ara_root)
    out = ara_root / "manifest.json"
    out.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    n_nodes = len(manifest["nodes"])
    n_edges = len(manifest["edges"])
    print(f"wrote {out} ({n_nodes} nodes, {n_edges} edges)")


if __name__ == "__main__":
    main()
