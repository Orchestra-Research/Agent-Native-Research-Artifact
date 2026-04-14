# Exploration Tree YAML Specification

The exploration tree is the "git log" for research — a structured, traversable record of every
successful branch, failed attempt, and design decision that shaped the final result.

## Format

```yaml
# Exploration Tree — {paper_id}
# Research DAG: nested tree with cross-edges (also_depends_on) forming a DAG.
# Node types: question | experiment | dead_end | decision | pivot

tree:
  - id: N01
    type: question
    support_level: explicit
    source_refs: ["§1", "Table 2"]
    title: "{Central research question}"
    description: "{What question is being investigated}"
    children:

      - id: N02
        type: experiment
        support_level: explicit
        source_refs: ["Figure 4", "Table 2"]
        title: "{What was tried}"
        result: "{What was observed}"
        evidence: [C01, "Figure 3", "§2.2"]
        children:

          - id: N04
            type: decision
            support_level: explicit
            source_refs: ["§3.2"]
            title: "{What was decided}"
            choice: "{The chosen approach}"
            alternatives:
              - "{Alternative 1}"
              - "{Alternative 2}"
            evidence: "{What informed this decision}"
            children:
              # ... deeper nesting

      - id: N03
        type: dead_end
        support_level: explicit
        source_refs: ["§4.3", "Table 6"]
        title: "{What was tried and failed}"
        hypothesis: "{What was expected}"
        failure_mode: "{Why it failed}"
        lesson: "{What was learned; what it led to}"
        # dead_end nodes have NO children — they are leaf nodes

  # For DAG edges (node with multiple parents):
  - id: N10
    type: experiment
    support_level: explicit
    source_refs: ["Table 5"]
    title: "{Convergent experiment}"
    also_depends_on: [N07, N08]  # additional parents beyond nesting
    result: "{What was observed}"
    evidence: [C05]
```

## Node Types

### question
The root driver. What is being investigated?
- **Required fields**: `description`
- **Children**: experiments, decisions, other questions

### experiment
An attempt to answer a question or validate a decision.
- **Required fields**: `result`
- **Optional fields**: `evidence` (list of claim IDs, figure/table refs, section refs)
- **Children**: decisions, dead_ends, more experiments

### dead_end
A failed approach. Valuable for downstream agents — prevents rediscovering known failures.
- **Required fields**: `hypothesis`, `failure_mode`, `lesson`, `framing_basis`
- **NO children** — always a leaf node
- **Narrative type**: only use when the source material explicitly frames something as a failed/abandoned approach. If the source merely reports a negative experimental result without framing it as an abandoned direction, use `experiment` with a negative `result` instead.
- `framing_basis`: a direct quote or specific citation showing the source uses this framing (e.g., *"We tried X but found it does not work because..."*)

### decision
A design choice with documented alternatives.
- **Required fields**: `choice`, `alternatives`, `framing_basis`
- **Optional fields**: `evidence`
- **Children**: experiments that test the decision, further decisions
- **Narrative type**: only use when the source material explicitly discusses choosing between alternatives. If the source simply proposes a method without comparing alternatives, use `experiment` instead.
- `framing_basis`: a direct quote or specific citation showing the source discusses this choice (e.g., *"We compared A, B, C and chose B because..."*)

### pivot
A change in research direction.
- **Required fields**: `from`, `to`, `trigger`, `framing_basis`
- **Children**: the new research direction
- **Narrative type**: only use when the source material explicitly describes a direction change. If the source simply presents a new approach without framing it as a pivot from a previous one, use `question` or `experiment` instead.
- `framing_basis`: a direct quote or specific citation showing the source describes a direction change

## Rules

1. **Nested YAML**: Children appear inline under parent node's `children` list
2. **Valid DAG**: No cycles. All `also_depends_on` IDs must exist in the tree
3. **Minimum 8 nodes**: Cover the paper's key research trajectory
4. **Narrative types require `framing_basis`**: `dead_end`, `decision`, and `pivot` are narrative node types — they carry process-level framing beyond the factual content. These types are only allowed when the source material explicitly uses that framing. Each must include a `framing_basis` field with a direct quote or citation. If you cannot fill `framing_basis`, downgrade to a neutral type (`experiment`, `question`).
5. **Do not force narrative types**: Include `dead_end`, `decision`, or `pivot` nodes only when the source material warrants them. A tree with only `question` and `experiment` nodes is perfectly valid if the source does not provide process narrative.
6. **Every node has**: `id` (N01, N02...), `type`, `title`
7. **Every node has `support_level: explicit`**: only source-grounded nodes are allowed; omit anything that would require inference
8. **Every node must have `source_refs`**: table/figure/section references from the input material
9. **`also_depends_on`**: Only for DAG convergence (node has multiple parents beyond nesting)

## Extraction Strategy

When building from a PDF:

Neutral types (always available — require only factual grounding):
- **Central questions** → `question` nodes
- **"We tried X" / "We evaluated Y"** → `experiment` nodes (including negative results)

Narrative types (require `framing_basis` — use only when the paper explicitly provides process framing):
- **"We considered X but chose Y because..."** → `decision` nodes with alternatives
- **"We tried X but abandoned it because..."** → `dead_end` nodes
- **"We initially pursued X but switched to Y when..."** → `pivot` nodes

Common mistake: a paper reports that baseline B underperforms method A. This is a **negative experimental result** (`experiment`), NOT a `dead_end` — the authors did not frame B as an approach they pursued and abandoned. Only use `dead_end` if the paper explicitly describes trying and abandoning a direction.

Support-level guidance:
- Only include a node if the source material directly reports or states it
- If a research step is not explicitly documented, omit it entirely — do not reconstruct or infer
- Prefer a smaller, fully-grounded tree over a larger tree with speculative nodes
- A tree composed entirely of `question` and `experiment` nodes is valid and preferred over one that forces narrative types without source support

When building from experiment logs:
- Each experiment run → experiment node
- Failed runs → dead_end nodes with actual error messages as failure_mode
- Parameter sweeps → decision nodes with sweep results informing the choice
- Direction changes → pivot nodes with the triggering observation
