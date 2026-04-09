# Evidence

| File | Source | Type | Claims | Description |
|------|--------|------|--------|-------------|
| `tables/table2_imagenet_plain_vs_residual.md` | Table 2 | raw_table | C01, C02 | Exact 18/34-layer plain-vs-residual top-1 validation comparison |
| `tables/table3_imagenet_validation_full.md` | Table 3 | raw_table | C03, C04 | Full ImageNet validation table including plain-34, ResNet-34 A/B/C, and deeper residual models |
| `tables/derived_from_table3_residual_depth_slice.md` | Derived from Table 3 | derived_subset | C03 | Filtered residual-depth rows used for the depth-scaling claim |
| `tables/derived_from_table3_shortcut_options.md` | Derived from Table 3 | derived_subset | C04 | Filtered plain-34 and ResNet-34 A/B/C rows used for the shortcut-variant claim |

## Notes

- Table values are transcribed directly from the paper's reported results for the represented slice.
- This test artifact emphasizes the degradation-to-residual-learning path rather than the full paper.
