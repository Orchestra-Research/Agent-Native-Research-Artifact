# Architecture

The ImageNet ResNet family is a stage-structured CNN. Per Table 1 / Fig. 3, every variant
shares the same five-stage skeleton; only the residual-block type and the per-stage block
count change with depth.

## Component graph

### Stem (`conv1`)
- **Inputs**: 224×224×3 image (per-pixel mean subtracted, ImageNet color/scale augmented).
- **Operation**: 7×7 conv, 64 filters, stride 2 → BN → ReLU → 3×3 max-pool, stride 2.
- **Outputs**: 56×56×64 feature map.
- **Notes**: Identical for every ResNet-{18, 34, 50, 101, 152}.

### Stage `conv2_x` (output 56×56)
- **Inputs**: 56×56×64.
- **Operation**: Stack of residual blocks. Basic block (ResNet-18/34): two 3×3 convs, 64 filters. Bottleneck (ResNet-50/101/152): 1×1, 64 → 3×3, 64 → 1×1, 256.
- **Block counts**: ResNet-18 ×2, ResNet-34 ×3, ResNet-50/101/152 ×3.
- **Outputs**: 56×56×64 (basic) or 56×56×256 (bottleneck).
- **Notes**: First block of `conv2_x` does not down-sample.

### Stages `conv3_x` (28×28), `conv4_x` (14×14), `conv5_x` (7×7)
- **Inputs**: previous stage's feature map.
- **Operation**: First block of each stage uses **stride 2** in the 3×3 conv to halve spatial size; channel count doubles. Subsequent blocks keep size and channels.
- **Block counts (basic)**: ResNet-18 — {2, 2, 2}; ResNet-34 — {4, 6, 3}.
- **Block counts (bottleneck)**: ResNet-50 — {4, 6, 3}; ResNet-101 — {4, 23, 3}; ResNet-152 — {8, 36, 3}.
- **Channel widths (basic)**: 128 → 256 → 512.
- **Channel widths (bottleneck)**: middle 128/256/512, output 512/1024/2048.
- **Outputs**: 28×28×{128 | 512}, 14×14×{256 | 1024}, 7×7×{512 | 2048} respectively.

### Residual block variants
- **Basic block (ResNet-18/34)**: `[3×3 conv → BN → ReLU → 3×3 conv → BN] + shortcut → ReLU` (Fig. 2). Total 2 weighted layers.
- **Bottleneck block (ResNet-50/101/152)**: `[1×1 conv → BN → ReLU → 3×3 conv → BN → ReLU → 1×1 conv → BN] + shortcut → ReLU` (Fig. 5 right). Total 3 weighted layers.
- **Shortcut paths**:
  - Identity (option A): direct add; for dimension-changing blocks, zero-pad extra channels and use stride-2 sampling.
  - Projection (option B/C): 1×1 conv with stride 2 (when down-sampling) and matching output channels. Default in deeper bottleneck nets is option B (projection only on dimension changes).

### Head
- **Inputs**: 7×7×{512 | 2048} feature map.
- **Operation**: Global average pooling → 1000-d fully-connected softmax.
- **Outputs**: 1000-class probability vector.

### CIFAR-10 architecture (separate variant)
- 32×32×3 input → first 3×3 conv with 16 filters → three feature-map sizes {32, 16, 8} with widths {16, 32, 64} and 2n layers each (total 6n+2 weighted layers) → global average pool → 10-way fc + softmax.
- Down-sampling done by stride-2 convolutions; **option A identity shortcuts everywhere**, so the residual nets have *exactly* the same parameter, depth, and width as the plain counterparts.

## Per-depth complexity (from Table 1)

| Depth | Block type | FLOPs | Block layout (conv2..conv5) |
|-------|------------|-------|------------------------------|
| 18  | basic       | 1.8×10⁹ | 2, 2, 2, 2 |
| 34  | basic       | 3.6×10⁹ | 3, 4, 6, 3 |
| 50  | bottleneck  | 3.8×10⁹ | 3, 4, 6, 3 |
| 101 | bottleneck  | 7.6×10⁹ | 3, 4, 23, 3 |
| 152 | bottleneck  | 11.3×10⁹ | 3, 8, 36, 3 |

For reference: VGG-19 = 19.6×10⁹ FLOPs (Table 1 caption), so ResNet-152 is roughly **8× deeper** at **~57% of the FLOPs**.

## Key design choices
- **VGG-style design rules** (§3.3): same output map size ⇒ same #filters; halving spatial size ⇒ doubling #filters.
- **Down-sampling by stride-2 conv**, not by pooling, in `conv3_1`, `conv4_1`, `conv5_1`.
- **Single 3×3 conv per layer** in basic blocks; bottleneck reduces the high-dim 1×1 ↔ 3×3 cost.
- **No dropout** anywhere (§3.4).
- **BN after every conv, before activation** (§3.4).
