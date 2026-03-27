# Phase: Literature Survey

## Goal

Build a comprehensive understanding of the state of the art (SOTA), identify gaps,
open problems, and underexplored areas — using a documented, reproducible search process.
This is always the first phase: you cannot generate good hypotheses without knowing
what the field has already done.

## Entry Conditions

- User has a broad research topic, domain, or specific question
- OR: looping back from Reflection because new evidence requires updating the survey

## Step-by-Step Protocol

### Step 1: Define the Review Protocol

Before searching, write down:

```
REVIEW PROTOCOL
- Research area: [broad topic or specific question]
- Key questions: [what do we need to learn about the field?]
- Inclusion criteria: [topic, methodology, data regime, outcome type, date range]
- Exclusion criteria: [irrelevant domains, non-peer-reviewed if applicable, languages]
- Databases to search: [see database list below]
- Search string structure: [Boolean terms with AND/OR/NOT]
- Screening process: [title/abstract first, then full-text]
```

**Database selection** (use at least 3 for comprehensive coverage):
- **arXiv** — preprints (CS, physics, math, quantitative biology)
- **Semantic Scholar** — AI-powered search with citation graphs
- **Google Scholar** — broadest coverage, includes grey literature
- **PubMed** — biomedical and life sciences
- **IEEE Xplore / ACM DL** — engineering and computing
- **Scopus / Web of Science** — multidisciplinary indexed literature
- **DBLP** — computer science bibliography

### Step 2: Execute Search

For each database:
1. Run the search string
2. Record: database name, exact query, date, number of results
3. Export results to a common format (BibTeX, CSV, or reference manager)

**Search string design tips:**
- Start broad, then narrow with filters
- Use synonyms and related terms (e.g., "large language model" OR "LLM" OR "foundation model")
- Combine concept blocks with AND: (method terms) AND (task terms) AND (evaluation terms)
- Test the string: does it retrieve known relevant papers? If not, revise.

**Complementary strategies** (beyond database search):
- **Citation chasing**: forward/backward citations from key papers
- **Author tracking**: prolific authors in the area
- **Conference proceedings**: targeted venues (NeurIPS, ICML, ACL, EMNLP, ICLR, etc.)
- **Twitter/social media**: recent work not yet indexed

### Step 3: Screen and Select

**Title/abstract screening** (first pass):
- Skim each result: is it plausibly relevant based on title and abstract?
- Decision: INCLUDE / EXCLUDE / MAYBE
- Record reason for every exclusion (even brief: "wrong task", "survey only", etc.)

**Full-text screening** (second pass):
- Read included + maybe papers more carefully
- Apply inclusion/exclusion criteria strictly
- Final decision: IN / OUT with reason

### Step 4: PRISMA-Style Audit Trail

Document the flow of papers through screening:

```
Records identified through database searching: N1
Additional records from citation chasing: N2
--- Duplicates removed: N3
Records screened (title/abstract): N4
--- Excluded at screening: N5
Full-text articles assessed: N6
--- Excluded at full-text (with reasons): N7
Studies included in synthesis: N8
```

### Step 5: Read and Extract (Three-Pass Method)

For each included paper, use a structured reading approach:

**Pass 1 — Gist (5-10 min):**
- Read title, abstract, introduction, section headings, conclusion
- Determine: what is claimed, what method, what data, what result
- Decide if deeper reading is needed

**Pass 2 — Understanding (30-60 min):**
- Read fully, annotate key claims and methods
- Identify strengths and weaknesses
- Note how it relates to the research area

**Pass 3 — Verification (for critical papers only):**
- Check math/proofs, re-derive key results if feasible
- Look at data details, code availability, reproducibility claims
- Assess whether results would replicate

**Extraction schema** (fill for each paper):

```
PAPER EXTRACTION
- Citation: [authors, year, title, venue]
- Claim: [one-sentence summary of main contribution]
- Method: [approach in 2-3 sentences]
- Data: [datasets used, sizes, splits]
- Evaluation: [metrics, baselines compared against]
- Key result: [headline number or finding]
- Limitations: [stated + unstated]
- Relevance to our area: [how it connects: baseline? comparison? building block?]
- Artifacts available: [code? data? models? configs?]
```

### Step 6: Synthesize into Evidence Map

Cluster papers by **claims and mechanisms**, not by venue or chronology:

```
EVIDENCE MAP
Theme 1: [e.g., "Scaling laws for X"]
  - Paper A claims... with evidence...
  - Paper B claims... with contradicting evidence...
  - Gap: [what is not addressed]

Theme 2: [e.g., "Evaluation methods for Y"]
  - Paper C proposes metric M1...
  - Paper D shows M1 is flawed because...
  - Gap: [what metric is needed]

Cross-cutting concerns:
  - Reproducibility: [which results have been replicated?]
  - Baselines: [what is the current strongest baseline?]
  - Datasets: [standard benchmarks, limitations, emerging alternatives]
```

### Step 7: Identify Open Problems and Underexplored Areas

This is the critical output that feeds hypothesis generation. Go beyond the evidence
map to explicitly catalogue:

**Open problems** — questions the field is actively struggling with:
- What contradictions exist between papers?
- What assumptions are widely held but unverified?
- What problems are acknowledged but unsolved?

**Underexplored areas** — topics with insufficient investigation:
- What combinations haven't been tried?
- What conditions haven't been tested under?
- What domains lack evaluation?
- What "obvious baselines" are missing?

**Update the research tree**: populate `field_understanding` with:
- `sota_summary`: 1-2 paragraph summary of where the field stands
- `key_papers`: papers critical to your research direction
- `open_problems`: explicit list of open questions
- `underexplored_areas`: gaps in the literature

### Artifact Locations

Save outputs to the project's `literature/` directory:
- `literature/survey.md` — search protocol, screening log, PRISMA numbers, evidence map
- `literature/evidence-map.md` — detailed evidence synthesis (if too large for survey.md)
- `literature/references.bib` — bibliography in BibTeX format

## Exit Criteria

- [ ] Search protocol is documented (databases, queries, dates, filters)
- [ ] Screening is tracked with inclusion/exclusion reasons
- [ ] PRISMA-style numbers are recorded
- [ ] Extraction schema filled for all included papers
- [ ] Evidence map synthesized with themes and gaps
- [ ] Open problems and underexplored areas explicitly catalogued
- [ ] Research tree `field_understanding` section populated
- [ ] Research log entry recorded

## Transition

**Forward → Hypothesis Generation**: carry the evidence map, open problems list, and
underexplored areas. These are the raw material for generating hypotheses.

**Backward ← Reflection**: if reflection reveals new questions or assumptions that need
checking, return here to update the survey.

**Backward ← Experiment Execution**: if new related work is discovered during execution
that changes assumptions, return here to update the evidence map.
