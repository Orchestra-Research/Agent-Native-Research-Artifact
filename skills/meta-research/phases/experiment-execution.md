# Phase: Experiment Execution

## Goal

Execute locked experiment protocols, track results, perform sanity checks and analysis,
and update the research tree with outcomes. This phase handles the full cycle from
running experiments through interpreting results.

## Entry Conditions

- At least one hypothesis has a locked experiment protocol (from Experiment Design)
- Code, environment, and tracking infrastructure are set up
- Research tree shows `experiment.status: locked` for the hypothesis

## Step-by-Step Protocol

### Step 1: Pre-Execution Checklist

Before running any experiments, verify:

```
PRE-EXECUTION CHECKLIST
[ ] Protocol is locked (no further changes without logging as EXPLORATORY)
[ ] Code runs end-to-end on a tiny subset
[ ] Environment is pinned (conda yml / pip lockfile / Docker)
[ ] Experiment tracking is configured (MLflow / W&B / DVC / etc.)
[ ] Data is loaded correctly (spot-check random samples)
[ ] Train/test split integrity confirmed (no overlap, correct sizes)
[ ] Random seeds are set and produce different runs (variance > 0)
[ ] Compute resources are available for the full experiment plan
```

Update research tree: `experiment.status: running`

### Step 2: Execute Experiments

Run experiments according to the locked protocol. For each hypothesis:

1. **Run all conditions** specified in the protocol (method + baselines)
2. **Track everything**: metrics per step, configs, hardware, timestamps
3. **Log intermediate results** — do not wait until all runs finish
4. **Monitor for failures**: OOM, NaN, divergence, hardware issues

**Parallel execution** (when multiple hypotheses are approved):
- Independent hypotheses can be run in parallel using sub-agents
- Each sub-agent handles one hypothesis's experiments
- Results are collected and merged into the research tree
- Dependencies between hypotheses (H1 must finish before H1.1) are respected

### Step 3: Sanity Checks (Before Analysis)

Run these BEFORE looking at primary results:

```
SANITY CHECKLIST
[ ] Training converged (loss curves look reasonable)
[ ] No NaN/Inf values in outputs
[ ] Baseline reproduces expected performance (within tolerance of published numbers)
[ ] Data loading is correct (spot-check random samples)
[ ] Train/test split integrity (no overlap, correct sizes)
[ ] Random seeds actually produced different runs (check variance > 0)
[ ] Metric computation matches the definition in the protocol
```

If ANY sanity check fails: log the failure in the research log, diagnose, fix, and
re-run. Do NOT proceed to analysis with broken infrastructure.

### Step 4: Primary Analysis (Confirmatory)

Execute exactly what was pre-committed in the analysis plan:

1. **Compute primary metric** across all seeds/folds for each condition
2. **Report uncertainty**: mean +/- CI (or full distribution)
3. **Apply the decision rule** from the protocol
4. **Run the pre-committed statistical test** (if applicable)

**Reporting format:**
```
| Method    | Dataset | Metric (mean +/- CI) | N runs | Beats baseline? |
|-----------|---------|----------------------|--------|-----------------|
| Ours      | D1      | 82.3 +/- 1.2         | 5      | Yes (p < 0.01)  |
| Baseline  | D1      | 79.1 +/- 0.8         | 5      | ---             |
```

**Critical**: report the primary metric for ALL conditions, including failures.
Do not cherry-pick the best seed or the best dataset.

### Step 5: Ablation Study

For each component identified in the protocol:

```
ABLATION RESULTS
| Configuration         | Metric (mean +/- CI) | Delta from full | Component isolated |
|-----------------------|----------------------|-----------------|--------------------|
| Full model            | 82.3 +/- 1.2         | ---             | ---                |
| - Component A         | 78.5 +/- 1.4         | -3.8            | A contributes ~4pts |
| - Component B         | 81.9 +/- 1.1         | -0.4            | B is marginal      |
| - Component A - B     | 76.2 +/- 1.6         | -6.1            | A+B interact       |
```

