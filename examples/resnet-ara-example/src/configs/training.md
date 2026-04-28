# Training Configuration

ImageNet recipe (§3.4 "Implementation"); CIFAR-10 recipe (§4.2).

## ImageNet — Mini-batch size
- **Value**: 256
- **Rationale**: Standard ILSVRC-era batch for SGD with momentum on multi-GPU setups.
- **Search range**: Not specified in paper.
- **Sensitivity**: low (within typical ImageNet ranges).
- **Source**: §3.4.

## ImageNet — Initial learning rate
- **Value**: 0.1
- **Rationale**: SGD baseline with BN; divided by 10 when error plateaus.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium — for the 110-layer CIFAR ResNet, 0.1 from iter 0 fails to start converging cleanly (see warmup).
- **Source**: §3.4.

## ImageNet — LR schedule
- **Value**: Step (÷10 on validation-error plateau)
- **Rationale**: Standard schedule for the era; trains for up to 60×10⁴ iterations.
- **Search range**: Not specified.
- **Sensitivity**: low.
- **Source**: §3.4.

## ImageNet — Total iterations
- **Value**: up to 60×10⁴
- **Rationale**: Continue training through plateau-triggered LR drops.
- **Search range**: Not specified.
- **Sensitivity**: low.
- **Source**: §3.4.

## ImageNet — Momentum
- **Value**: 0.9
- **Rationale**: Standard SGD momentum.
- **Sensitivity**: low.
- **Source**: §3.4.

## ImageNet — Weight decay
- **Value**: 0.0001 (= 1e-4)
- **Rationale**: Standard L2 regularization.
- **Sensitivity**: low.
- **Source**: §3.4.

## ImageNet — Dropout
- **Value**: not used (rate = 0)
- **Rationale**: BN replaces the regularization role of dropout in this recipe (following BN paper convention).
- **Sensitivity**: low (BN-paper convention).
- **Source**: §3.4 ("We do not use dropout, following the practice in [16].").

## ImageNet — Initialization
- **Value**: MSRA (He et al., 2015 — ref [13])
- **Rationale**: Variance-preserving init for ReLU networks; consistent across plain and residual nets.
- **Source**: §3.4 ("We initialize the weights as in [13]").

## ImageNet — Data augmentation
- **Value**: Image resized with shorter side ∈ [256, 480], 224×224 random crop with horizontal flip; standard color augmentation per Krizhevsky et al. (ref [21]); per-pixel mean subtraction.
- **Rationale**: Scale augmentation per VGG (ref [41]); color augmentation per AlexNet.
- **Sensitivity**: medium — standard ImageNet augmentation suite.
- **Source**: §3.4.

## ImageNet — Test-time evaluation
- **Value**: 10-crop testing for Tables 2/3; fully-convolutional multi-scale testing at scales {224, 256, 384, 480, 640} for Table 4.
- **Rationale**: Match prior comparisons (10-crop); push best single-model with multi-scale fully-convolutional inference.
- **Sensitivity**: medium for absolute error, low for relative comparisons.
- **Source**: §3.4 ("In testing").

## CIFAR-10 — Mini-batch size
- **Value**: 128
- **Rationale**: Standard CIFAR mini-batch.
- **Source**: §4.2.

## CIFAR-10 — Initial learning rate
- **Value**: 0.1 (with warmup at 0.01 for ~400 iters when n=18, i.e., 110 layers)
- **Rationale**: 0.1 alone is "slightly too large to start converging" at 110 layers; warmup allows clean convergence.
- **Sensitivity**: medium (only at extreme depth on CIFAR).
- **Source**: §4.2; footnote 5.

## CIFAR-10 — LR schedule
- **Value**: ÷10 at iter 32k and ÷10 again at iter 48k
- **Rationale**: Fixed step schedule (vs. plateau-triggered on ImageNet).
- **Source**: §4.2.

## CIFAR-10 — Total iterations
- **Value**: 64,000
- **Rationale**: Determined on a 45k/5k train/val split.
- **Source**: §4.2.

## CIFAR-10 — Momentum
- **Value**: 0.9
- **Source**: §4.2.

## CIFAR-10 — Weight decay
- **Value**: 0.0001
- **Source**: §4.2.

## CIFAR-10 — Dropout
- **Value**: not used.
- **Source**: §4.2.

## CIFAR-10 — Data augmentation
- **Value**: 4-pixel padding on each side, random 32×32 crop from the padded image (or its horizontal flip); per-pixel mean subtraction. For testing, only the original 32×32 image is evaluated.
- **Rationale**: Augmentation recipe from Lee et al. (DSN, ref [24]).
- **Source**: §4.2.

## CIFAR-10 — GPUs
- **Value**: 2
- **Source**: §4.2.

## Detection — Faster R-CNN fine-tuning LR
- **Value**: 0.001 for 240k iterations, then 0.0001 for 80k iterations.
- **Rationale**: Standard COCO Faster R-CNN schedule; mini-batch 8 (RPN step) / 16 (Fast R-CNN step) on 8 GPUs.
- **Sensitivity**: low (matches reference Faster R-CNN).
- **Source**: Appendix A.
