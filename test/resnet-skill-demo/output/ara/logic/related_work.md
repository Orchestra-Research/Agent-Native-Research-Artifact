# Related Work

## RW01: Simonyan & Zisserman, 2014 (VGGNet)
- **DOI**: arXiv:1409.1556
- **Type**: baseline
- **Delta**:
  - What changed: VGG demonstrated that depth (16–19 layers) with small 3×3 filters is effective for ImageNet classification, establishing the design philosophy that ResNet's plain baselines follow.
  - Why: ResNet's plain network is designed with the same principles (same filter count for same feature map size, double filters when size halves) but achieves 3.6B FLOPs vs VGG-19's 19.6B FLOPs.
- **Claims affected**: C02, C05
- **Adopted elements**: 3×3 convolution design philosophy, plain network template

## RW02: Szegedy et al., 2015 (GoogLeNet/Inception)
- **DOI**: arXiv:1409.4842
- **Type**: baseline
- **Delta**:
  - What changed: GoogLeNet introduced inception modules with multiple parallel branches, achieving competitive ImageNet results with lower computational cost.
  - Why: ResNet takes a different approach — instead of widening with parallel branches, it goes deeper with residual connections, achieving lower error with simpler design.
- **Claims affected**: C05
- **Adopted elements**: None directly; serves as a baseline comparison

## RW03: Ioffe & Szegedy, 2015 (Batch Normalization)
- **DOI**: arXiv:1502.03167
- **Type**: imports
- **Delta**:
  - What changed: BN normalizes activations within mini-batches, enabling higher learning rates and reducing sensitivity to initialization. ResNet applies BN after every convolution.
  - Why: BN addresses vanishing/exploding gradients but does not solve the degradation problem — ResNet's residual connections are additionally needed.
- **Claims affected**: C01, C02
- **Adopted elements**: BN applied after every convolution and before activation

## RW04: Srivastava et al., 2015 (Highway Networks)
- **DOI**: arXiv:1505.00387
- **Type**: extends
- **Delta**:
  - What changed: Highway networks use gating mechanisms T(x) and 1−T(x) to regulate information flow, where shortcuts are "gated" (parameterized). ResNet uses parameter-free identity shortcuts instead.
  - Why: Highway networks have not demonstrated accuracy gains with extremely increased depth (>100 layers). ResNet's identity shortcuts are simpler and empirically more effective for very deep networks.
- **Claims affected**: C01, C04
- **Adopted elements**: Concept of shortcut connections; simplified to identity mapping

## RW05: He et al., 2015 (PReLU-net / He Initialization)
- **DOI**: arXiv:1502.01852
- **Type**: imports
- **Delta**:
  - What changed: Introduced the He initialization method (variance scaled by 2/n) for ReLU networks and PReLU activation. ResNet adopts He initialization for all weights.
  - Why: Proper initialization is critical for training deep networks from scratch without pre-training.
- **Claims affected**: C01
- **Adopted elements**: Weight initialization method

## RW06: Girshick, 2015 (Fast R-CNN)
- **DOI**: arXiv:1504.08083
- **Type**: imports
- **Delta**:
  - What changed: Fast R-CNN provides the object detection framework. ResNet replaces the VGG backbone in Fast/Faster R-CNN to demonstrate generalization of residual representations.
  - Why: Using ResNet as a drop-in backbone replacement isolates the effect of the learned representations.
- **Claims affected**: C06
- **Adopted elements**: Detection framework for transfer experiments

## RW07: Ren et al., 2015 (Faster R-CNN)
- **DOI**: arXiv:1506.01497
- **Type**: imports
- **Delta**:
  - What changed: Faster R-CNN adds Region Proposal Networks (RPN) for end-to-end detection. ResNet-101 replaces VGG-16 in Faster R-CNN for all detection/segmentation experiments.
  - Why: Faster R-CNN provides the state-of-the-art detection pipeline for evaluating ResNet's transfer capabilities.
- **Claims affected**: C06
- **Adopted elements**: Full detection pipeline (RPN + Fast R-CNN)

## RW08: Romero et al., 2015 (FitNets)
- **DOI**: arXiv:1412.6550
- **Type**: baseline
- **Delta**:
  - What changed: FitNets use knowledge distillation to train thin deep networks. On CIFAR-10, FitNet achieves 8.39% error with 19 layers and 2.5M parameters.
  - Why: ResNet achieves 6.43% with 110 layers and 1.7M parameters on CIFAR-10 without distillation, demonstrating that residual learning enables depth scaling more effectively.
- **Claims affected**: C01
- **Adopted elements**: None; serves as a CIFAR-10 baseline
