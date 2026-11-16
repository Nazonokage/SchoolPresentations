# Android Alarms & Schedulers: Modern Background Task Scheduling

---

## A. Lesson Preview & Review

Welcome back! In previous modules, we explored how to run immediate tasks and handle system events. But what if you need an app to perform a task at a specific time in the future—even if the user isn't actively using the app or the device is asleep? 

This is where **scheduling** comes in. Android provides different APIs for different scheduling needs:
1.  **AlarmManager**: For tasks that must fire at a precise, exact time (like a calendar reminder or an alarm clock).
2.  **WorkManager**: For deferrable, guaranteed background tasks that can run at a time optimized by the system (like syncing data or uploading logs).

> **Important Note:** Modern Android development strongly favors **WorkManager** for most background tasks to protect battery life. Using `AlarmManager` for non-precise tasks is inefficient and heavily restricted.

**Learning Targets:**
By the end of this module, you will be able to:
1.  Differentiate between `AlarmManager` and `WorkManager` based on use cases.
2.  Understand the **Android 14 (API 34) exact alarm permission changes**.
3.  Implement a recurring background task using `WorkManager`.
4.  Implement a precise, one-time alarm using `AlarmManager` and `BroadcastReceiver` in a Compose app.

![Alarm and clock concept](https://images.unsplash.com/photo-1508962914676-134849a727f0?auto=format&fit=crop&q=80&w=800)

---

## B. Main Lesson

### Part 1: Choosing the Right Scheduler

| Feature | `WorkManager` | `AlarmManager` |
| :--- | :--- | :--- |
| **Primary Use Case** | Deferrable, guaranteed background work (sync, logs). | Exact-time user-facing events (alarms, reminders). |
| **Timing** | Inexact; system optimizes for battery (Doze, batching). | Can be **exact** (with permission). |
| **Guarantee** | Guarantees execution even if the app or device restarts. | Does not persist across reboots unless registered in a boot receiver. |
| **Battery Impact** | Low; respects Doze mode and batching. | High; can wake the device from Doze mode. |
| **Deprecation Status** | **Recommended** replacement for `JobScheduler`, `FirebaseJobDispatcher`, etc. | Still required for precise timing, but restricted. |

> **Pro Tip:** If your task does not *need* to run at an exact millisecond, **always use `WorkManager`**. The Android documentation explicitly recommends `AlarmManager` only for tasks that require firing at an exact time.

### Part 2: AlarmManager & The Exact Alarm Permission (Android 14+)

**`AlarmManager`** gives you a way to perform time-based operations outside the lifetime of your application. It can trigger an event even if the app is not running or the device is asleep.

#### Alarm Types
*   **`ELAPSED_REALTIME`**: Fires based on time since boot. Does not wake the device.
*   **`ELAPSED_REALTIME_WAKEUP`**: Fires based on time since boot and **wakes the device**.
*   **`RTC`**: Fires at a specific wall-clock time. Does not wake the device.
*   **`RTC_WAKEUP`**: Fires at a specific wall-clock time and **wakes the device**.

#### The Android 14 (API 34) Permission Change
Historically, apps could schedule exact alarms freely. However, to conserve battery, Google introduced the **`SCHEDULE_EXACT_ALARM`** permission in Android 12. 

> **Crucial Update:** Starting with **Android 14 (API 34)**, the `SCHEDULE_EXACT_ALARM` permission is **no longer pre-granted** to most newly installed apps targeting Android 13 or higher. It is denied by default. You must:
> 1.  Declare the permission in the manifest.
> 2.  **Check permission** using `AlarmManager.canScheduleExactAlarms()` before scheduling an exact alarm.
> 3.  Prompt the user to grant the permission in system settings if it is denied.

**Calendar and Alarm Clock Apps:** If your app's core function is being a calendar or alarm clock, you should declare the **`USE_EXACT_ALARM`** permission instead. This permission is granted automatically on install.

### Part 3: WorkManager for Recurring Background Tasks

**`WorkManager`** is a library for scheduling deferrable, guaranteed background work. It replaces older APIs like `JobScheduler` and `FirebaseJobDispatcher`. WorkManager is lifecycle-aware and handles device reboots and app restarts gracefully.

#### Key Components:
*   **`Worker`**: The class where you define the actual background task (e.g., `SendLogsWorker`).
*   **`WorkRequest`**: Defines the task. It can be a `OneTimeWorkRequest` or a `PeriodicWorkRequest`.
*   **`Constraints`**: Rules for when the work should run (e.g., `setRequiresCharging(true)` or `setRequiresNetworkType(NetworkType.CONNECTED)`).
*   **`WorkManager.enqueueUniquePeriodicWork()`**: Ensures you don't accidentally schedule duplicate tasks. It takes a unique name and an `ExistingPeriodicWorkPolicy` (like `KEEP` or `REPLACE`).

**Example: Scheduling a periodic log upload every 24 hours**
```kotlin
val sendLogsWorkRequest = PeriodicWorkRequestBuilder<SendLogsWorker>(24, TimeUnit.HOURS)
    .setConstraints(
        Constraints.Builder()
            .setRequiresCharging(true)
            .build()
    )
    .build()

WorkManager.getInstance(context).enqueueUniquePeriodicWork(
    "sendLogs",
    ExistingPeriodicWorkPolicy.KEEP,
    sendLogsWorkRequest
)
```

---

## C. Analogies and Use Cases

### Analogy: The Delivery Service vs. The Alarm Clock
*   **WorkManager (The Delivery Service):** You order a package. The company tells you it will arrive "sometime today when the truck is in your area." You don't care about the exact time, just that it arrives. This saves fuel (battery) because the truck can batch deliveries.
*   **AlarmManager (The Alarm Clock):** You have a flight to catch at 6:00 AM. You need the alarm to ring at exactly 5:00 AM. It *must* wake you up, regardless of whether you are in a deep sleep. This consumes more energy but is necessary for the exact timing.

### Real-World Use Case: The Habit Tracker
A habit tracker app uses **`WorkManager`** to sync user progress with a remote server every few hours. It doesn't matter if the sync happens at 2:00 PM or 3:00 PM, so the system batches it to save battery. However, if the user sets a daily reminder to "Drink Water," the app uses **`AlarmManager`** with `RTC_WAKEUP` to fire a notification at exactly 9:00 AM, ensuring the user is prompted on time.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   **`WorkManager`** is the modern, recommended API for deferrable, guaranteed background tasks. It replaces `JobScheduler` for most use cases.
*   **`AlarmManager`** is reserved for tasks that must fire at an exact time (alarms, calendar reminders).
*   Starting with **Android 14**, the `SCHEDULE_EXACT_ALARM` permission is denied by default. You must check `canScheduleExactAlarms()` before setting an exact alarm.
*   Always use `PendingIntent` with `FLAG_IMMUTABLE` when passing intents to `AlarmManager` for security.

### Frequently Asked Questions

**1. Why is scheduling important in Android apps?**
Scheduling allows apps to perform tasks outside their normal lifecycle, such as reminding a user of an upcoming event or syncing data in the background, without draining the battery with continuously running services.

**2. Can I still use `JobScheduler`?**
Yes, `JobScheduler` is a system service that is still supported. However, for most developers, **`WorkManager`** is the recommended abstraction layer because it automatically handles compatibility and device restarts.

**3. What is the difference between inexact and exact alarms?**
Inexact alarms (which use `set()` or `setWindow()`) allow the system to delay the alarm to save battery. Exact alarms (`setExact()` or `setExactAndAllowWhileIdle()`) fire at a precise moment but require the `SCHEDULE_EXACT_ALARM` permission (or `USE_EXACT_ALARM` for clock apps) on modern Android.

**4. How do I cancel a `PendingIntent` for an alarm?**
To cancel an alarm, you must recreate the `PendingIntent` with the same request code and intent, using the `FLAG_NO_CREATE` flag, and then pass it to `AlarmManager.cancel()`. You also need to recreate the alarm in a `BOOT_COMPLETED` receiver if you want it to persist across device restarts.

**5. What is the minimum interval for `WorkManager` periodic work?**
The minimum repeat interval for `WorkManager` is **15 minutes**. Attempting to set a shorter interval will result in the interval being clamped to 15 minutes.

---

## E. Guided Drills / Code Projects

### Skill Building Activity: Scheduling an Exact Alarm

**The Task:** Create a Compose app with a button that schedules an exact alarm to fire in 10 seconds. The alarm will trigger a `BroadcastReceiver` that shows a Toast message.

**Step 1: Update `AndroidManifest.xml`**
Declare the permission and register the receiver.

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <!-- Permission for exact alarms -->
    <uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM" />

    <application ...>
        <receiver
            android:name=".AlarmReceiver"
            android:exported="false" />
    </application>
</manifest>
```

**Step 2: Create the `AlarmReceiver`**
This is the component that gets triggered when the alarm fires.

```kotlin
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.widget.Toast

class AlarmReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context?, intent: Intent?) {
        Toast.makeText(context, "Alarm Triggered!", Toast.LENGTH_LONG).show()
    }
}
```

**Step 3: Set the Alarm in Compose**
Create a button that sets the alarm. Note the permission check.

```kotlin
import android.app.AlarmManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.os.Build
import android.os.SystemClock
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.platform.LocalContext

