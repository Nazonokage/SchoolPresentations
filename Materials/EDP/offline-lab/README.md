# EDP offline computer lab

Copy this ENTIRE folder to a lab PC. Keep vendor/, project.mjs and worker.mjs with the lesson files. No npm install or internet is needed for the supplied runtime demonstrations. Node must already be installed: the course baseline is Node 24.18.1. A modern browser is needed for M03, M08 and M09.

Double-click START-LAB.cmd on Windows, enter the module number, then follow the terminal instructions. Alternatively run `node lab.mjs`. M08 opens the local browser exercise; run `node m08.mjs` for its console companion. M21 uses the original m20.mjs readiness starter. M20 is written assessment only. Stop a running local server with Ctrl+C before starting another.

TypeScript execution in M06 uses Node's supported syntax stripping; this does NOT type-check the code. Full TypeScript checking needs the original examples toolchain prepared with npm ci beforehand. There are no public APIs or real brokers in these demos. Advanced examples are local simulations.

## Submission

Use edp-mNN-topic-surname-firstname-section-yyyy-mm-dd, all lowercase with hyphens. Example: edp-m08-reactive-search-dalisay-ina-it2a-yyyy-mm-dd. Mini-capstone: edp-capstone-project-surname-firstname-section-yyyy-mm-dd. Follow an instructor-assigned identifier if required.

Upload your modified source and required local supporting files, README.md with exact setup/run instructions, essays.md, and evidence/ with success and failure observations. Include package.json and package-lock.json when using installed dependencies. Do not upload node_modules, passwords, .env files or unrelated student data. If your code uses vendor/, include the needed vendored files and license, or restore package imports and document the npm installation instead. Do not remove vendor/ while retaining imports to it.

Create the repository with the recommended name, upload the files, verify the README displays, then submit the repository URL and final commit ID through the instructor's submission channel. Public visibility is not required; ensure the instructor has access. If internet is unavailable, prepare a ZIP with the same name and upload when access is available. The instructor sets the deadline.

## Third-party code

vendor/rxjs is the locally installed RxJS 7.8.2 package, included unchanged with its LICENSE.txt for offline use. Source lessons remain in ../examples. No Node installer is bundled.

## Classroom or assignment rule

Use the announced activity/assignment date for yyyy-mm-dd in the repository name. It is not the due date. No timetable date is assumed.

Odd modules 1–19 retain the 10-item quiz (5 MCQ, 5 output). Even modules use coding plus topic essays. If the required code and packages are available offline, complete coding in the computer lab. If the selected task requires npm install/npm ci downloads that are unavailable in the lab, finish that coding task as an assignment and draft the essays in class. Local HTTP on 127.0.0.1 does not require internet.

M06 full TypeScript checking requires the prepared compiler/toolchain; its Node-only runtime demonstration is not a substitute. M08 can run in the lab using the bundled RxJS copy; the original examples route requires packages to be installed beforehand. Other supplied even-module runtime examples use built-in Node APIs or local files. Node and the browser must be prepared before class.
