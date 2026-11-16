# Maintaining the authored pack

Student-facing files are in `modules`; runnable source is in `examples`. Instructor-only answers, validation evidence and authoring utilities are here.

The `authoring` folder contains the Python lesson text/assessment data, module builder and local QA scripts created for this pack. Run the builder from the original `Additional_Courses` workspace root so its relative paths resolve:

```powershell
python "Application Development and Emerging Technologies (Inluding event Driven programming)/EDP/instructor/authoring/build_edp_modules.py"
```

The builder embeds the current example files. Edit the lesson data there if you intend to regenerate; direct module edits would otherwise be overwritten. The validation utilities assume the same workspace working directory. The browser utility refers to the authoring environment's bundled Playwright installation and Edge; adapt that tooling path before running on another machine. It is not a student dependency.

`authoring/archive/author_edp_examples.py` is the initial generation snapshot. Do not rerun it over the final examples: later browser additions and server changes are maintained in the actual files. Keep package.json and package-lock.json together, and use npm ci for a reproducible install.

After changing code: run typecheck, relevant console/tests, and browser checks for affected pages; rebuild the Markdown to keep embedded code consistent. Update VALIDATION with observed results and limitations rather than assuming earlier checks still apply.

Visual enrichment is a second pass: after rebuilding modules, rerun the workspace-root enrich_edp_visuals.py script to restore per-module visual notes. SVGs and presentation guidance live in visuals/. The source-audit metadata records the five user-supplied reference HTML files.
