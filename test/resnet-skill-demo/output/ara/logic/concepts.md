# Concepts

## Residual Learning
- **Notation**: F(x) := H(x) - x, where H(x) is the desired underlying mapping
- **Definition**: A learning framework where stacked layers fit a residual function F(x) = H(x) - x rather than the unreferenced mapping H(x) directly. The original mapping is recovered as F(x) + x.
- **Boundary conditions**: Requires that the input x and output F(x) have compatible dimensions. When dimensions differ, a linear projection W_s is applied to x.
- **Related concepts**: Shortcut Connection, Identity Mapping, Degradation Problem

## Shortcut Connection
- **Notation**: y = F(x, {W_i}) + x (identity); y = F(x, {W_i}) + W_s * x (projection)
- **Definition**: A connection that skips one or more layers, performing identity mapping (or linear projection) and adding the result element-wise to the output of the stacked layers. Introduces neither extra parameters (identity case) nor computational complexity.
- **Boundary conditions**: Identity shortcuts apply when input and output dimensions match. When dimensions change (e.g., feature map size halves and channels double), a projection shortcut with stride 2 is used.
- **Related concepts**: Residual Learning, Identity Mapping, Bottleneck Architecture

## Degradation Problem
- **Notation**: E_train(deeper) > E_train(shallower) where E_train denotes training error
- **Definition**: The phenomenon where increasing network depth in plain (non-residual) architectures leads to higher training error, not caused by overfitting but by optimization difficulty. Demonstrated empirically by comparing 18-layer and 34-layer plain networks.
- **Boundary conditions**: Observed in plain networks without shortcut connections. Does not occur (or is greatly alleviated) in residual networks.
- **Related concepts**: Residual Learning, Plain Network

## Bottleneck Architecture
- **Notation**: 1x1 conv (reduce) -> 3x3 conv -> 1x1 conv (restore)
- **Definition**: A three-layer residual block design used for deeper ResNets (50/101/152 layers). The 1x1 layers reduce and then restore dimensions, with the 3x3 layer operating on a lower-dimensional bottleneck. Used instead of the two-layer 3x3 block to manage computational cost at greater depths.
- **Boundary conditions**: Parameter-free identity shortcuts are particularly important for bottleneck designs, as replacing them with projections would double the time complexity and model size (§4.1).
- **Related concepts**: Shortcut Connection, Residual Learning

## Identity Mapping
- **Notation**: y = x (pure identity); realized via F(x) + x where F(x) -> 0
- **Definition**: A mapping where the output equals the input. In the residual learning context, if the optimal mapping is close to identity, the residual function F(x) only needs to approximate zero. This is hypothesized to be easier for solvers than learning identity through stacked nonlinear layers.
- **Boundary conditions**: Applies when input and output have the same dimensions. Not directly applicable when spatial dimensions or channel counts change between stages.
- **Related concepts**: Residual Learning, Shortcut Connection

## Plain Network
- **Notation**: H(x) = f_L(...f_2(f_1(x)))
- **Definition**: A convolutional network without shortcut connections, where layers are simply stacked sequentially. The paper's plain baselines follow the VGG philosophy: (1) same feature map size implies same number of filters, (2) halving feature map size doubles filters. Downsampling uses stride-2 convolutions.
- **Boundary conditions**: Subject to the degradation problem at depths beyond ~18 layers on ImageNet. The 34-layer plain network has only 3.6 billion FLOPs, 18% of VGG-19.
- **Related concepts**: Degradation Problem, Residual Learning
