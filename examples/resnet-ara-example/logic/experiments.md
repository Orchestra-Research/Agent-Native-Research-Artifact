# Experiments

## E01: Plain vs. residual at matched depth on ImageNet (18 vs. 34 layers)
- **Verifies**: C01, C02
- **Setup**:
  - Model: 18-layer and 34-layer plain CNNs (VGG-style, 3.6 GFLOPs at 34 layers); residual counterparts adding identity shortcuts (Option A: zero-padding for dimension changes) — same parameter count.
  - Hardware: GPU(s) — paper does not specify count for ImageNet, mini-batch size = 256.
  - Dataset: ImageNet 2012 — 1.28M training images, 50k validation, 100k test (1000 classes).
  - System: BN after every conv, MSRA initialization, SGD momentum 0.9, weight decay 1e-4, LR start 0.1 with /10 step on plateau, up to 60×10⁴ iterations, no dropout. Standard color/scale augmentation; 224×224 random crop on shorter-side ∈ [256, 480].
- **Procedure**:
  1. Train plain-{18, 34} from scratch with the recipe above.
  2. Train ResNet-{18, 34} (option A shortcuts) with identical hyperparameters.
  3. Evaluate top-1 / top-5 error on the 50k validation set with 10-crop testing.
  4. Compare full training-error and validation-error trajectories (Fig. 4).
- **Metrics**: Top-1 error (%), top-5 error (%), and training-error trajectory.
- **Expected outcome**:
  - Plain-34 has *higher* validation error than plain-18 throughout training (degradation).
  - ResNet-34 has *lower* validation and training error than ResNet-18 (degradation removed).
  - ResNet-34 outperforms plain-34 by a meaningful margin.
- **Baselines**: Plain-{18, 34} (ablation control); each net is its own residual counterpart's control.
- **Dependencies**: none.

## E02: Training-trajectory comparison plain vs. residual on ImageNet
- **Verifies**: C01, C02
- **Setup**:
  - Model: Same plain-{18, 34} and ResNet-{18, 34} as E01.
  - Hardware: same as E01.
  - Dataset: ImageNet 2012 (training set tracked; validation tracked at intervals).
  - System: same training pipeline.
- **Procedure**:
  1. During training, log thin curves for training error and bold curves for validation error (center-crop) for each model, sampled at iter intervals up to ~60×10⁴ (Fig. 4 axes go to 50×10⁴ shown).
  2. Compare residual vs. plain trajectories side-by-side at depths 18 and 34.
- **Metrics**: Training error vs. iteration, validation (center-crop) error vs. iteration.
- **Expected outcome**:
  - Plain-34's training-error curve sits *above* plain-18's throughout training (degradation, not just a final-step issue).
  - ResNet-34's curve sits *below* ResNet-18's (residual easing).
  - ResNet-18 converges *faster* than plain-18 in early iterations even though their final accuracy is similar, indicating optimization easing.
- **Baselines**: Plain-{18, 34} curves act as the controls.
- **Dependencies**: E01.

## E03: Depth scan with bottleneck blocks on ImageNet (50 / 101 / 152 layers)
- **Verifies**: C03, C05
- **Setup**:
  - Model: ResNet-{50, 101, 152} built from 1×1 → 3×3 → 1×1 bottleneck blocks (Fig. 5 right) with option B shortcuts (projection only on dimension changes), per Table 1.
  - Hardware: GPU(s) per E01.
  - Dataset: ImageNet 2012.
  - System: Same SGD recipe as E01.
- **Procedure**:
  1. Train ResNet-50, ResNet-101, ResNet-152 with the recipe in E01.
  2. Evaluate with 10-crop testing on the 50k validation set; compare top-1 and top-5 error (Table 3).
  3. Evaluate the single-model multi-scale fully-convolutional variant for Table 4.
  4. Form an ensemble of six different-depth ResNets and evaluate on the ImageNet test set (Table 5).
- **Metrics**: Top-1 / top-5 error (%) at each depth; FLOPs (Table 1); test-set top-5 error for the ensemble.
- **Expected outcome**:
  - Top-1 / top-5 error decreases monotonically from ResNet-50 → 101 → 152.
  - All three are more accurate than ResNet-34 by considerable margins.
  - The ResNet-152 single-model multi-scale result is more accurate than every prior published single-model on ImageNet.
  - The 6-model ensemble outperforms all prior ensembles, taking 1st place in ILSVRC 2015 classification.
- **Baselines**: ResNet-34 (within-family); VGG, GoogLeNet, PReLU-net, BN-inception (across-family).
- **Dependencies**: E01.

## E04: Identity vs. projection shortcut ablation on ResNet-34
- **Verifies**: C04
- **Setup**:
  - Model: ResNet-34 with three shortcut variants — A (identity + zero-pad for dim changes, parameter-free), B (projections only when dimensions change), C (projections on every shortcut).
  - Hardware: GPU(s) per E01.
  - Dataset: ImageNet 2012.
  - System: Same training recipe as E01.
- **Procedure**:
  1. Train ResNet-34 A, B, C from scratch with identical hyperparameters.
  2. Evaluate top-1 / top-5 error on the 50k validation set with 10-crop testing.
  3. Compare to plain-34 to quantify the residual learning gain at each shortcut variant.
