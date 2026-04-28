# Evidence Index

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_imagenet_architectures.md](tables/table1_imagenet_architectures.md) | Table 1, §3.3 | C03, C05 | Per-depth ImageNet ResNet architectures — block layouts and FLOPs for ResNet-{18, 34, 50, 101, 152}. |
| [tables/table2_imagenet_plain_vs_residual.md](tables/table2_imagenet_plain_vs_residual.md) | Table 2, §4.1 | C01, C02 | Top-1 ImageNet validation error — plain-{18, 34} vs. ResNet-{18, 34} with 10-crop testing. |
| [tables/table3_imagenet_validation_full.md](tables/table3_imagenet_validation_full.md) | Table 3, §4.1 | C01, C02, C03, C04, C05 | Full ImageNet validation error table (10-crop): VGG-16, GoogLeNet, PReLU-net, plain-34, ResNet-{34A, 34B, 34C, 50, 101, 152}. |
| [tables/derived_from_table3_shortcut_options.md](tables/derived_from_table3_shortcut_options.md) | Derived from Table 3 | C04 | Subset of Table 3 isolating ResNet-34 shortcut options A / B / C plus plain-34 baseline. |
| [tables/table4_imagenet_singlemodel.md](tables/table4_imagenet_singlemodel.md) | Table 4, §4.1 | C03 | ImageNet single-model validation error (multi-scale fully-convolutional testing). |
| [tables/table5_imagenet_ensembles.md](tables/table5_imagenet_ensembles.md) | Table 5, §4.1 | C03 | ImageNet ensemble top-5 error on the test set — ResNet 6-model ensemble achieves 3.57%. |
| [tables/table6_cifar10.md](tables/table6_cifar10.md) | Table 6, §4.2 | C06, C07 | CIFAR-10 test error vs. depth for ResNet-{20, 32, 44, 56, 110, 1202} with baselines. |
| [tables/table7_pascal_voc_detection.md](tables/table7_pascal_voc_detection.md) | Table 7, §4.3 | C08 | PASCAL VOC 07/12 detection mAP with baseline Faster R-CNN — VGG-16 vs. ResNet-101. |
| [tables/table8_coco_detection.md](tables/table8_coco_detection.md) | Table 8, §4.3 | C08 | COCO val detection mAP with baseline Faster R-CNN — VGG-16 vs. ResNet-101. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/figure1_cifar_plain_curves.md](figures/figure1_cifar_plain_curves.md) | Figure 1, §1 | C01 | CIFAR-10 training (left) and test (right) error curves for plain-{20, 56} — illustrates degradation. |
| [figures/figure4_imagenet_curves.md](figures/figure4_imagenet_curves.md) | Figure 4, §4.1 | C01, C02 | ImageNet training/validation curves: plain-{18, 34} (left) vs. ResNet-{18, 34} (right). |
| [figures/figure6_cifar_curves.md](figures/figure6_cifar_curves.md) | Figure 6, §4.2 | C06 | CIFAR-10 training/test curves for plain (left), ResNet-{20, 32, 44, 56, 110} (middle), and ResNet-{110, 1202} (right). |
| [figures/figure7_layer_response_std.md](figures/figure7_layer_response_std.md) | Figure 7, §4.2 | C02 (Fig. 7 supports the "responses closer to zero" interpretation referenced under O5) | Layer-response std on CIFAR-10 for plain-{20, 56} and ResNet-{20, 56, 110}, in original layer order (top) and ranked by magnitude (bottom). |
