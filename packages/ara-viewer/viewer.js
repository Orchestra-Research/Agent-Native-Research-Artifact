// ARA Viewer — claims-first reading view with progressive expansion.
// Load with ?ara=<path-to-ara-dir>  (path relative to this file).
// Default: ../../ara-output/andes-qoe

// Surface any runtime error in the loading slot so the page is never just blank.
function showFatal(msg) {
  const slot = document.getElementById("loading")
    || document.getElementById("sections")
    || document.body;
  const div = document.createElement("div");
  div.className = "error";
  div.style.cssText = "color:#f08585;padding:20px;font-family:ui-monospace,monospace;white-space:pre-wrap;";
  div.textContent = "ARA Viewer error: " + msg;
  slot.prepend(div);
}
window.addEventListener("error", (e) => showFatal(`${e.message}\n  at ${e.filename}:${e.lineno}:${e.colno}`));
window.addEventListener("unhandledrejection", (e) => showFatal("unhandled promise rejection: " + (e.reason && e.reason.message || e.reason)));

const params = new URLSearchParams(location.search);
const ARA_PATH = (params.get("ara") || "../../ara-output/andes-qoe").replace(/\/+$/, "");

// Section definitions: order, label, node kinds, and any blurb.
const SECTIONS = [
  { id: "claims", label: "Claims", kinds: ["claim"],
    blurb: "Falsifiable assertions the paper defends" },
  { id: "experiments", label: "Experiments", kinds: ["experiment"],
    blurb: "How the claims are tested" },
  { id: "observations", label: "Observations", kinds: ["observation"],
    blurb: "Empirical facts that motivated the work" },
  { id: "concepts", label: "Concepts", kinds: ["concept"],
    blurb: "Formal definitions" },
  { id: "heuristics", label: "Heuristics", kinds: ["heuristic"],
    blurb: "Design rules used in the solution" },
  { id: "solution", label: "Solution", kinds: ["solution"],
    blurb: "Architecture, algorithm, and constraints" },
  { id: "trace", label: "Exploration trace", kinds: ["trace_question","trace_decision","trace_experiment","trace_dead_end","trace_pivot"],
    blurb: "Research path including dead ends and pivots" },
  { id: "related", label: "Related work", kinds: ["related"],
    blurb: "Prior work this builds on or compares against" },
  { id: "evidence", label: "Evidence", kinds: ["figure","table"],
    blurb: "Figures and tables backing the claims" },
];

const KIND_BADGE = {
  claim: "claim", experiment: "experiment", observation: "observation",
  concept: "concept", heuristic: "heuristic", related: "RW",
  solution: "solution", figure: "figure", table: "table",
  code: "code", config: "config",
  trace_question: "trace?", trace_decision: "trace→", trace_experiment: "trace✱",
  trace_dead_end: "dead end", trace_pivot: "pivot",
};

const state = {
  data: null,
  byId: new Map(),
  outEdges: new Map(),
  inEdges: new Map(),
  // cache of markdown -> parsed sections per file path
  mdCache: new Map(),
};

// ---------------------------------------------------------------------------
// boot
// ---------------------------------------------------------------------------

async function main() {
  let manifest;
  try {
    const r = await fetch(`${ARA_PATH}/manifest.json`);
    if (!r.ok) throw new Error(r.status);
    manifest = await r.json();
  } catch (e) {
    document.getElementById("loading").innerHTML =
      `<div class="error">Could not load <code>${ARA_PATH}/manifest.json</code>. ` +
      `Run <code>python3 build_manifest.py ${ARA_PATH}</code> first.</div>`;
    return;
  }
  document.getElementById("loading").remove();

  state.data = manifest;
  state.byId = new Map(manifest.nodes.map((n) => [n.id, n]));
  manifest.nodes.forEach((n) => {
    state.inEdges.set(n.id, []);
    state.outEdges.set(n.id, []);
  });
  manifest.edges.forEach((e) => {
    if (state.outEdges.has(e.source)) state.outEdges.get(e.source).push(e);
    if (state.inEdges.has(e.target)) state.inEdges.get(e.target).push(e);
  });

  renderTopBar();
  renderHero();
  renderSections();
  renderTOC();
  wireControls();
  setupTOCScrollSpy();
}

// ---------------------------------------------------------------------------
// top bar / hero
// ---------------------------------------------------------------------------