### Step 6: Error Analysis

**Quantitative error analysis:**
- Slice performance by meaningful subgroups (by difficulty, domain, length, etc.)
- Identify where the method fails worst
- Compare failure patterns between method and baselines

**Qualitative error analysis:**
- Sample N random errors (e.g., 50-100)
- Categorize errors into types
- Look for systematic patterns

**Behavioral tests** (CheckList-style):
- Test specific capabilities: negation, entity swap, paraphrase, etc.
- Test robustness: noise, typos, distribution shift
- Test edge cases identified during design

### Step 7: Uncertainty Quantification

Report uncertainty at multiple levels:

**Across-run variance** (from multiple seeds):
- Standard deviation or confidence interval
- Use bootstrap CI if distribution is non-normal
- If variance is very high, this IS a result — report it prominently

**Across-dataset variance** (if applicable):
- Performance on each dataset separately
- Do not only report the average — show the spread

**Calibration** (if model outputs probabilities):
- Calibration curve (reliability diagram)
- Expected Calibration Error (ECE)

### Step 8: Determine Outcome

For each hypothesis, determine the outcome:

```
OUTCOME ASSESSMENT
1. Does the primary metric support the hypothesis?  [supported / refuted / inconclusive]
2. Is the effect size meaningful (not just statistical)? [yes / no]
3. Do ablations confirm the contribution is real?       [yes / no]
4. Are there important failure modes?                   [describe]
5. What is the honest headline of this result?          [1 sentence]
```

**Update the research tree** for each hypothesis:

```yaml
results:
  summary: "One-sentence summary of what was found"
  outcome: supported    # supported | refuted | inconclusive
  key_metrics:
    - metric: "accuracy"
      value: 82.3
      baseline_value: 79.1
      delta: 3.2
  artifacts_path: "experiments/H1-slug/results/"
```

Update `status`:
- `completed` — experiment finished, outcome determined
- `failed` — hypothesis was refuted (this is a valid, useful result)

### Step 9: Label Confirmatory vs Exploratory

**This is a critical discipline.**

Everything in the pre-committed analysis plan = CONFIRMATORY.
Everything else = EXPLORATORY.

Label them explicitly:

```
CONFIRMATORY RESULTS:
- [result 1]: pre-committed comparison of X vs Y on metric M
- [result 2]: pre-committed ablation of component A

EXPLORATORY RESULTS:
- [result 3]: post-hoc analysis of performance by input length (not pre-committed)
- [result 4]: additional baseline Z (found during execution, not in protocol)
```

Exploratory results can be just as interesting — but they must be labeled as such
and interpreted more cautiously.

### Artifact Locations

Save outputs to the hypothesis's experiment directory:
```
experiments/H[N]-slug/
  protocol.md           # Locked protocol (from experiment design)
  src/                  # Experiment code
  results/              # Raw results, metrics, logs
  analysis.md           # Consolidated analysis (sanity, primary, ablation, error)
```

## Exit Criteria

- [ ] All sanity checks passed
- [ ] Primary analysis completed per pre-committed plan
- [ ] Ablations completed for all identified components
- [ ] Error analysis performed (quantitative + qualitative + behavioral)
- [ ] Uncertainty reported at appropriate levels
- [ ] Confirmatory/exploratory boundary clearly marked
- [ ] Outcome determined and research tree updated for each hypothesis
- [ ] Research log entry recorded (including whether claim is supported)

## Transition

**Forward → Reflection**: carry all results, outcome assessments, and updated research tree
for strategic decision-making.

**Backward → Experiment Design**: if pipeline bugs, data leakage, or protocol issues are
found, return to fix the protocol and re-run.

**Backward → Literature Survey**: if execution reveals that assumptions from the evidence
map are wrong (e.g., a baseline performs differently than reported), return to investigate.
