# Architecture

## Component Graph

### Input Pipeline
- **Purpose**: Image preprocessing and augmentation
- **Inputs**: Raw image (variable size)
- **Outputs**: 224×224 crop (ImageNet) or 32×32 image (CIFAR-10)
- **Key design choices**: Random crop from [256, 480] resized image, horizontal flip, per-pixel mean subtraction, standard color augmentation

### Convolutional Backbone (Plain Baseline)
- **Purpose**: Feature extraction following VGG design philosophy
- **Inputs**: 224×224×3 image
- **Outputs**: 7×7 feature map
- **Design rules**:
  1. Same output feature map size → same number of filters
  2. Feature map size halved → number of filters doubled (to preserve time complexity per layer)
- **Key design choices**: 3×3 convolutions throughout; downsampling by stride-2 convolutions (not pooling); ends with global average pooling + 1000-way fc + softmax
- **Interactions**: Serves as the baseline and as the template for the residual variant

### Residual Block (Basic)
- **Purpose**: Core building block for ResNet-18 and ResNet-34
- **Inputs**: Feature map x of shape (H, W, C)
- **Outputs**: Feature map y = F(x) + x of shape (H, W, C) (same dimensions) or (H/2, W/2, 2C) (with downsampling)
- **Components**:
  - Two 3×3 convolutional layers with BN and ReLU
  - Shortcut connection (identity or projection)
- **Key design choices**: BN after each convolution, before activation; no dropout

### Bottleneck Block
- **Purpose**: Efficient building block for ResNet-50/101/152
- **Inputs**: Feature map x of shape (H, W, 4C)
- **Outputs**: Feature map y = F(x) + x of shape (H, W, 4C)
- **Components**:
  - 1×1 conv (reduce from 4C to C) + BN + ReLU
  - 3×3 conv (C to C) + BN + ReLU
  - 1×1 conv (restore from C to 4C) + BN
  - Shortcut connection + ReLU
- **Key design choices**: Similar time complexity to 2-layer basic block; identity shortcuts are critical (projection shortcuts would double time and model size)

### Shortcut Connection
- **Purpose**: Enable identity mapping or linear projection across layers
- **Inputs**: Feature map x from before the residual block
- **Outputs**: x (identity) or W_s·x (projection)
- **Variants**:
  - Option A: Identity with zero-padding for dimension increase
  - Option B: Projection (1×1 conv) only when dimensions change, identity elsewhere
  - Option C: All projections
- **Key design choices**: Option B used for deeper models; downsampling shortcuts use stride 2

### Classification Head
- **Purpose**: Map features to class predictions
- **Inputs**: Final feature map (7×7 for ImageNet, 8×8 for CIFAR-10)
- **Outputs**: Class logits (1000-dim for ImageNet, 10-dim for CIFAR-10)
- **Components**: Global average pooling → fully-connected layer → softmax
- **Key design choices**: Single fc layer (no hidden fc layers unlike VGG)

## Architecture Variants (ImageNet)

| Variant | Layers | Block Type | FLOPs | Parameters |
|---------|--------|------------|-------|------------|
| ResNet-18 | 18 | Basic (2-layer) | 1.8×10⁹ | — |
| ResNet-34 | 34 | Basic (2-layer) | 3.6×10⁹ | — |
| ResNet-50 | 50 | Bottleneck (3-layer) | 3.8×10⁹ | — |
| ResNet-101 | 101 | Bottleneck (3-layer) | 7.6×10⁹ | — |
| ResNet-152 | 152 | Bottleneck (3-layer) | 11.3×10⁹ | — |

Note: ResNet-152 (11.3 billion FLOPs) has lower complexity than VGG-16/19 (15.3/19.6 billion FLOPs).
