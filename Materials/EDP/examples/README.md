# EDP runnable example pack

## One-time setup

Use an editor, a modern desktop browser and Node.js. The execution host used for this pack is Node **24.18.1**; this is a tested baseline, not a claim about the newest release. The TypeScript examples use Node's supported erasable syntax and are checked separately with TypeScript **5.9.3** and Node typings **24.10.0**. RxJS is **7.8.2**. Exact dependencies are recorded in package-lock.json.

Open a terminal in this `examples` folder, then run:

```powershell
node --version
npm ci
npm run typecheck
npm test
```

Internet is needed to install dependencies initially. An instructor can prepare machines before class. Once installed, the examples use no remote data service. Do not commit or distribute node_modules as source; use the package manifest and lockfile. Keep every example filename unchanged when following a module.

## Entry points

- M01: `node m01.mjs`; optional typed companion `node m01-types.ts` after type checking.
- M02/M04/M05/M07/M08/M10/M12–M20: `node mNN.mjs` with the two-digit module number.
- M03, M08 and M09: `npm run serve`, then open http://127.0.0.1:4173/m03-first.html (first click), /m03.html (form/list), /m08.html (reactive search) or /m09.html (SSE). Keep the terminal open; stop with Ctrl+C. Do not run two copies on the same port.
- M06: `npm run typecheck`, then `node m06.ts`.
- M10 extension: `node m10-worker.mjs`; worker.mjs must remain beside it.
- M11: `node --test m11.test.mjs`.
- M18/M20 project checks: `node --test project.test.mjs`; both depend on project.mjs.

The server binds to loopback only. It is a local teaching server with no authentication, replay storage or public deployment configuration. The SSE counter restarts per connection. Browser examples are plain JavaScript; do not paste TypeScript annotations into their script blocks.

## Troubleshooting

`ERR_MODULE_NOT_FOUND`: run npm ci in this folder and check filenames. `EADDRINUSE`: stop the previous lesson server, or coordinate a deliberate port change in both instructions and server. TypeScript syntax failures: verify the supported Node version; do not confuse execution with tsc checking. An error expected by a test is not an unsuccessful test when the assertion catches it. Look for the final pass/fail result.

Examples from M12 onward are intentionally small local models. They do not establish durable delivery, database transactions, authentication, broker availability or production readiness. The lesson describes what is missing.
