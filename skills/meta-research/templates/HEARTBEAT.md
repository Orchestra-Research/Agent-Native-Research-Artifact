# HEARTBEAT.md

Use this file as the heartbeat contract for the **Research Advisor** role.
Keep it short, explicit, and action-oriented.

## Schedule

- Run every 15-30 minutes while the project is active.
- If there are no material changes and no new risks, emit `HEARTBEAT_OK`.

## Inputs to read each run

1. `research-tree.yaml`
2. `research-log.md`
3. Latest experiment artifacts for active branches (if any)

## Required heartbeat workflow

1. Infer current phase and active/stalled branches.
2. Audit rigor: assumptions, controls, baselines, confounders, and missing evidence.
3. Generate at least one high-upside insight or branch improvement when possible.
4. Choose direction per active branch: `deepen`, `broaden`, `pivot`, `conclude`, or `pause`.
5. Map each direction to one concrete next action for Clawbot Executor.
6. Append an `Advisor Review` entry to `research-log.md`.

## Required Review Packet format

### Status Snapshot

- Current phase:
- Active branches:
- Stalled branches:
- Immediate blockers:

### Rigorous Critique (highest impact first)

- [P0] ...
- [P1] ...
- [P2] ...

### New Insights

- Insight 1:
- Insight 2:

### Reflection Verdict

- Recommended loop move:
- Why:

### Direction -> Action Plan

| Direction / Branch | Move | Next Executor Action | Expected Evidence Signal | Priority |
|--------------------|------|----------------------|--------------------------|----------|
| H1                 | deepen | ...                | ...                      | P0       |

### Gate Decision

- Phase progression gate: `ready` or `not ready`

### User Asks (only if needed)

- ...

## Quiet mode rule

If no material update is detected and no new risk is present:

1. Output exactly `HEARTBEAT_OK`.
2. Add a brief `Advisor Review` log note that no action is required.

## Escalation triggers

Escalate to deep review immediately if any condition is true:

- Contradictory result vs prior conclusions
- Repeated experiment failures on the same branch
- Missing protocol lock before execution
- Stalled high-priority branch over multiple heartbeat cycles
- New literature that invalidates a core assumption
