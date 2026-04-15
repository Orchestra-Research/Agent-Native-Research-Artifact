# Concepts

## Residual Function
- **Notation**: F(x) = H(x) − x, where H(x) is the desired underlying mapping and x is the input
- **Definition**: The function learned by a stack of nonlinear layers in a residual block. Instead of learning the full mapping H(x) directly, the layers learn the residual F(x), and the output is F(x) + x. If the optimal mapping is close to identity, pushing F(x) toward zero is easier than fitting an identity with nonlinear layers.
- **Boundary conditions**: Requires input and output dimensions to match for identity shortcuts; when dimensions differ, a linear projection W_s is applied via the shortcut.
- **Related concepts**: Shortcut Connection, Identity Mapping, Degradation Problem

## Shortcut Connection
- **Notation**: y = F(x, {W_i}) + x (identity shortcut); y = F(x, {W_i}) + W_s·x (projection shortcut)
- **Definition**: A connection that skips one or more layers, performing identity mapping (or linear projection) and adding the result to the stacked layers' output via element-wise addition. Introduces neither extra parameters (identity case) nor computational complexity.
- **Boundary conditions**: Three options when dimensions change: (A) zero-padding, (B) projection only for dimension-changing shortcuts, (C) all projections. Option B is used for deeper models.
- **Related concepts**: Residual Function, Identity Mapping, Bottleneck Block

## Degradation Problem
- **Notation**: E_train(deeper) > E_train(shallower) where both are plain networks
- **Definition**: The phenomenon where adding more layers to a deep plain network leads to higher training error (not test error alone), indicating an optimization difficulty rather than overfitting. A construction argument shows that a deeper model's solution space contains the shallower model's solution space, so degradation reveals solver limitations.
- **Boundary conditions**: Observed in plain networks beyond ~30 layers. Addressed (not observed) in residual networks up to 152 layers on ImageNet and 110 layers on CIFAR-10.
- **Related concepts**: Residual Function, Plain Network

## Bottleneck Block
- **Notation**: 1×1 conv (reduce) → 3×3 conv → 1×1 conv (restore), with shortcut
- **Definition**: A three-layer residual building block used in deeper ResNets (50/101/152). The 1×1 convolutions reduce and then restore dimensions, making the 3×3 layer a bottleneck with smaller input/output dimensions. Has similar time complexity to the two-layer basic block. Used in place of the 2-layer block for practical efficiency in deep models.
- **Boundary conditions**: Parameter-free identity shortcuts are critical for bottleneck architectures — replacing identity with projection doubles time complexity and model size.
- **Related concepts**: Residual Function, Shortcut Connection

## Identity Mapping
- **Notation**: y = x (the shortcut path); combined: y = F(x) + x
- **Definition**: A mapping where the output equals the input. In ResNets, the shortcut connection performs identity mapping, allowing the gradient to flow directly through the skip path. The residual reformulation hypothesizes that if the optimal function is close to identity, it is easier to learn F(x) ≈ 0 than to learn H(x) ≈ x with nonlinear layers.
- **Boundary conditions**: Only applicable when input and output dimensions match. When dimensions change, a linear projection is used instead.
- **Related concepts**: Shortcut Connection, Residual Function

## Batch Normalization (BN)
- **Notation**: BN(x) = γ · (x − μ_B) / √(σ²_B + ε) + β
- **Definition**: A normalization technique applied after each convolution and before activation in ResNets. Normalizes activations to zero mean and unit variance within each mini-batch, then applies learnable scale (γ) and shift (β). Addresses vanishing/exploding gradients and enables training of deep networks, but does not solve the degradation problem alone.
- **Boundary conditions**: Requires sufficiently large mini-batch sizes for stable statistics. Used in all ResNet variants. The paper explicitly notes that BN alone does not solve degradation — neither forward nor backward signals vanish with BN, yet deep plain nets still degrade.
- **Related concepts**: Degradation Problem, Plain Network

## Plain Network
- **Notation**: A deep convolutional network without shortcut connections
- **Definition**: A baseline architecture following the VGG design philosophy: (1) same output feature map size → same number of filters, (2) halved feature map size → doubled filters to preserve time complexity per layer. The 34-layer plain net has 3.6 billion FLOPs, only 18% of VGG-19's 19.6 billion FLOPs. Serves as the baseline to demonstrate the degradation problem and the effectiveness of residual learning.
- **Boundary conditions**: Exhibits degradation beyond ~30 layers. The 18-layer and 34-layer variants are used for controlled comparison with their ResNet counterparts.
- **Related concepts**: Degradation Problem, Residual Function