- **Metrics**: Top-1 / top-5 error (%); parameter count delta from extra projection shortcuts.
- **Expected outcome**:
  - All three options outperform plain-34 by a sizable margin.
  - Differences among A, B, C are small (within ~1 top-1 point), with C marginally best, B slightly better than A.
  - Conclusion: identity shortcuts suffice for the degradation problem; option C's modest gain does not justify the extra parameters / memory.
- **Baselines**: Plain-34.
- **Dependencies**: E01.

## E05: CIFAR-10 depth scan and 1202-layer stress test
- **Verifies**: C06, C07
- **Setup**:
  - Model: CIFAR ResNet family with 6n+2 layers — n ∈ {3, 5, 7, 9, 18, 200} ⇒ depths {20, 32, 44, 56, 110, 1202}; 16/32/64 filters across the three feature-map sizes; option A identity shortcuts; ~0.27M params (n=3) up to 19.4M params (n=200).
  - Hardware: 2 GPUs.
  - Dataset: CIFAR-10 — 50k training, 10k test, 32×32 images, 10 classes; per-pixel mean subtraction; 4-pixel padded random crop and horizontal flip augmentation following [24].
  - System: SGD momentum 0.9, weight decay 1e-4, MSRA init, BN, no dropout, mini-batch 128, 45k/5k train/val split, LR 0.1 with /10 at iter 32k and 48k, terminate at 64k iters. For the 110-layer net: warm up at LR 0.01 for ~400 iters until training error <80%, then restore LR 0.1.
- **Procedure**:
  1. Train ResNet-{20, 32, 44, 56, 110} on CIFAR-10 with the recipe above; train plain-{20, 32, 44, 56, 110} as controls.
  2. Run the 110-layer ResNet 5 times and report mean ± std (best result form for Table 6).
  3. Train ResNet-1202 with the same recipe (no warmup needed at this depth per §"Exploring Over 1000 layers", since the n=18 warmup is the only special case noted).
  4. Compare to FitNet, Highway, Maxout, NIN, DSN baselines (Table 6).
- **Metrics**: Test-set classification error (%); parameter count (#params); training-error trajectory.
- **Expected outcome**:
  - ResNet test error decreases as depth grows from 20 → 110.
  - ResNet-1202 trains successfully (training error <0.1%) but its test error worsens versus the 110-layer model, indicating overfitting on this small dataset.
  - Plain-{56, 110} suffer the degradation problem; plain-110 is even reported to have >60% error and is not displayed.
- **Baselines**: Plain-{20, 32, 44, 56, 110}; Maxout, NIN, DSN, FitNet, Highway.
- **Dependencies**: E01 (for the residual recipe pattern).

## E06: COCO and PASCAL VOC detection transfer with ResNet-101
- **Verifies**: C08
- **Setup**:
  - Model: Faster R-CNN with two backbones — VGG-16 and ResNet-101. ResNet-101 is fine-tuned per Appendix A: full-image shared conv features through conv4_x; RoI pooling before conv5_x; conv5_x and up act as VGG's fc layers; final classification/box regression replaced. BN layers frozen during fine-tuning.
  - Hardware: 8 GPUs; mini-batch 8 images for RPN step (1/GPU), 16 for Fast R-CNN step.
  - Dataset: PASCAL VOC 2007 (5k trainval) + VOC 2012 (16k trainval) for "07+12"; "07++12" adds 10k VOC07 trainval+test for VOC12 evaluation. COCO 80k train + 40k val (val for evaluation in Tables 7/8/9).
  - System: Faster R-CNN baseline hyperparameters from [32]; Detection-network LR 0.001 for 240k iters, then 0.0001 for 80k iters; 4-step alternating training.
- **Procedure**:
  1. Replace VGG-16 with ResNet-101 in baseline Faster R-CNN; fine-tune on PASCAL VOC 07+12 and report VOC07 test mAP@.5 (Table 7).
  2. Fine-tune the same model on VOC 07++12 and report VOC12 test mAP@.5 (Table 7).
  3. Train on COCO train, evaluate on COCO val and report mAP@.5 and mAP@[.5,.95] (Table 8 baseline rows).
  4. Add box refinement, global context, multi-scale testing, ensemble (Table 9) for the competition entry.
- **Metrics**: PASCAL VOC mAP@.5 (%); COCO mAP@.5 (%); COCO mAP@[.5,.95] (%).
- **Expected outcome**:
  - ResNet-101 outperforms VGG-16 by a clear margin on every detection metric.
  - The COCO mAP@[.5,.95] gain (≥6 absolute points, ≥28% relative) is comparable to the gain on the looser COCO mAP@.5 (≈6.9 absolute), suggesting deeper features help both recognition and localization.
  - Adding box refinement, context, multi-scale, and ensemble further boosts COCO test-dev to >55% mAP@.5 / >34% mAP@[.5,.95].
- **Baselines**: VGG-16 backbone in Faster R-CNN.
- **Dependencies**: E03 (ResNet-101 must first be trained on ImageNet).
