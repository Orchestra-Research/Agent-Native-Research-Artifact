# Table 2 - ImageNet Validation, Plain vs. Residual

**Source**: Table 2 and the surrounding discussion in *Deep Residual Learning for Image Recognition*.
**Caption**: Top-1 error (%, 10-crop testing) on ImageNet validation.
**Extraction type**: raw_table

| Model family | Depth | Top-1 error (%) |
| --- | ---: | ---: |
| Plain | 18 | 27.94 |
| Plain | 34 | 28.54 |
| ResNet | 18 | 27.88 |
| ResNet | 34 | 25.03 |

## Derived observations

- The deeper plain model is worse than the shallower plain model.
- The deeper residual model is better than the shallower residual model.
- The 34-layer residual model improves by 3.51 points over the 34-layer plain model.