function renderTopBar() {
  const meta = state.data.meta;
  const el = document.getElementById("paper-meta");
  const authors = (meta.authors || []).slice(0, 3).join(", ") +
    ((meta.authors || []).length > 3 ? ", et al." : "");
  el.innerHTML = `<strong>${esc(meta.title)}</strong>` +
    (authors ? ` &middot; ${esc(authors)}` : "") +
    (meta.venue ? ` &middot; ${esc(meta.venue)}` : "");
}

function renderHero() {
  const meta = state.data.meta;
  const el = document.getElementById("hero");
  const nodes = state.data.nodes;
  const counts = Object.fromEntries(SECTIONS.map((s) => [s.id,
    nodes.filter((n) => s.kinds.includes(n.kind)).length]));
  el.innerHTML = `
    <h1>${esc(meta.title)}</h1>
    <div class="authors">${esc((meta.authors || []).join(", "))}</div>
    <div class="venue">${esc(meta.venue || "")}${meta.year ? " · " + esc(meta.year) : ""}</div>
    <div class="abstract" id="abstract-block">${esc(meta.abstract || "")}</div>
    <button class="toggle" id="abstract-toggle">read full abstract ▾</button>
    <div class="stats">
      ${SECTIONS.map((s) => counts[s.id] > 0
        ? `<div><strong>${counts[s.id]}</strong>${s.label.toLowerCase()}</div>` : "").join("")}
    </div>
  `;
  const block = document.getElementById("abstract-block");
  const toggle = document.getElementById("abstract-toggle");
  // Hide toggle if abstract fits.
  if (block.scrollHeight <= block.clientHeight + 2) {
    toggle.style.display = "none";
  }
  toggle.addEventListener("click", () => {
    const open = block.classList.toggle("open");
    toggle.textContent = open ? "collapse abstract ▴" : "read full abstract ▾";
  });
}

// ---------------------------------------------------------------------------
// sections + cards
// ---------------------------------------------------------------------------

function renderSections() {
  const container = document.getElementById("sections");
  container.innerHTML = "";
  SECTIONS.forEach((s) => {
    const items = state.data.nodes.filter((n) => s.kinds.includes(n.kind));
    if (items.length === 0) return;
    // Sort: by numeric id when present.
    items.sort((a, b) => idSortKey(a) - idSortKey(b));
    const sec = document.createElement("section");
    sec.id = `section-${s.id}`;
    sec.className = "section";
    sec.innerHTML = `
      <div class="section-header">
        <h2>${esc(s.label)} <span class="count">${items.length}</span>
          ${s.blurb ? `<span class="blurb">${esc(s.blurb)}</span>` : ""}
        </h2>
      </div>
      <div class="section-body"></div>
    `;
    const body = sec.querySelector(".section-body");
    items.forEach((node) => body.appendChild(buildCard(node)));
    container.appendChild(sec);
  });
}

function idSortKey(node) {
  const m = /(\d+)/.exec(node.id);
  return m ? parseInt(m[1], 10) : 9999;
}

function buildCard(node) {
  const card = document.createElement("article");
  card.className = "card";
  card.dataset.id = node.id;
  card.id = `card-${node.id}`;

  // Header
  const head = document.createElement("div");
  head.className = "card-head";
  head.innerHTML = `
    <span class="badge ${node.kind}">${esc(KIND_BADGE[node.kind] || node.kind)} ${esc(shortId(node.id))}</span>
    <span class="card-title">${esc(stripIdPrefix(node.label))}</span>
    ${node.status ? `<span class="status-pill ${esc(node.status)}">${esc(node.status)}</span>` : ""}
  `;
  card.appendChild(head);

  // Statement (always visible)
  if (node.summary) {
    const stmt = document.createElement("div");
    stmt.className = "statement";
    stmt.textContent = node.summary;
    card.appendChild(stmt);
  }

  // Expand bar: lazy — built when card is first opened.
  const bar = document.createElement("div");
  bar.className = "expand-bar";
  bar.innerHTML = `<span class="group-label">loading…</span>`;
  card.appendChild(bar);

  // Defer expand-bar construction until visible (cheap files anyway; sync is fine).
  // We populate immediately but lazily fetch on click.
  populateExpandBar(node, bar, card);

  return card;
}

