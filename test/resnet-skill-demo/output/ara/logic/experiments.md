# Experiments

## E01: Compare 18-layer and 34-layer plain networks on ImageNet
- **Verifies**: C02
- **Setup**:
  - Model: 18-layer and 34-layer plain networks (Table 1, Figure 3 left/middle)
  - Hardware: Not specified in paper (Microsoft Research infrastructure)
  - Dataset: ImageNet 2012 — 1.28M training images, 50k validation images, 1000 classes
  - System: SGD, mini-batch 256, 60x10^4 iterations
- **Procedure**:
  1. Train 18-layer plain network from scratch with BN, lr=0.1 (divided by 10 at plateaus)
  2. Train 34-layer plain network from scratch under identical conditions
  3. Evaluate both on ImageNet validation using 10-crop testing
  4. Compare top-1 error rates and training curves
- **Metrics**: Top-1 error (%), top-5 error (%), training error curves
- **Expected outcome**:
  - The 34-layer plain network should exhibit higher training and validation error than the 18-layer plain network, demonstrating degradation
- **Baselines**: 18-layer plain network serves as the shallower reference
- **Dependencies**: none

## E02: Compare 34-layer plain and 34-layer residual networks on ImageNet
- **Verifies**: C01
- **Setup**:
  - Model: 34-layer plain network and 34-layer residual network (Figure 3 middle/right)
  - Hardware: Not specified in paper
  - Dataset: ImageNet 2012 — 1.28M training, 50k validation, 1000 classes
  - System: SGD, mini-batch 256, identity shortcuts with zero-padding for dimension changes (option A)
- **Procedure**:
  1. Train 34-layer plain network from scratch
  2. Train 34-layer ResNet from scratch with identity shortcuts added to each pair of 3x3 filters
  3. Both networks have no extra parameter compared to their architectures
  4. Evaluate on ImageNet validation using 10-crop testing
  5. Compare top-1 error rates and training curves
- **Metrics**: Top-1 error (%), top-5 error (%), training error curves
- **Expected outcome**:
  - The 34-layer ResNet should achieve substantially lower validation error than the 34-layer plain network, demonstrating that residual learning alleviates degradation
- **Baselines**: 34-layer plain network
- **Dependencies**: E01

## E03: Compare shortcut options A, B, and C on ResNet-34
- **Verifies**: C04
- **Setup**:
  - Model: ResNet-34 with three shortcut variants — (A) identity with zero-padding, (B) projection for dimension changes only, (C) all shortcuts are projections
  - Hardware: Not specified in paper
  - Dataset: ImageNet 2012 — 1.28M training, 50k validation, 1000 classes
  - System: SGD, same training setup as E02
- **Procedure**:
  1. Train ResNet-34 option A (identity everywhere, zero-padding for dimension increase)
  2. Train ResNet-34 option B (projection shortcuts only when dimensions change)
  3. Train ResNet-34 option C (all shortcuts are projections via 1x1 convolutions)
  4. Evaluate all three on ImageNet validation (10-crop)
  5. Compare top-1 and top-5 error rates
- **Metrics**: Top-1 error (%), top-5 error (%)
- **Expected outcome**:
  - All three options should substantially outperform plain-34
  - The differences among A/B/C should be small, indicating projection shortcuts are not essential
- **Baselines**: plain-34, ResNet-34 A
- **Dependencies**: E02

## E04: Scale residual networks to 50, 101, and 152 layers on ImageNet
- **Verifies**: C03
- **Setup**:
  - Model: ResNet-50, ResNet-101, ResNet-152 using bottleneck architecture (1x1-3x3-1x1 blocks), option B shortcuts
  - Hardware: Not specified in paper
  - Dataset: ImageNet 2012 — 1.28M training, 50k validation, 1000 classes
  - System: SGD, same base training configuration
- **Procedure**:
  1. Replace 2-layer blocks with 3-layer bottleneck blocks in the 34-layer design
  2. Train ResNet-50, ResNet-101, and ResNet-152
  3. Evaluate on ImageNet validation (10-crop)
  4. Compare against ResNet-34 and all shallower variants
- **Metrics**: Top-1 error (%), top-5 error (%)
- **Expected outcome**:
  - Deeper residual models should progressively reduce both top-1 and top-5 error
  - No degradation should be observed as depth increases from 34 to 152 layers
- **Baselines**: ResNet-34 B, plain-34
- **Dependencies**: E02, E03
