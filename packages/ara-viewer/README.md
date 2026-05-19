# ARA Viewer

Reading-first browser for Agent-Native Research Artifacts. Renders the
artifact as a structured document with **claims as the primary content** and
**progressive expansion** — every claim, experiment, observation, etc. is
visible up front; the reader decides what to expand and when.

## Layout

- **Sticky TOC** (left) — every claim, experiment, concept, etc. by ID for
  quick jumping; highlights the section currently in view.
- **Reading column** (center) — hero (title, authors, abstract) followed by
  one section per node kind: Claims, Experiments, Observations, Concepts,
  Heuristics, Solution, Exploration trace, Related work, Evidence.
- **Cards** — each item is a card showing its ID badge, status pill, title,
  and one-line statement up front. Below: a row of `▶ field` buttons (parsed
  from the markdown — Falsification criteria, Proof, Evidence basis,
  Interpretation, etc.) that expand inline; and chip rows of linked
  artifacts (`proven by E01 E02 E03`, `depends on C02`, etc.) that expand as
  nested cards directly under the parent, recursively.
- **Search box** narrows the visible cards in place. `expand all` opens every
  field on every card; `collapse all` resets.

## Use

### 1. Build a manifest for an ARA

```bash
python3 build_manifest.py <path-to-ara-dir>
# writes <path-to-ara-dir>/manifest.json
```

The builder is stdlib-only (no PyYAML). It parses:

- `PAPER.md` frontmatter (title, authors, abstract, claims summary)
- `logic/problem.md` — observations (O01…)
- `logic/claims.md` — claims (C01…) and their `Proof` / `Dependencies` / `Evidence basis`
- `logic/experiments.md` — experiments (E01…) and `Verifies` / `Dependencies`
- `logic/concepts.md` — concept definitions
- `logic/solution/{architecture,algorithm,constraints,heuristics}.md` — solution layer + heuristics with `Code ref`
- `logic/related_work.md` — related work (RW01…) and `Claims affected`
- `trace/exploration_tree.yaml` — exploration DAG (N01…), parent-child + evidence citations
- `src/**` — code and config files
- `evidence/figures/*.md` and `evidence/tables/*.md`

Edges are inferred from cross-references in those files. Edges to non-existent
nodes (e.g. figures cited in text but without a file in `evidence/figures/`)
are dropped.

### 2. Serve the viewer

Browsers block `fetch()` for relative paths on `file://`, so start a local
server from the repo root:

```bash
python3 -m http.server 8000
```

Then open:

```
http://localhost:8000/packages/ara-viewer/?ara=../../ara-output/andes-qoe
```

The `?ara=` query param is the path to the ARA dir relative to
`packages/ara-viewer/index.html`. Defaults to `../../ara-output/andes-qoe`.

## Adding a new ARA

```bash
python3 packages/ara-viewer/build_manifest.py ara-output/<your-ara>
# then visit http://localhost:8000/packages/ara-viewer/?ara=../../ara-output/<your-ara>
```

The viewer is generic — any ARA following the standard layout will render.

## Files

- `index.html` — shell
- `style.css` — dark theme
- `viewer.js` — D3 force graph, detail pane, link panel
- `build_manifest.py` — manifest builder (Python 3, stdlib only)
