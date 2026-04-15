# Heuristics

## H01: BN after every convolution, before activation
- **Rationale**: Batch normalization stabilizes training by normalizing activations, addressing vanishing/exploding gradients. Applied after each convolution and before ReLU activation in all ResNet variants.
- **Sensitivity**: high
- **Bounds**: Required for all convolution layers in the network. Without BN, deep networks fail to converge.
- **Code ref**: [src/execution/residual_block.py]
- **Source**: §3.4 — "We adopt batch normalization (BN) right after each convolution and before activation, following [16]."

## H02: Learning rate warm-up for very deep networks
- **Rationale**: For the 110-layer CIFAR-10 ResNet, the standard initial learning rate of 0.1 is too large to start converging. A warm-up phase with lr=0.01 is used until training error drops below 80%, then lr is set to 0.1 and the normal schedule resumes.
- **Sensitivity**: high
- **Bounds**: Needed when depth exceeds ~100 layers on small datasets. The 0.01 warm-up phase lasts approximately 400 iterations.
- **Code ref**: [src/execution/residual_block.py]
- **Source**: §4.2 — "we find that the initial learning rate of 0.1 is slightly too large to start converging. So we use 0.01 to warm up the training until the training error is below 80% (about 400 iterations), and then go back to 0.1"

## H03: No dropout in residual networks
- **Rationale**: The paper intentionally omits dropout, following the practice of [14] (BN paper), to focus on the optimization aspects of residual learning without confounding regularization effects. The architecture uses BN for normalization instead.
- **Sensitivity**: low
- **Bounds**: Applied across all ResNet experiments (ImageNet and CIFAR-10). The paper notes that combining with stronger regularization may improve results but leaves this for future work.
- **Code ref**: [src/execution/residual_block.py]
- **Source**: §3.4 — "We do not use dropout [14], following the practice in [16]."

## H04: Stride-2 convolution for downsampling (no pooling between stages)
- **Rationale**: Downsampling is performed by convolutions with stride 2 at the first layer of each stage (conv3_1, conv4_1, conv5_1), rather than using separate pooling layers. This reduces information loss and maintains the residual connection structure. Only max pooling is used after conv1.
- **Sensitivity**: medium
- **Bounds**: Applied at 3 stage boundaries in ImageNet architectures. Both the shortcut and the residual branch use stride 2 when feature maps are halved.
- **Code ref**: [src/execution/residual_block.py]
- **Source**: §3.3, Table 1 — "Downsampling is performed by conv3_1, conv4_1, and conv5_1 with a stride of 2."

## H05: He initialization (weight initialization from [13])
- **Rationale**: Weights are initialized according to the method in [13] (Delving Deep into Rectifiers), which accounts for the ReLU nonlinearity by scaling initialization variance by 2/n_in. This is important for enabling convergence of deep networks.
- **Sensitivity**: medium
- **Bounds**: Applied to all convolutional and fully-connected layers. Combined with BN, enables training from scratch without pre-training.
- **Code ref**: [src/execution/residual_block.py]
- **Source**: §3.4 — "We initialize the weights as in [13] and train all plain/residual nets from scratch."
