---
title: "Deep Residual Learning for Image Recognition"
authors: [Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun]
year: 2016
venue: "CVPR 2016"
doi: "arXiv:1512.03385"
ara_version: "1.0"
domain: "Computer Vision"
keywords: [residual learning, degradation problem, identity shortcuts, ImageNet, CIFAR-10, optimization, deep convolutional networks, bottleneck architecture]
claims_summary:
  - "Residual learning with shortcut connections alleviates the degradation problem observed in deeper plain CNNs."
  - "A 34-layer ResNet optimizes better and validates better than a matched 34-layer plain network."
  - "Deeper residual variants (50/101/152 layers) continue to improve over the 34-layer residual baseline on ImageNet."
  - "Projection shortcuts help slightly but are not essential for addressing degradation."
abstract: "Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions. We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. On the ImageNet dataset we evaluate residual nets with a depth of up to 152 layers, 8x deeper than VGG nets but still having lower complexity. An ensemble of these residual nets achieves 3.57% error on the ImageNet test set. This result won the 1st place on the ILSVRC 2015 classification task."
---

# Deep Residual Learning for Image Recognition

## Overview

This artifact captures the core contribution of the ResNet paper: the degradation problem in deep plain networks and its resolution via residual learning with shortcut connections. It covers the degradation-to-residual-learning path, identity vs. projection shortcuts, and depth scaling to 152 layers on ImageNet. Every trace node is grounded in explicit source material — if a research step is not directly stated in the paper, it is omitted rather than reconstructed.

## Layer Index

### Cognitive Layer (`/logic`)

| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations, gaps, key insight, and assumptions behind the degradation problem |
| [claims.md](logic/claims.md) | 4 falsifiable claims about residual learning, depth scaling, and shortcut variants |
| [concepts.md](logic/concepts.md) | Formal definitions of residual-learning terms |
| [experiments.md](logic/experiments.md) | 4 declarative verification plans linked to the claims |
| [solution/architecture.md](logic/solution/architecture.md) | Residual block and stage-level component graph |
| [solution/algorithm.md](logic/solution/algorithm.md) | Residual formulation, pseudocode, and complexity |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and scope limits |
| [solution/heuristics.md](logic/solution/heuristics.md) | Training-critical heuristics and implementation sensitivities |
| [related_work.md](logic/related_work.md) | Typed dependencies on prior deep CNN and shortcut work |

### Physical Layer (`/src`)

| File | Description | Claims |
|------|-------------|--------|
| [configs/training.md](src/configs/training.md) | Training hyperparameters and schedule for ImageNet | C01, C02 |
| [configs/model.md](src/configs/model.md) | Residual block and model-family configuration | C01, C02, C03 |
| [execution/residual_block.py](src/execution/residual_block.py) | Minimal executable anchor for the residual block | C01 |
| [environment.md](src/environment.md) | Framework, dataset, and hardware assumptions from the paper | C01, C02, C03 |

### Exploration Graph (`/trace`)

| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 9-node research DAG covering the plain-depth failure, residual decision, shortcut comparison, and depth scaling |

### Evidence (`/evidence`)

| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index mapping every evidence file to claims |
| [tables/table2_imagenet_plain_vs_residual.md](evidence/tables/table2_imagenet_plain_vs_residual.md) | Exact Table 2 values for plain-vs-residual ImageNet comparison |
| [tables/table3_imagenet_validation_full.md](evidence/tables/table3_imagenet_validation_full.md) | Faithful Table 3 transcription with shortcut variants and deeper residual rows |
| [tables/table4_imagenet_single_model.md](evidence/tables/table4_imagenet_single_model.md) | Table 4 single-model results on ImageNet validation |
| [tables/derived_from_table3_residual_depth_slice.md](evidence/tables/derived_from_table3_residual_depth_slice.md) | Claim-specific subset for residual depth scaling (C03) |
| [tables/derived_from_table3_shortcut_options.md](evidence/tables/derived_from_table3_shortcut_options.md) | Claim-specific subset for shortcut option comparison (C04) |
