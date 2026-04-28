# Related Work

## RW01: Highway Networks (Srivastava, Greff & Schmidhuber, 2015)
- **DOI**: arXiv:1505.00387 (Highway), arXiv:1507.06228 (Training very deep nets)
- **Type**: refutes (the gating choice)
- **Delta**:
  - What changed: Replace highway's *data-dependent gated* shortcuts with parameter-free identity shortcuts.
  - Why: When a highway gate "closes" (approaches zero) the layer becomes non-residual; highway networks have not demonstrated accuracy gains beyond ~100 layers.
- **Claims affected**: C02, C03, C06.
- **Adopted elements**: The general idea of skip connections, but the gating mechanism is rejected.

## RW02: VGG (Simonyan & Zisserman, 2015)
- **DOI**: arXiv:1409.1556 (refs [41]; "very deep CNNs for large-scale image recognition")
- **Type**: baseline
- **Delta**:
  - What changed: Adopt VGG's design philosophy of stacked 3×3 convs and the "same map size ⇒ same #filters; halved size ⇒ doubled #filters" rule, but at much greater depth and lower complexity (3.6 GFLOPs at 34 layers vs. VGG-19's 19.6 GFLOPs).
  - Why: VGG provides the cleanest plain-net baseline against which residual learning can be measured.
- **Claims affected**: C01, C03, C08.
- **Adopted elements**: VGG-style design rules; reference numbers for FLOPs comparison.

## RW03: Batch Normalization (Ioffe & Szegedy, 2015)
- **DOI**: ref [16] in the paper
- **Type**: imports
- **Delta**:
  - What changed: BN is applied after every conv and before activation in *both* plain and residual nets. The paper uses BN to verify that vanishing forward signals are *not* the cause of degradation.
  - Why: BN is the standard tool for preventing signal collapse in deep nets and isolates the optimization-difficulty hypothesis.
- **Claims affected**: C01, C02, C03.
- **Adopted elements**: BN architecture; "no dropout" recipe combined with BN (also from this work).

## RW04: MSRA initialization (He, Zhang, Ren & Sun, 2015 — "Delving deep into rectifiers")
- **DOI**: ref [13] in the paper
- **Type**: imports
- **Delta**:
  - What changed: Initialize all conv weights with the MSRA scheme. The exact same init is used for plain and residual variants.
  - Why: Pairing PReLU-aware init with BN gives the cleanest starting point for the depth ablation.
- **Claims affected**: C01, C02, C06.
- **Adopted elements**: Weight initialization scheme.

## RW05: GoogLeNet / Inception (Szegedy et al., 2015)
- **DOI**: ref [44] in the paper
- **Type**: baseline
- **Delta**:
  - What changed: Compare against GoogLeNet on ILSVRC'14 (top-5 9.15) and Going Deeper (7.89) without adopting Inception's branching topology.
  - Why: A second strong reference point alongside VGG; GoogLeNet uses an "inception layer" composed of a shortcut branch and a few deeper branches.
- **Claims affected**: C03 (state-of-the-art comparison).
- **Adopted elements**: None architecturally; only the comparison.

## RW06: PReLU-net / "Surpassing human-level on ImageNet" (He et al., 2015)
- **DOI**: ref [13] (same group)
- **Type**: baseline
- **Delta**:
  - What changed: Used as the prior single-model state of the art on ImageNet validation (24.27 top-1 / 7.38 top-5 in Table 4). ResNet-152 single-model surpasses it (19.38 / 4.49).
  - Why: Direct comparison point at single-model level.
- **Claims affected**: C03.
- **Adopted elements**: None.

## RW07: BN-Inception (Ioffe & Szegedy, 2015)
- **DOI**: ref [16]
- **Type**: baseline
- **Delta**:
  - What changed: Used as the prior single-model SOTA on ImageNet (21.99 / 5.81 in Table 4) and as the prior best ensemble (4.82 in Table 5).
  - Why: Most competitive single-model and ensemble baselines available at the time.
- **Claims affected**: C03.
- **Adopted elements**: None architecturally; ensemble/single-model comparison points.

