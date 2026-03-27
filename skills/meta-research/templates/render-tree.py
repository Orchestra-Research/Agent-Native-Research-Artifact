#!/usr/bin/env python3
"""
render-tree.py — Render research-tree.yaml + research-log.md into an interactive HTML dashboard.

Usage:
    python render-tree.py [project_dir] [--output FILE] [--open]

    project_dir   Directory containing research-tree.yaml and research-log.md (default: cwd)
    --output FILE Output HTML path (default: project_dir/research-tree.html)
    --open        Open the rendered HTML in the default browser

No external dependencies required. Uses PyYAML if available, falls back to built-in parser.

Examples:
    python render-tree.py .
    python render-tree.py /path/to/project --open
    python render-tree.py . --output /tmp/tree.html --open
"""

import json
import os
import re
import sys
import webbrowser


# ── YAML loading (PyYAML if available, otherwise built-in subprocess to parse via
#    a simple line-based approach) ───────────────────────────────────────────────

def _load_yaml(path):
    """Load a YAML file, trying PyYAML first, falling back to subprocess + json."""
    try:
        import yaml
        with open(path, "r") as f:
            return yaml.safe_load(f) or {}
    except ImportError:
        pass

    # Fallback: use ruby if available (macOS ships ruby with YAML support)
    import subprocess
    for cmd in [
        ["ruby", "-ryaml", "-rjson", "-e", f"puts JSON.generate(YAML.load_file('{path}'))"],
        ["python3", "-c", f"import yaml,json,sys; print(json.dumps(yaml.safe_load(open('{path}'))))"],
    ]:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode == 0 and result.stdout.strip():
                return json.loads(result.stdout.strip())
        except (FileNotFoundError, subprocess.TimeoutExpired, json.JSONDecodeError):
            continue

    # Last resort: minimal line-based YAML parser for the research-tree structure
    return _minimal_yaml_parse(path)


def _minimal_yaml_parse(path):
    """
    Minimal YAML parser sufficient for research-tree.yaml.
    Handles: scalars, lists, nested dicts, quoted strings, booleans, nulls, numbers.
    Does NOT handle: anchors, aliases, multi-line strings, flow mappings, complex keys.
    """
    with open(path, "r") as f:
        lines = f.readlines()

    # Remove comment-only lines and blank lines at start, strip trailing whitespace
    cleaned = []
    for line in lines:
        stripped = line.rstrip()
        # Skip full-line comments and empty lines
        if not stripped or stripped.lstrip().startswith("#"):
            continue
        # Remove inline comments (not inside quotes)
        no_comment = re.sub(r'\s+#[^"\']*$', '', stripped)
        cleaned.append(no_comment)

    if not cleaned:
        return {}

    return _parse_block(cleaned, 0, 0)[0]


def _parse_value(raw):
    """Parse a scalar YAML value."""
    s = raw.strip()
    if not s or s == "~" or s.lower() == "null":
        return None
    if s.lower() == "true":
        return True
    if s.lower() == "false":
        return False
    # Quoted string
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    # Number
    try:
        if "." in s:
            return float(s)
        return int(s)
    except ValueError:
        pass
    # Flow sequence: [a, b, c]
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        if not inner:
            return []
        items = [_parse_value(x) for x in _split_flow(inner)]
        return items
    # Flow mapping: {a: b, c: d}
    if s.startswith("{") and s.endswith("}"):
        inner = s[1:-1].strip()
        if not inner:
            return {}
        result = {}
        for pair in _split_flow(inner):
            if ":" in pair:
                k, v = pair.split(":", 1)
                result[k.strip()] = _parse_value(v)
        return result
    return s


def _split_flow(s):
    """Split comma-separated flow values, respecting brackets."""
    items = []
    depth = 0
    current = ""
    for ch in s:
        if ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
        if ch == "," and depth == 0:
            items.append(current)
            current = ""
        else:
            current += ch
    if current.strip():
        items.append(current)
    return items


def _get_indent(line):
    """Return the number of leading spaces."""
    return len(line) - len(line.lstrip())


