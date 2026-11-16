import { copyFile, writeFile, readFile, mkdir } from "node:fs/promises";
const id = process.argv[2]?.padStart(2, "0");
if (
  !id ||
  !Array.from({ length: 20 }, (_, i) =>
    String(i + 1).padStart(2, "0"),
  ).includes(id)
)
  throw Error("Use node select.mjs 01 through 20");
const file = (p) => new URL(p, import.meta.url);
const mobile = file("mobile/");
await mkdir(new URL("app/office/", mobile), { recursive: true });
await copyFile(file("M" + id + "/App.tsx"), new URL("App.tsx", mobile));
if (id === "05") {
  await copyFile(file("M05/App.tsx"), new URL("app/index.tsx", mobile));
  await copyFile(file("M05/[id].tsx"), new URL("app/office/[id].tsx", mobile));
  await writeFile(
    new URL("app/_layout.tsx", mobile),
    "import {Stack} from 'expo-router';export default function Layout(){return <Stack/>}",
  );
}
if (id === "15")
  await copyFile(file("M15/tone.wav"), new URL("tone.wav", mobile));
await writeFile(
  new URL("index.js", mobile),
  id === "05"
    ? "import 'expo-router/entry';"
    : "import {registerRootComponent} from 'expo'; import App from './App'; registerRootComponent(App);",
);
console.log("Selected M" + id + ". From mobile run npm start -- --clear.");
