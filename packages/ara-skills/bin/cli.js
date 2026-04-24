#!/usr/bin/env node
import { main } from '../src/index.js';

main(process.argv.slice(2)).catch((err) => {
  console.error(`\nError: ${err?.message ?? err}`);
  if (process.env.ARA_SKILLS_DEBUG) console.error(err?.stack);
  process.exit(1);
});
