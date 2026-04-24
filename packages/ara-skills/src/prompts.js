import { checkbox, select, confirm } from '@inquirer/prompts';
import chalk from 'chalk';
import { SUPPORTED_AGENTS, detectAgents } from './agents.js';
import { listSkills } from './skills.js';
import { install, uninstall, update, listInstalled } from './installer.js';

function banner() {
  console.log();
  console.log(chalk.bold.cyan('  ARA Skills'));
  console.log(chalk.gray('  Agent-Native Research Artifact — skills installer'));
  console.log();
}

export async function interactiveFlow() {
  banner();

  const skills = listSkills();
  const detected = detectAgents();
  if (detected.length > 0) {
    console.log(chalk.gray(`  Detected agents: ${detected.map((a) => a.name).join(', ')}`));
  } else {
    console.log(chalk.yellow('  No coding agents detected — you can still install locally.'));
  }
  console.log();

  const action = await select({
    message: 'What would you like to do?',
    choices: [
      { name: 'Install skills', value: 'install' },
      { name: 'List installed skills', value: 'list' },
      { name: 'Update installed skills', value: 'update' },
      { name: 'Uninstall skills', value: 'uninstall' },
      { name: 'Exit', value: 'exit' },
    ],
  });

  if (action === 'exit') return;

  if (action === 'list') {
    const rows = listInstalled();
    if (rows.length === 0) {
      console.log(chalk.gray('  No ARA skills installed.'));
      return;
    }
    for (const r of rows) {
      console.log(`  ${chalk.bold(r.agent)} (${r.scope}) — ${chalk.gray(r.dir)}`);
      for (const s of r.skills) console.log(`    • ${s}`);
    }
    return;
  }

  const scope = await select({
    message: 'Install scope',
    choices: [
      { name: 'Global  (user-level, available in every project)', value: 'global' },
      { name: 'Local   (just this project / current directory)', value: 'local' },
    ],
  });
  const local = scope === 'local';

  const agentChoices = SUPPORTED_AGENTS.map((a) => ({
    name: `${a.name}${detected.includes(a) ? chalk.green('  ✓ detected') : ''}`,
    value: a.id,
    checked: detected.includes(a),
  }));
  const agentIds = await checkbox({
    message: 'Pick target agents',
    choices: agentChoices,
    required: true,
  });

  if (action === 'install') {
    const skillIds = await checkbox({
      message: 'Pick skills to install',
      choices: skills.map((s) => ({
        name: `${chalk.bold(s.id)}  —  ${chalk.gray(s.description.slice(0, 80))}`,
        value: s.id,
        checked: true,
      })),
      required: true,
    });
    const force = await confirm({
      message: 'Overwrite existing installations if present?',
      default: true,
    });
    console.log();
    for (const agentId of agentIds) {
      console.log(chalk.bold(`→ ${agentId} (${local ? 'local' : 'global'})`));
      install({ agentId, skillIds, local, force });
    }
  }

  if (action === 'update') {
    console.log();
    for (const agentId of agentIds) {
      console.log(chalk.bold(`→ ${agentId} (${local ? 'local' : 'global'})`));
      update({ agentId, local });
    }
  }

  if (action === 'uninstall') {
    const skillIds = await checkbox({
      message: 'Pick skills to remove (empty = all tracked)',
      choices: skills.map((s) => ({
        name: `${chalk.bold(s.id)}`,
        value: s.id,
      })),
    });
    console.log();
    for (const agentId of agentIds) {
      console.log(chalk.bold(`→ ${agentId} (${local ? 'local' : 'global'})`));
      uninstall({ agentId, skillIds, local });
    }
  }

  console.log();
  console.log(chalk.green('  Done.'));
}
