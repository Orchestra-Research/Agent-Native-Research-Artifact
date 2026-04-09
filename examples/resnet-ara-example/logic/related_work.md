# Related Work

## RW01: Simonyan and Zisserman, 2014
- **DOI**: arXiv:1409.1556
- **Type**: bounds
- **Delta**:
  - What changed: VGG-style depth established that deeper CNNs can improve ImageNet performance.
  - Why: ResNet uses this as the backdrop for asking why further plain-depth scaling breaks optimization.
- **Claims affected**: C01, C02
- **Adopted elements**: Deep convolutional stage stacking as the baseline design pattern

## RW02: Ioffe and Szegedy, 2015
- **DOI**: arXiv:1502.03167
- **Type**: imports
- **Delta**:
  - What changed: Batch normalization improves optimization stability in deep networks.
  - Why: ResNet inherits BN as a prerequisite but argues it is insufficient by itself to remove degradation.
- **Claims affected**: C01, C02
- **Adopted elements**: Batch normalization in the ImageNet training recipe

## RW03: Srivastava et al., 2015
- **DOI**: arXiv:1505.00387
- **Type**: baseline
- **Delta**:
  - What changed: Highway Networks introduced shortcut-like paths with gating.
  - Why: ResNet contrasts its always-open identity shortcut with gated highways to justify a simpler residual formulation.
- **Claims affected**: C01, C03
- **Adopted elements**: Shortcut-style architectural motivation
