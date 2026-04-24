#!/usr/bin/env node
// prepack: copy the monorepo's top-level skills/ into this package so the
// published tarball is self-contained. Clean-up runs from postpack.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const pkgRoot = path.resolve(here, '..');
const src = path.resolve(pkgRoot, '..', '..', 'skills');
const dst = path.join(pkgRoot, 'skills');

if (!fs.existsSync(src)) {
  console.error(`[ara-skills:prepack] source not found: ${src}`);
  process.exit(1);
}

// Don't clobber a bundle that's already inside the package (e.g. user ran
// `prepack` manually); refresh it anyway for determinism.
fs.rmSync(dst, { recursive: true, force: true });
fs.mkdirSync(dst, { recursive: true });

function copyDir(s, d) {
  fs.mkdirSync(d, { recursive: true });
  for (const e of fs.readdirSync(s, { withFileTypes: true })) {
    const a = path.join(s, e.name);
    const b = path.join(d, e.name);
    if (e.isDirectory()) copyDir(a, b);
    else fs.copyFileSync(a, b);
  }
}

copyDir(src, dst);
console.log(`[ara-skills:prepack] bundled skills/ from ${src}`);
