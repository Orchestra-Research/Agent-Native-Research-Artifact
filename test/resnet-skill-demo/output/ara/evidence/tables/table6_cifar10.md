# Table 6 - Classification error on the CIFAR-10 test set

**Source**: Table 6 in "Deep Residual Learning for Image Recognition"
**Caption**: "Classification error on the CIFAR-10 test set. All methods are with data augmentation. For ResNet-110, we run it 5 times and show 'best (mean±std)' as in [43]."
**Extraction type**: raw_table

| method | # layers | # params | error (%) |
|--------|----------|----------|-----------|
| FitNet [35] | 19 | 2.5M | 8.39 |
| Highway [42, 43] | 19 | 2.3M | 7.54 (7.72±0.16) |
| Highway [42, 43] | 32 | 1.25M | 8.80 |
| ResNet | 20 | 0.27M | 8.75 |
| ResNet | 32 | 0.46M | 7.51 |
| ResNet | 44 | 0.66M | 7.17 |
| ResNet | 56 | 0.85M | 6.97 |
| ResNet | 110 | 1.7M | 6.43 (6.61±0.16) |
| ResNet | 1202 | 19.4M | 7.93 |
