# Related Work

## RW01: Simonyan & Zisserman, 2014 (VGGNet)
- **DOI**: arXiv:1409.1556
- **Type**: baseline
- **Delta**:
  - What changed: ResNet follows VGG's philosophy of 3x3 filters and doubling-filters-when-halving-size, but introduces shortcut connections and achieves much greater depth (152 vs. 19 layers) with lower FLOPs (11.3B vs. 19.6B)
  - Why: VGG-19 was SOTA but could not scale further due to degradation
- **Claims affected**: C01, C03
- **Adopted elements**: Conv filter design rules (§3.3)

## RW02: Ioffe & Szegedy, 2015 (Batch Normalization)
- **DOI**: arXiv:1502.03167
- **Type**: imports
- **Delta**:
  - What changed: ResNet uses BN as a prerequisite, applied after every convolution and before activation. BN addresses vanishing/exploding gradients but does not solve the degradation problem
  - Why: Enables training of deep networks but the residual formulation is needed on top of BN
- **Claims affected**: C01, C02
- **Adopted elements**: BN layer placement (§3.4)

## RW03: He et al., 2015 (Weight Initialization)
- **DOI**: arXiv:1502.01852
- **Type**: imports
- **Delta**:
  - What changed: Weight initialization scheme designed for ReLU networks; used to initialize all ResNet models from scratch
  - Why: Combined with BN, eliminates the need for pre-training
- **Claims affected**: C01, C02
- **Adopted elements**: Initialization method (§3.4)

## RW04: Srivastava et al., 2015 (Highway Networks)
- **DOI**: arXiv:1505.00387
- **Type**: extends
- **Delta**:
  - What changed: Highway networks use gating functions on shortcuts, introducing extra parameters. ResNet uses parameter-free identity shortcuts, which are simpler and allow depth scaling beyond highway networks' demonstrated range
  - Why: Identity shortcuts are computationally free and sufficient; gating adds complexity without clear benefit at the depths tested
- **Claims affected**: C01, C04
- **Adopted elements**: Concept of shortcut paths (§2)

## RW05: Szegedy et al., 2015 (GoogLeNet/Inception)
- **DOI**: arXiv:1409.4842
- **Type**: baseline
- **Delta**:
  - What changed: GoogLeNet uses inception modules with multiple filter sizes. ResNet achieves better accuracy with simpler 3x3-only blocks plus shortcuts, scaling to much greater depth
  - Why: ResNet's architecture is simpler and more scalable
- **Claims affected**: C03
- **Adopted elements**: None directly; serves as accuracy baseline (Table 4)
