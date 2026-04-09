# Architecture

## Residual Block

- **Purpose**: Replace a plain stacked mapping with a residual branch plus shortcut merge.
- **Inputs**: Feature tensor `x` with shape `[B, C, H, W]`
- **Outputs**: Feature tensor `y` with matched or projected channel/stride shape
- **Interactions**: Feeds stage-to-stage through repeated block composition
- **Key design choices**:
  - Two 3x3 convolutions for the 18/34-layer family
  - Identity shortcut when dimensions match
  - Projection or padding when dimensions change
  - Element-wise addition followed by ReLU

## Shortcut Path

- **Purpose**: Preserve an identity-compatible route for information and gradients
- **Inputs**: Block input `x`
- **Outputs**: Either `x` or `W_s x`
- **Interactions**: Added to the residual branch output before activation
- **Key design choices**:
  - Option A: identity with zero-padding when dimensions increase
  - Option B: projection only when dimensions increase
  - Option C: projection for all shortcuts

## Stage Stack

- **Purpose**: Organize feature extraction across ImageNet spatial scales
- **Inputs**: Stem output from the initial 7x7 convolution and max-pooling
- **Outputs**: Stage-wise features at 56x56, 28x28, 14x14, and 7x7
- **Interactions**: Repeated residual blocks compose each stage
- **Key design choices**:
  - `conv2_x` through `conv5_x` organize depth at decreasing resolution
  - Depth scaling changes block counts while preserving the stage abstraction

## Classification Head

- **Purpose**: Convert final spatial features into ImageNet logits
- **Inputs**: Final 7x7 feature map stack
- **Outputs**: 1000-way class logits
- **Interactions**: Global average pooling feeds the final fully connected classifier
- **Key design choices**:
  - Global average pooling avoids large fully connected hidden stacks
  - Final classifier remains simple so the comparison isolates the residual mechanism
