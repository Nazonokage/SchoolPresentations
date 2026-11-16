# ADET M01 · React Native platform, tools and your first app

[Module index](README.md) · Prelim · 60–90 minutes · Individual coding activity

> **Course baseline — 2026-11-06.** Use Expo SDK 58, React 19.3.0, React Native 0.88.1 and TypeScript 6.0.3. The prepared starter pins exact direct versions and includes a lockfile. Preparation host: Node 24.18.1, npm 11.16.0. Explicit sdk-57 scaffolding produced SDK 57; plain blank-typescript produced SDK 58. --no-agents-md worked with both. Live Android and iOS store metadata identified Expo Go 58.0.5; Apple explicitly states SDK 58 support. Store compatibility is checked independently of project creation. Native-device and phone-LAN tests remain pending; see the stop-1 report.

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

Your computer runs a small server. Your phone opens the app from that server. Fast Refresh usually updates the development app after saving; some edits remount components or reload the app. Expo handles the hard setup so you can focus on writing the app.

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
   npx create-expo-app@latest ADET-M01-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
   cd ADET-M01-LASTNAME
   ```
   > The **default** template uses file-based routing and its first screen is `src/app/index.tsx`, with no `App.tsx`. If a student accidentally chooses it, create the course blank-typescript project instead of guessing where this checkpoint belongs.
2. Open `package.json` and read the `"expo"` version (the course baseline is `58.0.23`). Your Expo Go app must support that SDK.
3. Start the development server:
   ```powershell
   npx expo start
   ```
4. Scan the QR code with Expo Go, or press `a` (Android emulator) or `i` (iOS simulator). Follow the installed client’s sign-in prompt if one appears; verify access on the actual phone before class.
5. Phone and computer must be on the **same Wi-Fi**. **Online fallback only:** `npx expo start --tunnel` requires internet on both devices and tunnel tooling. It is not an offline-lab workaround. For the prepared lab use `npx expo start --offline` on a working local network.
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

### Optional online homework: adding a package safely

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

**Install first.** No extra packages for the lab checkpoint. expo-constants is optional online homework only, and is not installed in the offline starter.

**Fresh-project command (online preparation on your own laptop):**

```powershell
npx create-expo-app@latest ADET-M01-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M01-LASTNAME
npx tsc --noEmit
npx expo start
```

Metro transpiles; run `npx tsc --noEmit` separately after replacing App.tsx. In the prepared offline starter use `npx expo start --offline`. Bring that prepared laptop next meeting.

**Run it.**

```powershell
npx create-expo-app@latest ADET-M01-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M01-LASTNAME
npx tsc --noEmit
npx expo start
```

**App.tsx** (replace the whole file)

```tsx
import { View, Text } from "react-native";

export default function App() {
  const greeting = "Hello, ADET!"; // Constant: a name for a value.
  const prices = [25, 35];
  function calculateBalance(budget: number) {
    let remaining = budget; // Variable: updated as each price is paid.
    for (const price of prices) {
      remaining -= price; // Loop: apply the same step to every price.
    }
    return remaining; // Function: return the result to its caller.
  }
  const balance = calculateBalance(50);
  let message: string;
  if (balance >= 0) {
    message = "Change: PHP " + balance;
  } else {
    message = "Kulang: PHP " + Math.abs(balance);
  }
  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Text>{greeting}</Text>
      <Text>{message}</Text>
    </View>
  );
}
```

### Compact JavaScript refresher: trace the baon

A constant names a value; a variable holds a changing value. A loop repeats a step for each price. A function accepts a budget and returns the balance. A condition chooses the message.

**Predict first:** With PHP 50 and prices 25 and 35, will there be change or a shortage?

| Step | Calculation | remaining |
|---|---|---:|
| Start | budget | 50 |
| First price | 50 - 25 | 25 |
| Second price | 25 - 35 | -10 |
| Condition | -10 >= 0 is false | Show Kulang: PHP 10 |

Changing the budget to 80 produces Change: PHP 20. A negative balance is a valid calculation here, not a program crash.

**Expected behavior.** The phone shows "Hello, ADET!". Change the text, save, and the phone updates without a restart.

**Troubleshooting.**
- *QR opens but cannot load:* same Wi-Fi? An online-only alternative is `npx expo start --tunnel`; it needs internet and tunnel tooling.
- *Expo Go says the project is incompatible:* the project's SDK does not match your Expo Go. Install a matching Expo Go build from expo.dev/go, or recreate the project on the SDK your Expo Go supports.
- *"Unable to resolve module":* a package is missing. Run `npx expo install <name>` and restart.
- *Red type error vs red runtime error:* run `npx tsc --noEmit` to check types separately. Metro transpiles the code; it does not type-check. A runtime error happens while the app executes.
- *Screen looks stale:* save again, then `npx expo start --clear`.

## D. Assessment, Wrap-Up & References

### One individual coding activity

1. Create your own project with the blank TypeScript template and show your own greeting.
2. Add a second `Text` line with today's date using `new Date().toDateString()`.
3. Run `npx tsc --noEmit` and explain how this check differs from starting Metro.
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