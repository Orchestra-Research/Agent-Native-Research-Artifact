# Phase: Hypothesis Generation

## Goal

Generate a broad set of testable hypotheses from the literature survey findings and
maintain them in the research tree (YAML). This phase transforms open problems and
underexplored areas into concrete, falsifiable claims.

## Entry Conditions

- Literature survey is complete with populated `field_understanding` in the research tree
- Open problems and underexplored areas are explicitly catalogued
- OR: looping back from Reflection to generate new or refined hypotheses

## Step-by-Step Protocol

### Step 1: Diverge — Generate Candidate Hypotheses

Use the open problems and underexplored areas from the literature survey as seeds.
For each, generate 1-3 testable hypotheses. Aim for 10-20 candidates total.

**Sources of hypotheses:**
- Gaps identified in the evidence map
- Contradictions between papers
- Unverified assumptions in the field
- "What if the opposite were true?" inversions
- Combinations of existing techniques not yet tested
- Extensions to underexplored conditions (scale, domain, modality)

**How to generate candidates:**
- Select 2-3 ideation frameworks from [phases/ideation-frameworks.md](ideation-frameworks.md)
  based on your situation (see the Framework Selection Guide there)
- Walk through each framework interactively, using the literature survey findings
  as domain-specific input
- For each framework, push for specificity — "improve efficiency" is not a hypothesis;
  "method X reduces compute by 50% while maintaining accuracy within 2%" is.

**For a deep ideation session** (when broad exploration is needed), use the Integrated
Creative Thinking Protocol from [ideation-frameworks.md](ideation-frameworks.md), which
chains all 12 frameworks across four phases.

### Step 2: Write Testable Hypothesis Statements

For each candidate, write a precise, testable statement:

```
HYPOTHESIS TEMPLATE
- ID: H[N] (sequential) or H[parent].[N] (for sub-hypotheses)
- Statement: [Method/condition X] [improves/changes/enables/causes] [outcome Y]
            on [data/population Z] compared to [baseline B] under [conditions C].
- Motivation: [Why this is worth testing, grounded in literature survey findings]
- Parent: [null for root hypotheses; parent ID for sub-hypotheses]
```

**What makes a good hypothesis:**
- **Specific**: names the method, metric, data, and baseline
- **Directional**: predicts which way the effect goes
- **Falsifiable**: a clear negative outcome is specifiable
- **Grounded**: motivated by evidence from the literature survey
- **Scoped**: bounded conditions under which it applies

**What makes a bad hypothesis:**
- "X is better than Y" (better at what? on what data? by how much?)
- "This approach is promising" (not testable)
- "We explore the effect of..." (exploration framing, not a claim)

### Step 3: Apply the Two-Sentence Pitch Test

For each hypothesis, verify it passes the two-sentence pitch:

> **S1** (Problem): "[Domain] currently struggles with [specific problem], which
> matters because [concrete consequence]."
>
> **S2** (Insight): "We hypothesize that [mechanism/approach] because [reason
> grounded in evidence]."

If a hypothesis cannot pass this test, it needs refinement:
- Problem unclear → return to literature survey findings
- Mechanism unclear → sharpen the hypothesis statement
- Significance not established → check the evidence map for impact evidence

### Step 4: Organize into a Hypothesis Tree

Structure hypotheses hierarchically in the research tree:

- **Root hypotheses** (H1, H2, H3...): major independent research questions
- **Sub-hypotheses** (H1.1, H1.2...): refinements, follow-ups, or components of
  a root hypothesis. Created during initial generation OR spawned later during reflection.

**Update `research-tree.yaml`**: add each hypothesis to the `hypotheses` list with:
- `id`, `statement`, `parent`, `motivation`
- `status: pending` (all start as pending)
- Empty `judgment`, `experiment`, `results` sections (filled in later phases)

### Step 5: Prioritize for Judgment

Rank hypotheses by expected information value — which ones, if tested, would teach
us the most about the problem space? Consider:

- **Impact**: how much would a positive or negative result change understanding?
- **Feasibility**: can we test this with available resources?
- **Dependencies**: does testing H2 depend on H1's result?
- **Breadth**: are we covering different parts of the problem space?

Present the prioritized list to the user for review before proceeding to judgment.

## Prompt Bank

Use these questions to push hypothesis generation:

**From open problems:**
- What is the smallest, sharpest claim we can extract from this open problem?
- What would constitute strong evidence for or against this claim?
- If this claim is true, what else must be true? (implications → sub-hypotheses)

**From underexplored areas:**
- What is the most surprising thing that could be true in this area?
- What "obvious experiment" has nobody run? Why not?
- What assumptions about this area are borrowed from adjacent areas but never verified?

**From contradictions:**
- Paper A says X, Paper B says Y — what would reconcile them?
- Under what conditions is A right and B wrong, or vice versa?
- Is the contradiction real or a measurement artifact?

**Framework-specific probes** (from [ideation-frameworks.md](ideation-frameworks.md)):
- *Reformulation*: Are we testing the right question, or a convenient proxy?
- *Abstraction*: What is the general principle behind this specific claim?
- *Tension*: Which two goals does everyone want but treats as a trade-off?
- *Analogy*: What field solves a structurally similar problem with different tools?
- *What Changed*: What was dismissed 5 years ago that new conditions make viable?
- *Boundary*: Where exactly does the current best method break down?
- *Constraint*: Which hidden assumption, if dropped, would change everything?
- *Negation*: What if the opposite of conventional wisdom were true?
- *Composition*: What two existing techniques, combined, create emergent capability?
- *Simplicity*: If we strip this to one key idea, does it still work?
- *Stakeholder*: Who besides ML researchers would care about this problem?

## Creative Blocks

If hypothesis generation stalls, diagnose the block and apply a targeted framework
(see [ideation-frameworks.md](ideation-frameworks.md)):

| Block | Symptom | Unblock With |
|-------|---------|-------------|
| Fixation | Cannot think about the problem differently | F2 (Reformulation) |
| Tunnel vision | All hypotheses from same subfield | F5 (Cross-Pollination) |
| Self-censoring | Dismissing "weird" ideas too early | F9 (Negation) — evaluate after generating |
| Incrementalism | Every hypothesis is +2% on a benchmark | F8 (Constraint Manipulation) |
| Analysis paralysis | Too many options | F6 (Adjacent Possible) — what is feasible now? |
| False dichotomy | Stuck choosing A vs. B | F4 (Janusian Synthesis) |

## Exit Criteria

- [ ] At least 5 testable hypotheses generated with clear statements
- [ ] Each hypothesis passes the two-sentence pitch test
- [ ] Hypotheses are organized in the research tree with proper parent/child relationships
- [ ] Priority ordering is established for judgment
- [ ] Research log entry recorded

## Transition

**Forward → Judgment Gate**: carry the prioritized hypothesis list for evaluation.

**Backward ← Judgment**: if judgment reveals that all hypotheses are rejected (not novel,
not feasible, etc.), return here to generate new candidates — possibly after updating
the literature survey.

**Backward ← Reflection**: if reflection after experiments spawns new hypotheses or
refinements, return here to add them to the tree and re-enter the loop.
