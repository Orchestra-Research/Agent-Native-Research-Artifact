# Algorithm

## Mathematical Formulation

### Residual Function (§3.1)

For a building block with input x:

$$y = F(x, \{W_i\}) + x$$

Where F is the residual mapping to be learned.

For a two-layer block:

$$F = W_2 \cdot \sigma(W_1 \cdot x)$$

where $\sigma$ denotes ReLU. Biases are omitted for simplicity.

When input and output dimensions differ, a linear projection is applied:

$$y = F(x, \{W_i\}) + W_s \cdot x$$

The operation F + x is performed by element-wise addition after a shortcut connection.

### Bottleneck Function (§4.1)

For a three-layer bottleneck block with input x of dimension d:

$$F(x) = W_3 \cdot \sigma(W_2 \cdot \sigma(W_1 \cdot x))$$

where W_1 is 1x1 (d -> d/4), W_2 is 3x3 (d/4 -> d/4), W_3 is 1x1 (d/4 -> d).

## Pseudocode

```
function ResidualBlock(x, W1, W2, shortcut_type):
    # Residual branch
    h = conv3x3(x, W1)
    h = batch_norm(h)
    h = relu(h)
    h = conv3x3(h, W2)
    h = batch_norm(h)

    # Shortcut branch
    if shortcut_type == "identity":
        s = x
    elif shortcut_type == "projection":
        s = conv1x1(x, Ws, stride=2)
        s = batch_norm(s)

    # Merge
    y = h + s
    y = relu(y)
    return y

function BottleneckBlock(x, W1, W2, W3, shortcut_type):
    h = conv1x1(x, W1)      # reduce
    h = batch_norm(h); h = relu(h)
    h = conv3x3(h, W2)      # spatial
    h = batch_norm(h); h = relu(h)
    h = conv1x1(h, W3)      # restore
    h = batch_norm(h)

    if shortcut_type == "identity":
        s = x
    elif shortcut_type == "projection":
        s = conv1x1(x, Ws, stride=2)
        s = batch_norm(s)

    y = h + s
    y = relu(y)
    return y
```

## Complexity Analysis

From Table 1 and §3.3:

| Model | Layers | FLOPs | Parameters |
|-------|--------|-------|------------|
| VGG-19 | 19 | 19.6 billion | — |
| Plain-34 | 34 | 3.6 billion | — |
| ResNet-34 | 34 | 3.6 billion | — |
| ResNet-50 | 50 | ~3.8 billion | — |
| ResNet-101 | 101 | ~7.6 billion | — |
| ResNet-152 | 152 | 11.3 billion | — |

The 34-layer ResNet has only 18% of the FLOPs of VGG-19, while achieving better accuracy. ResNet-152 has lower complexity than VGG-16/19 in terms of FLOPs.