def _parse_block(lines, start, base_indent):
    """Parse a YAML block starting at `start` with `base_indent`. Returns (value, next_index)."""
    if start >= len(lines):
        return None, start

    result = {}
    i = start

    while i < len(lines):
        line = lines[i]
        indent = _get_indent(line)

        # Stop if we've de-indented past our block
        if indent < base_indent:
            break

        stripped = line.lstrip()

        # List item
        if stripped.startswith("- "):
            # We're in a list context — collect all items at this indent
            lst, i = _parse_list(lines, i, indent)
            return lst, i

        # Key-value pair
        if ":" in stripped:
            colon_pos = stripped.index(":")
            key = stripped[:colon_pos].strip()
            rest = stripped[colon_pos + 1:].strip()

            if rest:
                # Inline value
                result[key] = _parse_value(rest)
                i += 1
            else:
                # Block value — check next line indent
                if i + 1 < len(lines):
                    next_indent = _get_indent(lines[i + 1])
                    if next_indent > indent:
                        val, i = _parse_block(lines, i + 1, next_indent)
                        result[key] = val
                    else:
                        result[key] = None
                        i += 1
                else:
                    result[key] = None
                    i += 1
        else:
            i += 1

    return result, i


def _parse_list(lines, start, base_indent):
    """Parse a YAML list starting at `start`."""
    items = []
    i = start

    while i < len(lines):
        line = lines[i]
        indent = _get_indent(line)
        stripped = line.lstrip()

        if indent < base_indent:
            break
        if indent > base_indent and not stripped.startswith("- "):
            # Continuation of previous item (nested content)
            # Find the nested block
            val, i = _parse_block(lines, i, indent)
            if items and isinstance(items[-1], dict):
                items[-1].update(val if isinstance(val, dict) else {})
            continue

        if not stripped.startswith("- "):
            break

        # Strip the "- " prefix
        content = stripped[2:].strip()

        if ":" in content:
            # Dict item in list: - key: value
            colon_pos = content.index(":")
            key = content[:colon_pos].strip()
            rest = content[colon_pos + 1:].strip()

            item = {}
            if rest:
                item[key] = _parse_value(rest)
            else:
                if i + 1 < len(lines) and _get_indent(lines[i + 1]) > indent:
                    val, next_i = _parse_block(lines, i + 1, _get_indent(lines[i + 1]))
                    item[key] = val
                    # Collect remaining keys at the deeper indent
                    i = next_i
                    # Check if there are sibling keys at the list-item indent + 2
                    while i < len(lines) and _get_indent(lines[i]) > indent:
                        sub_stripped = lines[i].lstrip()
                        if ":" in sub_stripped:
                            sub_colon = sub_stripped.index(":")
                            sub_key = sub_stripped[:sub_colon].strip()
                            sub_rest = sub_stripped[sub_colon + 1:].strip()
                            sub_indent = _get_indent(lines[i])
                            if sub_rest:
                                item[sub_key] = _parse_value(sub_rest)
                                i += 1
                            else:
                                if i + 1 < len(lines) and _get_indent(lines[i + 1]) > sub_indent:
                                    val, i = _parse_block(lines, i + 1, _get_indent(lines[i + 1]))
                                    item[sub_key] = val
                                else:
                                    item[sub_key] = None
                                    i += 1
                        else:
                            i += 1
                    items.append(item)
                    continue
                else:
                    item[key] = None

            i += 1
            # Collect remaining keys for this dict item (indented deeper than the dash)
            while i < len(lines) and _get_indent(lines[i]) > indent:
                sub_stripped = lines[i].lstrip()
                if sub_stripped.startswith("- "):
                    break
                if ":" in sub_stripped:
                    sub_colon = sub_stripped.index(":")
                    sub_key = sub_stripped[:sub_colon].strip()
                    sub_rest = sub_stripped[sub_colon + 1:].strip()
                    sub_indent = _get_indent(lines[i])
                    if sub_rest:
                        item[sub_key] = _parse_value(sub_rest)
                        i += 1
                    else:
                        if i + 1 < len(lines) and _get_indent(lines[i + 1]) > sub_indent:
                            val, i = _parse_block(lines, i + 1, _get_indent(lines[i + 1]))
                            item[sub_key] = val
                        else:
                            item[sub_key] = None
                            i += 1
                else:
                    i += 1
            items.append(item)
        else:
            # Simple scalar list item: - value
            items.append(_parse_value(content))
            i += 1

    return items, i


# ── Log parsing ────────────────────────────────────────────────────────────────

