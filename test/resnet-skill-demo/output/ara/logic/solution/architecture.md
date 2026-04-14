# Architecture

## Residual Block (Basic)

The fundamental building block for ResNet-18 and ResNet-34.

- **Input**: Feature tensor x of shape (H, W, C)
- **Output**: y = F(x) + x of shape (H, W, C)
- **Components**:
  - 3x3 conv (C filters, stride 1, padding 1) -> BN -> ReLU
  - 3x3 conv (C filters, stride 1, padding 1) -> BN
  - Element-wise addition with shortcut x
  - ReLU
- **Key design choice**: No dropout; BN is applied after each convolution and before activation (§3.4)

## Residual Block (Bottleneck)

The building block for ResNet-50, ResNet-101, and ResNet-152.

- **Input**: Feature tensor x of shape (H, W, 4C)
- **Output**: y = F(x) + x of shape (H, W, 4C)
- **Components**:
  - 1x1 conv (C filters) -> BN -> ReLU (dimension reduction)
  - 3x3 conv (C filters) -> BN -> ReLU (spatial convolution)
  - 1x1 conv (4C filters) -> BN (dimension restoration)
  - Element-wise addition with shortcut x
  - ReLU
- **Key design choice**: Parameter-free identity shortcuts are especially important here; projection shortcuts would double time complexity and model size (§4.1)

## Shortcut Connection

- **Identity shortcut**: y = F(x) + x; used when dimensions match
- **Projection shortcut**: y = F(x) + W_s * x; used when dimensions change (done by 1x1 conv with stride 2)
- **Options evaluated**:
  - (A) Zero-padding for dimension increase, identity elsewhere
  - (B) Projection only for dimension changes, identity elsewhere
  - (C) All shortcuts are projections

## Stage-Level Design

Following VGG philosophy (§3.3):

| Stage | Output size | ResNet-34 blocks | ResNet-50/101/152 blocks | Filters |
|-------|-------------|------------------|--------------------------|---------|
| conv1 | 112x112 | 7x7 conv, stride 2 | 7x7 conv, stride 2 | 64 |
| pool | 56x56 | 3x3 max pool, stride 2 | 3x3 max pool, stride 2 | 64 |
| conv2_x | 56x56 | 3 basic blocks | 3/3/3 bottleneck blocks | 64 (256) |
| conv3_x | 28x28 | 4 basic blocks | 4/4/8 bottleneck blocks | 128 (512) |
| conv4_x | 14x14 | 6 basic blocks | 6/23/36 bottleneck blocks | 256 (1024) |
| conv5_x | 7x7 | 3 basic blocks | 3/3/3 bottleneck blocks | 512 (2048) |
| output | 1x1 | global avg pool, 1000-d fc, softmax | same | — |

Rules:
- Same feature map size -> same number of filters
- Feature map size halves -> number of filters doubles
- Downsampling by stride-2 convolutions at conv3_1, conv4_1, conv5_1
