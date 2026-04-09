# Training Configuration

## Optimizer
- **Value**: SGD
- **Rationale**: The paper's ImageNet experiments use SGD as the base optimizer for both plain and residual comparisons.
- **Search range**: Not specified in paper
- **Sensitivity**: high
- **Source**: ImageNet implementation details

## Batch size
- **Value**: 256
- **Rationale**: The reported ImageNet recipe uses a batch size of 256.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: ImageNet implementation details

## Initial learning rate
- **Value**: 0.1
- **Rationale**: Forms the starting point of the reported ImageNet training schedule.
- **Search range**: Not specified in paper
- **Sensitivity**: high
- **Source**: ImageNet implementation details

## Learning-rate schedule
- **Value**: divide by 10 when the error plateaus
- **Rationale**: Preserves the schedule described by the paper for the matched comparisons.
- **Search range**: plateau timing not specified
- **Sensitivity**: high
- **Source**: ImageNet implementation details

## Momentum
- **Value**: 0.9
- **Rationale**: Standard setting reported for the ImageNet experiments.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: ImageNet implementation details

## Weight decay
- **Value**: 0.0001
- **Rationale**: Reported regularization setting in the ImageNet recipe.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: ImageNet implementation details

## Maximum iterations
- **Value**: `60 x 10^4`
- **Rationale**: Upper bound for the reported ImageNet training run length.
- **Search range**: Not specified in paper
- **Sensitivity**: low
- **Source**: ImageNet implementation details
