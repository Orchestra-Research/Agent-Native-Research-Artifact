#!/usr/bin/env node
// postpack: remove the bundled skills/ copy so the working tree stays clean.
// The published tarball already contains it at this point.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const pkgRoot = path.resolve(here, '..');
const dst = path.join(pkgRoot, 'skills');

if (fs.existsSync(dst)) {
  fs.rmSync(dst, { recursive: true, force: true });
  console.log('[ara-skills:postpack] cleaned packages/ara-skills/skills/');
}
