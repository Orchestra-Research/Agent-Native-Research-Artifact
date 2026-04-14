# Problem Specification

## Observations

### O1: Deeper plain networks exhibit higher training error
- **Statement**: A 34-layer plain network has higher training error than an 18-layer plain network throughout the training procedure, even though the 18-layer network's solution space is a subspace of the 34-layer network's (Table 2, Figure 4 left).
- **Evidence**: Table 2 (plain-34: 28.54% top-1, plain-18: 27.94% top-1); Figure 4 left shows training curves
- **Implication**: Adding depth to plain networks actively hinders optimization rather than helping

### O2: The degradation is not caused by overfitting
- **Statement**: The deeper 34-layer plain model shows higher training error (not just test error), ruling out overfitting as the cause. These networks are trained with BN, which ensures forward-propagated signals have non-zero variances and backward gradients exhibit healthy norms (§4.1, Figure 4).
- **Evidence**: Figure 4 left (thin curves = training error); §4.1 discussion of vanishing gradients
- **Implication**: The degradation is an optimization difficulty, not a generalization problem

### O3: A constructed solution exists that should not degrade
- **Statement**: Given a shallower model, one can construct a deeper model by adding identity layers on top that copy the shallower model's learned features. This deeper model should produce no higher training error than the shallower one (§1, §3).
- **Evidence**: §1 paragraph on construction argument; §3 opening discussion
- **Implication**: Current solvers are unable to find solutions that are comparably good or better than the constructed solution

### O4: Network depth is critical for visual recognition
- **Statement**: Leading results on ImageNet (VGG-16/19, GoogLeNet) all use "very deep" models with 16–30 layers, and depth has been identified as crucial for performance (§1).
- **Evidence**: §1 cites [41, 44, 13, 16]; Table 4 and Table 5 show SOTA results
- **Implication**: The community needs a way to train much deeper networks without degradation

## Gaps

### G1: Plain depth fails to translate to accuracy
- **Statement**: Simply stacking more layers in a plain architecture leads to worse optimization and higher error
- **Caused by**: O1, O2
- **Existing attempts**: Normalized initialization [23, 9, 37, 13], intermediate normalization layers (BN) [16]
- **Why they fail**: BN enables convergence for networks with tens of layers, but the degradation problem persists at greater depths (§1)

### G2: No mechanism to exploit the identity construction argument
- **Statement**: The existence of a solution by construction (identity mapping on added layers) is not realizable by current solvers
- **Caused by**: O3
- **Existing attempts**: Standard SGD training of plain stacked layers
- **Why they fail**: The solver cannot find the identity mapping through direct optimization of unreferenced layers (§3)

## Key Insight
- **Insight**: Instead of learning the desired mapping H(x) directly, explicitly reformulate the layers as learning a residual function F(x) = H(x) - x, so the original mapping becomes F(x) + x. If the identity mapping is optimal, it is easier to push F(x) toward zero than to learn an identity through a stack of nonlinear layers.
- **Derived from**: O3 (construction argument), G2 (solver inability)
- **Enables**: Shortcut connections that perform identity mapping, adding neither parameters nor computational complexity, allowing networks to gain accuracy from substantially increased depth

## Assumptions
- A1: The degradation problem is a fundamental optimization difficulty, not caused by vanishing/exploding gradients (which are addressed by BN)
- A2: The residual function F(x) is easier to optimize toward zero than learning an identity through stacked nonlinear layers
- A3: Identity shortcuts introduce neither extra parameters nor computational complexity when input and output dimensions match
