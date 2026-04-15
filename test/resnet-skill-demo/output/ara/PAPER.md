---
title: "Deep Residual Learning for Image Recognition"
authors: [Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun]
year: 2015
venue: "arXiv (CVPR 2016)"
doi: "arXiv:1512.03385"
ara_version: "1.0"
domain: "Deep Learning / Computer Vision"
keywords: [residual learning, deep networks, image recognition, skip connections, degradation problem, ImageNet, CIFAR-10, batch normalization, shortcut connections, bottleneck architecture]
claims_summary:
  - "Residual learning framework enables training of substantially deeper networks without degradation"
  - "Deeper plain networks exhibit degradation: higher training error with more layers"
  - "ResNets gain accuracy from considerably increased depth, achieving state-of-the-art on ImageNet"
  - "Identity shortcuts are sufficient for addressing the degradation problem"
  - "Deep residual representations generalize well to detection and segmentation tasks"
abstract: "Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions. We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. On the ImageNet dataset we evaluate residual nets with a depth of up to 152 layers — 8x deeper than VGG nets but still having lower complexity. An ensemble of these residual nets achieves 3.57% error on the ImageNet test set. This result won the 1st place on the ILSVRC 2015 classification task. We also present analysis on CIFAR-10 with 100 and 1000 layers."
---

# Deep Residual Learning for Image Recognition

## Overview

This paper addresses the degradation problem in deep neural networks: as network depth increases beyond a certain point, training accuracy degrades (not due to overfitting but optimization difficulty). The authors introduce residual learning, where layers learn residual functions F(x) with reference to the input x via shortcut connections, making it easier to optimize identity-like mappings. ResNets with up to 152 layers achieve state-of-the-art results on ImageNet (3.57% top-5 error), win 1st place in ILSVRC 2015, and generalize to COCO and PASCAL VOC detection/segmentation tasks.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Degradation problem: observations → gaps → residual learning insight |
| [claims.md](logic/claims.md) | 6 falsifiable claims (C01–C06) |
| [concepts.md](logic/concepts.md) | 7 formal definitions (residual function, shortcut connection, bottleneck, etc.) |
| [experiments.md](logic/experiments.md) | 5 declarative experiment plans (E01–E05) |
| [solution/architecture.md](logic/solution/architecture.md) | ResNet component graph with plain/residual/bottleneck variants |
| [solution/algorithm.md](logic/solution/algorithm.md) | Residual block math + pseudocode + complexity |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and limitations |
| [solution/heuristics.md](logic/solution/heuristics.md) | 5 implementation heuristics (H01–H05) |
| [related_work.md](logic/related_work.md) | 8 typed dependencies (VGG, GoogLeNet, Highway, etc.) |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [configs/training.md](src/configs/training.md) | ImageNet + CIFAR-10 training hyperparameters | C01, C03, C05 |
| [configs/model.md](src/configs/model.md) | Architecture configurations for ResNet-18/34/50/101/152 | C03, C04 |
| [execution/residual_block.py](src/execution/residual_block.py) | Residual block + bottleneck block implementation | C01 |
| [environment.md](src/environment.md) | Framework, hardware, dependencies | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 9-node research DAG |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 7 tables + 2 figures |
