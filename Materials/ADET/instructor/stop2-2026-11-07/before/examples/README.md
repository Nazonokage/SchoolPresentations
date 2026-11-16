# Running the ADET labs
Use Node LTS supported by your Expo SDK, npm, an editor and a phone or emulator. The project uses the published blank TypeScript template dependency family for SDK 58. Check the phone’s installed Expo Go SDK before class. When the native runtime differs, install a compatible classroom client or prepare a development build with the same native dependencies. [Expo setup](https://docs.expo.dev/get-started/create-a-project/)

From this examples folder in PowerShell run:

```powershell
cd mobile
npm ci
cd ..
node select.mjs 01
cd mobile
npm start -- --clear
```

Open the QR code in the compatible client on the same reachable network. Selecting a lesson replaces the working App.tsx and entry file. Save student edits to a separate folder before switching. Stop Metro first. Module 5 selects its Router entry and route files. Module 15 copies the bundled original WAV cue. Installed libraries alone do not add native functionality to an existing client.

For modules 7, 8, 10, 16 and 18, follow [API setup](api/README.md). Put EXPO_PUBLIC_API_URL in mobile/.env.local, for example http://192.168.1.20:8000 with your actual PC address. Restart Metro after changing it. Every student should use a private lab dataset. Module 16 also demonstrates the offline path. Module 11 is a local session teaching model, with real authorization discussed in the lesson. Modules 12–15 need platform checks on physical devices.

Save a copy of a working checkpoint for students who missed a previous meeting. Set up packages and the API before class. Students can then spend the meeting reading, running and modifying the program.
