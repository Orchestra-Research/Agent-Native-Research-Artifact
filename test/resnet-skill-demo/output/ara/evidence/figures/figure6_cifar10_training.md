# Figure 6 - Training on CIFAR-10

**Source**: Figure 6 in "Deep Residual Learning for Image Recognition"
**Caption**: "Training on CIFAR-10. Dashed lines denote training error, and bold lines denote testing error. Left: plain networks. The error of plain-110 is higher than 60% and not displayed. Middle: ResNets. Right: ResNets with 110 and 1202 layers."
**Axes**: X = iterations (×10³), Y = error (%)

## Left panel: Plain networks
Key observations:
- Deep plain nets suffer from increased depth
- Exhibit higher training error when going deeper
- This phenomenon is similar to that on ImageNet (Figure 4 left) and on MNIST

## Middle panel: ResNets
Key observations:
- ResNets manage to overcome the optimization difficulty
- Demonstrate stagnant accuracy gains when depth increases
- Depths tested: n = {3, 5, 7, 9} → {20, 32, 44, 56} layers

## Right panel: ResNet-110 and ResNet-1202
Key observations:
- The 110-layer network converges well
- The 1202-layer network converges to similar training error as 110-layer
- The 1202-layer network has worse test error than 110-layer (7.93% vs 6.43%)
- This gap is attributed to overfitting, not optimization difficulty

## Final test errors (from Table 6, for reference)

| Model | Layers | Test error (%) |
|-------|--------|---------------|
| ResNet | 20 | 8.75 |
| ResNet | 32 | 7.51 |
| ResNet | 44 | 7.17 |
| ResNet | 56 | 6.97 |
| ResNet | 110 | 6.43 |
| ResNet | 1202 | 7.93 |

Note: Precise curve values are approximate from figure reading. Exact final test errors are in Table 6.
