# Experiments

## E01: Plain network degradation on ImageNet
- **Verifies**: C02
- **Setup**:
  - Model: 18-layer and 34-layer plain networks (Table 1)
  - Hardware: Not specified in paper
  - Dataset: ImageNet 2012, 1.28M training images, 50k validation images, 1000 classes
  - System: SGD, mini-batch 256, BN after each convolution
- **Procedure**:
  1. Train 18-layer plain network from scratch on ImageNet
  2. Train 34-layer plain network from scratch with identical training protocol
  3. Compare training error curves (Figure 4 left)
  4. Compare top-1 validation error (10-crop testing)
- **Metrics**: Top-1 validation error (%, 10-crop), training error curves
- **Expected outcome**:
  - The deeper 34-layer plain network should have higher training error than the 18-layer plain network throughout training
  - The deeper plain network should have higher validation error
- **Baselines**: 18-layer plain network serves as the shallower baseline
- **Dependencies**: none

## E02: Residual network performance on ImageNet
- **Verifies**: C01, C03, C05
- **Setup**:
  - Model: ResNet-18, ResNet-34, ResNet-50, ResNet-101, ResNet-152 (Table 1)
  - Hardware: Not specified in paper
  - Dataset: ImageNet 2012, 1.28M training images, 50k validation images, 1000 classes
  - System: SGD, mini-batch 256, learning rate 0.1 divided by 10 at error plateaus, BN, no dropout
- **Procedure**:
  1. Train ResNet-18 and ResNet-34 with option A shortcuts (identity, zero-padding)
  2. Train ResNet-50, ResNet-101, ResNet-152 with option B shortcuts (bottleneck blocks)
  3. Compare validation error across depths (Table 3, Table 4)
  4. Compare against prior state-of-the-art (Table 4, Table 5)
  5. Evaluate ensemble on test set (Table 5)
- **Metrics**: Top-1 and top-5 error (%, 10-crop validation; test set for ensemble)
- **Expected outcome**:
  - Deeper ResNets should achieve progressively lower validation error
  - ResNet-152 should outperform all prior single models on ImageNet
  - ResNet ensemble should achieve competitive top-5 error on test set
- **Baselines**: VGG-16, GoogLeNet, PReLU-net, BN-inception
- **Dependencies**: none

## E03: Shortcut connection ablation (identity vs projection)
- **Verifies**: C04
- **Setup**:
  - Model: ResNet-34 with three shortcut options: A (zero-padding), B (projection for dimension change only), C (all projections)
  - Hardware: Not specified in paper
  - Dataset: ImageNet 2012
  - System: Same training protocol as E02
- **Procedure**:
  1. Train ResNet-34 A with identity shortcuts and zero-padding for dimension increases
  2. Train ResNet-34 B with projection shortcuts only when dimensions change
  3. Train ResNet-34 C with all projection shortcuts
  4. Compare validation error across all three options (Table 3)
- **Metrics**: Top-1 and top-5 error (%, 10-crop validation)
- **Expected outcome**:
  - All three options should substantially outperform plain-34
  - Differences among A/B/C should be small, indicating projections are not essential
  - B should perform slightly better than A due to the projection capturing dimension-change information
- **Baselines**: plain-34 network
- **Dependencies**: E01

## E04: CIFAR-10 depth scaling with residual networks
- **Verifies**: C01
- **Setup**:
  - Model: ResNets with n = {3, 5, 7, 9} (20, 32, 44, 56 layers) and n = 18 (110 layers), plus n = 200 (1202 layers)
  - Hardware: Not specified in paper
  - Dataset: CIFAR-10, 50k training images, 10k test images, 10 classes
  - System: SGD, mini-batch 128, weight decay 0.0001, momentum 0.9, BN, no dropout
- **Procedure**:
  1. Train plain networks and ResNets with varying depths on CIFAR-10
  2. Compare training and test error across depths (Figure 6, Table 6)
  3. Scale to 110-layer and 1202-layer ResNets
- **Metrics**: Test error (%, on 10k test images)
- **Expected outcome**:
  - ResNets should benefit from increased depth on CIFAR-10
  - The 110-layer ResNet should achieve competitive results with state-of-the-art
  - The 1202-layer network may not improve over the 110-layer due to dataset size
- **Baselines**: Plain networks of matching depth, FitNet, Highway networks
- **Dependencies**: none

## E05: Object detection and segmentation transfer
- **Verifies**: C06
- **Setup**:
  - Model: Faster R-CNN with ResNet-101 backbone replacing VGG-16
  - Hardware: 8-GPU implementation for COCO
  - Dataset: PASCAL VOC 2007/2012, MS COCO (80k training, 40k validation images)
  - System: Faster R-CNN detection framework
- **Procedure**:
  1. Replace VGG-16 backbone in Faster R-CNN with ResNet-101
  2. Evaluate on PASCAL VOC 2007/2012 test sets (Table 7)
  3. Evaluate on COCO validation and test-dev sets (Table 8, Table 9)
  4. Apply box refinement, context, and multi-scale testing improvements
- **Metrics**: mAP@.5, mAP@[.5,.95] for detection; segmentation metrics for COCO
- **Expected outcome**:
  - ResNet-101 backbone should outperform VGG-16 backbone on all detection metrics
  - Gains should be attributable solely to better learned representations
- **Baselines**: Faster R-CNN with VGG-16 backbone
- **Dependencies**: E02
