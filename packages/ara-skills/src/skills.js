import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PACKAGE_ROOT = path.resolve(__dirname, '..');

/**
 * Locate the directory that holds the skill sources.
 *
 * Two modes:
 *   1. Published package: skills are bundled at <pkg>/skills/  (via `prepack`).
 *   2. Dev mode (running from monorepo): fall back to <repoRoot>/skills/
 *      which is <pkg>/../../skills.
 */
export function resolveSkillsRoot() {
  const bundled = path.join(PACKAGE_ROOT, 'skills');
  if (isSkillsDir(bundled)) return bundled;

  const monorepo = path.resolve(PACKAGE_ROOT, '..', '..', 'skills');
  if (isSkillsDir(monorepo)) return monorepo;

  throw new Error(
    `Could not locate skills directory. Looked in:\n  ${bundled}\n  ${monorepo}`
  );
}

function isSkillsDir(dir) {
  if (!fs.existsSync(dir) || !fs.statSync(dir).isDirectory()) return false;
  const entries = fs.readdirSync(dir);
  return entries.some((name) => {
    const skillMd = path.join(dir, name, 'SKILL.md');
    return fs.existsSync(skillMd);
  });
}

/**
 * Parse the YAML frontmatter at the top of SKILL.md.
 * Intentionally minimal — we only need `name` and `description`.
 */
function parseFrontmatter(mdPath) {
  const src = fs.readFileSync(mdPath, 'utf8');
  if (!src.startsWith('---')) return {};
  const end = src.indexOf('\n---', 3);
  if (end < 0) return {};
  const body = src.slice(3, end).trim();

  const out = {};
  let currentKey = null;
  let buffer = [];
  const flush = () => {
    if (currentKey !== null) {
      out[currentKey] = buffer.join('\n').trim();
    }
  };

  for (const raw of body.split('\n')) {
    const line = raw.replace(/\r$/, '');
    const m = line.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
    // A new top-level key starts only when the line has no leading whitespace.
    if (m && !raw.startsWith(' ') && !raw.startsWith('\t')) {
      flush();
      currentKey = m[1];
      const value = m[2];
      buffer = value === '' || value === '|' || value === '>' ? [] : [value];
    } else if (currentKey) {
      buffer.push(line.replace(/^\s{2}/, ''));
    }
  }
  flush();
  return out;
}

/**
 * Discover all skills by scanning <root>/<id>/SKILL.md.
 * Returns: [{ id, name, description, path }]
 */
export function listSkills(root = resolveSkillsRoot()) {
  const out = [];
  for (const id of fs.readdirSync(root).sort()) {
    const skillDir = path.join(root, id);
    const skillMd = path.join(skillDir, 'SKILL.md');
    if (!fs.existsSync(skillMd)) continue;
    if (!fs.statSync(skillDir).isDirectory()) continue;

    const meta = parseFrontmatter(skillMd);
    const name = meta.name || id;
    const description =
      (meta.description || '').replace(/\s+/g, ' ').trim().slice(0, 240) ||
      `(no description)`;
    out.push({ id, name, description, path: skillDir });
  }
  return out;
}

export function getSkill(id) {
  return listSkills().find((s) => s.id === id || s.name === id);
}