@Composable
fun SetAlarmButton() {
    val context = LocalContext.current

    Button(onClick = {
        val alarmManager = context.getSystemService(Context.ALARM_SERVICE) as AlarmManager

        // 1. Check for exact alarm permission (Android 12+)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
            if (!alarmManager.canScheduleExactAlarms()) {
                // Permission not granted. You should ideally prompt the user to grant it in Settings.
                // For this example, we'll just return.
                return@Button
            }
        }

        // 2. Create the PendingIntent
        val intent = Intent(context, AlarmReceiver::class.java)
        val pendingIntent = PendingIntent.getBroadcast(
            context,
            0,
            intent,
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
        )

        // 3. Set the alarm for 10 seconds from now
        val triggerTime = SystemClock.elapsedRealtime() + 10_000 // 10 seconds

        alarmManager.setExactAndAllowWhileIdle(
            AlarmManager.ELAPSED_REALTIME_WAKEUP,
            triggerTime,
            pendingIntent
        )
    }) {
        Text("Set Alarm in 10 Seconds")
    }
}
```

---

## F. Skill-Building Check

**1. Which API is the modern, recommended solution for deferrable, guaranteed background work?**
A) `AlarmManager`
B) `JobScheduler`
C) `WorkManager`
D) `FirebaseJobDispatcher`
> **Correct Answer: C** (`WorkManager` is the recommended replacement for older background scheduling APIs.)

**2. Starting with Android 14 (API 34), what happens to the `SCHEDULE_EXACT_ALARM` permission for most newly installed apps?**
A) It is granted automatically.
B) It is denied by default.
C) It is removed from the Android SDK.
D) It is replaced by `USE_EXACT_ALARM`.
> **Correct Answer: B** (The permission is no longer pre-granted and is set to denied by default.)

**3. Which alarm type would you use to wake up the device to fire an alarm at a specific wall-clock time (e.g., 8:00 AM)?**
A) `ELAPSED_REALTIME`
B) `ELAPSED_REALTIME_WAKEUP`
C) `RTC`
D) `RTC_WAKEUP`
> **Correct Answer: D** (`RTC_WAKEUP` fires at a specific time and wakes the device.)

**4. What is the primary purpose of the `AlarmManager.canScheduleExactAlarms()` method?**
A) To schedule an exact alarm.
B) To cancel an exact alarm.
C) To check if the app has permission to schedule exact alarms.
D) To check if the device is in Doze mode.
> **Correct Answer: C** (It returns a boolean indicating if the app has the `SCHEDULE_EXACT_ALARM` permission.)

**5. What is the minimum repeat interval for a `PeriodicWorkRequest` in `WorkManager`?**
A) 1 minute
B) 5 minutes
C) 15 minutes
D) 1 hour
> **Correct Answer: C** (`WorkManager` enforces a minimum interval of 15 minutes for periodic work.)

**6. True or False: `WorkManager` guarantees execution even if the app is closed or the device restarts.**
A) True
B) False
> **Correct Answer: A (True)** (`WorkManager` persists tasks across reboots and app terminations.)

**7. Which of the following is a correct use case for `AlarmManager`?**
A) Uploading logs every 24 hours.
B) Syncing a database when the network is available.
C) A user-set medication reminder at 9:00 AM sharp.
D) Downloading an image in the background.
> **Correct Answer: C** (Exact, user-facing reminders are the primary use case for `AlarmManager`.)

**8. Which flag should you always include when creating a `PendingIntent` for an alarm to prevent security vulnerabilities?**
A) `FLAG_UPDATE_CURRENT`
B) `FLAG_IMMUTABLE`
C) `FLAG_NO_CREATE`
D) `FLAG_CANCEL_CURRENT`
> **Correct Answer: B** (`FLAG_IMMUTABLE` is required from Android 12 onwards for security.)