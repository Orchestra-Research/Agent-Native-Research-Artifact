# Research Log Template & Guide

The research log is the project's chronological record of exploration, decisions,
and observations. It complements the research tree (which is structured by hypothesis)
with a timeline view of what happened and why.

## Format

Create `research-log.md` at the project root with this structure:

```markdown
# Research Log: [Project Title]

| # | Date | Phase | Summary |
|---|------|-------|---------|
```

## Entry Types

### Phase Entry (work within a phase)

```
| 3 | 2026-03-01 | Literature Survey | Searched 4 databases (arXiv, Scholar, Scopus, DBLP). Screened 47 papers, 12 included. Key gap: no evaluation of X under Y conditions. |
```

### Phase Transition

```
| 4 | 2026-03-02 | Lit Survey → Hypothesis Gen | Survey complete. Identified 3 open problems and 2 underexplored areas. Moving to hypothesis generation. |
```

### Judgment Decision

```
| 5 | 2026-03-03 | Judgment | H1 approved (novel, high importance, feasible). H2 rejected (already solved by [paper]). H3 deferred (compute infeasible until Q3). |
```

### Experiment Update

```
| 7 | 2026-03-06 | Experiment Execution | H1: sanity checks passed. Baseline reproduces published numbers (within 0.5%). Primary runs submitted (5 seeds × 3 datasets). |
```

### Reflection Decision

```
| 9 | 2026-03-10 | Reflection | H1 supported on 2/3 datasets. Spawned H1.1 to investigate failure on dataset C. Decided to go deeper before concluding. |
```

### Backtrack

```
| 10 | 2026-03-11 | Reflection → Literature Survey | New related work [paper] discovered during reflection. Returning to survey to assess impact on assumptions. |
```

### Negative Result

```
| 8 | 2026-03-08 | Experiment Execution | H2: negative finding — method X does not improve over baseline B on metric M (delta = -0.3 +/- 0.5). Logged as valid result. Updated research tree: H2 status → failed. |
```

### Error / Recovery

```
| 6 | 2026-03-05 | Experiment Execution | ERROR: GPU OOM during evaluation on large test set. Switched to batch evaluation. Results unaffected. |
```

## Rules

1. **Always log** phase work, transitions (including backtracks), and key decisions
2. **Keep summaries to 2-4 sentences** — concise but informative
3. **Include the trigger reason** for any backward transition or loop
4. **Number sequentially** — never renumber, even after backtracks
5. **Log negative results** as valid milestones, not failures
6. **Reference hypothesis IDs** (e.g., H1, H2.1) to connect log entries to the research tree
7. **Timestamp every entry** with the date it was logged

## Example: Complete Research Log

```markdown
# Research Log: Scaling Laws for Few-Shot Learning

| # | Date | Phase | Summary |
|---|------|-------|---------|
| 1 | 2026-02-15 | Literature Survey | Searched arXiv, Scholar, DBLP, Scopus for "few-shot scaling laws". 52 papers screened, 18 included. SOTA summary written. |
| 2 | 2026-02-18 | Literature Survey | Identified 3 open problems: (1) no cross-architecture scaling analysis, (2) under-explored low-resource regime, (3) missing theoretical framework. |
| 3 | 2026-02-19 | Lit Survey → Hypothesis Gen | Survey complete. Generated 8 candidate hypotheses from open problems and underexplored areas. |
| 4 | 2026-02-20 | Hypothesis Generation | Refined to 5 testable hypotheses (H1-H5). H1: cross-architecture scaling follows power law. H2: few-shot performance saturates below 1B params. |
| 5 | 2026-02-21 | Judgment | H1 approved (novel, high importance, feasible). H2 approved (medium importance). H3 rejected (already shown by [paper]). H4-H5 deferred (compute). |
| 6 | 2026-02-23 | Experiment Design | H1: protocol designed. 4 architecture families × 5 scale points × 5 seeds. Primary metric: few-shot accuracy at k=5. |
| 7 | 2026-02-25 | Experiment Design | H1: protocol locked. H2: protocol designed and locked. |
| 8 | 2026-02-27 | Exp Design → Execution | Both protocols locked. Implementation complete. Submitting H1 runs first (higher priority). |
| 9 | 2026-02-28 | Experiment Execution | H1: sanity checks passed. Baselines reproduce published numbers. 20 runs submitted. |
| 10 | 2026-03-03 | Experiment Execution | H1: all runs complete. H2: 15/25 runs complete, remaining queued. |
| 11 | 2026-03-05 | Execution → Reflection | H1 results in. Power-law fit R^2 = 0.94 across 3/4 architectures. Architecture D deviates significantly. |
| 12 | 2026-03-05 | Reflection | H1 partially supported. Spawned H1.1: "Architecture D deviates because of [mechanism]". Decided to investigate before concluding. |
| 13 | 2026-03-06 | Reflection → Hypothesis Gen | Generated H1.1. Updated research tree. Moving to judgment for H1.1. |
| 14 | 2026-03-06 | Judgment | H1.1 approved (novel sub-question, high importance for understanding deviation). |
| 15 | 2026-03-08 | Experiment Execution | H2: all runs complete. Result: saturation point is ~500M params, not 1B as hypothesized. Updating research tree: H2 outcome → refuted (but informative). |
| 16 | 2026-03-10 | Reflection | H2 refuted but finding is publishable — saturation at 500M is a useful empirical result. H1.1 experiment designed and running. |
| 17 | 2026-03-15 | Reflection → Writing | H1 and H2 results stable. H1.1 results confirm mechanism hypothesis. Concluding research loop. Moving to writing. |
| 18 | 2026-03-17 | Writing | Methods and results sections drafted. Reproducibility checklist: 91%. |
| 19 | 2026-03-20 | Writing | Draft complete. Artifacts packaged. Pre-submission checklist passed. |
```

Notice the natural looping between phases — this is expected and healthy. The log
makes the non-linear research process transparent and auditable.
