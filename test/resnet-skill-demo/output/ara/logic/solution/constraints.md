# Constraints

## Dimension Matching
- Identity shortcuts require input and output dimensions to match. When dimensions change (at downsampling stages), either zero-padding (option A) or 1×1 projection (option B) is needed.
- Downsampling is performed with stride-2 convolutions at conv3_1, conv4_1, conv5_1.

## Dataset Scale and Overfitting
- The 1202-layer ResNet on CIFAR-10 achieves similar training error to the 110-layer model but has higher test error (7.93% vs 6.43%), suggesting overfitting on the small 50k-image dataset. The paper notes that no regularization (maxout, dropout) was applied, as the focus was on optimization difficulty rather than regularization.
- The degradation problem is distinct from overfitting and is observed even on training error.

## Bottleneck Identity Shortcut Criticality
- For bottleneck architectures, parameter-free identity shortcuts are particularly important. Replacing identity shortcuts with projections in bottleneck designs doubles time complexity and model size, as the shortcut connects two high-dimensional ends.

## Training Protocol Sensitivity
- The 110-layer CIFAR-10 ResNet requires a modified learning rate schedule: starting at 0.01 (not 0.1) to warm up until training error is below 80%, then switching to 0.1 and proceeding as normal. The initial learning rate of 0.1 is too large for convergence of very deep networks.

## Solver Limitations
- The paper conjectures that deep plain nets may have exponentially low convergence rates, impacting the optimization. Even with BN (which prevents vanishing/exploding gradients), the solver cannot find good solutions for deep plain networks.
- The current SGD solver is still able to find good solutions for plain nets that are "not overly deep" (18 layers).

## Known Limitations
- The paper does not explore whether the degradation problem is fully eliminated or merely pushed to greater depths. The 1202-layer CIFAR-10 experiment shows no optimization difficulty but encounters overfitting.
- No analysis of residual learning on architectures beyond CNNs (though the paper speculates applicability to other domains).
- The paper does not study the combination of residual learning with stronger regularization (dropout, maxout), leaving this for future work.
