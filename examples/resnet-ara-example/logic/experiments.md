# Experiments

## E01: Plain networks at matched depth

- **Verifies**: C02
- **Setup**:
  - Model: 18-layer plain net vs. 34-layer plain net
  - Hardware: Not specified in paper
  - Dataset: ImageNet 2012 classification
  - System: Matched training recipe with standard ImageNet augmentation and 10-crop validation testing
- **Procedure**:
  1. Train both plain architectures with the same recipe.
  2. Compare training behavior and validation error.
  3. Check whether the deeper plain net improves validation error as expected.
- **Metrics**: top-1 validation error (%)
- **Expected outcome**:
  - the 34-layer plain net exhibits worse optimization behavior and worse validation error than the 18-layer plain net
- **Baselines**: 18-layer plain net
- **Dependencies**: none

## E02: Residual learning vs. plain counterpart

- **Verifies**: C01, C02
- **Setup**:
  - Model: 34-layer plain net vs. 34-layer ResNet
  - Hardware: Not specified in paper
  - Dataset: ImageNet 2012 classification
  - System: Shortcut option A with identity mapping and zero-padding when dimensions increase
- **Procedure**:
  1. Replace each paired stack of 3x3 filters with a residual block plus shortcut.
  2. Keep the depth and comparison setting matched to the plain network.
  3. Compare training error and validation error.
- **Metrics**: top-1 validation error (%)
- **Expected outcome**:
  - the 34-layer residual net has lower validation error than the 34-layer plain net
- **Baselines**: 34-layer plain net
- **Dependencies**: E01

## E03: Residual depth scaling

- **Verifies**: C03
- **Setup**:
  - Model: ResNet-34 B, ResNet-34 C, ResNet-50, ResNet-101, ResNet-152
  - Hardware: Not specified in paper
  - Dataset: ImageNet 2012 classification
  - System: Residual family comparison using the paper's reported 10-crop ImageNet validation settings
- **Procedure**:
  1. Scale the residual family by increasing block count.
  2. Measure top-1 and top-5 validation error.
  3. Check whether deeper residual models continue to improve.
- **Metrics**: top-1 validation error (%), top-5 validation error (%)
- **Expected outcome**:
  - deeper residual variants outperform the reported ResNet-34 B baseline and remain better than the other reported 34-layer residual comparator
- **Baselines**: ResNet-34 B
- **Dependencies**: E02

## E04: Shortcut variant comparison

- **Verifies**: C04
- **Setup**:
  - Model: ResNet-34 with shortcut options A, B, and C
  - Hardware: Not specified in paper
  - Dataset: ImageNet 2012 classification
  - System: Compare identity shortcuts, projection-on-increase, and projection-on-all-shortcuts
- **Procedure**:
  1. Evaluate parameter-free identity shortcuts with zero-padding.
  2. Evaluate projection shortcuts only for dimension increases.
  3. Evaluate all-shortcut projections.
- **Metrics**: top-1 validation error (%)
- **Expected outcome**:
  - all shortcut variants improve on the plain counterpart
  - projection is helpful but not essential for addressing degradation
- **Baselines**: 34-layer plain net, ResNet-34 option A
- **Dependencies**: E02
