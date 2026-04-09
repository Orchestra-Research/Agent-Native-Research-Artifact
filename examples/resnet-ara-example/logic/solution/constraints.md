# Constraints

## Applicability

- Identity shortcuts apply only when the input and residual output dimensions match.
- When spatial or channel dimensions increase, the shortcut must be adapted by padding or projection.
- The basic-block formulation here applies directly to the 18/34-layer family; deeper variants introduce bottleneck blocks.

## Failure / Boundary Conditions

- Simply increasing depth in a plain architecture does not guarantee better optimization and may worsen training error.
- Shortcut design interacts with stage transitions; incorrect dimension matching breaks the residual merge.
- Very deep models on smaller datasets can introduce separate overfitting concerns even if optimization improves.

## Scope Notes

- This artifact is a partial reconstruction centered on the degradation-to-residual-learning slice.
- Hardware details are not fully specified in the source paper, so environment notes remain conservative.
