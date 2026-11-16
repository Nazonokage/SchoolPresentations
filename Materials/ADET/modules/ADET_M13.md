# ADET M13 · Notifications and background work

[Module index](README.md) · Pre-final · 60–90 minutes · 10-item quiz

## A. Lesson Preview & Review

**Schedule a reminder, then close the screen.** Recall M12: a permission can be denied. Today the permission is for notifications, and the system, not your app, decides when work runs.

**Learning targets:** separate permission, scheduling, delivery and tap; explain what "Scheduled" does and does not prove; tell a local notification from a remote push; explain why background work is not an exact alarm.

**Trace:** Permission → Schedule → OS policy → Delivery. Explain in your own words: a permitted request shows "Scheduled"; with the app in the background, the Study break notification appears after about 10 seconds.

## B. Detailed Main Lesson

### In plain words

A local notification is a reminder your app asks the phone to show later. The student must allow notifications. When your code says "Scheduled", the phone only agreed to try. Whether and how the alert appears depends on the phone's settings, battery rules and focus mode.

| Concept | Why it exists / how it works | If misunderstood |
|---|---|---|
| Permission | The student decides whether notifications are allowed | Scheduling without asking |
| Android channel | Describes the category and importance of the alert | Alerts that are silent or missing |
| Schedule result | Acknowledges the request, not delivery | Claiming delivery from "Scheduled" |
| OS policy | The system decides when and how to show it | Expecting exact timing |
| Foreground | Needs its own handler policy to show a banner | "No banner" blamed on the code |
| Remote push | A backend sends through a push service to a device token; test in a supported development build | Expecting push to work like a local alert |
| Background task | Deferrable work the OS runs when it chooses; not an alarm | Using it for exact reminders |

```text
request permission -> schedule (10 s) -> OS decides -> banner shown -> student taps
   denied: "Reminders disabled"       "Scheduled" = request accepted only
```

**Predict first:** you press the button and keep the app open. Do you see a banner in 10 seconds? What if you background the app?

| Moment | Evidence |
|---|---|
| Permission requested | Granted or denied result |
| Scheduled | Message on screen |
| Delivered | Banner or notification shade, seen on the device |
| Tapped | A response listener fires (needs cleanup when leaving the screen) |

**Misconception:** "Scheduled means the student saw it." Each of the four moments has different evidence. Route a tap using validated notification data, because the screen may have been closed.

### Common mistakes

- Reporting success from "Scheduled".
- Skipping the Android channel.
- Using background tasks for exact-time reminders.

## C. Analogy, Guided Program & Practice

**Analogy.** Naka-schedule ang paalala. Iba pa ang tanong kung nakita ito ng student. Parang pag-set ng alarm: tumunog ba, at narinig ba niya?

**Use case:** a study-break reminder in a planner app.

**Install first (online):**

```powershell
npx expo install expo-notifications
```

Remote push needs a supported development build; check the package docs by platform. Local-notification behavior in Expo Go has not yet been tested on the course baseline.

**Run it.** Copy this lesson's complete `App.tsx` into your prepared project from M01 (replace the whole file). Run `npx tsc --noEmit`, then `npx expo start --offline` in the prepared lab or `npx expo start` while online. Metro transpiles; it does not type-check. Course versions are recorded in M01.

**Lab note.** Quiz modules do not need a delivery mode. Show this on one prepared physical device, or trace the four moments on paper.

**App.tsx — complete checkpoint** · [Copyable file](../examples/M13/App.tsx)

```tsx
import { useState } from "react";
import { View, Text, Button } from "react-native";
import * as Notifications from "expo-notifications";

export default function App() {
  const [message, setMessage] = useState("");

  async function scheduleReminder() {
    try {
      // Android needs a channel; it sets the importance of the alert
      await Notifications.setNotificationChannelAsync("study", {
        name: "Study",
        importance: Notifications.AndroidImportance.DEFAULT,
      });
      const permission = await Notifications.requestPermissionsAsync();
      if (!permission.granted) {
        setMessage("Reminders disabled");
        return;
      }
      await Notifications.scheduleNotificationAsync({
        content: { title: "Study break", body: "Review one campus task." },
        trigger: {
          type: Notifications.SchedulableTriggerInputTypes.TIME_INTERVAL,
          seconds: 10,
          channelId: "study",
        },
      });
      setMessage("Scheduled. Background the app to observe delivery.");
    } catch (error) {
      setMessage(String(error));
    }
  }

  return (
    <View style={{ flex: 1, padding: 24, paddingTop: 60, gap: 12 }}>
      <Button title="Schedule local reminder" onPress={scheduleReminder} />
      <Text>{message}</Text>
    </View>
  );
}
```

**Breakdown.** `setNotificationChannelAsync` creates the Android channel. `requestPermissionsAsync` asks the student. If denied, the screen says so and stops. Otherwise the request is scheduled with a 10-second interval on that channel and the message says "Scheduled".

**Expected behavior.** A permitted request shows Scheduled. With the app backgrounded, the Study break notification appears after the delay.

**Ungraded practice.** Keep the returned schedule ID and add a Cancel action. Compare denial, scheduling and receipt.

**Troubleshooting.** Check permission, Android channel settings, focus mode, foreground state and device support before changing the timer.

## D. Assessment, Wrap-Up & References

### 10-item quiz

Give a short answer for each item. The guided change above is ungraded.

1. What is a local notification?
2. What does remote push add?
3. Who decides when deferrable background work runs?
4. What delay does this example request?
5. What message appears when permission is denied?
6. What does "Scheduled" confirm?
7. Why might no banner appear while the app is in the foreground?
8. Why might a background task run late?
9. What should the app show when permission is denied?
10. Which facility suits an occasional maintenance job?

**Answer key (instructor).**
1. A reminder the device schedules and shows without a server.
2. A backend sender, a push service and a device token.
3. The operating system.
4. 10 seconds.
5. "Reminders disabled".
6. Only that the request was accepted, not that it was shown.
7. A foreground notification needs a handler that allows showing it.
8. The OS applies battery, network and other constraints.
9. A clear message and an alternative such as an in-app reminder list.
10. BackgroundTask / TaskManager (deferrable work), not an exact alarm.

**Wrap-up.** Explain the four moments from permission to tap and what evidence each needs. Name the layer you would inspect first if the notification never appeared.

[Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/)

### Instructor notes

Pacing: 5 review, 15 explanation, 10 demo, 25 quiz, 5 wrap-up. Replace any BackgroundFetch teaching with BackgroundTask and TaskManager. Never promise delivery timing. Device behavior is not yet recorded on the course baseline.
