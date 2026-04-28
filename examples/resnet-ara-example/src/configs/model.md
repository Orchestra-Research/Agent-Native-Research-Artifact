# Model Configuration

All depths share the same five-stage skeleton (Table 1 / Fig. 3).

## Stem (`conv1`)
- **Value**: 7×7 conv, 64 filters, stride 2 → BN → ReLU → 3×3 max-pool, stride 2.
- **Rationale**: Standard VGG-derived stem; fixed across ResNet-{18, 34, 50, 101, 152}.
- **Source**: Table 1; §3.3 / §3.4.

## ResNet-18 — Block layout
- **Value**: Basic block (two 3×3 convs); per-stage block counts {2, 2, 2, 2}; widths {64, 128, 256, 512}; FLOPs 1.8×10⁹.
- **Source**: Table 1.

## ResNet-34 — Block layout
- **Value**: Basic block; per-stage counts {3, 4, 6, 3}; widths {64, 128, 256, 512}; FLOPs 3.6×10⁹.
- **Rationale**: Designed to match the FLOPs of plain-34 (3.6×10⁹ ≈ 18% of VGG-19's 19.6×10⁹).
- **Source**: Table 1; §3.3.

## ResNet-50 — Block layout
- **Value**: Bottleneck block (1×1 → 3×3 → 1×1); per-stage counts {3, 4, 6, 3}; bottleneck widths {64, 128, 256, 512}, output widths {256, 512, 1024, 2048}; FLOPs 3.8×10⁹.
- **Rationale**: Replace each 2-layer block in ResNet-34 with a 3-layer bottleneck of comparable per-block time complexity.
- **Source**: Table 1; §"Deeper Bottleneck Architectures".

## ResNet-101 — Block layout
- **Value**: Bottleneck; per-stage counts {3, 4, 23, 3}; FLOPs 7.6×10⁹.
- **Source**: Table 1.

## ResNet-152 — Block layout
- **Value**: Bottleneck; per-stage counts {3, 8, 36, 3}; FLOPs 11.3×10⁹.
- **Rationale**: Deepest single model; still 57% of VGG-19's FLOPs.
- **Source**: Table 1; §4.1.

## Shortcut option
- **Value**:
  - Tables 2, Fig. 4 (right), Fig. 6: Option A (identity + zero-pad) for both 18- and 34-layer ResNets.
  - Table 3, Tables 4–5 deeper nets: Option B (projection only on dimension changes).
  - Option C (projection on every shortcut) is studied as ablation only and not used in deeper models.
- **Rationale**: A is parameter-free and isolates residual-learning gain; B is preferred at depth because dimension-change shortcuts are rarer and projections elsewhere are expensive in bottleneck blocks.
- **Sensitivity**: low (≤0.65 top-1 difference between A/B/C on ResNet-34).
- **Source**: §3.3 "Residual Network"; §"Identity vs. Projection Shortcuts"; Table 3.

## Activation
- **Value**: ReLU after every (conv, BN) pair, including a final ReLU after the residual sum (Fig. 2).
- **Source**: §3.2 — "We adopt the second nonlinearity after the addition (i.e., σ(y))."

## Head
- **Value**: Global average pooling → 1000-way fc → softmax (ImageNet); 10-way fc → softmax (CIFAR-10).
- **Source**: §3.3.

## CIFAR-10 architecture
- **Value**: First layer 3×3 conv, 16 filters, then `2n` layers each at three feature-map sizes {32×32, 16×16, 8×8} with widths {16, 32, 64}. Total weighted layers = `6n + 2`. Down-sampling by stride-2 conv. Identity shortcuts everywhere (Option A) → ResNets have *exactly* the same depth/width/parameters as plain counterparts.
- **Studied n**: {3, 5, 7, 9, 18, 200} ⇒ depths {20, 32, 44, 56, 110, 1202}.
- **Param counts (Table 6)**: 0.27M, 0.46M, 0.66M, 0.85M, 1.7M, 19.4M for ResNets at those depths.
- **Source**: §4.2; Table 6.
