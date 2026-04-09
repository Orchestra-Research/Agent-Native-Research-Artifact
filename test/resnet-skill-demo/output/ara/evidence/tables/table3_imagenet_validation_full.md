# Table 3 - ImageNet Validation, Shortcut Options and Residual Depth

**Source**: Table 3 in *Deep Residual Learning for Image Recognition*.
**Caption**: Error rates (%, 10-crop testing) on ImageNet validation. VGG-16 is based on the authors' test. ResNet-50/101/152 are of option B that only uses projections for increasing dimensions.
**Extraction type**: raw_table

| Model | Top-1 error (%) | Top-5 error (%) |
| --- | ---: | ---: |
| VGG-16 | 28.07 | 9.33 |
| GoogLeNet | - | 9.15 |
| PReLU-net | 24.27 | 7.38 |
| plain-34 | 28.54 | 10.02 |
| ResNet-34 A | 25.03 | 7.76 |
| ResNet-34 B | 24.52 | 7.46 |
| ResNet-34 C | 24.19 | 7.40 |
| ResNet-50 | 22.85 | 6.71 |
| ResNet-101 | 21.75 | 6.05 |
| ResNet-152 | 21.43 | 5.71 |

## Derived observations

- All residual variants in the table outperform `plain-34`.
- Option B is slightly better than option A, and option C is slightly better than option B.
- The deeper residual models continue to reduce top-1 and top-5 error relative to the 34-layer residual variants.
