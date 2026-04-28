# ResNet Walkthrough

This is the simplest way to understand how to use ARA on a real paper.

## Inputs in This Repo

- `resnet-paper.pdf`: source paper
- `resnet-ara-example/`: example output artifact

## What "using the compiler" means

The compiler is not a standalone binary in this repository. It is a skill specification for an agent. In practice, you use it by giving an agent a research input and asking it to produce an ARA artifact.

For ResNet, the conceptual command is:

```text
/compiler examples/resnet-paper.pdf --output examples/resnet-ara-example/
```

## What the agent is expected to do

When applied to the ResNet paper, the compiler should:

1. Read the paper and extract the core research objects.
2. Turn the degradation problem into `logic/problem.md`.
3. Turn the residual-learning assertions into `logic/claims.md`.
4. Turn the residual block and shortcut mechanism into `logic/solution/`.
5. Preserve the failed deeper-plain-network branch in `trace/exploration_tree.yaml`.
6. Store exact benchmark support in `evidence/`.
7. Add a minimal executable anchor in `src/`.

## How to inspect the example

Start with:

- `resnet-ara-example/PAPER.md`

Then open:

- `resnet-ara-example/logic/problem.md`
- `resnet-ara-example/logic/claims.md`
- `resnet-ara-example/logic/solution/architecture.md`
- `resnet-ara-example/evidence/tables/table2_imagenet_plain_vs_residual.md`
- `resnet-ara-example/trace/exploration_tree.yaml`

## Practical workflow

If you want to use this on another paper or codebase, repeat the same pattern:

1. Put the input PDF or repo in a reachable path.
2. Ask the agent to run the compiler on that input.
3. Choose an output folder such as `./ara-output/`.
4. Review `PAPER.md` first, then verify claims, evidence, and trace links.

## Important limitation

The current `resnet-ara-example/` is a useful worked example, but it is still a curated artifact, not the output of a packaged command-line program in this repository.
