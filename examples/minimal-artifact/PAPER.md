---
title: "Example Paper: Attention Is All You Need"
authors: [Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin]
year: 2017
venue: "NeurIPS"
doi: "arXiv:1706.03762"
ara_version: "1.0"
domain: "Natural Language Processing"
keywords: [transformer, attention, sequence-to-sequence, machine translation]
claims_summary:
  - "Self-attention alone achieves SOTA on machine translation"
  - "Transformers train faster than recurrent/convolutional alternatives"
abstract: "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks..."
---

# Attention Is All You Need

## Overview

This is a minimal example ARA artifact demonstrating the format. A real artifact would contain complete content in every file.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations about RNN limitations -> transformer insight |
| [claims.md](logic/claims.md) | 2 falsifiable claims (C01-C02) |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | Minimal 3-node research DAG |
