# Training Configuration

## ImageNet Training

### Learning rate
- **Value**: 0.1 (initial), divided by 10 when error plateaus
- **Rationale**: Standard SGD schedule; division at plateaus allows fine-grained convergence
- **Search range**: Not specified in paper
- **Sensitivity**: high
- **Source**: §3.4

### Mini-batch size
- **Value**: 256
- **Rationale**: Standard batch size for ImageNet SGD training
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §3.4

### Weight decay
- **Value**: 0.0001
- **Rationale**: Standard L2 regularization
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: §3.4

### Momentum
- **Value**: 0.9
- **Rationale**: Standard SGD momentum value
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: §3.4

### Training iterations
- **Value**: Up to 60 × 10⁴ iterations
- **Rationale**: Sufficient for convergence on ImageNet with the learning rate schedule
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §3.4

### Dropout
- **Value**: Not used
- **Rationale**: Following practice in [16] (BN paper); focus is on optimization, not regularization
- **Search range**: N/A
- **Sensitivity**: low
- **Source**: §3.4

## CIFAR-10 Training

### Learning rate
- **Value**: 0.1 (initial), divided by 10 at 32k and 48k iterations; for 110-layer: 0.01 warm-up until error < 80%, then 0.1
- **Rationale**: Standard schedule with warm-up needed for very deep networks
- **Search range**: Not specified in paper
- **Sensitivity**: high
- **Source**: §4.2

### Mini-batch size
- **Value**: 128
- **Rationale**: Standard for CIFAR-10
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §4.2

### Training iterations
- **Value**: Terminate at 64k iterations
- **Rationale**: Determined on a 45k/5k train/val split
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §4.2

### Weight decay
- **Value**: 0.0001
- **Rationale**: Same as ImageNet
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: §4.2

### Momentum
- **Value**: 0.9
- **Rationale**: Same as ImageNet
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: §4.2

### Data augmentation (CIFAR-10)
- **Value**: 4 pixels padded on each side, random 32×32 crop from padded image or horizontal flip
- **Rationale**: Following simple data augmentation in [24]
- **Search range**: N/A
- **Sensitivity**: medium
- **Source**: §4.2
