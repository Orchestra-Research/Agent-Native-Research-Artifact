# Derived subset — ResNet-34 shortcut option ablation

**Source**: Derived from Table 3 in "Deep Residual Learning for Image Recognition"
**Caption**: Subset preserving the rows directly relevant to C04 (shortcut option ablation): plain-34 baseline + ResNet-34 with options A / B / C. Other Table 3 rows are intentionally omitted.
**Extraction type**: derived_subset
**Derived from**: `table3_imagenet_validation_full.md`

| model       | shortcut option | top-1 err. | top-5 err. | Δ vs. plain-34 (top-1) |
|-------------|-----------------|------------|------------|------------------------|
| plain-34    | none            | 28.54      | 10.02      | —                      |
| ResNet-34 A | identity + zero-pad | 25.03  | 7.76       | −3.51                  |
| ResNet-34 B | projection on dim change only | 24.52 | 7.46 | −4.02                  |
| ResNet-34 C | projection on every shortcut | 24.19 | 7.40 | −4.35                  |

Per-paper interpretation (§"Identity vs. Projection Shortcuts"):
- All three options are considerably better than plain-34.
- B is slightly better than A; the paper attributes this to A's zero-padded extra dimensions carrying "no residual learning."
- C is marginally better than B; the paper attributes this to extra parameters from the 13 projection shortcuts and rejects C as not essential for fixing degradation.
