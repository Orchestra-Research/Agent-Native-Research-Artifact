# Phase: Reflection

## Goal

Analyze experiment results strategically and decide: go deeper, go broader, pivot, or
conclude. This phase is the decision point in the research loop — it determines whether
to continue iterating or exit to writing.

## Entry Conditions

- At least one hypothesis has completed experiments with determined outcomes
- Research tree is updated with results
- Confirmatory/exploratory boundary is marked

## Step-by-Step Protocol

### Step 1: Review the Research Tree

Read the current state of `research-tree.yaml` and assess the overall picture:

- How many hypotheses have been tested?
- What fraction were supported vs. refuted vs. inconclusive?
- Are there patterns across results?
- What surprises emerged?
- What questions remain open?

### Step 2: Assess Claim Strength

For each completed hypothesis, answer honestly:

```
CLAIM ASSESSMENT: [H-ID]
1. Does the primary metric support the hypothesis?     [yes / no / partially]
2. Is the effect size meaningful (not just significant)?  [yes / no]
3. Do ablations confirm the contribution is real?         [yes / no]
4. Are there important failure modes that limit the claim? [describe]
5. Would we be comfortable if someone tried to replicate?  [yes / no / concerns]
6. What is the honest "headline" of this work?            [1 sentence]
```

**If the claim is NOT supported**: this is a valid result. Log it as a negative
finding. Consider whether it is publishable as a negative result or as useful evidence
for the community.

### Step 3: Identify Follow-Up Questions

Every experiment — successful or not — generates new questions:

**From supported hypotheses:**
- Does the effect hold under different conditions? (→ sub-hypothesis)
- What is the mechanism behind the effect? (→ deeper investigation)
- Can the approach be generalized? (→ broader hypothesis)

**From refuted hypotheses:**
- Why was the hypothesis wrong? (→ diagnostic hypothesis)
- Does a modified version of the claim hold? (→ refined hypothesis)
- Is there a surprising finding in the negative result? (→ new direction)

**From inconclusive results:**
- Is more data/compute needed? (→ scaled experiment)
- Is the metric wrong? (→ measurement hypothesis)
- Is there a confound we missed? (→ design fix)

### Step 4: Strategic Decision

Choose one of four paths:

| Decision | When | Action |
|----------|------|--------|
| **Go Deeper** | Supported hypothesis raises important sub-questions | Generate sub-hypotheses (H1.1, H1.2...) → Hypothesis Generation |
| **Go Broader** | Current results are solid, but adjacent questions are untested | Generate new root hypotheses → Hypothesis Generation |
| **Pivot** | Results invalidate key assumptions or reveal better direction | Return to Literature Survey to reassess the field |
| **Conclude** | Sufficient evidence exists for a coherent contribution | Proceed to Writing |

**Decision criteria for concluding:**
- At least one hypothesis is supported with strong evidence
- Key ablations and error analyses are complete
- The contribution is clear and defensible
- OR: a coherent set of negative results constitutes a contribution
- No critical open questions remain that would change the story

### Step 5: Update the Research Tree

Based on the decision:

**If going deeper or broader:**
- Add new hypotheses to the tree (return to Hypothesis Generation)
- Set `parent` field to connect sub-hypotheses to their parents
- Keep the research loop going

**If pivoting:**
- Update `project.status` or add notes about the pivot
- Return to Literature Survey with specific questions

**If concluding:**
- Set `project.status: completed` (or keep `active` if writing will spawn revisions)
- Ensure all hypothesis statuses are final
- Prepare results summary for writing

### Step 6: Log the Reflection

Record the reflection decision in the research log with:
- Summary of results analyzed
- Key insights and surprises
- Decision made (deeper/broader/pivot/conclude) and rationale
- New hypotheses spawned (if any)

## Reflection Checklist

Before making the strategic decision, verify:

```
REFLECTION CHECKLIST
[ ] All completed experiments have been reviewed
[ ] Claim assessments are honest (no overclaiming)
[ ] Negative results are logged as valid findings
[ ] Follow-up questions have been identified
[ ] The decision (deeper/broader/pivot/conclude) is justified
[ ] New hypotheses (if any) are added to the research tree
[ ] The research log captures the reflection and decision
```

## Exit Criteria

- [ ] All completed hypotheses have claim assessments
- [ ] Follow-up questions are identified
- [ ] Strategic decision is made (deeper/broader/pivot/conclude)
- [ ] Research tree is updated accordingly
- [ ] Research log entry recorded with decision and rationale

## Transition

**Forward → Writing** (conclude): carry the complete research tree with all results,
claim assessments, and the overall narrative.

**Loop → Hypothesis Generation** (deeper/broader): carry new hypotheses back into the
generation phase. They go through judgment → design → execution → reflection again.

**Loop → Literature Survey** (pivot): carry specific questions that need answering
before generating new hypotheses.

**The Research Loop:**
```
Literature Survey → Hypothesis Generation → Judgment → Experiment Design → Execution → Reflection
       ^                    ^                                                              |
       |                    |                                                              |
       +--------------------+--------------------------------------------------------------+
                                            (loop back)
```

The loop continues until Reflection decides to conclude. There is no fixed number of
iterations — the research drives the pace. Most projects will loop 2-5 times before
concluding.