// Build the row of expand-buttons (for sub-sections of this node's markdown)
// and chips (for linked artifacts).
async function populateExpandBar(node, bar, card) {
  bar.innerHTML = "";

  // 1. Sub-section expand buttons (from this node's markdown fields)
  const fields = await fetchNodeFields(node);
  const fieldEntries = Object.entries(fields).filter(([k, v]) => v && v.trim());
  // Skip the field that's already shown as the headline statement.
  const skipFields = new Set();
  if (node.kind === "claim") skipFields.add("Statement");
  if (node.kind === "experiment") skipFields.add("Verifies");
  if (node.kind === "observation") skipFields.add("Statement");
  if (node.kind === "heuristic") skipFields.add("Rationale");
  if (node.kind === "concept") skipFields.add("Definition");
  if (node.kind === "related") skipFields.add("DOI");

  const interesting = fieldEntries.filter(([k]) => !skipFields.has(k));
  if (interesting.length > 0) {
    const label = document.createElement("span");
    label.className = "group-label";
    label.textContent = "show";
    bar.appendChild(label);
    interesting.forEach(([k, v]) => {
      const btn = document.createElement("button");
      btn.className = "expand-btn";
      btn.innerHTML = `<span class="arrow">▶</span> ${esc(k.toLowerCase())}`;
      btn.addEventListener("click", () => toggleField(card, btn, k, v));
      bar.appendChild(btn);
    });
  }

  // 2. Linked artifact chips, grouped by relationship.
  const linkGroups = buildLinkGroups(node);
  for (const [groupLabel, items] of linkGroups) {
    const row = document.createElement("div");
    row.className = "expand-bar";
    row.style.borderTop = "none";
    row.innerHTML = `<span class="group-label">${esc(groupLabel)}</span>`;
    items.forEach((id) => {
      const other = state.byId.get(id);
      if (!other) return;
      const chip = document.createElement("button");
      chip.className = "chip";
      chip.innerHTML = `<span class="chip-id">${esc(shortId(id))}</span>` +
        `<span class="chip-label">${esc(stripIdPrefix(other.label).slice(0, 60))}</span>`;
      chip.addEventListener("click", () => toggleNested(card, chip, id));
      row.appendChild(chip);
    });
    if (row.querySelectorAll(".chip").length > 0) card.appendChild(row);
  }

  if (bar.children.length === 0) bar.style.display = "none";
}

function buildLinkGroups(node) {
  const out = state.outEdges.get(node.id) || [];
  const inc = state.inEdges.get(node.id) || [];
  const groups = new Map();
  const push = (label, id) => {
    if (!groups.has(label)) groups.set(label, []);
    if (!groups.get(label).includes(id)) groups.get(label).push(id);
  };
  // Outgoing
  out.forEach((e) => {
    if (e.kind === "proves") push("proven by experiments", e.target);
    else if (e.kind === "verifies") push("verifies claims", e.target);
    else if (e.kind === "implements") push("implements", e.target);
    else if (e.kind === "references") push("references", e.target);
    else if (e.kind === "depends_on") push("depends on", e.target);
    else if (e.kind === "affects") push("affects claims", e.target);
    else if (e.kind === "trace_evidence") push("cites", e.target);
    else if (e.kind === "trace_edge") push("trace child", e.target);
  });
  // Incoming
  inc.forEach((e) => {
    if (e.kind === "proves") push("proven by experiments", e.source);
    else if (e.kind === "verifies") push("verified by experiments", e.source);
    else if (e.kind === "implements") push("implemented by heuristic", e.source);
    else if (e.kind === "references") push("referenced by", e.source);
    else if (e.kind === "depends_on") push("required by", e.source);
    else if (e.kind === "affects") push("affected by related work", e.source);
    else if (e.kind === "trace_evidence") push("cited in trace", e.source);
    else if (e.kind === "trace_edge") push("trace parent", e.source);
  });
  // Preferred order
  const order = [
    "proven by experiments", "verifies claims", "verified by experiments",
    "implements", "implemented by heuristic",
    "references", "referenced by",
    "depends on", "required by",
    "affects claims", "affected by related work",
    "trace parent", "trace child", "cites", "cited in trace",
  ];
  return order
    .filter((k) => groups.has(k))
    .map((k) => [k, groups.get(k)]);
}

// ---------------------------------------------------------------------------
// expand/collapse: field block
// ---------------------------------------------------------------------------

function toggleField(card, btn, key, value) {
  const slug = "fld-" + key.toLowerCase().replace(/\W+/g, "-");
  const existing = card.querySelector(`[data-field="${slug}"]`);
  if (existing) {
    existing.remove();
    btn.classList.remove("active");
    return;
  }
  const block = document.createElement("div");
  block.className = "detail-block";
  block.dataset.field = slug;
  block.innerHTML = `<span class="field-label">${esc(key)}</span>` +
    `<div class="field-value">${marked.parse(value)}</div>`;
  // Insert immediately after the btn's parent row
  insertAfter(block, btn.closest(".expand-bar"));
  btn.classList.add("active");
}

