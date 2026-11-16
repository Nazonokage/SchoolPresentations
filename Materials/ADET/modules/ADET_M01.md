# ADET M01 · React Native platform, tools and your first app

[Module index](README.md) · Prelim · 60–90 minutes · Individual coding activity

> **Tested course baseline — November 6–7, 2026:** Expo SDK 58 (expo 58.0.23), React Native 0.88.1, React 19.3.0, TypeScript 6.0.3, Node 24.18.1 and npm 11.16.0. Use the prepared starter and lockfile. Local compilation/bundling passed; native-device and phone-network checks remain pending.

## A. Lesson Preview & Review

**Can you go from an empty folder to a running app on your phone?** Learn what each tool does, create a project, run it, change a calculation and explain its result.

**Learning targets.**
1. Install and check the tools you need.
2. Create and run an Expo project.
3. Read the project folder and `package.json`.
4. Trace variables, conditions, loops and a function using a baon calculation.

By the end, trace **Install tools → Create project → Start server → Open on phone → Edit → See change**, and explain in your own words: the app displays a greeting and the calculated balance after your edit.

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
   > A Router-based template uses route files rather than this course's App.tsx entry. If a student accidentally chooses it, create the course blank-typescript project instead of guessing where this checkpoint belongs.
2. Open `package.json` and read the `"expo"` version (the course baseline is `58.0.23`). Your Expo Go app must support that SDK.
3. Start the development server:
   ```powershell
   npx expo start
   ```
4. Scan the QR code with Expo Go, or press `a` (Android emulator) or `i` (iOS simulator). Follow the installed client’s sign-in prompt if one appears; verify access on the actual phone before class.
5. Phone and computer must be on the **same Wi-Fi**. **Online fallback only:** `npx expo start --tunnel` requires internet on both devices and tunnel tooling. It is not an offline-lab workaround. For the prepared lab use `npx expo start --offline` on a working local network.
6. Save a change. **Fast Refresh** usually updates the development screen; some edits trigger a remount or reload. Use `npx expo start --clear` to clear Metro's cache if the screen looks stale.

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

### Read the baon program before typing

| Concept | What / why | How this example works | What goes wrong |
|---|---|---|---|
| `const` / `let` | Name values; use let when reassignment is needed | prices stays assigned to one array; remaining changes | Reassigning a const is invalid; const does not freeze an array |
| Function | Reuse a calculation with an input and result | calculateBalance receives budget and returns remaining | Forgetting return gives undefined instead of a balance |
| Loop | Apply a step to each item | Subtract each price once | Subtracting the total again double-counts spending |
| Condition | Select one result | balance >= 0 chooses Change; otherwise Kulang | Using > would classify a zero balance incorrectly |
| Type annotation | Check a value's expected type separately | budget: number rejects a string during tsc checking | Metro may still transpile code containing type errors |

**Misconception:** TypeScript validates every real-world input at runtime. Its types help check source code; actual external data still needs validation.

### Common mistakes

- Using `npm install` where `npx expo install` is needed, then getting a version mismatch.
- Phone and computer on different networks, so the QR opens but never loads.
- Editing the wrong file after choosing the default template.

## C. Analogy, Guided Program & Practice

**Analogy.** Parang karinderya: ang Node ang kalan, ang Expo ang kumpletong kitchen set, ang Metro ang tagaluto na naghahanda ng order, at ang telepono ang customer. Kapag nagbago ka ng recipe (code) at nag-save, agad nakikita ng customer ang bagong luto (Fast Refresh).

**Real-world use case.** A student checks whether today's baon covers two purchases. The screen explains a shortage instead of treating a negative number as a crash.

### Core dependency check

| Import / tool | Prepared source | Extra install / permission / plugin |
|---|---|---|
| react | Blank template; component state/effects where used | None |
| react-native | Blank template; native views and built-in APIs | None |
| TypeScript / Expo CLI | Prepared dev toolchain | None during offline class |

Core entry: index.ts → App.tsx. Compatible Expo Go can host these APIs; perform the actual native-client smoke test before class. This does not certify the phone/network route.

**Install first.** No extra packages for the lab checkpoint. expo-constants is optional online homework only, and is not installed in the offline starter.

**Fresh-project command (online preparation on your own laptop):**

```powershell
npx create-expo-app@latest ADET-M01-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M01-LASTNAME
npx tsc --noEmit
npx expo start
```

Metro transpiles; run `npx tsc --noEmit` separately after replacing App.tsx. In the prepared offline starter use `npx expo start --offline`. Bring that prepared laptop next meeting.

**Run it.** Copy the complete App.tsx below into that project, then repeat `npx tsc --noEmit` and start Expo. The type check must happen after your code changes.

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

**Expected behavior.** The phone shows "Hello, ADET!" and "Kulang: PHP 10". Change the text, save, and Fast Refresh normally updates the development screen.

