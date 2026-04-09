# Claims

## C01: Residual shortcuts ease optimization at matched depth
- **Statement**: A 34-layer residual network achieves lower top-1 validation error than a matched 34-layer plain network in the paper's ImageNet comparison.
- **Status**: supported
- **Falsification criteria**: A matched 34-layer residual model fails to improve training behavior or top-1 validation error over the 34-layer plain model.
- **Proof**: [E02]
- **Evidence basis**: Table 2 reports 25.03% top-1 error for ResNet-34 A versus 28.54% for plain-34.
- **Interpretation**: The paper also reports lower training error in the associated Figure 4 discussion, but this artifact treats the table-backed validation improvement as the primary supported claim.
- **Dependencies**: none
- **Tags**: residual learning, optimization, ImageNet, matched-depth comparison

## C02: Residual formulation reverses the plain-depth degradation pattern
- **Statement**: The validation-error relationship observed for plain networks from 18 to 34 layers is reversed in the matched residual comparison reported by the paper.
- **Status**: supported
- **Falsification criteria**: Plain and residual depth scaling show the same degradation pattern under the paper's controlled setup.
- **Proof**: [E01, E02]
- **Evidence basis**: Table 2 shows plain-34 worse than plain-18, while ResNet-34 A is better than ResNet-18.
- **Interpretation**: This supports the paper's degradation argument at the comparison level represented in the artifact, without claiming more than the reported matched results.
- **Dependencies**: C01
- **Tags**: degradation problem, plain network, residual block

## C03: Residual families continue to benefit from increased depth
- **Statement**: In Table 3, the deeper bottleneck models ResNet-50, ResNet-101, and ResNet-152 achieve lower top-1 and top-5 error than ResNet-34 B.
- **Status**: supported
- **Falsification criteria**: Any of ResNet-50, ResNet-101, or ResNet-152 fails to improve over ResNet-34 B in the reported ImageNet validation table.
- **Proof**: [E03]
- **Evidence basis**: Table 3 lists ResNet-34 B at 24.52 / 7.46 and the deeper bottleneck models at progressively lower top-1 / top-5 error.
- **Interpretation**: The deeper option-B family continues to improve over the paper's main 34-layer residual baseline; ResNet-34 C is retained as an additional comparator rather than the primary baseline.
- **Dependencies**: C01
- **Tags**: depth scaling, ImageNet, ResNet-50, ResNet-101, ResNet-152

## C04: Projection shortcuts help slightly but are not essential
- **Statement**: All shortcut options A, B, and C outperform the plain-34 baseline, while option B is slightly better than option A and option C is only marginally better than option B.
- **Status**: supported
- **Falsification criteria**: A, B, or C fails to improve over plain-34, or the reported ordering among A/B/C is not present in the source table and discussion.
- **Proof**: [E04]
- **Evidence basis**: Table 3 reports plain-34 at 28.54 / 10.02, ResNet-34 A at 25.03 / 7.76, ResNet-34 B at 24.52 / 7.46, and ResNet-34 C at 24.19 / 7.40.
- **Interpretation**: The paper's main takeaway is qualitative: projection shortcuts help slightly, but the identity-dominant formulation is already sufficient to address degradation.
- **Dependencies**: C01
- **Tags**: shortcut variants, option A, option B, option C, projection shortcuts
