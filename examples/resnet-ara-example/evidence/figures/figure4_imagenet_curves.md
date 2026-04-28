# Figure 4: ImageNet training and validation curves — plain vs. ResNet at 18/34 layers

**Source**: Figure 4, §4.1
**Caption**: "Training on ImageNet. Thin curves denote training error, and bold curves denote validation error of the center crops. Left: plain networks of 18 and 34 layers. Right: ResNets of 18 and 34 layers. In this plot, the residual networks have no extra parameter compared to their plain counterparts."
**Axes**: X = iterations (×10⁴, axis runs 0–50), Y = error (%) (axis runs ~20–60)
**Extraction type**: figure_summary

Per-iteration values are not tabulated by the paper. Qualitative shape (read off from the figure):

### Left panel — plain-18 (cyan) vs. plain-34 (red)
- Both curves descend in three plateaus separated by LR drops at ≈ 20×10⁴ and ≈ 40×10⁴.
- **plain-34 lies above plain-18 throughout training** (both training and validation curves), demonstrating degradation throughout, not only at convergence.
- Final readings (≈ 50×10⁴): plain-18 validation ≈ 28%, plain-34 validation ≈ 28.5% (consistent with Table 2: 27.94 vs. 28.54).

### Right panel — ResNet-18 (cyan) vs. ResNet-34 (red)
- Both curves descend in similar three-plateau fashion.
- **ResNet-34 lies below ResNet-18 throughout training** — the order is *reversed* from the plain case.
- ResNet-18 also converges *faster* than plain-18 in the early phase (residual easing of optimization), reaching low error sooner even though final accuracy is comparable.
- Final readings (≈ 50×10⁴): ResNet-18 validation ≈ 27.9%, ResNet-34 validation ≈ 25% (consistent with Table 2: 27.88 vs. 25.03).

**Key observation**: The plain pair shows degradation; the residual pair removes it (cited under C01, C02).
