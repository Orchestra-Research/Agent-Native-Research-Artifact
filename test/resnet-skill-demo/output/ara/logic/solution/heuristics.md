# Heuristics

## H01: Batch normalization after each convolution
- **Rationale**: The paper's ImageNet recipe assumes batch normalization as part of the stable optimization setup for both plain and residual comparisons.
- **Sensitivity**: high
- **Bounds**: Applies to the reported ImageNet comparison slice; changing placement changes comparability.
- **Code ref**: [src/execution/residual_block.py, src/execution/training_recipe.py]
- **Source**: Paper implementation details for ImageNet training

## H02: Use SGD with the reported schedule
- **Rationale**: The optimizer schedule is part of the controlled setup that makes the plain-vs-residual comparison meaningful.
- **Sensitivity**: high
- **Bounds**: Batch size 256, momentum 0.9, weight decay 0.0001, initial learning rate 0.1, divide by 10 when error plateaus, train up to `60 x 10^4` iterations.
- **Code ref**: [src/execution/training_recipe.py]
- **Source**: Paper implementation details for ImageNet training

## H03: Preserve the ImageNet augmentation pipeline
- **Rationale**: The reported ImageNet numbers depend on the resize, crop, flip, mean subtraction, and color augmentation procedure described by the paper.
- **Sensitivity**: medium
- **Bounds**: Resize shorter side in `[256, 480]`, random `224 x 224` crop, horizontal flip, per-pixel mean subtraction, standard color augmentation.
- **Code ref**: [src/execution/training_recipe.py]
- **Source**: Paper implementation details for ImageNet training

## H04: Keep dropout disabled in the main comparison
- **Rationale**: The paper explicitly omits dropout so that the observed gains are attributed to residual reformulation rather than added regularization.
- **Sensitivity**: medium
- **Bounds**: Applies to the main ImageNet slice represented in this artifact.
- **Code ref**: [src/execution/training_recipe.py]
- **Source**: Paper implementation details for ImageNet training