// ---------------------------------------------------------------------------
// expand/collapse: nested artifact card
// ---------------------------------------------------------------------------

async function toggleNested(card, chip, nodeId) {
  const existing = card.querySelector(`[data-nested="${nodeId}"]`);
  if (existing) {
    existing.remove();
    chip.classList.remove("active");
    return;
  }
  chip.classList.add("active");
  const node = state.byId.get(nodeId);

  const wrap = document.createElement("div");
  wrap.className = "nested";
  wrap.dataset.nested = nodeId;
  wrap.innerHTML = `
    <div class="nested-header">
      <span>expanded ${esc(node.kind.replace(/_/g, " "))}</span>
      <button class="close" title="collapse">×</button>
    </div>
  `;
  // Recursive: just build another card and slot it in.
  const sub = buildCard(node);
  // The nested card opens with one default block already shown:
  // first interesting field for claims/experiments, full markdown for code/figure.
  wrap.appendChild(sub);
  insertAfter(wrap, chip.closest(".expand-bar"));

  wrap.querySelector(".close").addEventListener("click", () => {
    wrap.remove();
    chip.classList.remove("active");
  });

  // For figure/table/code/config — auto-show the whole file content since
  // those aren't field-structured.
  if (["figure", "table", "code", "config", "solution"].includes(node.kind)) {
    autoShowFullContent(node, sub);
  }
}

async function autoShowFullContent(node, card) {
  if (!node.file) return;
  try {
    const md = await fetchRawMarkdown(node);
    const block = document.createElement("div");
    block.className = "detail-block";
    block.dataset.field = "full";
    if (node.kind === "code" || (node.kind === "config" && /\.py$/.test(node.file))) {
      block.innerHTML = `<span class="field-label">${esc(node.file)}</span>` +
        `<pre><code>${esc(md)}</code></pre>`;
    } else {
      block.innerHTML = marked.parse(md);
    }
    card.appendChild(block);
  } catch (e) {
    // ignore
  }
}

// ---------------------------------------------------------------------------
// fetch + parse markdown sections into field maps
// ---------------------------------------------------------------------------

async function fetchRawMarkdown(node) {
  if (!node.file) return "";
  const key = node.file;
  if (state.mdCache.has(key)) return state.mdCache.get(key);
  const r = await fetch(`${ARA_PATH}/${node.file}`);
  if (!r.ok) throw new Error(`fetch ${node.file}: ${r.status}`);
  const text = await r.text();
  state.mdCache.set(key, text);
  return text;
}

// Returns the narrowed markdown for this specific node (one section out of a
// multi-section file).
async function fetchNodeSection(node) {
  if (!node.file) return "";
  const text = await fetchRawMarkdown(node);
  // Multi-section files
  const idMatch = /^(?:C|E|H|RW|O)\d+/.exec(node.id);
  if (idMatch) {
    const rx = new RegExp(
      `(\\n##+ ${idMatch[0]}:[^\\n]*[\\s\\S]*?)(?=\\n##+ (?:C|E|H|RW|O)\\d+:|$)`
    );
    const m = rx.exec("\n" + text);
    if (m) return m[1].replace(/^\n/, "");
  }
  if (node.id.startsWith("Concept:")) {
    const escaped = node.label.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const rx = new RegExp(`(\\n## ${escaped}[\\s\\S]*?)(?=\\n## |$)`);
    const m = rx.exec("\n" + text);
    if (m) return m[1].replace(/^\n/, "");
  }
  if (/^N\d+$/.test(node.id)) {
    const rx = new RegExp(`(  - id: ${node.id}[\\s\\S]*?)(?=\\n  - id: N\\d+|$)`);
    const m = rx.exec(text);
    if (m) return "```yaml\n" + m[1].trim() + "\n```";
  }
  return text;
}

