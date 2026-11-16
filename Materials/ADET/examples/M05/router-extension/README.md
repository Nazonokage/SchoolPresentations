# M05 optional Router extension — separate project

This is the real Router version. The sibling App.tsx is a template-only navigation simulation. Never place this app/ directory inside the core offline starter; use a separate student project.

## Install first (online, before class)

```powershell
npx create-expo-app@latest ADET-M05-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M05-LASTNAME
npx expo install expo-router react-native-safe-area-context react-native-screens expo-linking expo-constants expo-status-bar
```

Use the SDK 58 course baseline and TypeScript 6.0.3. The install command selects SDK-compatible native packages; save this separate project's lockfile. All six dependencies are intentional: Router, safe area, screens, linking, Expo constants, and status bar. No new package is required by the offline simulation.

## Configure and copy

1. Copy the complete app/ folder beside package.json. Use app/ only, not a competing src/app/ tree.
2. Change only the main field in package.json to `"main": "expo-router/entry"`. Keep dependencies and scripts.
3. Merge these fields into the existing expo object in app.json; preserve its existing name, slug, icons and other settings:

```json
{
  "scheme": "adetlab",
  "plugins": ["expo-router"]
}
```

If a plugins array already exists, append expo-router once. No permission prompt is needed for in-app navigation. The custom scheme takes effect in a native build containing that configuration; Expo Go does not become an installed adetlab app. Typed-route generation is optional and is not enabled in this beginner checkpoint.

4. Use this complete tsconfig.json to include all route files:

```json
{
  "extends": "expo/tsconfig.base",
  "compilerOptions": { "strict": true },
  "include": ["**/*.ts", "**/*.tsx", ".expo/types/**/*.ts", "expo-env.d.ts"]
}
```

5. Keep the template's Expo Babel defaults; no custom Babel file is needed here. App.tsx and index.ts are no longer the entry, so leave them unused or omit them from this separate project.
6. Run `npx tsc --noEmit`, then `npx expo start --clear`. In-app navigation supports compatible Expo Go. Custom installed URL-scheme tests need a prepared development build; no such device test has been completed.

## Files and trace

- app/_layout.tsx supplies Stack.
- app/index.tsx supplies Home and two push actions.
- app/office/[id].tsx reads and checks the ID before rendering the record.

Predict before running: library → known record → Library — Open 8 AM. unknown → no own record → Office not found. Back returns to Home when history exists. On a direct entry with no history, Home replaces the destination. Checking Object.hasOwn also prevents inherited object properties such as constructor from being mistaken for records.

Add clinic to offices and a push button on Home as ungraded practice. Test known, unknown and no-history cases. Expo Go external links and a standalone custom scheme have different URL forms; do not infer native linking success from a bundle test.

## Troubleshooting

Old screen: inspect main. Unmatched route: inspect app/office/[id].tsx exactly. Missing package: complete online setup before class. Native mismatch: inspect the installed client's SDK instead of changing the lab starter blindly.

[Official manual installation](https://docs.expo.dev/router/installation/). Refer to the [stop-2 validation record](../../../instructor/stop2-2026-11-07/VALIDATION.md) for measured results.
