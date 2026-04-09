# Derived subset - Shortcut options from Table 3

**Source**: Derived from Table 3 in *Deep Residual Learning for Image Recognition*.
**Caption**: Plain-34 and ResNet-34 A/B/C rows used to inspect shortcut option behavior.
**Extraction type**: derived_subset
**Derived from**: `table3_imagenet_validation_full.md`

| Model | Top-1 error (%) | Top-5 error (%) |
| --- | ---: | ---: |
| plain-34 | 28.54 | 10.02 |
| ResNet-34 A | 25.03 | 7.76 |
| ResNet-34 B | 24.52 | 7.46 |
| ResNet-34 C | 24.19 | 7.40 |

## Derived observations

- All shortcut variants A/B/C outperform the plain-34 baseline.
- Option B improves over option A, and option C improves marginally over option B.
