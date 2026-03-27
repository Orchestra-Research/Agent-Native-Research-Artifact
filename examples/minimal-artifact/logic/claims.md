# Claims

## C01: Attention-only architecture achieves SOTA
- **Statement**: A model based entirely on self-attention, without recurrence or convolution, achieves state-of-the-art BLEU on WMT 2014 English-to-German translation.
- **Status**: supported
- **Falsification criteria**: A recurrent or convolutional model trained under identical conditions achieves higher BLEU.
- **Proof**: [E01]
- **Dependencies**: []
- **Tags**: architecture, translation, BLEU

## C02: Transformers train faster
- **Statement**: The Transformer requires significantly less training time than architectures based on recurrent or convolutional layers.
- **Status**: supported
- **Falsification criteria**: An RNN-based model achieves comparable quality with equal or less compute.
- **Proof**: [E02]
- **Dependencies**: [C01]
- **Tags**: efficiency, training-time
