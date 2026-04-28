---
title: "Deep Residual Learning for Image Recognition"
authors: ["Kaiming He", "Xiangyu Zhang", "Shaoqing Ren", "Jian Sun"]
year: 2015
venue: "arXiv (later CVPR 2016)"
doi: "arXiv:1512.03385"
ara_version: "1.0"
domain: "computer vision / deep learning"
keywords: ["residual learning", "deep networks", "image classification", "ImageNet", "CIFAR-10", "shortcut connections", "identity mapping", "bottleneck", "ILSVRC 2015", "object detection"]
claims_summary:
  - "Stacking more layers in plain CNNs causes a degradation in training accuracy that is not explained by overfitting or vanishing gradients."
  - "Reformulating layers to fit a residual mapping F(x) = H(x) - x with identity shortcuts removes the degradation and allows accuracy to grow with depth up to 152 layers on ImageNet."
  - "Identity shortcuts are sufficient (no extra parameters); deeper bottleneck blocks make 50/101/152-layer ResNets practical and achieve 3.57% top-5 ImageNet ensemble error, winning ILSVRC 2015."
abstract: "Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions. We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. On the ImageNet dataset we evaluate residual nets with a depth of up to 152 layers — 8x deeper than VGG nets but still having lower complexity. An ensemble of these residual nets achieves 3.57% error on the ImageNet test set. This result won the 1st place on the ILSVRC 2015 classification task. We also present analysis on CIFAR-10 with 100 and 1000 layers. The depth of representations is of central importance for many visual recognition tasks. Solely due to our extremely deep representations, we obtain a 28% relative improvement on the COCO object detection dataset. Deep residual nets are foundations of our submissions to ILSVRC & COCO 2015 competitions, where we also won the 1st places on the tasks of ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation."
---

# Deep Residual Learning for Image Recognition

## Overview

He et al. identify a *degradation* problem: as plain feed-forward CNNs grow deeper, both training and test error get worse — even though the deeper network's solution space contains the shallower one. They propose **residual learning**: each block fits F(x) := H(x) − x, with the original mapping recovered by adding back x via a parameter-free identity *shortcut connection*. The reformulation makes very deep networks (up to 152 layers, and even 1202 on CIFAR-10) trainable end-to-end with SGD, with accuracy that grows with depth. An ensemble of six ResNets achieved **3.57% top-5 error** on ImageNet test, winning ILSVRC 2015 classification, and ResNet-101 yielded a 28% relative mAP improvement on COCO detection over a VGG-16 baseline.

This artifact captures the core ResNet slice that motivates the ARA format particularly well: deeper plain networks degrade as depth increases, residual reformulation changes the optimization problem, and evidence ties the mechanism directly to empirical gains. It binds claims, experiments, evidence, code stubs, and the failed plain-depth branch into one traversable artifact. When the paper does not present an explicit research-session log, reconstructed trace decisions are marked as inferred rather than presented as direct historical facts.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Degradation observations on CIFAR-10 and ImageNet → optimization gap → residual reformulation insight |
| [claims.md](logic/claims.md) | 8 falsifiable claims (C01–C08) on degradation, residual easing, depth gains, shortcut design, generalization |
| [concepts.md](logic/concepts.md) | 8 formal concepts (residual mapping, identity / projection shortcut, bottleneck block, degradation problem, plain network, BN, 10-crop testing) |
| [experiments.md](logic/experiments.md) | 6 declarative experiment plans (E01–E06) covering plain vs. residual, depth scan, shortcut options, bottleneck, CIFAR depth, COCO transfer |
| [solution/architecture.md](logic/solution/architecture.md) | Component graph: stem, conv stages, residual / bottleneck blocks, shortcut variants, head |
| [solution/algorithm.md](logic/solution/algorithm.md) | Math formulation of F(x)+x, pseudocode for forward pass, complexity analysis |
| [solution/constraints.md](logic/solution/constraints.md) | Dimension-matching constraints, when option A vs B/C applies, regularization caveats |
| [solution/heuristics.md](logic/solution/heuristics.md) | 6 heuristics (H01–H06) — identity over projection, BN placement, warmup for very deep nets, etc. |
| [related_work.md](logic/related_work.md) | Typed dependency graph: residual representations, shortcut connections, highway networks, baselines |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [configs/training.md](src/configs/training.md) | ImageNet/CIFAR SGD hyperparameters with rationale | C02, C03, C07 |
| [configs/model.md](src/configs/model.md) | Layer counts, channels, FLOPs for ResNet-{18,34,50,101,152} and CIFAR variants | C03, C05 |
| [configs/imagenet_resnet34.yaml](src/configs/imagenet_resnet34.yaml) | Concrete config for the 34-layer ImageNet ResNet | C02 |
| [execution/residual_block.py](src/execution/residual_block.py) | Basic and bottleneck residual blocks with identity / projection shortcut options | C01, C02, C04, C05 |
| [execution/training_recipe.py](src/execution/training_recipe.py) | SGD + step LR schedule + BN-after-conv recipe for ImageNet ResNets | C02, C03 |
| [environment.md](src/environment.md) | Framework, hardware, augmentation, seed assumptions | C02, C07 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 14-node research DAG with explicit / inferred provenance, dead ends and decisions |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 8 raw tables / 4 figures / 1 derived subset and the claims they support |
