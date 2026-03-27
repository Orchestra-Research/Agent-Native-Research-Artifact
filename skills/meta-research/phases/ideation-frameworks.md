# Ideation Frameworks for Research

Twelve empirically grounded frameworks for generating research ideas. Each targets a
distinct cognitive operation — orienting, reformulating, abstracting, analogizing,
constraining, inverting, combining, simplifying, probing, and synthesizing. Use them
individually during hypothesis generation Step 1, or combine them using the integrated
protocol at the end of this file.

**Relationship to the hypothesis generation phase**: These frameworks are the *cognitive
engines* that power candidate hypothesis generation. The hypothesis generation phase file
([phases/hypothesis-generation.md](hypothesis-generation.md)) provides the *operational
workflow* (generate, test, organize into tree). Use both together.

---

## Framework 1: Problem-First vs. Solution-First Thinking

Research ideas originate from two modes. Knowing which you are in prevents building
solutions without problems, or chasing problems without feasible approaches.

**Problem-First** (pain point → method):
- Start with a concrete failure, bottleneck, or unmet need
- Naturally yields impactful work because the motivation is intrinsic
- Risk: may converge on incremental fixes rather than paradigm shifts

**Solution-First** (new capability → application):
- Start with a new tool, insight, or technique seeking application
- Often drives breakthroughs by unlocking previously impossible approaches
- Risk: "hammer looking for a nail" — solution may lack genuine demand

**Workflow**:
1. Write down your idea in one sentence
2. Classify it: Is this problem-first or solution-first?
3. If problem-first → verify the problem matters (who suffers? how much?)
4. If solution-first → identify at least two genuine problems it addresses
5. For either mode, articulate the gap: what cannot be done today that this enables?

**Self-Check**:
- [ ] Can I name a specific person or community who needs this?
- [ ] Is the problem I am solving actually unsolved (not just under-marketed)?
- [ ] If solution-first, does the solution create new capability or just replicate existing ones?

---

## Framework 2: Problem Reformulation (Representational Change)

Breakthroughs often come not from solving the problem as stated, but from re-representing
the problem itself. Kaplan and Simon's insight research shows that changing the problem
space — the constraints, the abstraction level, the formalism — is often where creativity
lives.

**The Key Shift**: From "How do I solve this problem?" to "Am I even thinking about this
problem correctly?"

**Reformulation Strategies**:

| Strategy | Example |
|----------|---------|
| **Change the objective** | "Make the algorithm faster" → "Eliminate the need for this computation" |
| **Change the formalism** | Graph problem → linear algebra problem (spectral methods) |
| **Change the granularity** | Per-token prediction → per-span prediction |
| **Change the agent** | "How should the model learn?" → "How should the data teach?" (curriculum learning) |
| **Change the timescale** | Real-time optimization → amortized inference |
| **Invert the direction** | Forward simulation → inverse problem (learning from observations) |

**Workflow**:
1. State your current problem in one sentence
2. Identify hidden assumptions: What formalism? What objective? What granularity? Whose
   perspective?
3. For each assumption, generate the alternative: "What if [opposite assumption]?"
4. Ask: Does this reformulation make the problem easier, harder, or different in a useful
   way?
5. A reformulation that makes a hard problem easy is often a publishable insight on its own

**Classic CS Examples**:
- **PageRank**: Reformulated "find important web pages" from content analysis to graph
  eigenvalue problem
- **Dropout**: Reformulated "prevent overfitting" from regularization to approximate
  ensemble
- **Attention**: Reformulated "handle long sequences" from remembering everything to
  selectively querying

---

## Framework 3: Abstraction Laddering

Every research problem sits at a particular level of abstraction. Deliberately moving up,
down, or sideways reveals ideas invisible at your current level. Combines Polya's heuristics
with generalization/specialization moves.

| Direction | Action | Outcome |
|-----------|--------|---------|
| **Move Up** (generalize) | Turn a specific result into a broader principle | Framework papers, theoretical contributions |
| **Move Down** (instantiate) | Test a general paradigm under concrete constraints | Empirical papers, surprising failure analyses |
| **Move Sideways** (analogize) | Apply same abstraction level to adjacent domain | Cross-pollination, transfer papers |