// Parse a node's markdown into a {field: value} map.
// Recognizes the canonical ARA bullet format:  - **Field**: value...
// Multi-line continuations are joined.
async function fetchNodeFields(node) {
  const md = await fetchNodeSection(node);
  if (!md) return {};
  const fields = {};
  const lines = md.split("\n");
  let curKey = null;
  let curBuf = [];
  const flush = () => {
    if (curKey != null) {
      fields[curKey] = curBuf.join("\n").trim();
    }
  };
  for (let i = 0; i < lines.length; i++) {
    const ln = lines[i];
    const m = /^- \*\*([^*]+)\*\*:\s*(.*)$/.exec(ln);
    if (m) {
      flush();
      curKey = m[1].trim();
      curBuf = [m[2]];
    } else if (curKey != null && /^\s+\S/.test(ln)) {
      // continuation (indented)
      curBuf.push(ln.replace(/^\s+/, "  "));
    } else if (curKey != null && /^\s*-\s/.test(ln)) {
      // nested list item under current field
      curBuf.push(ln);
    } else if (curKey != null && ln.trim() === "") {
      curBuf.push("");
    } else {
      flush();
      curKey = null;
      curBuf = [];
    }
  }
  flush();
  // For trace nodes (YAML) — fields not bullets; expose a single "yaml" field.
  if (Object.keys(fields).length === 0 && md) {
    fields["details"] = md;
  }
  return fields;
}

// ---------------------------------------------------------------------------
// TOC + scroll spy
// ---------------------------------------------------------------------------

function renderTOC() {
  const toc = document.getElementById("toc");
  toc.innerHTML = "";
  SECTIONS.forEach((s) => {
    const items = state.data.nodes.filter((n) => s.kinds.includes(n.kind));
    if (items.length === 0) return;
    items.sort((a, b) => idSortKey(a) - idSortKey(b));
    const h = document.createElement("h4");
    h.innerHTML = `<a href="#section-${s.id}" style="color:inherit;text-decoration:none">${esc(s.label)}</a>`;
    toc.appendChild(h);
    const ul = document.createElement("ul");
    items.forEach((n) => {
      const li = document.createElement("li");
      const a = document.createElement("a");
      a.href = `#card-${n.id}`;
      a.dataset.target = `card-${n.id}`;
      a.innerHTML = `<span class="id">${esc(shortId(n.id))}</span>${esc(stripIdPrefix(n.label).slice(0, 50))}`;
      li.appendChild(a);
      ul.appendChild(li);
    });
    toc.appendChild(ul);
  });
}

function setupTOCScrollSpy() {
  const links = Array.from(document.querySelectorAll('#toc a[data-target]'));
  if (links.length === 0) return;
  const obs = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        links.forEach((a) => a.classList.toggle("active", a.dataset.target === entry.target.id));
      }
    });
  }, { rootMargin: "-70px 0px -60% 0px", threshold: 0 });
  document.querySelectorAll(".card").forEach((c) => obs.observe(c));
}

// ---------------------------------------------------------------------------
// controls
// ---------------------------------------------------------------------------

function wireControls() {
  document.getElementById("search").addEventListener("input", (e) => {
    const q = e.target.value.trim().toLowerCase();
    document.querySelectorAll(".card").forEach((c) => {
      if (!q) { c.classList.remove("hidden"); return; }
      const id = c.dataset.id || "";
      const text = c.textContent.toLowerCase();
      c.classList.toggle("hidden", !(id.toLowerCase().includes(q) || text.includes(q)));
    });
  });

  document.getElementById("expand-all").addEventListener("click", () => {
    document.querySelectorAll(".card .expand-btn:not(.active)").forEach((btn) => btn.click());
  });
  document.getElementById("collapse-all").addEventListener("click", () => {
    document.querySelectorAll(".card .expand-btn.active, .card .chip.active")
      .forEach((btn) => btn.click());
    document.querySelectorAll(".nested").forEach((n) => n.remove());
  });
}

// ---------------------------------------------------------------------------
// utils
// ---------------------------------------------------------------------------

function shortId(id) {
  // For "Concept:Foo" -> "Foo"; for "Code:src/foo.py" -> "foo.py"
  if (id.startsWith("Concept:")) return id.slice("Concept:".length);
  if (id.startsWith("Code:")) return id.slice("Code:".length).split("/").pop();
  if (id.startsWith("Sol:")) return id.slice("Sol:".length);
  return id;
}

function stripIdPrefix(label) {
  // Labels often look like "C03: Token-level..." — strip leading "ID: ".
  return String(label || "").replace(/^[A-Z]+\d+[a-z]?:\s*/, "");
}

function insertAfter(newNode, ref) {
  ref.parentNode.insertBefore(newNode, ref.nextSibling);
}

function esc(s) {
  return String(s == null ? "" : s).replace(/[&<>"']/g, (c) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
  }[c]));
}

main();
