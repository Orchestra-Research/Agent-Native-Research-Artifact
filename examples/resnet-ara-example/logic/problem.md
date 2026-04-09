# Problem Specification

## Observations

### O1: Deeper plain models do not automatically optimize better
- **Statement**: Simply increasing CNN depth does not guarantee improved optimization behavior even in ImageNet-scale settings.
- **Evidence**: Paper motivation and the controlled plain-network comparisons in Table 2.
- **Implication**: Architectural depth alone is not a sufficient recipe for trainability.

### O2: The 34-layer plain network is worse than the 18-layer plain network
- **Statement**: In Table 2, the 18-layer plain model has 27.94% top-1 error while the 34-layer plain model has 28.54% top-1 error.
- **Evidence**: `evidence/tables/table2_imagenet_plain_vs_residual.md`
- **Implication**: The deeper plain model exhibits degradation despite having a strictly richer solution space.

### O3: The failure is visible in training behavior, not only validation error
- **Statement**: The paper explicitly states that the degradation phenomenon appears in training error, so the issue is not explained away as ordinary overfitting.
- **Evidence**: Discussion around the degradation problem and the optimization framing in the source paper.
- **Implication**: The core problem is optimization difficulty rather than insufficient capacity.

## Gaps

### G1: Prior deep CNN practice lacked a formulation that made very deep stacks easy to optimize
- **Statement**: Earlier successful CNN families demonstrated the value of depth but did not provide an always-open mechanism that preserved an identity path through many layers.
- **Caused by**: O1, O2
- **Existing attempts**: Standard stacked layers, modern initialization, and batch normalization.
- **Why they fail**: They improve convergence conditions but do not remove the deeper-plain degradation pattern.

### G2: Plain stacked layers obscure the identity solution
- **Statement**: If the ideal mapping is close to identity, standard stacks still require the optimizer to synthesize that mapping through multiple nonlinear layers.
- **Caused by**: O2, O3
- **Existing attempts**: Increasing depth while preserving the same plain architecture.
- **Why they fail**: The optimization path does not expose a direct shortcut to the identity mapping.

## Key Insight
- **Insight**: Learn a residual function around a shortcut path so that each block computes `H(x) = F(x) + x` instead of fitting `H(x)` directly.
- **Derived from**: O2, O3
- **Enables**: Deep networks in which identity-preserving information flow remains available while only the residual correction is learned.

## Assumptions
- A1: The degradation problem is primarily an optimization issue in the paper's matched-comparison setting.
- A2: Identity shortcuts are sufficient when input and output dimensions match.
- A3: When dimensions differ, the shortcut path must be adapted by padding or projection.
