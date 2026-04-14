# Constraints

## Boundary Conditions

1. **Dimension matching**: Identity shortcuts (y = F(x) + x) require input and output to have the same dimensions. When dimensions change between stages, either zero-padding or projection shortcuts must be used (§3.1, Eq.2).

2. **Depth range validated**: The paper validates residual learning from 18 to 152 layers on ImageNet and up to 1202 layers on CIFAR-10. The 1202-layer network shows no optimization difficulty but has marginally higher test error than the 110-layer model, possibly due to overfitting on the small dataset (§4.2).

3. **Dataset scale**: The ImageNet experiments use 1.28 million training images. CIFAR-10 uses 50k training images. The bottleneck design and depth scaling results are demonstrated on ImageNet.

4. **Single-dataset evaluation per experiment**: Each experiment configuration is evaluated on one dataset (ImageNet or CIFAR-10), not transferred across datasets in this paper.

## Assumptions

1. **BN prerequisite**: All networks use Batch Normalization, which addresses vanishing/exploding gradients. The degradation problem is assumed to persist even with BN (§1).

2. **No dropout**: The paper follows [16] and does not use dropout. Regularization comes from deep and thin architectures (§4.2).

3. **Training from scratch**: All ImageNet models are trained from scratch (not fine-tuned from a shallower model), using weight initialization from [13] and BN (§3.4).

## Known Limitations

1. **No theoretical guarantee**: The paper provides an empirical demonstration, not a proof, that residual learning solves degradation. The hypothesis that it is "easier to optimize the residual mapping than the original" is stated but not formally proven (§3.1).

2. **Overfitting at extreme depth on small datasets**: The 1202-layer ResNet on CIFAR-10 shows slightly worse test error than the 110-layer model despite similar training error, suggesting overfitting with too many parameters on small datasets (§4.2).

3. **Bottleneck necessity for deep models**: The basic two-layer block becomes impractical at 50+ layers due to computational cost. The switch to bottleneck blocks at depth 50 makes direct comparison with the 34-layer basic architecture less clean.
