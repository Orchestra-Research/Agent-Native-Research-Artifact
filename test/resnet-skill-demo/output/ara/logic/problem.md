# Problem Specification

## Observations

### O1: Depth is critical for visual recognition
- **Statement**: Recent evidence reveals that network depth is of crucial importance; leading results on ImageNet all exploit "very deep" models with depth of sixteen to thirty layers.
- **Evidence**: §1; VGG-16 [41], GoogLeNet [44], PReLU-net [13] results on ImageNet
- **Implication**: Deeper networks capture richer hierarchical features needed for complex recognition tasks.

### O2: Deeper plain networks exhibit degradation
- **Statement**: With network depth increasing, accuracy gets saturated and then degrades rapidly. The 34-layer plain network has higher training error (28.54% top-1) than the 18-layer plain network (27.94% top-1) on ImageNet validation.
- **Evidence**: Table 2, Figure 4 (left), §4.1
- **Implication**: Adding more layers to a suitably deep model leads to higher training error — this is not caused by overfitting.

### O3: Degradation is an optimization problem, not overfitting
- **Statement**: The deeper 34-layer plain network has higher training error throughout the whole training procedure, even though the solution space of the 18-layer plain network is a subspace of the 34-layer one.
- **Evidence**: Figure 4 (left), §4.1
- **Implication**: The solver cannot find solutions at least as good as the shallower model, indicating optimization difficulty rather than capacity issues.

### O4: Construction argument for identity mapping
- **Statement**: There exists a solution by construction to the deeper model: the added layers are identity mapping, and the other layers are copied from the learned shallower model. The existence of this constructed solution indicates that a deeper model should produce no higher training error than its shallower counterpart.
- **Evidence**: §1, §3
- **Implication**: Current solvers are unable to find solutions that are comparably good or better than the constructed solution.

## Gaps

### G1: Deep networks cannot be trained effectively
- **Statement**: Plain networks deeper than ~30 layers suffer from degradation — higher training error with more depth — despite having larger solution spaces.
- **Caused by**: O2, O3
- **Existing attempts**: Normalized initialization [23, 9, 37, 13], intermediate normalization layers (BN) [16]
- **Why they fail**: These methods enable convergence for tens of layers but do not solve the degradation problem for very deep networks. The 34-layer plain net still degrades despite using BN.

### G2: No explicit mechanism to learn identity mappings
- **Statement**: Standard stacked nonlinear layers have difficulty approximating identity mappings when the optimal function is close to identity.
- **Caused by**: O3, O4
- **Existing attempts**: Highway networks [42, 43] with gating mechanisms
- **Why they fail**: Highway networks have not demonstrated accuracy gains with extremely increased depth (e.g., over 100 layers).

## Key Insight
- **Insight**: Instead of hoping each stack of layers directly fits a desired underlying mapping H(x), explicitly let the layers fit a residual function F(x) = H(x) − x. The original function becomes F(x) + x. If identity mapping is optimal, it is easier to push F(x) toward zero than to fit an identity mapping with nonlinear layers.
- **Derived from**: O3, O4
- **Enables**: Training of extremely deep networks (100+ layers) via shortcut connections that perform identity mapping, adding neither extra parameters nor computational complexity.

## Assumptions
- A1: The degradation problem is caused by optimization difficulty, not by overfitting or vanishing/exploding gradients (the latter being addressed by BN).
- A2: Residual functions are easier to optimize than unreferenced mappings when the optimal function is close to identity.
- A3: Identity shortcuts (adding no parameters) are sufficient to address the degradation problem.
- A4: The residual learning formulation is generic and applicable across different vision tasks and architectures.
