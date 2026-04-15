# Claims

## C01: Residual learning enables training of very deep networks
- **Statement**: The residual learning framework, which reformulates layers as learning residual functions F(x) with reference to the input via shortcut connections, enables effective training of networks with over 100 layers without degradation.
- **Status**: supported
- **Falsification criteria**: A residual network of 100+ layers that shows degradation (higher training error than a shallower residual network of the same family) under the same training protocol.
- **Proof**: [E01, E02, E04]
- **Evidence basis**: Table 2 shows ResNet-34 achieves 25.03% top-1 error vs plain-34's 28.54%. Table 3 shows ResNet-50/101/152 achieve progressively lower error (22.85/21.75/21.43% top-1). Table 6 shows CIFAR-10 ResNets scale to 110 layers with 6.43% error.
- **Interpretation**: The residual formulation addresses the fundamental optimization difficulty of training very deep networks by making identity-like mappings easy to learn.
- **Dependencies**: []
- **Tags**: residual learning, depth, optimization, core contribution

## C02: Deeper plain networks exhibit training degradation
- **Statement**: Increasing depth of plain (non-residual) networks beyond approximately 30 layers leads to higher training error, which is not caused by overfitting but by optimization difficulty.
- **Status**: supported
- **Falsification criteria**: A plain network deeper than 34 layers that achieves training error equal to or lower than its shallower counterpart under the same training protocol without any skip connections or equivalent mechanism.
- **Proof**: [E01]
- **Evidence basis**: Table 2 shows plain-34 has 28.54% top-1 validation error vs plain-18's 27.94%. Figure 4 (left) shows the 34-layer plain net has higher training error throughout training. Figure 6 shows the same degradation pattern on CIFAR-10.
- **Interpretation**: This degradation is a fundamental optimization problem — the solver cannot find solutions at least as good as the shallower model despite the deeper model having a strictly larger solution space.
- **Dependencies**: []
- **Tags**: degradation, plain networks, optimization, depth

## C03: Residual networks gain accuracy from increased depth
- **Statement**: Unlike plain networks, residual networks consistently improve accuracy as depth increases from 18 to 152 layers on ImageNet.
- **Status**: supported
- **Falsification criteria**: A deeper ResNet (e.g., ResNet-101) that has higher validation error than a shallower ResNet (e.g., ResNet-50) under the same training protocol and architecture family.
- **Proof**: [E02, E03]
- **Evidence basis**: Table 3 shows monotonic improvement: ResNet-34 (25.03%), ResNet-50 (22.85%), ResNet-101 (21.75%), ResNet-152 (21.43%) top-1 error. Table 4 shows ResNet-152 achieves 19.38% top-1 single-model error on test set.
- **Interpretation**: The residual formulation successfully addresses the degradation problem, enabling the benefits of depth to be realized in practice.
- **Dependencies**: [C01, C02]
- **Tags**: depth scaling, accuracy, ImageNet

## C04: Identity shortcuts are sufficient for addressing degradation
- **Statement**: Identity shortcut connections (option A: zero-padding for dimension changes) are sufficient to address the degradation problem and do not require projection shortcuts.
- **Status**: supported
- **Falsification criteria**: A residual network using identity shortcuts (option A) that shows degradation as depth increases, while the same architecture with projection shortcuts (option B/C) does not.
- **Proof**: [E03]
- **Evidence basis**: Table 3 shows ResNet-34 A (25.03%), B (24.52%), C (24.19%) — all three options substantially outperform plain-34 (28.54%). The differences among A/B/C are small.
- **Interpretation**: The small margins among shortcut options suggest that projection shortcuts are not essential for addressing degradation. Identity shortcuts suffice; projections provide only marginal gains, likely from the extra parameters rather than being critical to the residual mechanism.
- **Dependencies**: [C01]
- **Tags**: identity shortcuts, projection shortcuts, ablation

## C05: ResNets achieve state-of-the-art on ImageNet classification
- **Statement**: A 152-layer ResNet achieves 19.38% top-1 single-model error on ImageNet validation (Table 4), and an ensemble of ResNets achieves 3.57% top-5 error on the test set (Table 5), winning 1st place in ILSVRC 2015.
- **Status**: supported
- **Falsification criteria**: Another method achieving lower top-5 test error than 3.57% on the same ILSVRC 2015 benchmark under comparable conditions.
- **Proof**: [E02]
- **Evidence basis**: Table 4 shows ResNet-152 at 19.38/4.49 top-1/top-5 single-model error, outperforming VGG-16 (28.07/9.33), GoogLeNet (–/9.15), PReLU-net (24.27/7.38). Table 5 shows the ensemble at 3.57% top-5 test error.
- **Interpretation**: ResNets demonstrate that depth, enabled by residual learning, is the dominant factor for classification performance improvement.
- **Dependencies**: [C01, C03]
- **Tags**: ImageNet, ILSVRC, state-of-the-art, classification

## C06: Deep residual representations generalize to other vision tasks
- **Statement**: Replacing VGG-16 with ResNet-101 as the backbone in Faster R-CNN yields a 6.0% increase in COCO mAP@[.5,.95] (from 21.2% to 27.2%), and ResNets won 1st place in ILSVRC & COCO 2015 detection and segmentation competitions.
- **Status**: supported
- **Falsification criteria**: A non-residual backbone of comparable depth and FLOPs that matches or exceeds ResNet-101's detection/segmentation performance when used as a drop-in replacement.
- **Proof**: [E05]
- **Evidence basis**: Table 8 shows ResNet-101 achieves 48.4/27.2 mAP@.5/mAP@[.5,.95] on COCO vs VGG-16's 41.5/21.5. The paper reports winning 1st place in ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation at ILSVRC & COCO 2015.
- **Interpretation**: The learned residual representations are not specific to classification — they provide fundamentally better features that transfer across recognition tasks.
- **Dependencies**: [C01, C05]
- **Tags**: generalization, detection, segmentation, COCO, PASCAL VOC, transfer