**Workflow**:
1. State your current research focus in one sentence
2. **Move UP**: What is the general principle? What class of problems does this belong to?
3. **Move DOWN**: What is the most specific, constrained instance? What happens at the extreme?
4. **Move SIDEWAYS**: Where else does this pattern appear in a different field?
5. For each new level, ask: Is this a publishable contribution on its own?

**Example**:
- **Current**: "Improving retrieval accuracy for RAG systems"
- **Up**: "What makes context selection effective for any augmented generation system?"
- **Down**: "How does retrieval accuracy degrade when documents are adversarially perturbed?"
- **Sideways**: "Database query optimization uses similar relevance ranking — what can we
  borrow?"

**When to Generalize vs. Specialize**:
- Generalize when you have results but no explanation
- Specialize when you have theory but no grounding
- Analogize when you are stuck in either direction

---

## Framework 4: Tension & Contradiction Hunting (with Janusian Synthesis)

Breakthroughs often come from resolving tensions between widely accepted but seemingly
conflicting goals. Albert Rothenberg's studies found that *holding two contradictory ideas
simultaneously* — Janusian thinking — is a hallmark of creative research. The key is to
seek synthesis, not compromise.

**Common Research Tensions**:

| Tension Pair | Research Opportunity |
|-------------|---------------------|
| Performance ↔ Efficiency | Can we match SOTA with 10x less compute? |
| Privacy ↔ Utility | Can federated/encrypted methods close the accuracy gap? |
| Generality ↔ Specialization | When does fine-tuning beat prompting, and why? |
| Safety ↔ Capability | Can alignment improve rather than tax capability? |
| Interpretability ↔ Performance | Do mechanistic insights enable better architectures? |
| Scale ↔ Accessibility | Can small models replicate emergent behaviors? |
| Consistency ↔ Availability | CAP theorem → then CRDTs found practical middle ground |
| Memorization ↔ Generalization | Grokking: models memorize first, then generalize |
| Compression ↔ Quality | Neural codecs exceed information-theoretic limits via priors |

**Workflow**:
1. Pick your research area
2. List the top 3-5 desiderata (things everyone wants)
3. Identify pairs that are commonly treated as trade-offs
4. For each pair, ask: Is this trade-off fundamental or an artifact of current methods?
5. If artifact → the reconciliation IS your research contribution
6. If fundamental → characterizing the Pareto frontier is itself valuable

**Janusian Synthesis** (going beyond identifying tensions):
1. Resist choosing a side. Instead ask:
   - "What would a system look like that achieves both A and B?"
   - "Under what conditions is the A-B trade-off not fundamental?"
   - "Is the opposition an artifact of how we formalized the problem?"
2. Seek synthesis: the resolution often requires a new abstraction that reframes the
   relationship
3. Test: can you demonstrate empirically that both goals are achievable?

**Self-Check**:
- [ ] Have I confirmed this tension is real (not just assumed)?
- [ ] Can I point to papers that optimize for each side independently?
- [ ] Is my proposed reconciliation technically plausible, not just aspirational?
- [ ] Does the resolution change how people think about the problem, not just the solution?

---

## Framework 5: Analogical Reasoning & Cross-Pollination (Structure-Mapping)

Borrowing structural ideas from other disciplines is one of the most generative research
heuristics. Dedre Gentner's structure-mapping theory and Kevin Dunbar's studies of real
labs show that *distant* analogies generate ideas while *nearby* analogies refine them.
Arthur Koestler called this **bisociation** — connecting two previously unrelated frames.

**Levels of Analogical Depth**:

| Level | Description | Value | Example |
|-------|-------------|-------|---------|
| **Surface** | Things look similar | Low | "A neural network is like a brain" |
| **Relational** | Relationships between entities match | Medium | "Attention in models parallels resource allocation in economics" |
| **Structural** | Deep causal mechanisms map | High | "Diffusion models reverse a thermodynamic process; stat-mech math directly applies" |

**High-Yield Source Fields for ML Research**:

| Source Field | Transferable Concepts |
|-------------|----------------------|
| Neuroscience | Attention, memory consolidation, hierarchical processing |
| Physics | Energy-based models, phase transitions, renormalization |
| Economics | Mechanism design, auction theory, incentive alignment |
| Ecology | Population dynamics, niche competition, co-evolution |
| Linguistics | Compositionality, pragmatics, grammatical induction |
| Control Theory | Feedback loops, stability, adaptive regulation |

