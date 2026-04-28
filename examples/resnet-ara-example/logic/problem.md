# Problem Specification

## Observations

### O1: Plain CNNs degrade with depth on CIFAR-10
- **Statement**: A 56-layer plain CNN reaches *higher* training error and *higher* test error than a 20-layer plain CNN on CIFAR-10 (Fig. 1, §1).
- **Evidence**: Fig. 1 (training/test error curves vs. iterations) and Fig. 6 (left) for plain-{20,32,44,56,110}.
- **Implication**: Adding layers to a working network does not monotonically improve — and sometimes hurts — even training accuracy, contradicting the construction argument that a deeper net can at least match a shallower one by learning identity in the extra layers.

### O2: Same degradation appears on ImageNet
- **Statement**: 34-layer plain net obtains 28.54% top-1 ImageNet validation error vs. 27.94% for the 18-layer plain net — the deeper plain net is worse despite having strictly more capacity (Table 2, Fig. 4 left).
- **Evidence**: Table 2 (plain vs. ResNet, 18/34 layers); Fig. 4 left (plain training/validation curves).
- **Implication**: The degradation is not specific to CIFAR-scale data and is observed throughout the whole training trajectory, not just at the end.

### O3: Degradation is not caused by vanishing gradients
- **Statement**: Plain networks here use Batch Normalization, which keeps forward signals at non-zero variance, and backward gradient norms are verified to be healthy. The 34-layer plain net is "still able to achieve competitive accuracy" (24.19% top-1 with 10-crop testing, Table 3), so SGD is making progress, just slowly.
- **Evidence**: §4.1 "Plain Networks" discussion; Table 3 (plain-34 = 28.54% top-1 / 10.02% top-5).
- **Implication**: The bottleneck is *optimization difficulty* — exponentially low convergence rates conjectured — not signal collapse.

### O4: Identity-mapping construction proves a deeper net *should* be at least as good
- **Statement**: Given a shallow network, one can construct a deeper one by appending identity layers; this deeper construction has, by definition, training error ≤ the shallow net's. Yet SGD does not find it (§1, §3.1).
- **Evidence**: §1 introduction argument.
- **Implication**: Solvers struggle to approximate identity mappings via stacks of nonlinear layers, motivating an architecture that makes identity easy to express.

### O5: Layer responses in plain nets have larger magnitudes than in ResNets
- **Statement**: Std of 3×3 layer outputs (after BN, before ReLU) is consistently smaller for ResNets than for plain nets, and gets smaller as depth grows (Fig. 7).
- **Evidence**: Fig. 7 (CIFAR-10 layer-response std for plain-{20,56,110} vs. ResNet-{20,56,110}).
- **Implication**: Empirical support for the prior that, in real tasks, optimal mappings are closer to identity than to zero — so a residual parameterization is a better-conditioned starting point.

## Gaps

### G1: No way to train networks much deeper than ~20–30 layers
- **Statement**: As of 2015, leading ImageNet models top out at depths in the teens (VGG-19, GoogLeNet); naive deeper variants degrade (O1, O2).
- **Caused by**: O1, O2, O3, O4.
- **Existing attempts**: Better initialization (Xavier/MSRA), Batch Normalization, intermediate auxiliary classifiers, highway networks with gated shortcuts.
- **Why they fail**: They allow tens-of-layer nets to converge but do not enable monotonic accuracy gains with extreme depth. Highway gates are data-dependent and have parameters; when a gate closes, the layer behaves non-residually, and highway networks have not shown gains beyond ~100 layers.

### G2: No parameter-free, drop-in mechanism to bias optimization toward near-identity solutions
- **Statement**: Existing shortcut variants either add parameters (projection / gated) or change the function class (highway).
- **Caused by**: O4, O5.
- **Existing attempts**: Linear / projection shortcuts, gated skip connections.
- **Why they fail**: They couple the shortcut to additional learnable parameters or close the residual path entirely.

## Key Insight
- **Insight**: Reformulate each block to fit a *residual* mapping F(x) := H(x) − x, so the original mapping is recovered as F(x) + x via a parameter-free identity shortcut. If the optimal mapping is close to identity, the solver only needs to push F toward zero, which is empirically easier than fitting H from scratch (§3.1).
- **Derived from**: O3, O4, O5.
- **Enables**: End-to-end training of networks with 50, 101, 152, and even 1202 layers without auxiliary losses, without changing the optimizer, and without adding parameters relative to the plain counterpart.

## Assumptions
- A1: Multiple stacked nonlinear layers can asymptotically approximate complex functions (and, by the same hypothesis, residual functions). This is noted as still an open question (footnote 2).
- A2: Optimal mappings in real recognition tasks are closer to identity than to a generic random function — supported a posteriori by Fig. 7.
- A3: Standard SGD with momentum and BN is sufficient as the optimizer; no second-order or specialized solver is required.
- A4: Identity shortcuts can be applied wherever input and output dimensions agree; dimension-changing shortcuts use either zero-padding (option A) or 1×1 projections (option B/C).
