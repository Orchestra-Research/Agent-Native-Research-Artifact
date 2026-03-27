# Agent-Native Research Artifact (ARA)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-green)](https://agentskills.io)

**Agent skills for structured research knowledge extraction, management, and tracking.**

ARA is a structured, machine-executable knowledge format designed for AI agents. Instead of flat PDFs, ARA organizes research into cross-linked layers — cognitive (claims, concepts, heuristics), physical (configs, code stubs), exploration (research DAG), and evidence (tables, figures) — so that agents can navigate, verify, and build on research efficiently.

This repository contains three open-source agent skills that work with ARA:

| Skill | Description | Invoke |
|-------|-------------|--------|
| **[ingestor](skills/ingestor/)** | Converts papers, repos, notes, or any research input into a structured ARA artifact | `/ingestor <path>` |
| **[meta-research](skills/meta-research/)** | Hypothesis-driven research workflow with literature survey, experiment design, and reflection loops | `/meta-research <topic>` |
| **[pm](skills/pm/)** | Post-session research process recorder with provenance tracking | `/pm` |

## Install

### Quick install (all agents)

```bash
npx skills add Orchestra-Research/Agent-Native-Research-Artifact
```

### Install a specific skill

```bash
npx skills add Orchestra-Research/Agent-Native-Research-Artifact --skill ingestor
```

### Manual install (Claude Code)

```bash
# All skills — project-level
cp -r skills/* .claude/skills/

# All skills — user-level (available in all projects)
cp -r skills/* ~/.claude/skills/

# Single skill
cp -r skills/ingestor ~/.claude/skills/ingestor
```

## What is ARA?

An ARA artifact is a directory with this structure:

```
artifact/
  PAPER.md                    # Root manifest + layer index
  logic/                      # Cognitive layer (What & Why)
    problem.md                #   Observations -> gaps -> key insight
    claims.md                 #   Falsifiable assertions with proof refs
    concepts.md               #   Formal definitions
    experiments.md            #   Declarative experiment plans
    solution/
      architecture.md         #   System design + component graph
      algorithm.md            #   Math + pseudocode
      constraints.md          #   Boundary conditions
      heuristics.md           #   Implementation tricks + rationale
    related_work.md           #   Typed dependency graph
  src/                        # Physical layer (How)
    configs/                  #   Hyperparameters with rationale
    execution/                #   Code stubs (core algorithm only)
    environment.md            #   Dependencies, hardware, seeds
  trace/                      # Exploration graph (Journey)
    exploration_tree.yaml     #   Research DAG with typed nodes
  evidence/                   # Raw proof
    tables/                   #   Exact result tables
    figures/                  #   Extracted data points
```

### Key design principles

- **Progressive disclosure**: `PAPER.md` (~200 tokens) tells agents if the artifact is relevant. Deeper files load on demand.
- **Cross-layer binding**: Claims reference experiments, experiments reference evidence, heuristics reference code. Everything is linked.
- **Dead ends preserved**: Failed approaches and rejected alternatives are first-class nodes in the exploration tree — they prevent agents from rediscovering known failures.
- **Provenance tracking**: Every entry carries a provenance tag (`user`, `ai-suggested`, `ai-executed`, `user-revised`) distinguishing human-confirmed facts from AI inferences.

## Skills

### Ingestor

Converts ANY research input into a complete ARA artifact. Accepts PDFs, GitHub repos, experiment logs, code directories, raw notes, or combinations.

```
/ingestor path/to/paper.pdf
/ingestor https://github.com/org/repo
/ingestor path/to/paper.pdf path/to/code/ --output ./my-artifact/
```

The ingestor follows a 4-stage epistemic protocol:
1. **Semantic Deconstruction** — extract raw knowledge atoms
2. **Cognitive Mapping** — map to claims, concepts, experiments
3. **Physical Stubbing** — generate configs and code stubs
4. **Exploration Graph Extraction** — reconstruct the research DAG

See [skills/ingestor/SKILL.md](skills/ingestor/SKILL.md) for the full specification.

### Meta-Research

A hypothesis-driven research workflow agent with two roles:
- **Clawbot Executor**: runs the research lifecycle end-to-end
- **Research Advisor (Heartbeat)**: periodic strategic review and course correction

```
/meta-research "Does scaling law X hold for architecture Y?"
```

Workflow: Literature Survey -> Hypothesis Generation -> Judgment Gate -> Experiment Design -> Execution -> Reflection (loop)

See [skills/meta-research/SKILL.md](skills/meta-research/SKILL.md) for the full specification.

### PM (Process Manager)

A post-session research recorder that extracts decisions, experiments, dead ends, claims, and heuristics from your coding session and writes them to an ARA artifact.

```
/pm
```

Runs automatically at the end of each session. Maintains provenance tracking so you always know what came from the human vs. the AI.

See [skills/pm/SKILL.md](skills/pm/SKILL.md) for the full specification.

## Compatibility

These skills follow the [Agent Skills open standard](https://agentskills.io/specification) and work with:

- [Claude Code](https://claude.ai/code) (Anthropic)
- [Codex CLI](https://github.com/openai/codex) (OpenAI)
- [GitHub Copilot](https://github.com/features/copilot)
- [Cursor](https://cursor.com)
- Any agent supporting the Agent Skills specification

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add or improve skills.

## License

[MIT](LICENSE)
