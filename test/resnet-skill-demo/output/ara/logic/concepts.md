# Concepts

## Degradation Problem
- **Notation**: none
- **Definition**: The regime where a deeper plain network shows higher training error than a shallower counterpart despite containing the shallower solution space.
- **Boundary conditions**: Applies to the matched plain-network comparisons in the paper; it is not equivalent to ordinary overfitting.
- **Related concepts**: Residual Mapping, Plain Network

## Plain Network
- **Notation**: `H(x)`
- **Definition**: A deep convolutional stack without shortcut additions, where each block attempts to learn the full mapping directly.
- **Boundary conditions**: Used as the comparison baseline in the 18-layer and 34-layer experiments.
- **Related concepts**: Degradation Problem, Residual Mapping

## Residual Mapping
- **Notation**: `F(x) = H(x) - x`
- **Definition**: A reformulation in which the learned function represents the deviation from an identity shortcut rather than the full target mapping.
- **Boundary conditions**: Most natural when the desired mapping is close to identity or can be represented as an identity plus correction.
- **Related concepts**: Shortcut Connection, Residual Block

## Shortcut Connection
- **Notation**: `x` or `W_s x`
- **Definition**: A path that bypasses the residual branch and is added to its output.
- **Boundary conditions**: Identity shortcuts apply when dimensions match; projection shortcuts apply when dimensions differ.
- **Related concepts**: Residual Mapping, Projection Shortcut

## Projection Shortcut
- **Notation**: `W_s x`
- **Definition**: A learned linear shortcut, typically a 1x1 convolution, used to match dimensions across stage transitions.
- **Boundary conditions**: Used only when channel count or spatial resolution changes.
- **Related concepts**: Shortcut Connection, Residual Block

## Residual Block
- **Notation**: `y = F(x, {W_i}) + x`
- **Definition**: A building block consisting of a residual branch and a shortcut merge.
- **Boundary conditions**: The 18/34-layer family uses two 3x3 convolutions per basic block, while deeper variants use bottlenecks.
- **Related concepts**: Residual Mapping, Shortcut Connection
