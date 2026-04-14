# Heuristics

## H01: Learning rate schedule with plateau-driven division
- **Rationale**: Starting with lr=0.1 and dividing by 10 when the error plateaus allows the network to converge quickly initially and then fine-tune. Models are trained for up to 60x10^4 iterations on ImageNet (§3.4).
- **Sensitivity**: high
- **Bounds**: lr starts at 0.1, divided by 10 at plateaus; for CIFAR-10 110-layer ResNet, lr starts at 0.1, reduced at 32k and 48k iterations with total 64k iterations
- **Code ref**: [src/execution/residual_block.py]
- **Source**: §3.4, §4.2

## H02: BN after every convolution, before activation
- **Rationale**: Batch Normalization is adopted right after each convolution and before activation, following [16]. This ensures forward-propagated signals have non-zero variances and backward gradients have healthy norms, addressing vanishing/exploding gradients (§3.4, §4.1).
- **Sensitivity**: high
- **Bounds**: Applied to every convolutional layer in both the residual branch and projection shortcuts
- **Code ref**: [src/execution/residual_block.py]
- **Source**: §3.4

## H03: Weight initialization from He et al. [13]
- **Rationale**: Weights are initialized as in [13], designed for ReLU networks to maintain variance across layers. Combined with BN, this allows training from scratch without pre-training (§3.4).
- **Sensitivity**: medium
- **Bounds**: Applied to all convolutional layers
- **Code ref**: [src/execution/residual_block.py]
- **Source**: §3.4

## H04: No dropout
- **Rationale**: Following the practice in [16], dropout is not used. The paper argues that deep and thin architectures impose regularization by design, without needing dropout (§3.4, §4.2).
- **Sensitivity**: low
- **Bounds**: Not used in any configuration reported
- **Code ref**: [src/execution/residual_block.py]
- **Source**: §3.4

## H05: Warm-up learning rate for very deep CIFAR-10 models
- **Rationale**: For the 110-layer ResNet on CIFAR-10, the initial lr of 0.1 is "too large to start converging." A warm-up of lr=0.01 is used until training error drops below 80% (about 400 iterations), then lr is set to 0.1 and the normal schedule resumes (§4.2).
- **Sensitivity**: high
- **Bounds**: Only needed for networks that fail to converge with lr=0.1 from the start; applies to CIFAR-10 110-layer model
- **Code ref**: [src/execution/residual_block.py]
- **Source**: §4.2