def parse_research_log(log_path):
    """Parse research-log.md table into a list of entry dicts."""
    entries = []
    if not os.path.exists(log_path):
        return entries

    with open(log_path, "r") as f:
        lines = f.readlines()

    in_table = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("| #") or stripped.startswith("| ---"):
            in_table = True
            continue
        if in_table and stripped.startswith("|"):
            cols = [c.strip() for c in stripped.split("|")]
            cols = [c for c in cols if c]
            if len(cols) >= 4:
                entries.append({
                    "num": cols[0],
                    "date": cols[1],
                    "phase": cols[2],
                    "summary": cols[3],
                })
        elif in_table and not stripped.startswith("|"):
            in_table = False

    return entries


# ── Phase inference ────────────────────────────────────────────────────────────

def infer_current_phase(tree_data, log_entries):
    """Infer the current research phase from tree data and log entries."""
    hyps = tree_data.get("hypotheses") or []
    field = tree_data.get("field_understanding") or {}

    if log_entries:
        last_phase = log_entries[-1].get("phase", "").lower().replace(" ", "_")
        phase_map = {
            "literature_survey": "literature_survey",
            "literature_survey": "literature_survey",
            "lit_survey": "literature_survey",
            "hypothesis_gen": "hypothesis_generation",
            "hypothesis_generation": "hypothesis_generation",
            "judgment": "judgment",
            "judgment_gate": "judgment",
            "experiment_design": "experiment_design",
            "experiment_execution": "experiment_execution",
            "execution": "experiment_execution",
            "reflection": "reflection",
            "writing": "writing",
            "advisor_review": "reflection",
        }
        for key, val in phase_map.items():
            if key in last_phase:
                return val

    if not hyps:
        if field.get("sota_summary"):
            return "hypothesis_generation"
        return "literature_survey"

    has_approved = any(
        (h.get("judgment") or {}).get("verdict") == "approved"
        or h.get("status") in ("approved", "in_progress", "completed", "failed")
        for h in hyps
    )
    has_experiment = any(
        (h.get("experiment") or {}).get("status") not in (None, "not_started")
        for h in hyps
    )
    has_results = any(
        (h.get("results") or {}).get("outcome") is not None
        for h in hyps
    )

    if has_results:
        return "reflection"
    if has_experiment:
        return "experiment_execution"
    if has_approved:
        return "experiment_design"
    if hyps:
        return "judgment"

    return "literature_survey"


# ── Main render logic ──────────────────────────────────────────────────────────

def render(project_dir, output_path=None):
    """Render research-tree.yaml into HTML. Returns the output file path."""
    project_dir = os.path.abspath(project_dir)
    tree_path = os.path.join(project_dir, "research-tree.yaml")
    log_path = os.path.join(project_dir, "research-log.md")

    template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "research-tree.html")
    if not os.path.exists(template_path):
        print(f"ERROR: Template not found at {template_path}")
        sys.exit(1)

    if not os.path.exists(tree_path):
        print(f"ERROR: research-tree.yaml not found in {project_dir}")
        sys.exit(1)

    tree_data = _load_yaml(tree_path)
    log_entries = parse_research_log(log_path)
    current_phase = infer_current_phase(tree_data, log_entries)

    render_data = {
        "project": tree_data.get("project", {}),
        "field_understanding": tree_data.get("field_understanding", {}),
        "hypotheses": tree_data.get("hypotheses") or [],
        "research_log": log_entries,
        "current_phase": current_phase,
    }

    with open(template_path, "r") as f:
        html = f.read()

    html = html.replace("{{RESEARCH_DATA_JSON}}", json.dumps(render_data, default=str))

    if output_path is None:
        output_path = os.path.join(project_dir, "research-tree.html")

    with open(output_path, "w") as f:
        f.write(html)

    return output_path


def main():
    args = sys.argv[1:]
    project_dir = "."
    output_path = None
    open_browser = False

    i = 0
    while i < len(args):
        if args[i] == "--output" and i + 1 < len(args):
            output_path = args[i + 1]
            i += 2
        elif args[i] == "--open":
            open_browser = True
            i += 1
        elif not args[i].startswith("-"):
            project_dir = args[i]
            i += 1
        else:
            i += 1

    out = render(project_dir, output_path)
    print(f"Rendered: {out}")

    if open_browser:
        webbrowser.open("file://" + os.path.abspath(out))


if __name__ == "__main__":
    main()