**Troubleshooting.**
- *QR opens but cannot load:* same Wi-Fi? An online-only alternative is `npx expo start --tunnel`; it needs internet and tunnel tooling.
- *Expo Go says the project is incompatible:* the project's SDK does not match your Expo Go. Ask the instructor to check the actual client against the SDK 58 baseline using expo.dev/go. Physical iOS devices cannot be assumed to install arbitrary older Expo Go versions. Do not change the course SDK independently.
- *"Unable to resolve module":* a package is missing. For this core checkpoint, check the import spelling and prepared dependencies first. Extra packages require online preparation, not an unplanned lab download.
- *Red type error vs red runtime error:* run `npx tsc --noEmit` to check types separately. Metro transpiles the code; it does not type-check. A runtime error happens while the app executes.
- *Screen looks stale:* save again, then `npx expo start --clear`.

## D. Assessment, Wrap-Up & References

### One individual coding activity

1. Create your own project with the blank TypeScript template and show your own greeting.
2. Change the budget to 80 and add a third price of 15. Show the resulting balance and explain each subtraction. Also test a budget equal to total spending.
3. Run `npx tsc --noEmit` and explain how this check differs from starting Metro.
4. **Failure case:** misspell `react-native` in the import, copy the red error message, then fix it.

Submit the modified source, the exact commands you ran, one screenshot of a successful run and the error message from step 4. Explain the line responsible for the difference.

| Evidence | Points |
|---|---:|
| Working app and independent change | 4 |
| Meaningful failure case and fix | 2 |
| Explain what each command did | 2 |
| Reproducible setup and readable source | 2 |

### Three equal-point delivery modes

**Mode 1 — Offline computer lab.** Before class, PCs need Node 24.18.1, npm 11.16.0, VS Code and a separate copy of the prepared starter including node_modules. Use `START-LAB.cmd`; replace only the student's App.tsx. No new installs in class. Local type-checking and Android bundling passed; a reachable phone on local Wi-Fi with compatible Expo Go or a prepared emulator still needs a successful [smoke test](../offline-lab/SMOKE-TEST.md). If no native display route passes, use Mode 3, not an untested promise of offline phone access. `--tunnel` is an online fallback only.

**Mode 2 — Prepared personal laptop.** Follow the announcement below before class; bring your laptop and run the same activity during the next scheduled coding meeting. Submit source, package.json, lockfile, README with commands and the actual activity date, success/failure evidence and a brief explanation. Recommended repository: `ADET-M01-LASTNAME` (instructor confirms the pattern). Do not upload node_modules, cache or secrets.

**Mode 3 — Written alternative (10 points).** Trace budgets 50, 60 and 80 with prices 25 and 35; then add price 15. Identify the loop, condition, function input/return and a type-error correction. Submit a step-by-step table plus a 150–250-word explanation. This earns the same maximum as the coding activity; no device screenshot is required.

| Written evidence | Points |
|---|---:|
| Correct complete trace and proposed independent change | 4 |
| Edge/failure case and justified correction | 2 |
| Explanation connecting code to visible behavior | 2 |
| Labeled inputs, ordered steps and readable evidence | 2 |

Guided copying and predictions are ungraded. Only the one selected assessment mode is graded.

**Wrap-up.** Explain, in order, what happens from "Install tools" to "See change". Name the tool you would check first if the QR code opened but the app never loaded.

[Create a project](https://docs.expo.dev/get-started/create-a-project/) · [Start developing](https://docs.expo.dev/get-started/start-developing/) · [create-expo-app options](https://docs.expo.dev/more/create-expo/) · [Expo Go version mismatch](https://docs.expo.dev/troubleshooting/expo-go-version-mismatch/)

### Instructor notes

**60-minute pacing:** 5 review, 15 explanation, 10 guided program, 25 individual activity, 5 wrap-up. Use the additional 30 minutes for support and deeper traces, not another graded task.

Environment evidence: [stop-1 report](../instructor/stop1-2026-11-06/REPORT.md). SDK support was checked using store metadata separately from create-expo-app; --no-agents-md succeeded for both tested templates. The optional expo-constants exploration is not assessed.

- Re-check the version note and the `blank-typescript` template's SDK on the day you teach.
- Emulators need extra setup (Android Studio or Xcode). Treat them as optional.
- Keep a spare phone or a pre-built project for students whose network blocks the QR flow.

**Teaching evidence:** keys and grading guidance are in [the separate instructor key](../instructor/OPENER_ANSWER_KEY.md). Use the local flow diagram beside the matching code; no external image download is required. Record actual hardware outcomes rather than treating expected output as a measured device result.

**Instructor scheduling note:** reuse the following preparation block at the end of the meeting BEFORE this coding activity. It is included here as the activity's setup handout.

### Before next meeting — M01 preparation handout (send before this lesson)

For the upcoming **M01 coding meeting**, prepare **your own laptop**, then bring it and do the activity in class. The instructor confirms the date and naming pattern; `ADET-M01-LASTNAME` is the recommended folder/repository name.

```powershell
npx create-expo-app@latest ADET-M01-LASTNAME --template blank-typescript@sdk-58 --no-agents-md
cd ADET-M01-LASTNAME
npx tsc --noEmit
npx expo start
```

No extra packages are needed for this core activity. Use the distributed manifest and lockfile for exact versions. Open the app once before class; bring a screenshot or the exact error. Without home internet, prepare on campus Wi-Fi, mobile data or an agreed hotspot, or copy the [prepared starter and dependencies by USB](../offline-lab/README.md). Internet preparation is not the graded activity. Put this announcement on the **last presentation slide of the previous meeting**; the teacher supplies the real meeting date.
