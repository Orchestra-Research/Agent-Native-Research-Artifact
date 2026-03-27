# Judgment Gate Rubric

Use this rubric during the Judgment phase to evaluate each hypothesis before investing
resources in experiment design and execution. The goal is to filter out hypotheses that
are not novel, not important, not feasible, or not falsifiable — before wasting time on them.

## Evaluation Criteria

Evaluate each hypothesis on five dimensions:

| Criterion | Question | Pass | Fail |
|-----------|----------|------|------|
| **Novelty** | Has this already been tested or answered? | No prior work addresses this exact claim | Substantially covered by existing work |
| **Importance** | Does the answer matter? | Changes theory, practice, or measurement | Only we would care about the answer |
| **Feasibility** | Can we actually test this? | Data, compute, skills, and time are available | Missing critical resources with no path to acquire |
| **Falsifiability** | Can we design an experiment that would disprove this? | Clear negative outcome is specifiable | No way to distinguish success from failure |
| **Not Already Solved** | Is the problem genuinely open? | Literature survey confirms a gap | Solution already exists (even if not well-known) |

## Scoring Template

For each hypothesis, fill this assessment:

```
HYPOTHESIS JUDGMENT: [H-ID]
Statement: [hypothesis statement]

Novelty:        [ ] PASS  [ ] FAIL
  Evidence: [cite literature survey — what was/wasn't found]

Importance:     [ ] LOW  [ ] MEDIUM  [ ] HIGH
  Impact if true: [what changes for theory / practice / measurement]
  Impact if false: [is a null result also informative?]

Feasibility:    [ ] PASS  [ ] FAIL
  Data:    [available? accessible? sufficient?]
  Compute: [realistic for timeline?]
  Skills:  [team has or can acquire?]
  Time:    [meaningful result in available window?]

Falsifiability: [ ] PASS  [ ] FAIL
  Null hypothesis: [what would disprove the claim]
  Cheapest test:   [simplest experiment that could kill this hypothesis]

Already Solved: [ ] NO (proceed)  [ ] YES (stop)
  Evidence: [cite papers or lack thereof from literature survey]

─────────────────────────────────
VERDICT:        [ ] APPROVED  [ ] REJECTED
Rationale: [1-2 sentences explaining the decision]
```

## Decision Rules

| Condition | Action |
|-----------|--------|
| All criteria pass, importance ≥ medium | **Approve** — proceed to experiment design |
| Novelty FAIL | **Reject** — already solved; return to hypothesis generation |
| Feasibility FAIL | **Reject** or **Defer** — park the hypothesis; revisit if conditions change |
| Falsifiability FAIL | **Revise** — sharpen the hypothesis statement and re-evaluate |
| Importance LOW | **Deprioritize** — keep in tree but pursue higher-impact hypotheses first |
| Already Solved YES | **Reject** — log evidence and return to hypothesis generation |

## Batch Evaluation

When evaluating multiple hypotheses, use this comparison table:

```
| H-ID | Statement (abbreviated) | Novel? | Importance | Feasible? | Falsifiable? | Open? | Verdict |
|------|------------------------|--------|------------|-----------|-------------|-------|---------|
| H1   | ...                    | Y      | HIGH       | Y         | Y           | Y     | APPROVED |
| H2   | ...                    | Y      | MEDIUM     | N         | Y           | Y     | DEFERRED |
| H3   | ...                    | N      | HIGH       | Y         | Y           | N     | REJECTED |
```

## Relationship to Old Scoring Rubric

This rubric replaces the FINER + AI-specific scoring rubric used in the old brainstorming
phase. Key differences:

- **Binary gates** (pass/fail) instead of 1-5 scales for most criteria — reduces
  false precision and speeds up evaluation
- **Importance** uses a three-level scale (low/medium/high) instead of a numeric score
- **Falsifiability** is now an explicit criterion (was implicit before)
- **Already Solved** is checked explicitly against the literature survey (was part of
  novelty gap validation before)
- Evaluation is per-hypothesis, not per-idea — more granular and actionable

## Tips

- Be ruthless at this gate — it is far cheaper to reject a hypothesis now than to
  discover it is unworkable after weeks of experimentation
- A rejected hypothesis is not wasted work; it narrows the search space and is logged
  in the research tree
- When in doubt about novelty, do a targeted literature search before deciding
- Feasibility failures can become approvals later if conditions change (new compute,
  new data release) — mark as "deferred" rather than "rejected" when appropriate
- The cheapest possible falsification test (from the Falsifiability criterion) should
  be run before committing to a full experiment design
