# Training Hyperparameters

## Optimizer
- **Value**: SGD with momentum
- **Rationale**: Standard choice for ImageNet classification at the time
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: §3.4

## Learning Rate
- **Value**: 0.1 (initial), divided by 10 when error plateaus
- **Rationale**: Plateau-driven schedule allows fast initial convergence then fine-tuning
- **Search range**: Not specified in paper
- **Sensitivity**: high
- **Source**: §3.4

## Weight Decay
- **Value**: 0.0001
- **Rationale**: Standard regularization
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: §3.4

## Momentum
- **Value**: 0.9
- **Rationale**: Standard SGD momentum
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: §3.4

## Mini-batch Size
- **Value**: 256
- **Rationale**: Not discussed; standard ImageNet training batch size
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §3.4

## Training Duration
- **Value**: Up to 60x10^4 iterations
- **Rationale**: Sufficient for convergence with the plateau-driven lr schedule
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §3.4

## Data Augmentation
- **Value**: Shorter side randomly sampled in [256, 480], 224x224 random crop, horizontal flip, per-pixel mean subtracted, standard color augmentation from [21]
- **Rationale**: Following the practice in [21, 41] for ImageNet training
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §3.4

## Dropout
- **Value**: Not used
- **Rationale**: Following the practice in [14, 16]; deep thin architectures regularize by design
- **Search range**: N/A
- **Sensitivity**: low
- **Source**: §3.4
