# Model Configuration

## ImageNet Architectures (Table 1)

### ResNet-18
- **Layers**: 18 weight layers
- **Block type**: Basic (2-layer, 3×3 + 3×3)
- **Blocks per stage**: [2, 2, 2, 2]
- **Channel progression**: [64, 128, 256, 512]
- **FLOPs**: 1.8 × 10⁹
- **Source**: Table 1

### ResNet-34
- **Layers**: 34 weight layers
- **Block type**: Basic (2-layer, 3×3 + 3×3)
- **Blocks per stage**: [3, 4, 6, 3]
- **Channel progression**: [64, 128, 256, 512]
- **FLOPs**: 3.6 × 10⁹
- **Source**: Table 1

### ResNet-50
- **Layers**: 50 weight layers
- **Block type**: Bottleneck (3-layer, 1×1 + 3×3 + 1×1)
- **Blocks per stage**: [3, 4, 6, 3]
- **Channel progression**: [256, 512, 1024, 2048] (bottleneck widths: [64, 128, 256, 512])
- **FLOPs**: 3.8 × 10⁹
- **Source**: Table 1

### ResNet-101
- **Layers**: 101 weight layers
- **Block type**: Bottleneck (3-layer, 1×1 + 3×3 + 1×1)
- **Blocks per stage**: [3, 4, 23, 3]
- **Channel progression**: [256, 512, 1024, 2048] (bottleneck widths: [64, 128, 256, 512])
- **FLOPs**: 7.6 × 10⁹
- **Source**: Table 1

### ResNet-152
- **Layers**: 152 weight layers
- **Block type**: Bottleneck (3-layer, 1×1 + 3×3 + 1×1)
- **Blocks per stage**: [3, 8, 36, 3]
- **Channel progression**: [256, 512, 1024, 2048] (bottleneck widths: [64, 128, 256, 512])
- **FLOPs**: 11.3 × 10⁹
- **Source**: Table 1

## CIFAR-10 Architectures

### General Structure
- **Input**: 32×32 images
- **First layer**: 3×3 conv, 16 filters
- **Stages**: 3 stages with feature map sizes {32, 16, 8} and filter counts {16, 32, 64}
- **Each stage**: 2n layers (n pairs of 3×3 convolutions)
- **Subsampling**: Stride-2 convolution at stage boundaries
- **Head**: Global average pooling → 10-way fc → softmax
- **Total layers**: 6n + 2
- **Shortcuts**: Identity (option A) in all cases
- **Source**: §4.2

### Variants Tested
| n | Total layers | Parameters |
|---|-------------|------------|
| 3 | 20 | 0.27M |
| 5 | 32 | 0.46M |
| 7 | 44 | 0.66M |
| 9 | 56 | 0.85M |
| 18 | 110 | 1.7M |
| 200 | 1202 | 19.4M |

Source: Table 6

## Shared Design Principles
- Same output feature map size → same number of filters
- Feature map size halved → number of filters doubled
- Downsampling by stride-2 convolution (not pooling)
- BN after every convolution, before ReLU
- No dropout
- Global average pooling before classifier