**Structure-Mapping Workflow**:
1. Describe your problem using only relational/causal language (strip domain jargon)
   - Bad: "We need to improve transformer attention efficiency"
   - Good: "We have a system that must selectively aggregate information from a large
     set, where relevance is context-dependent and cost scales quadratically with set size"
2. Search for structural matches in other fields
3. Pick the most distant match with genuine structural fidelity
4. Map the solution mechanism: how does the source domain solve this?
5. Transfer and adapt: what changes when bringing that mechanism into your domain?
6. Generate predictions the analogy makes in your domain

**Systematic Bisociation** (cross-product matrix):
1. Select two domains you have passing familiarity with
2. List core primitives in each (5-10 per domain)
3. Create a cross-product matrix: rows = Domain A concepts, columns = Domain B concepts
4. For each cell, ask: "What would it mean to apply A's concept to B's problem?"
5. Filter for non-trivial, testable research questions

**Quality Test**: A strong analogy is not a surface metaphor ("the network is like a
brain") but a structural mapping where the mechanism transfers.

**Validation**:
- [ ] Does the mapping preserve causal/relational structure (not just labels)?
- [ ] Does the combination generate testable predictions?
- [ ] Would an expert in both fields find the connection non-obvious but sound?

---

## Framework 6: What Changed? + The Adjacent Possible

Strong ideas often come from revisiting old problems under new conditions. Stuart
Kauffman's "adjacent possible" concept explains why: innovation happens at the boundary
of what is currently reachable. New ideas become thinkable once their prerequisites exist.

**Categories of Change to Monitor**:

| Change Type | Example | Research Implication |
|------------|---------|---------------------|
| **Compute** | GPUs 10x faster | Methods dismissed as too expensive become feasible |
| **Scale** | Trillion-token datasets | Statistical arguments that failed at small scale may now hold |
| **Regulation** | EU AI Act, GDPR | Creates demand for compliant alternatives |
| **Tooling** | New frameworks, APIs | Reduces implementation barrier for complex methods |
| **Failure** | High-profile system failures | Exposes gaps in existing approaches |
| **Cultural** | New user behaviors | Shifts what problems matter most |

**Workflow**:
1. Pick a well-known negative result or abandoned approach (3-10 years old)
2. List the assumptions that led to its rejection
3. For each assumption, ask: Is this still true today?
4. If any assumption is invalidated → re-run the idea under new conditions
5. Frame: "X was previously impractical because Y, but Z has changed"

**Adjacent Possible Mapping**:
1. List recent enablers (last 1-3 years): hardware, datasets, tools, theory, regulation
2. For each enabler, ask: "What was previously impossible that this now permits?"
3. Combine enablers: the most powerful adjacent possibles arise from intersections of
   multiple new enablers
4. Check for competition: if many people see the same adjacent possible, speed or a unique
   angle matters

**Timing Signal**: If your idea requires technology that doesn't exist yet, it's beyond
the adjacent possible — park it. If it could have been done 5 years ago, someone probably
did — check the literature. The sweet spot is ideas that became feasible in the last
6-18 months.

---

## Framework 7: Failure Analysis & Boundary Probing

Understanding where a method breaks is often as valuable as showing where it works.
Boundary probing systematically exposes the conditions under which accepted techniques fail.

**Types of Boundaries to Probe**:
- **Distributional**: What happens with out-of-distribution inputs?
- **Scale**: Does the method degrade at 10x or 0.1x the typical scale?
- **Adversarial**: Can the method be deliberately broken?
- **Compositional**: Does performance hold when combining multiple capabilities?
- **Temporal**: Does the method degrade over time (concept drift)?

**Workflow**:
1. Select a widely-used method with strong reported results
2. Identify implicit assumptions in its evaluation (dataset, scale, domain)
3. Systematically violate each assumption
4. Document where and how the method breaks
5. Diagnose the root cause of each failure
6. Propose a fix or explain why the failure is fundamental

**Self-Check**:
- [ ] Am I probing genuine boundaries, not just confirming known limitations?
- [ ] Can I explain WHY the method fails, not just THAT it fails?
- [ ] Does my analysis suggest a constructive path forward?

---

## Framework 8: Constraint Manipulation (Boden's Framework)

Margaret Boden distinguishes three forms of creativity based on how they interact with
constraints:

| Type | Operation | CS Example |
|------|-----------|------------|
| **Exploratory** | Search within existing conceptual space | Hyperparameter tuning, architecture search within a fixed paradigm |
| **Combinational** | Combine elements from different spaces | Multi-task learning, neuro-symbolic methods |
| **Transformational** | Change the rules of the space itself | Self-supervised learning (dropped the "labels required" assumption) |

Transformational creativity is the rarest and highest-impact. It happens when you change
what is even considered a valid solution.

**Constraint Analysis Workflow**:
1. List the constraints of your current approach (5-10):
   - Computational: "Must fit in GPU memory"
   - Methodological: "Requires labeled data"
   - Architectural: "Uses fixed-length context"
   - Evaluative: "Measured by accuracy on benchmark X"
2. Classify each: **Hard** (physically necessary), **Soft** (convention/historical
   accident), **Hidden** (implicitly assumed — most fertile for innovation)
3. For each soft/hidden constraint, ask:
   - What if we relaxed it?
   - What if we tightened it?
   - What if we replaced it entirely?
4. The most productive move is often exposing and dropping a hidden constraint

**Classic Constraint Transformations**:
- "Data must fit in memory" → dropped → streaming algorithms, external memory
- "Training requires human labels" → dropped → self-supervised learning
- "Models must be deterministic" → dropped → variational methods, diffusion
- "Inference must happen in one pass" → dropped → iterative refinement, chain-of-thought

---

## Framework 9: Negation and Inversion

Take a core assumption in your field and negate it. Formalized in De Bono's lateral
thinking and the TRIZ methodology from engineering.

**The Pattern**: "What if [widely held assumption] is wrong, unnecessary, or invertible?"

**Workflow**:
1. List 5-10 core assumptions in your subfield (the things "everyone knows")
2. Negate each one and ask: What system would you build?
3. Evaluate each negation:
   - Incoherent → discard
   - Already explored → check if conditions have changed (see Framework 6)
   - Unexplored and coherent → potential research direction

**Negation Hall of Fame in CS**:

| Assumption | Negation | Result |
|-----------|----------|--------|
| "We need strong consistency" | What if we don't? | Eventual consistency, CRDTs |
| "We need exact answers" | What if approximate is fine? | Sketches, LSH, approximate NN |
| "Labels are necessary" | What if we learn without them? | Self-supervised, contrastive methods |
| "More parameters = more compute" | What if we don't use all parameters? | Mixture of Experts, sparse models |
| "Training and inference are separate" | What if the model keeps learning? | Online learning, test-time training |
| "Errors must be prevented" | What if we embrace and correct them? | Speculative decoding, self-correction |

**TRIZ-Inspired Principles for CS**:

| Principle | CS Application |
|-----------|----------------|
| **Inversion** | Reverse the process (generative vs. discriminative) |
| **Segmentation** | Break monolithic into modular (microservices, MoE) |
| **Merging** | Combine separate steps (end-to-end learning) |
| **Universality** | One component serves multiple functions (multi-task models) |
| **Nesting** | Place one system inside another (meta-learning) |
| **Dynamization** | Make static things adaptive (dynamic architectures) |

---

## Framework 10: Composition & Decomposition

Novelty often emerges from recombination or modularization. Innovation frequently lies not
in new primitives, but in how components are arranged or separated.

**Composition** (combining existing techniques):
- Identify two methods that solve complementary subproblems
- Ask: What emergent capability arises from combining them?
- Example: RAG + Chain-of-Thought → retrieval-augmented reasoning

**Decomposition** (breaking apart monolithic systems):
- Identify a complex system with entangled components
- Ask: Which component is the actual bottleneck?
- Example: Decomposing "fine-tuning" into data selection, optimization, and regularization
  reveals that data selection often matters most

**Workflow**:
1. List the 5-10 key components or techniques in your area
2. **Compose**: pick pairs and ask what happens when you combine them
3. **Decompose**: pick a complex method and isolate each component's contribution
4. For compositions: does the combination create emergent capabilities?
5. For decompositions: does isolation reveal a dominant or redundant component?

---

## Framework 11: The Simplicity Test

Before accepting complexity, ask whether a simpler approach suffices. Fields sometimes
over-index on elaborate solutions when a streamlined baseline performs competitively.

**Warning Signs of Unnecessary Complexity**:
- The method has many hyperparameters with narrow optimal ranges
- Ablations show most components contribute marginally
- A simple baseline was never properly tuned or evaluated
- The improvement over baselines is within noise on most benchmarks

**Workflow**:
1. Identify the current SOTA method for your problem
2. Strip it to its simplest possible core (what is the one key idea?)
3. Build that minimal version with careful engineering
4. Compare fairly: same compute budget, same tuning effort
5. If the gap is small → the contribution is the simplicity itself
6. If the gap is large → you now understand what the complexity buys

**Contribution Framing**:
- "We show that [simple method] with [one modification] matches [complex SOTA]"
- "We identify [specific component] as the critical driver, not [other components]"

---

## Framework 12: Stakeholder Rotation

Viewing a system from multiple perspectives reveals distinct classes of research questions.
Each stakeholder sees different friction, risk, and opportunity.

| Stakeholder | Key Questions |
|-------------|---------------|
| **End User** | Is this usable? What errors are unacceptable? Latency tolerance? |
| **Developer** | Is this debuggable? Maintenance burden? How does it compose? |
| **Theorist** | Why does this work? Formal guarantees? Where are the gaps? |
| **Adversary** | How can this be exploited? What are the attack surfaces? |
| **Ethicist** | Who is harmed? What biases are embedded? Who is excluded? |
| **Regulator** | Is this auditable? Can decisions be explained? Accountability? |
| **Operator** | What is the cost? How does it scale? Failure modes? |

**Workflow**:
1. Describe your system or method in one paragraph
2. Assume each stakeholder perspective in turn (spend 5 minutes per role)
3. For each perspective, list the top 3 concerns or questions
4. Identify which concerns are unaddressed by existing work
5. The unaddressed concern with the broadest impact is your research question

---

## The Two-Sentence Pitch Test (Convergence Filter)

A strong research idea should be defensible in two sentences to a smart non-expert. Use
this as a convergence filter after generating candidates.

**Template**:
> **Sentence 1** (Problem): "[Domain] currently struggles with [specific problem], which
> matters because [concrete consequence]."
>
> **Sentence 2** (Insight): "We [approach] by [key mechanism], which works because [reason]."

**If you cannot fill this template**:
- Problem not well-defined → return to Framework 1 (Problem-First check)
- Insight not clear → return to Framework 11 (Simplicity Test)
- Significance not established → return to Framework 4 (find the tension)

**Calibration Questions**:
- Would a smart colleague outside your subfield understand why this matters?
- Does the explanation stand without jargon?
- Can you predict what a skeptic's first objection would be?

---

## Framework Selection Guide

Not sure which framework to start with? Use your situation to pick:

| Your Situation | Start With |
|---------------|------------|
| "I don't know what area to work in" | Tension Hunting (F4) → What Changed (F6) |
| "I have a vague area but no specific idea" | Abstraction Laddering (F3) → Failure Analysis (F7) |
| "I have an idea but I'm not sure it's good" | Two-Sentence Test → Simplicity Test (F11) |
| "I have a good idea but need a fresh angle" | Cross-Pollination (F5) → Stakeholder Rotation (F12) |
| "I want to combine existing work" | Composition/Decomposition (F10) |
| "I found a cool technique, want to apply it" | Problem-First Check (F1) → Stakeholder Rotation (F12) |
| "I want to challenge conventional wisdom" | Negation (F9) → Failure Analysis (F7) |
| "I feel stuck in one way of thinking" | Problem Reformulation (F2) → Constraint Manipulation (F8) |
| "I want to revisit an old/failed idea" | What Changed (F6) → Adjacent Possible mapping |

---

## Integrated Creative Thinking Protocol

Use this end-to-end protocol for a deep ideation session. It combines all 12 frameworks
in four phases. Budget about 90 minutes for a thorough session.

### Phase 1: Map the Space (15 min)

1. **Constraint Manipulation** (F8): List all constraints of the current paradigm. Mark
   hard, soft, hidden.
2. **What Changed / Adjacent Possible** (F6): List recent enablers that change the
   feasibility landscape.
3. **Problem-First vs. Solution-First** (F1): Classify your starting orientation.

### Phase 2: Generate Disruptions (30 min)

4. **Negation** (F9): Negate 3 soft/hidden constraints. What systems emerge?
5. **Cross-Pollination / Bisociation** (F5): Pick a distant field and create a
   cross-product matrix with your domain.
6. **Problem Reformulation** (F2): Restate your problem 3 different ways (change
   objective, formalism, agent).
7. **Tension Hunting** (F4): List 3-5 trade-offs. For each: fundamental or artifact?
8. **Composition / Decomposition** (F10): Combine 2 existing techniques or split 1 apart.

### Phase 3: Deepen Promising Leads (30 min)

9. **Analogical Reasoning** (F5): For each promising idea, find a structural analogy and
   extract predictions.
10. **Abstraction Laddering** (F3): Move each idea up (generalize) and down (specialize).
11. **Janusian Synthesis** (F4): Identify tensions within ideas. Synthesize rather than
    choose.
12. **Failure Analysis** (F7): Where would each idea break? Is the failure informative?

### Phase 4: Filter and Sharpen (15 min)

13. **Two-Sentence Pitch Test**: Can you state each idea in two sentences?
14. **Simplicity Test** (F11): Is the complexity justified?
15. **Stakeholder Rotation** (F12): Who benefits? Who might object?
16. **Feasibility check**: Can you execute with available resources?

Any idea that survives all four phases and passes the two-sentence test is ready for the
brainstorming protocol's scoring rubric (Step 4).

---

## Common Creative Blocks and Unblocking Strategies

| Block | Symptom | Framework to Apply |
|-------|---------|-------------------|
| **Fixation** | Cannot stop thinking about the problem one way | Problem Reformulation (F2) |
| **Tunnel vision** | All ideas from the same subfield | Cross-Pollination (F5) or Analogical Reasoning |
| **Self-censoring** | Dismissing ideas as "too weird" | Negation (F9) — weird is the point; evaluate later |
| **Incrementalism** | Every idea is "+2% on benchmark X" | Constraint Manipulation (F8) — change the rules |
| **Analysis paralysis** | Too many options, cannot commit | Adjacent Possible (F6) — what is feasible now? |
| **False dichotomy** | Stuck choosing between two approaches | Janusian Synthesis (F4) — seek synthesis |
| **Echo chamber** | Reading the same 10 papers | Cross-Pollination (F5) from a distant field |
| **Stale assumptions** | "This was tried and didn't work" | What Changed (F6) — conditions may have shifted |
| **Complexity worship** | Method has 8 components, each helps marginally | Simplicity Test (F11) |
| **Single-perspective bias** | Only considering the ML engineer's view | Stakeholder Rotation (F12) |

---

## Common Pitfalls in Research Ideation

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| **Novelty without impact** | "No one has done X" but no one needs X | Problem-First Check (F1) |
| **Incremental by default** | Idea is +2% on a benchmark | Abstraction Laddering (F3) — go up |
| **Complexity worship** | 8 components, each contributing marginally | Simplicity Test (F11) |
| **Echo chamber** | All ideas from the same 10 papers | Cross-Pollination (F5) |
| **Stale assumptions** | "This was tried and didn't work" (5 years ago) | What Changed (F6) |
| **Single-perspective bias** | Only the ML engineer's view | Stakeholder Rotation (F12) |
| **Premature convergence** | Committed to first idea without exploring | Run full diverge phase |
| **Surface analogies** | "X is like Y" without mechanism transfer | Structure-Mapping (F5) — go deeper |

---

## Agent Usage Instructions

When a researcher needs help generating hypotheses:

1. **Identify their starting point**: exploring a new area, stuck on a project, or
   evaluating an existing idea? Use the Framework Selection Guide.
2. **Select 2-3 frameworks** appropriate to their situation.
3. **Walk through frameworks interactively**: apply each step-by-step, asking the
   researcher for domain-specific inputs.
4. **Generate candidates**: aim for 10-20 raw hypotheses across frameworks.
5. **Apply the Two-Sentence Pitch Test** to filter to top candidates.
6. **Hand off to hypothesis generation** for organizing into the research tree, then
   to the judgment gate for evaluation.

**Key Principles**:
- Generative mode first, evaluative mode second — do not filter prematurely
- Push for specificity — vague ideas ("improve efficiency") are not actionable
- Challenge assumptions — ask "why?" at least three times
- Maintain a written list of all candidates, even rejected ones (they may recombine later)
- Distant analogies are more valuable than nearby ones, but need more validation
- The researcher makes the final call; the agent facilitates structured thinking
