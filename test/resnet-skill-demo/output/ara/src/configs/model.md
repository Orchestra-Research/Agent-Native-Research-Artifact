# Model Configuration

## Stem convolution
- **Value**: 7x7 convolution, 64 channels, stride 2
- **Rationale**: Reported ImageNet entry stem for the family used in the comparisons.
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: ResNet architecture description

## Pooling stem
- **Value**: 3x3 max pooling, stride 2
- **Rationale**: Standard front-end before the residual stage stack.
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: ResNet architecture description

## Basic block layout
- **Value**: two 3x3 convolutions per block for 18/34-layer models
- **Rationale**: This is the novel residual block structure used in the core comparison slice.
- **Search range**: Not specified in paper
- **Sensitivity**: high
- **Source**: Figure 2 and architecture section

## Shortcut policy
- **Value**: identity when dimensions match; zero-padding or projection when dimensions differ
- **Rationale**: Preserves an identity-compatible path while handling stage transitions.
- **Search range**: options A, B, and C in the paper
- **Sensitivity**: medium
- **Source**: Shortcut-option discussion in the architecture section

## Classification head
- **Value**: global average pooling plus fully connected classifier
- **Rationale**: Keeps the comparison focused on the residual body rather than a complex classifier head.
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: Architecture description
