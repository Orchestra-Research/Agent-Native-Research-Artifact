import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

/**
 * Minimal agent registry. Each entry declares where the agent expects skills
 * to live, both globally (user-level) and locally (per-project).
 *
 * The layout we write is: <skillsDir>/<skill-id>/SKILL.md (+ any files).
 */
export const SUPPORTED_AGENTS = [
  {
    id: 'claude-code',
    name: 'Claude Code',
    globalSkillsDir: path.join(os.homedir(), '.claude', 'skills'),
    localSkillsDir: '.claude/skills',
    detect: () => fs.existsSync(path.join(os.homedir(), '.claude')),
  },
  {
    id: 'cursor',
    name: 'Cursor',
    globalSkillsDir: path.join(os.homedir(), '.cursor', 'skills'),
    localSkillsDir: '.cursor/skills',
    detect: () => fs.existsSync(path.join(os.homedir(), '.cursor')),
  },
  {
    id: 'gemini-cli',
    name: 'Gemini CLI',
    globalSkillsDir: path.join(os.homedir(), '.gemini', 'skills'),
    localSkillsDir: '.gemini/skills',
    detect: () => fs.existsSync(path.join(os.homedir(), '.gemini')),
  },
  {
    id: 'opencode',
    name: 'OpenCode',
    globalSkillsDir: path.join(os.homedir(), '.opencode', 'skills'),
    localSkillsDir: '.opencode/skills',
    detect: () => fs.existsSync(path.join(os.homedir(), '.opencode')),
  },
  {
    id: 'codex',
    name: 'Codex CLI',
    globalSkillsDir: path.join(os.homedir(), '.codex', 'skills'),
    localSkillsDir: '.codex/skills',
    detect: () => fs.existsSync(path.join(os.homedir(), '.codex')),
  },
  {
    id: 'hermes',
    name: 'Hermes Agent',
    globalSkillsDir: path.join(os.homedir(), '.hermes', 'skills'),
    localSkillsDir: '.hermes/skills',
    detect: () => fs.existsSync(path.join(os.homedir(), '.hermes')),
  },
  {
    id: 'generic',
    name: 'Generic (./skills)',
    globalSkillsDir: path.join(os.homedir(), '.skills'),
    localSkillsDir: 'skills',
    detect: () => false,
  },
];

export function detectAgents() {
  return SUPPORTED_AGENTS.filter((a) => a.detect());
}

export function getAgentById(id) {
  return SUPPORTED_AGENTS.find((a) => a.id === id);
}

export function getSupportedAgentIds() {
  return SUPPORTED_AGENTS.map((a) => a.id);
}

export function targetDirFor(agent, { local = false, cwd = process.cwd() } = {}) {
  return local ? path.resolve(cwd, agent.localSkillsDir) : agent.globalSkillsDir;
}
