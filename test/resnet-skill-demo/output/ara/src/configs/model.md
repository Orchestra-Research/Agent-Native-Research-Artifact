# Model Configuration

## Base Architecture Design Rules (§3.3)
- **Value**: VGG-style: (1) same feature map size -> same number of filters, (2) halve feature map -> double filters
- **Rationale**: Keeps computational cost roughly uniform per layer
- **Sensitivity**: low
- **Source**: §3.3

## Convolutional Filters
- **Value**: 3x3 throughout (basic blocks); 1x1-3x3-1x1 (bottleneck blocks)
- **Rationale**: 3x3 is the smallest size that captures spatial patterns; bottleneck reduces parameters at greater depth
- **Sensitivity**: low
- **Source**: §3.3, §4.1

## Downsampling
- **Value**: Stride-2 convolutions at conv3_1, conv4_1, conv5_1 (not pooling layers)
- **Rationale**: First layer of each stage changes spatial dimensions; only conv1 uses 7x7 stride-2, and one 3x3 max pool follows conv1
- **Sensitivity**: low
- **Source**: Table 1, §3.3

## ResNet-34 (Basic Blocks)
- **Value**: [3, 4, 6, 3] basic blocks across 4 stages; total 34 weighted layers; 3.6 billion FLOPs
- **Rationale**: Matched to 34-layer plain network for controlled comparison
- **Sensitivity**: medium
- **Source**: Table 1, Figure 3

## ResNet-50 (Bottleneck Blocks)
- **Value**: [3, 4, 6, 3] bottleneck blocks; 50 weighted layers; ~3.8 billion FLOPs
- **Rationale**: Each 2-layer basic block is replaced by a 3-layer bottleneck; similar FLOPs to ResNet-34
- **Sensitivity**: medium
- **Source**: Table 1, §4.1

## ResNet-101 (Bottleneck Blocks)
- **Value**: [3, 4, 23, 3] bottleneck blocks; 101 weighted layers; ~7.6 billion FLOPs
- **Rationale**: Deeper conv4_x stage (23 blocks) captures richer mid-level representations
- **Sensitivity**: medium
- **Source**: Table 1

## ResNet-152 (Bottleneck Blocks)
- **Value**: [3, 8, 36, 3] bottleneck blocks; 152 weighted layers; 11.3 billion FLOPs (still less than VGG-16/19)
- **Rationale**: Deepest single model evaluated; achieves 21.43% top-1 (10-crop) and 19.38% (single-model, Table 4)
- **Sensitivity**: medium
- **Source**: Table 1, Table 3, Table 4

## Classifier Head
- **Value**: Global average pooling -> 1000-d fully-connected -> softmax
- **Rationale**: Standard ImageNet classification head; global avg pool replaces flatten to reduce parameters
- **Sensitivity**: low
- **Source**: Table 1, §3.3
