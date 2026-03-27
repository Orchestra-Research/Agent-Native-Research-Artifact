# Reproducibility Checklist

Use this checklist before submission. It is designed to be compatible with ML venue
checklists (NeurIPS, ICML, ICLR), ACM artifact standards, and FAIR principles.

---

## Claims & Scope

- [ ] Claims are explicitly stated and match the experiments
- [ ] Limitations are explicitly stated (what was not tested; external validity)
- [ ] Intended use and non-intended use documented (Model Card-style if applicable)
- [ ] Confirmatory vs exploratory analyses clearly labeled

## Data

- [ ] Dataset source + access instructions + license/terms documented
- [ ] Dataset statistics documented (sizes, label distributions, key attributes)
- [ ] Train/val/test splits documented; leakage risks assessed and mitigated
- [ ] Preprocessing pipeline is deterministic and versioned
- [ ] Dataset documentation provided (Datasheet/Data Statement where appropriate)
- [ ] Data version identifiers or checksums recorded

## Code

- [ ] Code repository is publicly available (or sharing constraints justified)
- [ ] Single "entry point" scripts exist to reproduce main tables/figures
- [ ] Exact commit hash + release tag for paper version documented
- [ ] Dependencies pinned (environment.yml / lockfile / container)
- [ ] Randomness handled: seeds logged; nondeterminism noted
- [ ] README includes reproduction instructions

## Compute & Runtime

- [ ] Hardware specified (GPU/CPU type, memory, count)
- [ ] Runtime estimates provided (per experiment; total)
- [ ] Distributed or accelerator-specific assumptions documented
- [ ] Cost estimates provided if using cloud compute

## Training & Evaluation

- [ ] Baselines specified and implemented under comparable conditions
- [ ] Hyperparameter search space and budget documented
- [ ] Primary metric specified with exact definition
- [ ] Secondary metrics labeled as such
- [ ] Multiple runs reported (seeds/folds) where variance is meaningful
- [ ] Uncertainty reported (CI, std, or distribution) with method described
- [ ] Ablations included for key components (or explicitly justified if absent)
- [ ] Error analysis performed (slices, qualitative audits, behavioral tests)
- [ ] Negative results reported (not hidden)

## Artifacts

- [ ] Trained weights/models shared OR sharing constraints justified
- [ ] Artifact package includes configs used for all reported runs
- [ ] Experiment tracking links run IDs to paper figures/tables
- [ ] Model Card provided if releasing a model

## Archival & Citation

- [ ] Repository has a license
- [ ] Citation instructions provided (CITATION.cff or equivalent)
- [ ] Archival copy created (e.g., Zenodo archive) with DOI when feasible
- [ ] Data and software adhere to FAIR principles where possible
- [ ] Software dependencies properly cited

## Ethics & Compliance

- [ ] Human subjects determination documented (if relevant)
- [ ] IRB/ethics review pathway documented (if relevant)
- [ ] Privacy/risk mitigations documented
- [ ] Dual-use or deployment risks discussed (when applicable)
- [ ] Environmental impact acknowledged (for large-scale compute)
- [ ] Author contributions documented (CRediT taxonomy)

---

## Scoring

Count the checked boxes. Use this as a quality signal, not a strict gate:

| Score        | Interpretation                                          |
|-------------|--------------------------------------------------------|
| 90-100%     | Excellent — ready for top-tier venues                  |
| 75-89%      | Good — address gaps before submission                  |
| 60-74%      | Needs work — significant reproducibility risks remain  |
| Below 60%   | Not ready — revisit methodology and documentation      |

## Notes

Record any items that are intentionally unchecked with justification:

```
- [ ] Item X: Not applicable because [reason]
- [ ] Item Y: Will address before camera-ready because [plan]
```
