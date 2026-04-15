# Figure 4 - Training on ImageNet

**Source**: Figure 4 in "Deep Residual Learning for Image Recognition"
**Caption**: "Training on ImageNet. Thin curves denote training error, and bold curves denote validation error of the center crops. Left: plain networks of 18 and 34 layers. Right: ResNets of 18 and 34 layers. In this plot, the residual networks have no extra parameter compared to their plain counterparts."
**Axes**: X = iterations (×10⁴), Y = error (%)

## Left panel: Plain networks
Key observations from the figure:
- plain-34 has consistently higher training error than plain-18 throughout training
- plain-34 has consistently higher validation error than plain-18
- Both converge but plain-34 converges to a worse solution

| Approximate iteration (×10⁴) | plain-18 training (%) | plain-34 training (%) | plain-18 val (%) | plain-34 val (%) |
|------|------|------|------|------|
| ≈5 | ≈45 | ≈48 | ≈42 | ≈45 |
| ≈20 | ≈28 | ≈30 | ≈32 | ≈34 |
| ≈40 | ≈24 | ≈26 | ≈30 | ≈32 |
| ≈60 | ≈22 | ≈25 | ≈28 | ≈30 |

## Right panel: Residual networks
Key observations from the figure:
- ResNet-34 has lower training error than ResNet-18
- ResNet-34 has lower validation error than ResNet-18
- The degradation pattern is reversed — deeper is better

| Approximate iteration (×10⁴) | ResNet-18 training (%) | ResNet-34 training (%) | ResNet-18 val (%) | ResNet-34 val (%) |
|------|------|------|------|------|
| ≈5 | ≈42 | ≈40 | ≈40 | ≈38 |
| ≈20 | ≈26 | ≈24 | ≈30 | ≈28 |
| ≈40 | ≈22 | ≈20 | ≈28 | ≈26 |
| ≈60 | ≈20 | ≈18 | ≈27 | ≈25 |

Note: Values are approximate readings from the figure. Exact final values are in Table 2.
