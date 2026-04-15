# Algorithm

## Mathematical Formulation

### Residual Learning Formulation

Let H(x) be the desired underlying mapping for a stack of layers. Instead of learning H(x) directly, the layers learn the residual function:

$$F(x) = H(x) - x$$

The output of the residual block is:

$$y = F(x, \{W_i\}) + x$$

where F(x, {W_i}) represents the residual mapping learned by the stacked layers, and x is the identity shortcut.

### With Projection Shortcut

When input and output dimensions differ (dimension increase at downsampling stages):

$$y = F(x, \{W_i\}) + W_s x$$

where W_s is a linear projection (implemented as 1×1 convolution with stride 2) used only to match dimensions.

### Two-Layer Basic Block (ResNet-18/34)

$$y = W_2 \cdot \sigma(BN(W_1 \cdot x)) + x$$

where σ is ReLU, BN is batch normalization, and W_1, W_2 are 3×3 convolution weight matrices.

### Three-Layer Bottleneck Block (ResNet-50/101/152)

$$y = W_3 \cdot \sigma(BN(W_2 \cdot \sigma(BN(W_1 \cdot x)))) + x$$

where W_1 is 1×1 (reduce), W_2 is 3×3, W_3 is 1×1 (restore).

## Pseudocode

```python
def residual_block_basic(x, W1, W2, shortcut_proj=None):
    """Basic 2-layer residual block (ResNet-18/34)."""
    identity = x

    out = conv3x3(x, W1)
    out = batch_norm(out)
    out = relu(out)

    out = conv3x3(out, W2)
    out = batch_norm(out)

    if shortcut_proj is not None:
        identity = conv1x1(x, shortcut_proj, stride=2)
        identity = batch_norm(identity)

    out = out + identity
    out = relu(out)
    return out


def residual_block_bottleneck(x, W1, W2, W3, shortcut_proj=None):
    """3-layer bottleneck block (ResNet-50/101/152)."""
    identity = x

    out = conv1x1(x, W1)       # reduce dimensions
    out = batch_norm(out)
    out = relu(out)

    out = conv3x3(out, W2)     # 3x3 convolution
    out = batch_norm(out)
    out = relu(out)

    out = conv1x1(out, W3)     # restore dimensions
    out = batch_norm(out)

    if shortcut_proj is not None:
        identity = conv1x1(x, shortcut_proj, stride=2)
        identity = batch_norm(identity)

    out = out + identity
    out = relu(out)
    return out


def resnet(x, blocks_per_stage, block_type):
    """Full ResNet forward pass."""
    # Initial convolution
    x = conv7x7(x, stride=2)
    x = batch_norm(x)
    x = relu(x)
    x = max_pool(x, 3, stride=2)

    # 4 stages with increasing channels [64, 128, 256, 512]
    for stage in range(4):
        for block in range(blocks_per_stage[stage]):
            stride = 2 if (stage > 0 and block == 0) else 1
            x = block_type(x, stride=stride)

    # Classification head
    x = global_avg_pool(x)
    x = fully_connected(x, num_classes=1000)
    return softmax(x)
```

## Complexity Analysis

### Time Complexity
- Basic block: 2 × (3×3 × C × C × H × W) = 18C²HW FLOPs
- Bottleneck block: (1×1 × 4C × C + 3×3 × C × C + 1×1 × C × 4C) × H × W = (4C² + 9C² + 4C²)HW = 17C²HW FLOPs
- The bottleneck block has similar per-block complexity to the basic block despite having 3 layers

### Space Complexity
- Identity shortcuts add zero parameters
- Projection shortcuts (option B) add W_s parameters only at dimension-change boundaries (3 projections in a typical ResNet)
- ResNet-34: 3.6 billion FLOPs (18% of VGG-19)
- ResNet-152: 11.3 billion FLOPs (still less than VGG-16/19's 15.3/19.6 billion FLOPs)
