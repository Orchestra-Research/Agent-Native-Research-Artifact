# Figure 6: CIFAR-10 training/test curves for plain and ResNet families

**Source**: Figure 6, §4.2
**Caption**: "Training on CIFAR-10. Dashed lines denote training error, and bold lines denote testing error. Left: plain networks. The error of plain-110 is higher than 60% and not displayed. Middle: ResNets. Right: ResNets with 110 and 1202 layers."
**Axes**: X = iterations (×10⁴), Y = error (%)
**Extraction type**: figure_summary

### Left — plain-{20, 32, 44, 56, 110}
- Error curves diverge with depth: deeper plain nets have *higher* training and test error in the late phase.
- Plain-110 fails badly (>60% error throughout) and is not shown — strong evidence for degradation at very large plain-net depth.

### Middle — ResNet-{20, 32, 44, 56, 110}
- Curves stack monotonically: deeper ResNets achieve lower training and test error.
- Final test error matches Table 6 (8.75 → 7.51 → 7.17 → 6.97 → 6.43 for depths 20 → 110).

### Right — ResNet-{110, 1202}
- ResNet-1202 trains successfully — final training error <0.1% (text §"Exploring Over 1000 layers").
- ResNet-1202 test error is *higher* than ResNet-110 (7.93 vs. 6.43), consistent with overfitting on a 50k-image dataset given a 19.4M-parameter model.

**Key observation**: ResNet families overcome the plain-net degradation, and even 1202 layers train cleanly — but extreme depth overfits without explicit regularization on this small dataset (cited under C06).
