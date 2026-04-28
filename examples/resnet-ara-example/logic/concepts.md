# Concepts

## Residual Mapping
- **Notation**: $\mathcal{F}(\mathbf{x}) := \mathcal{H}(\mathbf{x}) - \mathbf{x}$, with the original mapping recovered as $\mathcal{H}(\mathbf{x}) = \mathcal{F}(\mathbf{x}) + \mathbf{x}$.
- **Definition**: An auxiliary mapping fit by a few stacked nonlinear layers, expressing the *difference* between a desired underlying mapping $\mathcal{H}$ and its input $\mathbf{x}$. The block as a whole computes $\mathcal{F}(\mathbf{x}, \{W_i\}) + \mathbf{x}$.
- **Boundary conditions**: Only well-defined for blocks whose input and output have matching dimensions; for dimension changes a linear projection $W_s$ is introduced (Eqn. 2). A single-layer $\mathcal{F}$ degenerates to a linear layer with no observed advantage; $\mathcal{F}$ should have ≥2 layers (§3.2).
- **Related concepts**: Identity Shortcut, Projection Shortcut, Plain Network.

## Identity Shortcut (Option A)
- **Notation**: $\mathbf{y} = \mathcal{F}(\mathbf{x}, \{W_i\}) + \mathbf{x}$.
- **Definition**: A parameter-free skip connection that adds the input of a residual block directly to its output. When dimensions increase across the shortcut, missing channels are filled with zero padding (no learnable parameters).
- **Boundary conditions**: Requires $\dim(\mathbf{x}) = \dim(\mathcal{F}(\mathbf{x}))$, or zero-padding for the extra channels. Adds neither parameters nor computational cost beyond an element-wise add.
- **Related concepts**: Projection Shortcut, Residual Mapping, Bottleneck Block.

## Projection Shortcut (Option B / Option C)
- **Notation**: $\mathbf{y} = \mathcal{F}(\mathbf{x}, \{W_i\}) + W_s \mathbf{x}$.
- **Definition**: A 1×1 convolutional shortcut that linearly projects $\mathbf{x}$ to match the output dimension. Option B uses projections only when dimensions change; option C uses projections on every shortcut.
- **Boundary conditions**: $W_s$ adds parameters and FLOPs proportional to channel count. In bottleneck blocks, replacing identity with a projection roughly *doubles* the block's time complexity and model size, so it is reserved for dimension-changing shortcuts.
- **Related concepts**: Identity Shortcut, Bottleneck Block.

## Bottleneck Residual Block
- **Notation**: 1×1, $C_\text{in} \to C_\text{mid}$ → 3×3, $C_\text{mid} \to C_\text{mid}$ → 1×1, $C_\text{mid} \to C_\text{out}$, with $C_\text{out} = 4 C_\text{mid}$ (Fig. 5 right).
- **Definition**: A 3-layer residual building block whose first 1×1 reduces channels, the 3×3 operates on the bottleneck, and the second 1×1 restores the high-dimensional output. Used in ResNet-50/101/152 in place of the 2-layer 3×3 block.
- **Boundary conditions**: Designed to keep per-block compute comparable to the 2-layer block while permitting much greater depth. Identity shortcuts are particularly important here because projection shortcuts on the high-dimensional ends are expensive.
- **Related concepts**: Residual Mapping, Identity Shortcut, Plain Network.

## Degradation Problem
- **Notation**: For network depth $d$, training error $\epsilon_\text{train}(d)$ ceases to be monotonically non-increasing as $d$ grows.
- **Definition**: An empirical phenomenon where deeper plain CNNs reach *higher* training error than shallower counterparts that are nominally a subspace of the deeper architecture (§1).
- **Boundary conditions**: Observed in plain networks even when BN, MSRA initialization, and SGD with momentum are used. The paper attributes it to *optimization* difficulty, not vanishing/exploding gradients (§4.1).
- **Related concepts**: Plain Network, Residual Mapping, Identity Mapping by Shortcuts.

## Plain Network
- **Notation**: Sequential composition of conv → BN → ReLU layers without skip connections, sharing the VGG-style design rules: same output map size ⇒ same #filters; halving spatial size ⇒ doubling #filters (§3.3).
- **Definition**: The non-residual baseline architecture used to isolate the effect of residual learning. The 34-layer plain net has 3.6 GFLOPs (≈18% of VGG-19's 19.6 GFLOPs).
- **Boundary conditions**: Used purely as a control. Plain-{18,34} on ImageNet and plain-{20,32,44,56,110} on CIFAR-10 are the studied depths.
- **Related concepts**: Residual Network, Degradation Problem.

## Batch Normalization (BN)
- **Notation**: $y = \gamma \cdot (x - \mu_B) / \sigma_B + \beta$, normalization computed per channel over a mini-batch.
- **Definition**: Per-channel normalization placed *right after each convolution and before activation* (§3.4). Used for all plain and residual nets in this paper, with no dropout.
- **Boundary conditions**: At inference time, running statistics are used; for the COCO/PASCAL detection fine-tuning experiments, BN statistics are *frozen* after pre-training and BN behaves as an affine transform (Appendix A).
- **Related concepts**: Plain Network, MSRA Initialization (RW04).

## 10-Crop Testing
- **Notation**: Forward 10 fixed crops per image (4 corner crops + 1 center crop, each with horizontal flip) and average the predicted class probabilities.
- **Definition**: Standard test-time augmentation following Krizhevsky et al. used to report ImageNet validation error in Tables 2, 3.
- **Boundary conditions**: Distinct from "single-model" results in Table 4, which additionally use fully-convolutional multi-scale testing at scales {224, 256, 384, 480, 640}; and from the test-set ensemble result of 3.57% top-5 in Table 5.
- **Related concepts**: Multi-scale Testing, Ensembling.
