import { mkdtemp, copyFile, writeFile, unlink, rmdir } from 'node:fs/promises';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const mobile = fileURLToPath(new URL('./', import.meta.url));
const staging = await mkdtemp(join(mobile, '.adet-check-'));
const files = [];
async function stage(source, name) {
  const output = join(staging, name);
  await copyFile(new URL(source, import.meta.url), output);
  files.push(output);
}
try {
  for (let number = 1; number <= 20; number++) {
    const id = String(number).padStart(2, '0');
    await stage('../M' + id + '/App.tsx', 'M' + id + '.tsx');
  }
  await stage('../M05/[id].tsx', 'detail.tsx');
  const config = join(staging, 'tsconfig.json');
  await writeFile(config, JSON.stringify({extends:'../tsconfig.json',include:['*.tsx']}));
  files.push(config);
  const result = spawnSync(process.execPath, [join(mobile,'node_modules/typescript/bin/tsc'),'--noEmit','-p',config], {stdio:'inherit'});
  process.exitCode = result.status ?? 1;
  if (!process.exitCode) console.log('Checked all 20 checkpoints and the M05 detail route.');
} finally {
  for (const file of files) await unlink(file);
  await rmdir(staging);
}
