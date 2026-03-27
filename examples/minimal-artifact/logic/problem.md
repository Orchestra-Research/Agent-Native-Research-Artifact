# Problem Specification

## Observations

### O1: Sequential computation bottleneck
- **Statement**: RNNs process tokens sequentially, preventing parallelization and limiting training speed on modern hardware.
- **Evidence**: Section 1, established practice
- **Implication**: Training time scales linearly with sequence length.

### O2: Long-range dependency decay
- **Statement**: Despite gating mechanisms (LSTM, GRU), learning dependencies between distant positions remains difficult.
- **Evidence**: Section 1, prior work
- **Implication**: Quality degrades for long sequences.

## Gaps

### G1: No fully parallel sequence model
- **Statement**: No competitive sequence transduction model eliminates sequential computation entirely.
- **Caused by**: O1
- **Existing attempts**: Convolutional models (ByteNet, ConvS2S) reduce but do not eliminate the bottleneck.
- **Why they fail**: Still require O(log n) or O(n/k) operations for long-range dependencies.

## Key Insight
- **Insight**: Self-attention computes all pairwise token interactions in O(1) sequential operations, enabling full parallelization while maintaining direct access to any position.
- **Derived from**: O1, O2
- **Enables**: A fully attention-based architecture (Transformer) that is both faster to train and better at capturing long-range dependencies.

## Assumptions
- A1: Sufficient GPU memory to store the full attention matrix (O(n^2) space).
- A2: Positional information can be injected via learned or sinusoidal encodings.
