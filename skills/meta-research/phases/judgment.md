# Phase: Judgment Gate

## Goal

Evaluate each pending hypothesis for novelty, importance, feasibility, and falsifiability
before investing resources in experiment design. This gate prevents wasted effort on
hypotheses that are already solved, unimportant, infeasible, or untestable.

## Entry Conditions

- Hypothesis tree has at least one hypothesis with `status: pending`
- Literature survey is complete (needed to assess novelty and "already solved")
- OR: re-entering from Reflection with newly generated hypotheses

## Step-by-Step Protocol

### Step 1: Load the Judgment Rubric

Read [templates/judgment-rubric.md](../templates/judgment-rubric.md) for the full scoring
criteria, decision rules, and templates.

### Step 2: Evaluate Each Hypothesis

For each pending hypothesis in priority order, assess five criteria:

**Novelty** — Has this already been tested or answered?
- Cross-reference against the literature survey's evidence map
- Check for recent preprints not in the original survey
- A hypothesis can be novel even if the general area is well-studied, as long as the
  specific claim has not been addressed

**Importance** — Does the answer matter?
- Rate as LOW / MEDIUM / HIGH
- Consider impact on theory, practice, and measurement
- A null result should also be informative for a good hypothesis

**Feasibility** — Can we actually test this?
- Data: available and accessible?
- Compute: realistic for timeline and budget?
- Skills: team has or can quickly acquire needed expertise?
- Time: meaningful result obtainable in available window?

**Falsifiability** — Can we design an experiment that would disprove this?
- State the null hypothesis explicitly
- Identify the cheapest experiment that would kill the hypothesis
- If no negative outcome is specifiable, the hypothesis needs sharpening

**Not Already Solved** — Is the problem genuinely open?
- Distinct from novelty: "novel" means the specific test hasn't been done;
  "not already solved" means the answer isn't already known

### Step 3: Render Verdict

Apply the decision rules from the judgment rubric:

| Verdict | Condition | Action |
|---------|-----------|--------|
| **APPROVED** | All criteria pass, importance ≥ medium | Proceed to experiment design |
| **REJECTED** | Novelty fail OR already solved | Return to hypothesis generation |
| **DEFERRED** | Feasibility fail (but otherwise good) | Park; revisit when conditions change |
| **REVISE** | Falsifiability fail | Sharpen the statement, re-evaluate |

### Step 4: Run Cheapest Falsification Test

For approved hypotheses, before committing to full experiment design, run the
**cheapest possible falsification test**:

- Implement the simplest possible version (hours, not days)
- Run a sanity-check baseline — if the baseline already solves it, the hypothesis is moot
- Check for data leakage and label quality issues
- Test on a tiny subset first

**Key question**: "What is the cheapest experiment that would make me abandon this hypothesis?"

If the hypothesis survives, proceed. If not, update its status to `failed` in the
research tree and log the result (negative findings are valid milestones!).

### Step 5: Update the Research Tree

For each evaluated hypothesis, update `research-tree.yaml`:

```yaml
judgment:
  novelty: true         # or false
  importance: high      # low | medium | high
  feasibility: true     # or false
  falsifiability: true  # or false
  already_solved: false  # or true
  verdict: approved     # approved | rejected
  rationale: "Brief explanation"
```

Update `status`:
- `approved` — passed judgment, ready for experiment design
- `rejected` — failed judgment, will not be pursued
- `pending` — not yet evaluated (only if deferring evaluation)

### Step 6: Present Results to User

Show the user a summary table of all evaluated hypotheses:

```
| H-ID | Statement (abbreviated) | Novel? | Importance | Feasible? | Falsifiable? | Open? | Verdict |
|------|------------------------|--------|------------|-----------|-------------|-------|---------|
| H1   | ...                    | Y      | HIGH       | Y         | Y           | Y     | APPROVED |
| H2   | ...                    | Y      | MEDIUM     | N         | Y           | Y     | DEFERRED |
| H3   | ...                    | N      | HIGH       | Y         | Y           | N     | REJECTED |
```

Checkpoint with the user before proceeding — they may override verdicts based on
domain knowledge the agent lacks.

## Exit Criteria

- [ ] All prioritized hypotheses have been evaluated
- [ ] At least one hypothesis is approved (or all are rejected/deferred → loop back)
- [ ] Cheapest falsification test passed for approved hypotheses
- [ ] Research tree updated with judgment results for all evaluated hypotheses
- [ ] Research log entry recorded with verdicts and rationale

## Transition

**Forward → Experiment Design**: carry approved hypotheses for protocol design. Design
experiments one hypothesis at a time, starting with the highest-priority approved one.

**Backward → Hypothesis Generation**: if all hypotheses are rejected, return to generate
new candidates. Consider whether the literature survey needs updating first.

**Backward → Literature Survey**: if judgment reveals uncertainty about novelty or
"already solved" status, return to do a targeted search before deciding.
