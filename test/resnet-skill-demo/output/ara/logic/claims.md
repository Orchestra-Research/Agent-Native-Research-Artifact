# Claims

## C01: Residual learning alleviates the degradation problem
- **Statement**: A 34-layer residual network achieves lower top-1 validation error than its 34-layer plain counterpart on ImageNet, reversing the degradation observed in plain networks.
- **Status**: supported
- **Falsification criteria**: If a 34-layer residual network validates worse than or equal to a 34-layer plain network under matched training conditions.
- **Proof**: [E01, E02]
- **Evidence basis**: Table 2 shows plain-34 at 28.54% top-1 and ResNet-34 at 25.03% top-1, a 3.5% reduction. Figure 4 right shows ResNet-34 training/validation curves are lower than ResNet-18.
- **Interpretation**: The shortcut connections change the optimization landscape to allow deeper networks to benefit from added capacity rather than suffering from degradation.
- **Dependencies**: [C02]
- **Tags**: residual learning, degradation, shortcut connections, ImageNet

## C02: Deeper plain networks degrade compared to shallower plain networks
- **Statement**: A 34-layer plain network has higher top-1 validation error (28.54%) than an 18-layer plain network (27.94%) on ImageNet, despite having a strictly larger solution space.
- **Status**: supported
- **Falsification criteria**: If a 34-layer plain network achieves lower or equal top-1 validation error compared to an 18-layer plain network.
- **Proof**: [E01]
- **Evidence basis**: Table 2 reports plain-18 at 27.94% and plain-34 at 28.54% top-1 error (10-crop). Figure 4 left shows training error curves where 34-layer is consistently above 18-layer.
- **Interpretation**: This demonstrates a fundamental optimization difficulty, not overfitting, since the training error is also higher for the deeper model.
- **Dependencies**: []
- **Tags**: degradation problem, plain networks, depth, optimization

## C03: Deeper residual networks continue to improve over shallower residual networks
- **Statement**: ResNet-50, ResNet-101, and ResNet-152 progressively reduce top-1 and top-5 ImageNet validation error compared to ResNet-34, with ResNet-152 achieving 21.43% top-1 and 5.71% top-5.
- **Status**: supported
- **Falsification criteria**: If increasing depth beyond 34 layers in residual networks yields no improvement or causes degradation on ImageNet validation.
- **Proof**: [E04]
- **Evidence basis**: Table 3 reports ResNet-34 B at 24.52/7.46, ResNet-50 at 22.85/6.71, ResNet-101 at 21.75/6.05, ResNet-152 at 21.43/5.71 (top-1/top-5, 10-crop). Table 4 reports single-model results: ResNet-152 at 19.38/4.49.
- **Interpretation**: The residual formulation successfully enables accuracy gains from increased depth, solving the degradation problem for at least up to 152 layers on ImageNet.
- **Dependencies**: [C01]
- **Tags**: depth scaling, bottleneck architecture, ImageNet

## C04: Projection shortcuts provide marginal improvement over identity shortcuts
- **Statement**: On ImageNet, shortcut option B (projection only for dimension changes) achieves 24.52% top-1, slightly better than option A (identity with zero-padding, 25.03%), while option C (all projections, 24.19%) is only marginally better than B.
- **Status**: supported
- **Falsification criteria**: If identity shortcuts (option A) perform comparably to or better than projection shortcuts (option B or C) across all metrics.
- **Proof**: [E03]
- **Evidence basis**: Table 3 reports option A at 25.03/7.76, option B at 24.52/7.46, option C at 24.19/7.40 (top-1/top-5). The differences among A/B/C are small.
- **Interpretation**: The small differences suggest projection shortcuts are not essential for addressing degradation. The paper adopts option B to balance complexity and accuracy, and explicitly states identity shortcuts are "particularly important for not increasing the complexity of the bottleneck architectures" (§4.1).
- **Dependencies**: [C01]
- **Tags**: identity shortcuts, projection shortcuts, shortcut design
