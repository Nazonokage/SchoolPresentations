# Five-minute smoke test

Do this on each lab machine before class. Record date, Node/npm versions, native client version, OS and connection route.

1. Minute 0–1: copy offline-lab to a short writable local path. Run node -v and npm -v. Baseline: 24.18.1 / 11.16.0. Verify starter/package-lock.json and installed node_modules exist.
2. Minute 1–2: from starter run npm run typecheck. Confirm exit 0. Launch START-LAB.cmd. It invokes the locally installed Expo CLI with --offline, without npx trying to download a CLI.
3. Minute 2–3: open a preinstalled compatible Expo Go on the local network, or an already prepared Android emulator. Confirm the greeting and baon shortage. A PC bundle test alone does not count as this step.
4. Minute 3–4: change budget 50 to 80, save, and expect Change: PHP 20. Check the displayed result. A full reload is acceptable; record whether Fast Refresh actually worked.
5. Minute 4–5: deliberately misspell an import in a saved copy, observe the error, restore it, and rerun type checking. Record the exact error and fix.

For M02, separately open React Native DevTools Console and record mount/unmount messages. Hide/show performs conditional removal. Background/foreground tests AppState; the sample does not pause the interval. Record where logs really appear in that client.

If step 3 fails, record PC address, client version and local-network isolation/firewall result. Do not use an internet tunnel to claim the offline route passed. Use the written alternative for students until the setup is repaired.

Result form: [ ] typecheck [ ] server [ ] native screen [ ] saved change [ ] failure/fix. Device/network: ____. Actual logs: ____. Blocker: ____.
