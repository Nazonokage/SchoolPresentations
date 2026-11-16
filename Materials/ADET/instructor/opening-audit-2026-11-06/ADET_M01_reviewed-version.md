# ADET M01 · React Native platform, tools and your first app

[Module index](README.md) · Prelim · 60–90 minutes · Individual coding activity

> **Version check — tested 2026-11-06 (Asia/Manila).** A fresh `--template blank-typescript` project resolved to Expo SDK 58 (`expo ~58.0.23`), React Native 0.88.1 and TypeScript ~6.0.3, using Node v24.18.1 and npm 11.16.0. The M01–M03 samples passed `tsc --noEmit` and local Expo `start --offline` Android bundling. No phone/emulator was connected, so rendered UI, Fast Refresh on a device and offline LAN operation are not yet verified. Check the installed Expo Go compatibility before class. The official project-creation page retrieved during the audit contained conflicting transition guidance; its default-template note does not establish the SDK selected by the explicit blank-typescript command. See [audit findings](AUDIT.md) and [test results](validation.json).

## A. Lesson Preview & Review

**Can you go from an empty folder to a running app on your phone?** Learn what each tool does, create a project, run it, change one line and add one package.

**Learning targets.**
1. Install and check the tools you need.
2. Create and run an Expo project.
3. Read the project folder and `package.json`.
4. Add a package safely.

By the end, trace **Install tools → Create project → Start server → Open on phone → Edit → See change**, and explain in your own words: the phone shows "Hello, ADET!" after you save, without reinstalling anything.

## B. Detailed Main Lesson

### In plain words

Your computer runs a small server. Your phone opens the app from that server. Every time you save a file, the phone updates by itself. Expo handles the hard setup so you can focus on writing the app.

### The tools and what each is for

| Tool | What it is | How to check |
|---|---|---|
| Node.js (LTS) | Runs JavaScript on your computer. Everything below needs it. | `node -v` |
| npm | Comes with Node. Downloads packages and runs scripts. | `npm -v` |
| VS Code | The editor where you write code | Open it |
| Expo Go | A ready-made app on your phone that opens your project | Install from your phone's app store |
| Android Emulator / iOS Simulator | Optional virtual phone | Press `a` or `i` after starting the server |

**Metro** packs your code into a bundle on your computer. **Hermes** runs that JavaScript on the phone. **Expo Go** is a prebuilt native app that opens your project. A **development build** is your own host app with the extra native libraries your project needs.

```text
Your computer                              Your phone
+-----------------+   same Wi-Fi / QR   +--------------------+
| Code (App.tsx)  | ------------------> | Expo Go            |
| Metro bundler   |   sends the bundle  | Hermes runs the JS |
| npx expo start  | <------------------ | Native screen      |
+-----------------+    reload on save   +--------------------+
```

### Create and run a project

1. Create the project with the **blank TypeScript** template so the lesson file is `App.tsx`:
   ```powershell
   npx create-expo-app@latest my-first-app --template blank-typescript
   cd my-first-app
   ```
   > The **default** template uses file-based routing and its first screen is `src/app/index.tsx`, with no `App.tsx`. If a student uses it, put checkpoint code in that file.
2. Open `package.json` and read the `"expo"` version (for example `~57.0.0`). Your Expo Go app must support that SDK.
3. Start the development server:
   ```powershell
   npx expo start
   ```
4. Scan the QR code with Expo Go, or press `a` (Android emulator) or `i` (iOS simulator). On a **physical iPhone**, Expo CLI and Expo Go must be signed in to the **same Expo account**: run `npx expo login` on the computer, then sign in inside Expo Go.
5. Phone and computer must be on the **same Wi-Fi**. If a router blocks it, use `npx expo start --tunnel`. It works but reloads more slowly.
6. Save a change. **Fast Refresh** updates the phone without a restart. Use `npx expo start --clear` to clear Metro's cache if the screen looks stale.

### The project folder

| File or folder | What it does | Edit it? |
|---|---|---|
| `App.tsx` (blank template) | Your first screen | Yes |
| `package.json` | Project name, scripts and dependencies | Yes, mostly through commands |
| `package-lock.json` | Exact versions installed | No, npm manages it |
| `node_modules/` | Downloaded packages (large) | Never; do not submit it |
| `app.json` | App name, icon and settings | Yes, when a package asks |
| `tsconfig.json` | TypeScript settings | Rarely |
| `assets/` | Images and icons | Yes |

