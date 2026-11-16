// Instructor-only convenience. This replaces mobile/App.tsx; save student work first.
import { copyFile, writeFile } from "node:fs/promises";
const id = process.argv[2]?.padStart(2, "0");
if (!id || !Array.from({ length: 20 }, (_, index) => String(index + 1).padStart(2, "0")).includes(id)) {
  throw Error("Use node select.mjs 01 through 20; M00/M21 are not executable checkpoints.");
}
const file = (relative) => new URL(relative, import.meta.url);
await copyFile(file(`M${id}/App.tsx`), file("mobile/App.tsx"));
if (id === "15") await copyFile(file("M15/tone.wav"), file("mobile/tone.wav"));
await writeFile(file("mobile/index.js"), 'import { registerRootComponent } from "expo"; import App from "./App"; registerRootComponent(App);\n');
console.log(`Selected M${id} as App.tsx. Real M05 Router uses its separate extension. From mobile run npm start -- --clear.`);
