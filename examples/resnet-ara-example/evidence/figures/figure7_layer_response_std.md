# Figure 7: CIFAR-10 layer-response std (after BN, before nonlinearity)

**Source**: Figure 7, §4.2
**Caption**: "Standard deviations (std) of layer responses on CIFAR-10. The responses are the outputs of each 3×3 layer, after BN and before nonlinearity. Top: the layers are shown in their original order. Bottom: the responses are ranked in descending order."
**Axes**: X (top) = layer index in original order; X (bottom) = layer index ranked by magnitude. Y = std of activations.
**Extraction type**: figure_summary

The figure overlays four series: plain-20, plain-56, ResNet-20, ResNet-56, ResNet-110.

Qualitative observations from the plot (numerical curves are not tabulated):

- **ResNet response stds are smaller than plain-net stds at corresponding layer indices**, supporting the paper's argument that residual functions are typically closer to zero than non-residual functions.
- **Deeper ResNets have smaller per-layer response magnitudes**: ResNet-110 < ResNet-56 < ResNet-20. The paper interprets this as "an individual layer of ResNets tends to modify the signal less" when more layers are available.
- The ranking (bottom plot) shows that even the largest-magnitude residual layers in ResNet-110 are smaller than those in ResNet-20 / ResNet-56.

**Key observation**: Empirical support for the prior that optimal mappings sit near identity (used as motivation for the residual reformulation; cited under O5 and as supporting interpretation for C02).
