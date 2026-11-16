# ADET M00 · What is app development?

[Module index](README.md) · Prelim · 60–90 minutes · 10-item quiz

## A. Lesson Preview & Review

**What happens between an idea and an app on someone's phone?** Learn what an app is, how apps get built, and where React Native fits.

**Learning targets.** By the end you can:
1. Define application software and application development.
2. Name the steps of building an app.
3. Compare native, cross-platform and web apps.
4. Describe the React Native layers from your code down to the phone.

By the end, trace **Idea → Design → Build → Test → Release → Update**, and explain in your own words: **shared JavaScript code supports Android and iOS, with platform-specific differences.**

## B. Detailed Main Lesson

### In plain words

An app is a program that helps a person do a job on their device, like paying a bill or checking a class schedule. Building one follows the same steps as an iterative process: understand the need, design it, build it, test it, release it, then keep fixing and improving it. This course builds phone apps with React Native, which lets you share JavaScript or TypeScript code across Android and iOS, with platform-specific differences where needed.

### Application and application development

- **Application software (app):** a program that does a specific personal, educational or business task for a user.
- **Application development:** the process of creating the program a person or business needs.
- **Mobile application development:** creating apps that run on phones and tablets, mainly **Android** and **iOS**.

Apps come in many kinds: web, desktop, enterprise, database and mobile. This course focuses on mobile.

### The steps of building an app

| Step | Question it answers | Example (campus queue app) |
|---|---|---|
| 1. Requirements | What problem are we solving? | Students waste time lining up at the registrar |
| 2. Design / prototype | What will it look like and do? | Sketch a screen with a ticket number |
| 3. Build | How do we make it real? | Write the screens in React Native |
| 4. Test | Does it work, including when things go wrong? | Try empty input, no internet |
| 5. Release | How do users get it? | App store or a shared build |
| 6. Maintain | What do we fix or add next? | Bug fixes, new features |

### Mobile platforms and three ways to build

- **Android** is an operating system made by Google, used by many manufacturers. Its apps are often written in Kotlin or Java.
- **iOS** is Apple's operating system for iPhone. Its apps are often written in Swift.

| Approach | You write | Pros | Trade-off |
|---|---|---|---|
| **Native** | Kotlin (Android) and Swift (iOS), separately | Full access to the platform | Two codebases |
| **Cross-platform** (React Native, Flutter) | Shared code, with platform-specific parts | Faster to build for both | You depend on the framework |
| **Web app** | HTML, CSS, JavaScript in a browser | No store needed | Less access to device features |

### Why React Native?

React Native uses **real native screen components**, not a web page inside an app. You write React components in JavaScript or TypeScript, and React Native turns them into native views on each platform. **Expo** is a framework and set of tools around React Native that makes setup, running and adding features much easier.

### The React Native stack

**House analogy, not a runtime-layer diagram.** The app is like a house plan, React Native coordinates its rooms and fixtures, and the operating system supplies the building site. An analogy helps us remember roles; it does not show the actual order of calls.

| Part | Actual role |
|---|---|
| Your app | Components, data and behavior written in TypeScript/JavaScript |
| Hermes | Executes JavaScript on the mobile device |
| React Native | Coordinates the component tree with platform-native views |
| Expo libraries | Provide supported native services through JavaScript APIs |
| Operating system and hardware | Supply platform UI, device capabilities and system rules |
| Metro and Expo CLI | Prepare and serve development code from the computer |

```text
COMPUTER: source → Metro prepares the JavaScript bundle
                              |
                              v
DEVICE: Hermes executes the app's JavaScript
            | calls React Native / Expo APIs
            v
        Native views and native services
            |
            v
        Android or iOS + hardware
```

Hermes is the JavaScript engine, not an AI tool. Shared source does not eliminate platform testing.

### Key terms

| Term | Meaning |
|---|---|
| SDK | Software Development Kit: the tools and libraries for building apps |
| Emulator / simulator | A virtual phone on your computer |
| Expo Go | A ready-made app that opens your project during development |
| Development build | Your own host app with the native libraries your project needs |
| App store | Where users download apps (Google Play, Apple App Store) |

### Common mistakes

- Thinking React Native mobile screens are web pages in a wrapper. The taught mobile components use native views.
- Thinking Expo and React Native are two competitors. Expo is built around React Native.
- Skipping requirements and design, then rewriting the app halfway through.

## C. Analogy, Use Case & Guided Activity

**Analogy.** Parang pagpapatayo ng bahay: kailangan muna ng plano (requirements at design), saka itatayo (build), susuriin (test), ipapakita sa may-ari (release), at aayusin kapag may sira (maintain). Ang React Native ang kontratistang kayang magtayo ng bahay sa dalawang lote (Android at iOS) gamit ang iisang plano.

**Real-world use case.** A school builds a queue-ticket app. Some students have Android phones and some have iPhones. With React Native the team writes one set of screens and ships to both.

**Guided activity (no coding, no installation).** Work in pairs with pen and paper or a shared note.

1. **Steps.** Pick an everyday app idea (for example a class-schedule app). Write one sentence for each of the six steps in the table above.
2. **Choose an approach.** Match each situation to Native, Cross-platform or Web app, and give one reason:
   - A small team needs the same app on Android and iPhone quickly.
   - An app must use a feature that exists on only one platform.
   - Users should open the app from a browser with no store download.
3. **Label the stack.** Draw the role diagram above and name one app feature, its JavaScript logic and its native view.

**Expected result.** A completed list of six steps, three matched situations with reasons, and a labeled role diagram. Suggested answers for part 2: cross-platform, native, web app.

**Class discussion.** Which step would you most likely skip, and what could go wrong if you did?

## D. Assessment, Wrap-Up & References

### 10-item quiz

1. What is application software?
   A. A program that does a specific task for a user · B. Only a game · C. Only a website · D. The operating system
2. Which step comes first when building an app?
   A. Release · B. Requirements · C. Testing · D. Maintenance
3. What is the main downside of building two separate native apps?
   A. Apps cannot be tested · B. You maintain two codebases · C. They cannot use the camera · D. Phones reject them
4. Which language is commonly used for native iOS apps?
   A. Swift · B. COBOL · C. SQL · D. PHP
5. React Native builds screens from…
   A. A web page inside an app · B. Native components · C. Only images · D. Spreadsheets
6. What does Hermes do?
   A. Draws images · B. Runs your JavaScript on the phone · C. Sells apps · D. Stores passwords
7. What is Expo?
   A. A phone operating system · B. A framework and tools built around React Native · C. A database · D. An app store
8. Which tool opens your project on a phone during development?
   A. Expo Go · B. Photoshop · C. Excel · D. An app store listing
9. Which is NOT a mobile approach in this lesson?
   A. Native · B. Cross-platform · C. Web app · D. Spreadsheet macro
10. Which step makes sure the app works when users enter empty or wrong input?
    A. Requirements · B. Design · C. Test · D. Release

**Answer key (instructor).** 1 A · 2 B · 3 B · 4 A · 5 B · 6 B · 7 B · 8 A · 9 D · 10 C

**Wrap-up.** Explain how an idea becomes an app in React Native, naming at least three steps and two parts of the runtime. Name the part you would inspect first if your JavaScript did not run.

[React Native introduction](https://reactnative.dev/docs/intro-react) · [Expo: create a project](https://docs.expo.dev/get-started/create-a-project/)

### Instructor notes

- This is an introduction. No installation or coding is needed. M01 is the first hands-on module.
- Avoid market-share statistics and "latest Android version" claims. They go out of date quickly.
- Event-driven programming is covered in a separate subject. Do not teach it here.