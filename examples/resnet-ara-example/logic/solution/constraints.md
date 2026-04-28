# Constraints and Limitations

## Dimension-matching constraints
- Eqn. (1) (`y = F(x) + x`) is only well-defined when `dim(F(x)) == dim(x)`. When stages change spatial size or channel count, one of two strategies is required:
  - **Option A (identity + zero-pad)**: down-sample by stride-2 sampling on the shortcut and zero-pad the extra channels — *no learnable parameters*.
  - **Option B/C (projection)**: 1×1 conv with stride 2 (when down-sampling), introducing parameters `C_in × C_out`.
- Within a stage (no spatial or channel change), identity shortcuts are always used.

## Shortcut-design caveats
- **Single-layer F is rejected.** When `F` has only one weighted layer, Eqn. (1) is similar to a linear layer; the paper "did not observe advantages" and uses ≥2 layers in `F` (§3.1).
- **Option A has a residual-learning blind spot at dimension changes.** Zero-padded extra channels carry "no residual learning" — the paper attributes the small Option B>A gap on ImageNet to this fact.
- **Option C is not worth its cost.** Although marginally better than B (24.19 vs. 24.52 ResNet-34 top-1), C adds 13 extra projection shortcuts and is "not essential for addressing the degradation problem"; the paper rejects C "to reduce memory/time complexity and model sizes" (§"Identity vs. Projection Shortcuts").
- **Bottleneck blocks particularly require identity shortcuts.** Replacing the bottleneck identity with a projection "doubles" both time complexity and model size.

## Training-recipe constraints
- **No dropout** anywhere (§3.4).
- **BN must come right after each conv and before activation** (§3.4).
- **MSRA initialization** for all conv weights.
- **Mini-batch size**: 256 for ImageNet, 128 for CIFAR-10.
- **LR schedule** depends on a *plateau* signal for ImageNet (LR /10 when error plateaus) but a *fixed* step schedule for CIFAR-10 (32k, 48k iters).

## Optimization caveats specific to extreme depth
- **Warmup is required for the 110-layer CIFAR ResNet.** LR 0.1 from iter 0 is "slightly too large to start converging"; the recipe is LR 0.01 for ~400 iters until training error <80%, then restore LR 0.1 (footnote 5). LR 0.1 from start *eventually* converges to similar accuracy after several epochs of >90% error, but warmup is the chosen recipe.
- **No warmup is needed for ResNet-1202** at the same recipe — the paper notes "no optimization difficulty" for the 1202-layer model.
- **Overfitting bites at extreme depth on small data.** ResNet-1202 (19.4M params on 50k CIFAR images) trains fine but tests at 7.93% vs. ResNet-110's 6.43%; the paper does not apply maxout/dropout/strong regularization in this work.

## Generalization caveats
- All ImageNet results use 10-crop testing for Tables 2/3 and an additional fully-convolutional multi-scale test for Table 4. Mixing these protocols across rows is not legitimate.
- The 3.57% top-5 ensemble result (Table 5) is a 6-model ensemble on the test set — not reproducible from a single model.

## Detection-transfer caveats (Appendix A)
- BN layer statistics are *frozen* during Faster R-CNN fine-tuning to reduce memory consumption.
- Per-class RPN with binary logistic classification is used for ImageNet localization; for COCO/PASCAL detection, the standard category-agnostic RPN is used.
- The COCO+PASCAL "baseline+++" rows in Tables 9/10/11 combine box refinement, global context, multi-scale testing, and ensembling on top of ResNet-101; these gains are not solely attributable to the backbone.

## Unverified hypothesis
- **A1 (open question)**: The paper's residual-learning argument relies on the hypothesis that stacked nonlinear layers can asymptotically approximate any function (and thus also any residual function). Footnote 2 explicitly notes this remains open.

## Out-of-scope
- The paper does not formally prove that residual learning improves *optimization landscape* properties (it proposes this as a hypothesis supported empirically by Fig. 7).
- The paper does not study extremely *wide* networks; only depth scaling.
- No comparison with second-order optimizers; SGD is the only solver studied.