## RW08: Residual representations — VLAD / Fisher Vector / Encoding residual vectors
- **DOI**: refs [18], [17] (residual encoding); refs [4], [48] (VLAD/Fisher use)
- **Type**: extends
- **Delta**:
  - What changed: Generalize the *residual representation* idea (encoding residuals rather than originals, e.g., VLAD encoding by residual vectors w.r.t. a dictionary) to deep learning by reformulating each layer as a residual function.
  - Why: Provides motivation that residual representations can be "more effective" for retrieval/classification (refs [4], [48]) and have a long history.
- **Claims affected**: C02.
- **Adopted elements**: Conceptual motivation only.

## RW09: Multigrid / hierarchical basis preconditioning (Briggs et al., 2000; Szeliski 2006/2010)
- **DOI**: refs [3], [45], [46]
- **Type**: extends
- **Delta**:
  - What changed: Carry the low-level vision insight that solvers operating on residual variables converge much faster than solvers unaware of the residual nature into deep CNNs.
  - Why: Provides a precedent that "good reformulation or preconditioning can simplify the optimization."
- **Claims affected**: C02 (motivation for why residual easing is plausible).
- **Adopted elements**: Conceptual motivation only.

## RW10: Faster R-CNN (Ren, He, Girshick & Sun, 2015)
- **DOI**: ref [32]
- **Type**: imports
- **Delta**:
  - What changed: Use Faster R-CNN as the detection framework, swapping the VGG-16 backbone with ResNet-101 (Appendix A). Otherwise identical hyperparameters in the baseline rows.
  - Why: Isolates the contribution of the backbone (i.e., the learned representation).
- **Claims affected**: C08.
- **Adopted elements**: 4-step alternating training, RPN + Fast R-CNN, anchor design.

## RW11: Networks on Conv feature maps / NoC (Ren, He, Girshick & Sun, 2015)
- **DOI**: ref [33]
- **Type**: imports
- **Delta**:
  - What changed: Use the NoC idea to share full-image conv features through layers with stride ≤16 and treat conv5_x as the per-RoI fc-equivalent in ResNet-101 Faster R-CNN.
  - Why: Lets ResNet-101 (which lacks hidden fc layers) plug into the Faster R-CNN architecture cleanly.
- **Claims affected**: C08.
- **Adopted elements**: Conv-feature-sharing strategy.

## RW12: PASCAL VOC (Everingham et al., 2010); ImageNet (Russakovsky et al., 2015); COCO (Lin et al., 2014)
- **DOI**: refs [5], [36], [26]
- **Type**: imports (datasets)
- **Delta**: Used as the evaluation datasets for ImageNet classification, ImageNet localization, COCO detection, and PASCAL VOC detection benchmarks.
- **Claims affected**: C03, C06, C08.
- **Adopted elements**: Standard splits and evaluation protocols.

## Briefer citations (no specific technical delta, captured for citation footprint)

