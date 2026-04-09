---
title: "Deep Residual Learning for Image Recognition"
authors: [Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun]
year: 2016
venue: "CVPR 2016"
doi: "arXiv:1512.03385"
ara_version: "1.0"
domain: "Computer Vision"
keywords: [residual learning, degradation problem, identity shortcuts, ImageNet, optimization, deep convolutional networks]
claims_summary:
  - "Residual learning with shortcut connections alleviates the degradation problem observed in deeper plain CNNs."
  - "A 34-layer ResNet optimizes better and validates better than a matched 34-layer plain network."
  - "Deeper residual variants in the reported ImageNet validation table continue to improve over the 34-layer residual baselines."
  - "Projection shortcuts help slightly, but are not essential for addressing degradation."
abstract: "Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions. We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. On the ImageNet dataset we evaluate residual nets with a depth of up to 152 layers, 8x deeper than VGG nets but still having lower complexity. An ensemble of these residual nets achieves 3.57% error on the ImageNet test set. This result won the 1st place on the ILSVRC 2015 classification task."
---

# Deep Residual Learning for Image Recognition

## Overview

This test artifact captures the core ResNet slice that motivates the ARA format particularly well: deeper plain networks degrade as depth increases, residual reformulation changes the optimization problem, and evidence ties the mechanism directly to empirical gains. The artifact intentionally focuses on the degradation-to-residual-learning path rather than reconstructing every result from the full paper.

The goal of this folder is to simulate what the `ingestor` skill would produce for a concrete paper input. It binds claims, experiments, evidence, code stubs, and the failed plain-depth branch into one traversable artifact. When the paper does not present an explicit research-session log, reconstructed trace decisions are marked as inferred rather than presented as direct historical facts.

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
| [configs/training.md](src/configs/training.md) | Training hyperparameters and schedule for the ImageNet slice | C01, C02 |
| [configs/model.md](src/configs/model.md) | Residual block and model-family configuration notes | C01, C02, C03 |
| [execution/residual_block.py](src/execution/residual_block.py) | Minimal executable anchor for the residual block | C01 |
| [environment.md](src/environment.md) | Framework, dataset, and hardware assumptions from the paper | C01, C02, C03 |

### Exploration Graph (`/trace`)

| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 8-node research DAG covering the plain-depth failure, residual decision, and depth-scaling path |

### Evidence (`/evidence`)

| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index mapping raw and derived evidence files to claims |
| [tables/table2_imagenet_plain_vs_residual.md](evidence/tables/table2_imagenet_plain_vs_residual.md) | Exact Table 2 values for plain-vs-residual ImageNet comparison |
| [tables/table3_imagenet_validation_full.md](evidence/tables/table3_imagenet_validation_full.md) | Faithful Table 3 transcription with plain, shortcut-variant, and deeper residual rows |
| [tables/derived_from_table3_residual_depth_slice.md](evidence/tables/derived_from_table3_residual_depth_slice.md) | Claim-specific subset for residual depth scaling |
| [tables/derived_from_table3_shortcut_options.md](evidence/tables/derived_from_table3_shortcut_options.md) | Claim-specific subset for shortcut option comparison |
