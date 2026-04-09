# Claims

## C01: Residual shortcuts ease optimization at matched depth
- **Statement**: A 34-layer residual network optimizes better and validates better than a matched 34-layer plain network.
- **Status**: supported
- **Falsification criteria**: A matched 34-layer residual model fails to improve training behavior or top-1 validation error over the 34-layer plain model.
- **Proof**: [E02]
- **Dependencies**: none
- **Tags**: residual learning, optimization, ImageNet, matched-depth comparison

## C02: Residual formulation reverses the plain-depth degradation pattern
- **Statement**: The degradation observed when scaling a plain network from 18 to 34 layers is not intrinsic to depth itself; it is substantially alleviated by residual reformulation.
- **Status**: supported
- **Falsification criteria**: Plain and residual depth scaling show the same degradation pattern under the paper's controlled setup.
- **Proof**: [E01, E02]
- **Dependencies**: C01
- **Tags**: degradation problem, plain network, residual block

## C03: Residual families continue to benefit from increased depth
- **Statement**: In the reported ImageNet validation comparisons, ResNet-50, ResNet-101, and ResNet-152 achieve lower top-1 and top-5 error than the 34-layer residual variants shown in Table 3.
- **Status**: supported
- **Falsification criteria**: Any of ResNet-50, ResNet-101, or ResNet-152 fails to improve over the reported 34-layer residual variants in Table 3.
- **Proof**: [E03]
- **Dependencies**: C01
- **Tags**: depth scaling, ImageNet, ResNet-50, ResNet-101, ResNet-152

## C04: Projection shortcuts help slightly but are not essential
- **Statement**: All shortcut options A, B, and C outperform the plain-34 baseline, while option B is slightly better than option A and option C is only marginally better than option B.
- **Status**: supported
- **Falsification criteria**: A, B, or C fails to improve over plain-34, or the reported ordering among A/B/C is not present in the source table and discussion.
- **Proof**: [E04]
- **Dependencies**: C01
- **Tags**: shortcut variants, option A, option B, option C, projection shortcuts