- [1] Bengio, Simard & Frasconi, "Learning long-term dependencies with gradient descent is difficult" (1994) — historical reference for gradient-vanishing problem (§1).
- [2] Bishop, *Neural networks for pattern recognition* (1995) — historical reference on shortcut connections.
- [6] Gidaris & Komodakis, "Object detection via multi-region & semantic segmentation-aware CNN" (2015) — context for VOC2012 SOTA discussion in Appendix B.
- [7] Girshick, "Fast R-CNN" (2015) — Fast R-CNN ROI pooling, used inside Faster R-CNN.
- [8] Girshick et al., "Rich feature hierarchies (R-CNN)" (2014) — R-CNN, referenced as the precursor pipeline used in ImageNet localization (Appendix C).
- [9] Glorot & Bengio, "Understanding the difficulty of training deep feedforward NNs" (AISTATS 2010) — Xavier init reference, baseline for initialization discussion.
- [10] Goodfellow et al., "Maxout networks" (2013) — CIFAR-10 baseline in Table 6.
- [11] He, Zhang, Ren & Sun, "Convolutional networks at constrained time cost" (2015) — corroborating prior report of degradation (§1).
- [12] He, Zhang, Ren & Sun, "Spatial pyramid pooling in deep convs" (2014) — SPP/RoI feature pyramid; used in COCO multi-scale testing.
- [14] Hinton et al., "Improving NNs by preventing co-adaptation (dropout)" (2012) — explicitly *not* used here (no dropout).
- [15] Hochreiter & Schmidhuber, "Long short-term memory" (1997) — gating motivation referenced when contrasting with highway networks.
- [17] Jegou, Douze & Schmid, "Product quantization for nearest neighbor" (TPAMI 2011) — residual-vector encoding precedent.
- [19] Jia et al., "Caffe" (2014) — implementation library reference.
- [20] Krizhevsky, "Multiple layers of features from tiny images" (2009) — CIFAR-10 dataset.
- [21] Krizhevsky, Sutskever & Hinton, "ImageNet classification with deep CNNs" (NIPS 2012) — AlexNet, historical reference for color/scale augmentation and 10-crop testing.
- [22] LeCun et al., "Backpropagation applied to handwritten zip code recognition" (1989) — historical reference for SGD with backprop.
- [23] LeCun et al., "Efficient backprop" (1998) — historical reference for normalization.
- [24] Lee et al., "Deeply-supervised nets (DSN)" (2014) — auxiliary classifier baseline; CIFAR-10 augmentation recipe (4-pixel pad + crop) borrowed.
- [25] Lin, Chen & Yan, "Network in network (NIN)" (2013) — CIFAR-10 baseline in Table 6.
- [27] Long, Shelhamer & Darrell, "Fully convolutional networks for semantic segmentation" (CVPR 2015) — referenced for fully-convolutional dense testing.
- [28] Montufar, Pascanu, Cho & Bengio, "On the number of linear regions of deep NNs" (NIPS 2014) — cited at footnote 2 for the asymptotic-approximation hypothesis.
- [29] Nair & Hinton, "ReLU" (ICML 2010) — activation function used throughout.
- [30] Perronnin & Dance, "Fisher kernels on visual vocabularies" (CVPR 2007) — historical residual-encoding precedent.
- [31] Raiko, Valpola & LeCun, "Deep learning made easier by linear transformations in perceptrons" (AISTATS 2012) — linear-shortcut precedent.
- [33] Ren, He, Girshick & Sun, "Object detection networks on conv feature maps (NoC)" (arXiv:1504.06066) — see RW11.
- [34] Ripley, *Pattern recognition and neural networks* (1996) — historical shortcut reference.
- [35] Romero et al., "FitNets: Hints for thin deep nets" (ICLR 2015) — CIFAR-10 baseline in Table 6.
- [37] Saxe, McClelland & Ganguli, "Exact solutions to the nonlinear dynamics of learning in deep linear NNs" (arXiv:1312.6120) — referenced for normalization discussion.
- [38] Schraudolph, "Accelerated gradient descent by factor-centering decomposition" (1998) — precondition / centering precedent.
- [39] Schraudolph, "Centering NN gradient factors" (1998) — see [38].
- [40] Sermanet et al., "OverFeat" (ICLR 2014) — ImageNet localization baseline in Table 14.
- [42] Srivastava, Greff & Schmidhuber, "Highway networks" (arXiv:1505.00387) — see RW01.
- [43] Srivastava, Greff & Schmidhuber, "Training very deep networks" (arXiv:1507.06228) — see RW01.
- [45] Szeliski, "Fast surface interpolation using hierarchical basis functions" (TPAMI 1990) — see RW09.
- [46] Szeliski, "Locally adapted hierarchical basis preconditioning" (SIGGRAPH 2006) — see RW09.
- [47] Vatanen, Raiko, Valpola & LeCun, "Pushing stochastic gradient towards second-order methods" (NIPS 2013) — second-order/preconditioning context.
- [48] Vedaldi & Fulkerson, "VLFeat" (2008) — VLFeat library / VLAD support.
- [49] Venables & Ripley, *Modern applied statistics with s-plus* (1999) — historical shortcut reference.
- [50] Zeiler & Fergus, "Visualizing and understanding convolutional networks" (ECCV 2014) — referenced for "low/mid/high-level features" framing in §1.
