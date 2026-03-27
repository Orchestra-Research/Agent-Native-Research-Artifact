# Experiment Design Protocol

Fill this template during the Experiment Design phase. Once complete, mark the protocol
as LOCKED in the research tree (`experiment.status: locked`) and log the lock in the
research log. Any deviations after locking must be logged as EXPLORATORY.

---

## 1. Hypothesis

- **Hypothesis ID:** [e.g., H1, H2.1 — must match an entry in research-tree.yaml]

- **Statement:**
  [Copy the testable hypothesis statement from the research tree]

- **Judgment verdict:** [approved — with rationale from judgment gate]

- **Scope:**
  [ ] In-domain  [ ] Cross-domain  [ ] Cross-lingual  [ ] Deployment-like  [ ] Mechanistic  [ ] Causal

## 2. Contribution Type

- **Type:** [ ] New method  [ ] New theory  [ ] New dataset  [ ] New measurement  [ ] Replication  [ ] Negative result

- **Why existing evidence is insufficient (2-4 sentences):**
  [Reference the evidence map from Lit Review]

## 3. Data

- **Dataset(s):** [name, source URL, version, access method]
- **License/terms:** [what is permitted]
- **Population/coverage:** [what does the data represent? what is missing?]
- **Sizes:** Train: ___ / Val: ___ / Test: ___
- **Split strategy:** [ ] Random  [ ] Stratified  [ ] Temporal  [ ] Predefined  [ ] Other: ___
- **Leakage prevention:** [how train/test contamination is prevented]
- **Preprocessing:** [deterministic steps, tool versions]
- **Dataset documentation:** [ ] Datasheet  [ ] Data Statement  [ ] N/A (existing well-documented dataset)

## 4. Variables & Controls

- **Independent variable(s):** [what is manipulated]
- **Dependent variable(s):**
  - Primary metric: [name, exact formula, averaging policy]
  - Secondary metrics (exploratory): [list]
- **Baselines:**
  - [Baseline 1]: [description, source, how run]
  - [Baseline 2]: [description, source, how run]
- **Ablations:**
  - [−Component A]: [expected effect]
  - [−Component B]: [expected effect]
- **Negative control:** [condition where method should NOT work]
- **Sanity check:** [test that would invalidate the pipeline if it fails]

## 5. Training & Compute Plan

- **Model architecture:** [family, size, key choices]
- **Fixed hyperparameters:** [list with values and justification]
- **Tuned hyperparameters:** [list with search space, method, budget]
- **Tuning performed on:** [ ] Validation set only  [ ] Other: ___
- **Random seeds:** [number of runs per condition, e.g., 5]
- **Hardware:** [GPU/TPU type, count, memory]
- **Expected runtime:** per run: ___ / total: ___
- **Checkpointing:** [frequency, what is saved]
- **Early stopping:** [criterion, patience]

## 6. Analysis Plan

### Primary analysis
- **Comparison:** [method vs baselines on primary metric]
- **Statistical test:** [e.g., paired bootstrap, Wilcoxon, none]
- **Decision rule:** [what constitutes "better"]

### Uncertainty reporting
- **Method:** [ ] Multiple seeds  [ ] Cross-validation  [ ] Bootstrap CI
- **Format:** [mean ± std / mean (95% CI) / distribution plot]

### Multiple comparisons
- **Number of comparisons:** [N models × M datasets × K metrics = ___]
- **Correction:** [ ] Bonferroni  [ ] Holm  [ ] None (framed as exploratory)

### Error analysis
- **Slices to check:** [list subgroups]
- **Qualitative audit:** [N examples sampled from errors]
- **Behavioral tests:** [specific patterns, CheckList-style]

### Exploratory analyses (pre-declared)
- [analysis 1]: [what and why]
- [analysis 2]: [what and why]

## 7. Reproducibility Artifacts

- **Code repository:** [URL]
- **Environment:** [ ] conda yml  [ ] pip lockfile  [ ] Docker  [ ] Other: ___
- **Experiment tracking:** [ ] MLflow  [ ] W&B  [ ] DVC  [ ] Neptune  [ ] Other: ___
- **Run naming scheme:** [e.g., {method}_{dataset}_{seed}_{timestamp}]
- **Paper → run ID mapping:** [where documented]
- **Data release:** [ ] Open  [ ] Restricted (reason: ___)  [ ] Not possible (reason: ___)
- **Model release:** [ ] Open  [ ] Restricted (reason: ___)  [ ] Not possible (reason: ___)
- **Storage estimate:** [for artifacts, checkpoints, logs]

## 8. Ethics & Risk

- **Human subjects:** [ ] No  [ ] Yes → IRB status: ___
- **Identifiable data:** [ ] No  [ ] Yes → De-identification plan: ___
- **Dual-use concerns:** [ ] No  [ ] Yes → Mitigation: ___
- **Environmental cost:** [estimated GPU-hours and approximate CO2 if large-scale]
- **Model documentation:** [ ] Model Card planned  [ ] N/A

## 9. Stop Criteria & Reporting Commitment

- **When we stop iterating:** [ ] Budget exhausted  [ ] Performance plateau  [ ] Target effect reached  [ ] Other: ___
- **Reporting commitment:** We will report results regardless of outcome, including negative/neutral findings.

---

**Protocol status:** [ ] DRAFT  [ ] UNDER REVIEW  [ ] LOCKED (date: ___)
**Locked by:** [name/initials]
**Deviations from locked protocol are logged in the research log as EXPLORATORY.**
