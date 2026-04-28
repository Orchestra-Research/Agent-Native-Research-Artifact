# Figure 1: CIFAR-10 training/test error for plain-{20, 56}

**Source**: Figure 1, §1
**Caption**: "Training error (left) and test error (right) on CIFAR-10 with 20-layer and 56-layer 'plain' networks. The deeper network has higher training error, and thus test error. Similar phenomena on ImageNet is presented in Fig. 4."
**Axes**: X = iterations (×10⁴), Y = error (%)
**Extraction type**: figure_summary

The figure is a 2-panel plot (left = training error, right = test error). Exact per-iteration data points are not tabulated in the paper. Qualitative readings:

| iter range | plain-20 train err. | plain-56 train err. | plain-20 test err. | plain-56 test err. |
|------------|---------------------|---------------------|--------------------|--------------------|
| early (≤1×10⁴) | ≈ high (>40%) | ≈ high (>40%) | ≈ high (>40%) | ≈ high (>40%) |
| mid  (~3×10⁴, after first LR drop) | drops sharply to ≈ 20% | drops to ≈ 25–30% | similar drop to ≈ 20–25% | drops to ≈ 25–30% |
| late (~6×10⁴) | ≈ 5% | ≈ 10% | ≈ 8–10% | ≈ 13–15% |

**Key observation**: throughout training, the 56-layer plain net's curves lie *above* the 20-layer plain net's, demonstrating the degradation problem (referenced as O1 in `/logic/problem.md`).
