# Algorithm: Residual Learning

## Mathematical formulation

Let $\mathcal{H}(\mathbf{x})$ denote the underlying mapping a stack of layers should fit, with $\mathbf{x}$ the input to the first layer in the stack. Rather than fitting $\mathcal{H}$ directly, residual learning hypothesizes a residual function

$$\mathcal{F}(\mathbf{x}) := \mathcal{H}(\mathbf{x}) - \mathbf{x}.$$

The original mapping is recovered as $\mathcal{F}(\mathbf{x}) + \mathbf{x}$. A residual *building block* (Fig. 2) is

$$\mathbf{y} = \mathcal{F}(\mathbf{x}, \{W_i\}) + \mathbf{x} \qquad (\text{Eqn. 1})$$

When the input and output dimensions differ (e.g., on stride-2 down-sampling stages), a linear projection $W_s$ is introduced on the shortcut:

$$\mathbf{y} = \mathcal{F}(\mathbf{x}, \{W_i\}) + W_s \mathbf{x} \qquad (\text{Eqn. 2})$$

For a 2-layer basic block, $\mathcal{F} = W_2 \, \sigma(W_1 \mathbf{x})$, where $\sigma$ is ReLU and biases are omitted. The element-wise add is followed by a second ReLU: $\sigma(\mathbf{y})$. For a 3-layer bottleneck block, $\mathcal{F} = W_3 \, \sigma(W_2 \, \sigma(W_1 \mathbf{x}))$, where $W_1, W_3$ are 1×1 convolutions and $W_2$ is 3×3.

## Pseudocode (forward pass of one residual block)

```
function ResidualBlock(x, F, shortcut_type, downsample):
    # F is the residual function (basic or bottleneck)
    out = F(x)                        # conv -> BN -> ReLU -> conv -> BN
                                      # (or 1x1 -> 3x3 -> 1x1 for bottleneck)
    if dim(out) == dim(x) and not downsample:
        identity = x                  # parameter-free identity shortcut
    else:
        if shortcut_type == "A":
            identity = zero_pad_channels(maybe_stride2(x))   # option A
        else:
            identity = projection(x)  # option B / C: 1x1 conv (+stride 2)
    out = out + identity              # element-wise add
    return ReLU(out)
```

`maybe_stride2(x)` performs the 2× spatial down-sampling that matches the residual function's stride. For ImageNet ResNets, down-sampling occurs at the *first* block of stages `conv3_x`, `conv4_x`, `conv5_x`.

The full network is a stage-by-stage stack of `ResidualBlock` instances (architecture.md), preceded by the 7×7 stem and followed by global average pool + fc + softmax.

## Step-by-step explanation
1. **Pre-process**: subtract per-pixel mean; standard color/scale augmentation; 224×224 random crop on a shorter-side ∈ [256, 480] image.
2. **Stem**: 7×7 conv stride 2 → BN → ReLU → 3×3 max-pool stride 2.
3. **Residual stages**: for each residual block, compute $\mathcal{F}(\mathbf{x})$ by 2 (basic) or 3 (bottleneck) conv layers each followed by BN; the second/third has no ReLU before the addition.
4. **Shortcut add**: identity (option A) or projection (option B/C); element-wise sum.
5. **Block output**: ReLU after the add.
6. **Head**: global average pool over the 7×7 final map → 1000-way fc → softmax.

## Complexity analysis
- Identity shortcut adds **zero** parameters and only an element-wise addition (negligible vs. the conv FLOPs).
- Projection shortcut adds parameters proportional to $C_{in} \cdot C_{out}$ for a 1×1 conv, with FLOPs of $C_{in} \cdot C_{out} \cdot H_{out} \cdot W_{out}$.
- A bottleneck block with identity shortcut has the same time complexity as a basic 2-layer block (paper §"Deeper Bottleneck Architectures"); replacing its identity with a projection roughly *doubles* the block's time complexity and model size.
- Whole-network FLOPs: ResNet-{18, 34, 50, 101, 152} = {1.8, 3.6, 3.8, 7.6, 11.3} × 10⁹ (Table 1). VGG-19 = 19.6 × 10⁹.
- For comparison, the 34-layer plain net has 3.6 × 10⁹ FLOPs (≈18% of VGG-19) — adding identity shortcuts to make ResNet-34 leaves FLOPs unchanged.
