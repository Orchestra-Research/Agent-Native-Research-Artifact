# Algorithm

## Mathematical Formulation

Instead of fitting `H(x)` directly, the residual block learns:

`F(x) := H(x) - x`

so the block output is:

`y = F(x, {W_i}) + x`

When dimensions do not match:

`y = F(x, {W_i}) + W_s x`

where `W_s` is a learned projection, typically a 1x1 convolution.

## Pseudocode

```text
function residual_block(x, conv1, bn1, conv2, bn2, shortcut):
    residual = conv1(x)
    residual = bn1(residual)
    residual = relu(residual)
    residual = conv2(residual)
    residual = bn2(residual)

    skip = shortcut(x)
    y = residual + skip
    return relu(y)
```

## Step-by-step Explanation

1. Apply the first convolution, normalization, and activation to produce an intermediate residual feature.
2. Apply the second convolution and normalization to complete the residual branch.
3. Route the input through either an identity shortcut or a projection shortcut.
4. Add the shortcut output to the residual branch output.
5. Apply ReLU after the merge.

## Complexity Analysis

- For the basic 18/34-layer block, the residual branch uses two 3x3 convolutions.
- The identity-shortcut case adds negligible parameter cost beyond the residual branch itself.
- Projection shortcuts add parameters only at stage transitions where dimensions change.