`dependencies` are packages the app needs to run. `devDependencies` are tools used only while developing.

### Adding a package safely

```powershell
npx expo install expo-constants
```

`npx expo install` works like `npm install` but picks a version compatible with your Expo SDK. Plain `npm install` may pick a version your SDK does not support. If versions look wrong:

```powershell
npx expo-doctor@latest
npx expo install --check
npx expo install --fix
```

`expo-doctor` reports problems, `--check` lists out-of-date packages and `--fix` aligns them with your SDK. After installing, restart the server. Read the package's docs page for any `app.json` setting. Some packages need a development build instead of Expo Go.

### Packages this course uses

A **planning list**. Confirm each row against that module's actual imports before teaching.

| Module | Package | Install command | app.json setting or dev build? |
|---|---|---|---|
| M01–M03 | none beyond `react-native` | none | No |
| Later modules | to be confirmed from each module's imports | `npx expo install <name>` | Check each package's docs |

### Common mistakes

- Using `npm install` where `npx expo install` is needed, then getting a version mismatch.
- Phone and computer on different networks, so the QR opens but never loads.
- Editing the wrong file after choosing the default template.

## C. Analogy, Guided Program & Practice

**Analogy.** Parang karinderya: ang Node ang kalan, ang Expo ang kumpletong kitchen set, ang Metro ang tagaluto na naghahanda ng order, at ang telepono ang customer. Kapag nagbago ka ng recipe (code) at nag-save, agad nakikita ng customer ang bagong luto (Fast Refresh).

**Install first.** No extra packages for this checkpoint.

**Run it.**

```powershell
npx create-expo-app@latest my-first-app --template blank-typescript
cd my-first-app
npx expo start
```

**App.tsx** (replace the whole file)

```tsx
import { View, Text } from "react-native";

export default function App() {
  // A constant holding the text we want to show
  const greeting = "Hello, ADET!";
  return (
    // View is a container, like a div on the web
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      {/* Text shows words on screen. The braces insert the constant. */}
      <Text>{greeting}</Text>
    </View>
  );
}
```

**Expected behavior.** The phone shows "Hello, ADET!". Change the text, save, and the phone updates without a restart.

**Troubleshooting.**
- *QR opens but cannot load:* same Wi-Fi? Try `npx expo start --tunnel`.
- *Expo Go says the project is incompatible:* the project's SDK does not match your Expo Go. Install a matching Expo Go build from expo.dev/go, or recreate the project on the SDK your Expo Go supports.
- *"Unable to resolve module":* a package is missing. Run `npx expo install <name>` and restart.
- *Red type error vs red runtime error:* a type error is TypeScript warning you before running; a runtime error happens while running.
- *Screen looks stale:* save again, then `npx expo start --clear`.

## D. Assessment, Wrap-Up & References

### One individual coding activity

1. Create your own project with the blank TypeScript template and show your own greeting.
2. Add a second `Text` line with today's date using `new Date().toDateString()`.
3. Run `npx expo install expo-constants` and show it listed under `dependencies` in `package.json`.
4. **Failure case:** misspell `react-native` in the import, copy the red error message, then fix it.

Submit the modified source, the exact commands you ran, one screenshot of a successful run and the error message from step 4. Explain the line responsible for the difference.

| Evidence | Points |
|---|---:|
| Working app and independent change | 4 |
| Meaningful failure case and fix | 2 |
| Explain what each command did | 2 |
| Reproducible setup and readable source | 2 |

**Wrap-up.** Explain, in order, what happens from "Install tools" to "See change". Name the tool you would check first if the QR code opened but the app never loaded.

[Create a project](https://docs.expo.dev/get-started/create-a-project/) · [Start developing](https://docs.expo.dev/get-started/start-developing/) · [create-expo-app options](https://docs.expo.dev/more/create-expo/) · [Expo Go version mismatch](https://docs.expo.dev/troubleshooting/expo-go-version-mismatch/)

### Instructor notes

- Re-check the version note and the `blank-typescript` template's SDK on the day you teach.
- Emulators need extra setup (Android Studio or Xcode). Treat them as optional.
- Keep a spare phone or a pre-built project for students whose network blocks the QR flow.