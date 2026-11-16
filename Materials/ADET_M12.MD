Here is the updated and modernized module on Android Services, revised to reflect current best practices like WorkManager, foreground service types (Android 14), and Kotlin/Compose implementation.

---

# Android Services & Modern Background Work

---

## A. Lesson Preview & Review

Welcome! In previous modules, you learned how to build interactive UIs. However, many of the most critical tasks an app performs happen behind the scenes—syncing data, downloading files, or playing music. These long-running operations require **Services**.

> **Quick Recap:** An **Activity** is a screen with a user interface. A **Service** is a component without a UI that runs in the background to perform long-running operations, even if the user switches to another app.

**Learning Targets:**
By the end of this module, you will be able to:
1. Differentiate between **Started Services**, **Bound Services**, and **Foreground Services**.
2. Understand Android 14 (API 34) requirements for **Foreground Service Types**.
3. Know when to use **WorkManager** instead of a Service for persistent background tasks.
4. Implement a modern foreground service in Kotlin.

![Background processing concept](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&q=80&w=800)

---

## B. Main Lesson

### Understanding Android Services
A **Service** is an application component that can perform long-running operations in the background. It does not provide a user interface. Once started, a service might continue running for some time, even after the user switches to another application.

#### Types of Services
1.  **Foreground Services:** Performs an operation that is noticeable to the user (e.g., playing music, tracking a run). It **must** display a persistent notification. Modern Android enforces strict rules on these.
2.  **Background Services:** Performs operations not directly noticed by the user (e.g., syncing data). **Note:** Due to modern restrictions, background services are heavily limited. Google recommends using **WorkManager** for these tasks.
3.  **Bound Services:** Offers a client-server interface. An application component (like an Activity) binds to the service, sends requests, and receives results.

### The Modern Shift: WorkManager vs. Services
For persistent, deferrable background tasks (like uploading logs or syncing databases), **WorkManager** is the recommended solution. It handles compatibility issues and guarantees execution even if the app restarts or the device reboots. Use a Foreground Service only for tasks that must execute **immediately** and **cannot be deferred** (like music playback or navigation).

### Foreground Service Types (Android 14+)
Starting with **Android 14 (API level 34)**, you must declare a specific **Service Type** for every foreground service. This tells the system *why* your app needs to run in the background.

*   **Manifest Declaration:** You must declare the type in `AndroidManifest.xml` (e.g., `android:foregroundServiceType="mediaPlayback"`).
*   **Permissions:** You must request a specific permission for that type (e.g., `FOREGROUND_SERVICE_MEDIA_PLAYBACK`).
*   **Runtime:** Pass the type constant to `startForeground()`.

| Type | Use Case | Manifest Permission |
| :--- | :--- | :--- |
| `mediaPlayback` | Music/Video playback | `FOREGROUND_SERVICE_MEDIA_PLAYBACK` |
| `location` | GPS tracking | `FOREGROUND_SERVICE_LOCATION` |
| `dataSync` | Data upload/download | `FOREGROUND_SERVICE_DATA_SYNC` |

### The Service Lifecycle
A service has two possible paths, but a modern Foreground Service primarily follows the "Started" path.
*   **Started Service:** Started via `startService()` or `startForegroundService()`. It runs indefinitely until it calls `stopSelf()` or another component calls `stopService()`.
*   **Bound Service:** Created when a component binds to it via `bindService()`. It runs as long as components are bound to it.

> **Important:** If you start a service using `startForegroundService()`, you **must** call `startForeground()` within 5 seconds, or the system will throw a `RemoteServiceException` and crash your app.

---

## C. Analogies and Use Cases

### Analogy: The Restaurant Kitchen
*   **Activity:** The dining area where the customer interacts with the menu.
*   **Service:** The kitchen. It works behind the scenes to prepare food.
*   **Foreground Service:** A chef cooking at a live station in front of the customers. You can see what they are doing (the persistent notification), and they must keep working until the dish is done.
*   **WorkManager:** A meal prep service. You tell them to deliver meals for the week, and they figure out the best time to cook and deliver them, even if you are asleep or the restaurant is closed.

### Real-World Use Case: Music Streaming App
When a user taps "Play" and then locks their phone, the app uses a **Foreground Service** with the `mediaPlayback` type. This service continues streaming audio, updating the persistent notification with the current song, and allows the user to pause or skip tracks from the lock screen.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   **Services** run in the background without a UI.
*   **Foreground Services** are visible to the user via a persistent notification and require specific **types** (Android 14+) and permissions.
*   For deferrable background tasks, **WorkManager** is the modern, recommended replacement for background services.
*   You must call `startForeground()` within 5 seconds of starting a foreground service.

### Frequently Asked Questions

**1. Can a service continue even after the application is closed?**
Yes, a Started Service can run continuously in the background even if the app is closed or the user switches to another app.

**2. What is the difference between a Foreground and Background Service?**
A Foreground Service is actively running and shown in the notification tray, making the user aware of its operation. A Background Service runs silently but is heavily restricted by the system to save battery.

**3. How does a service manage downloads?**
For downloads, the modern approach is to use **User-Initiated Data Transfer Jobs** or **WorkManager**. If using a Foreground Service, you would call `startForeground()` with the `dataSync` type and update the notification with the progress.

**4. What happens if I don't call `startForeground()` in time?**
The Android system will throw a `RemoteServiceException` and crash your app if the 5-second window is missed.

**5. Is `startService()` deprecated?**
`startService()` still exists, but for foreground services, you should use `ContextCompat.startForegroundService()`. For background work, you should use `WorkManager`.

---

## E. Guided Drills / Code Projects

### Skill Building Activity: Implementing a Foreground Service

**The Task:** Create a simple foreground service that simulates a download and updates a notification.

**Step 1: Update `AndroidManifest.xml`**
Declare the service with its type and permissions.

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <!-- Permissions -->
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE_DATA_SYNC" />
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />

    <application ...>
        <!-- ... -->
        <service
            android:name=".MyDownloadService"
            android:exported="false"
            android:foregroundServiceType="dataSync" />
    </application>
</manifest>
```

**Step 2: Create the Service in Kotlin**
Create a new Kotlin class named `MyDownloadService.kt`.

```kotlin
import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.Service
import android.content.Intent
import android.content.pm.ServiceInfo
import android.os.Build
import android.os.IBinder
import androidx.core.app.NotificationCompat
import androidx.core.app.ServiceCompat

class MyDownloadService : Service() {

    private val CHANNEL_ID = "download_channel"
    private val NOTIFICATION_ID = 1

    override fun onCreate() {
        super.onCreate()
        createNotificationChannel()
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        // 1. Create the notification
        val notification: Notification = NotificationCompat.Builder(this, CHANNEL_ID)
            .setContentTitle("Downloading...")
            .setContentText("Your file is downloading in the background.")
            .setSmallIcon(android.R.drawable.stat_sys_download)
            .build()

        // 2. Promote to Foreground with the type
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            ServiceCompat.startForeground(
                this,
                NOTIFICATION_ID,
                notification,
                ServiceInfo.FOREGROUND_SERVICE_TYPE_DATA_SYNC
            )
        } else {
            startForeground(NOTIFICATION_ID, notification)
        }

        // 3. Simulate work (e.g., download)
        // ... (Use a coroutine or thread here)

        // 4. Stop the service when done
        // stopSelf()

        return START_NOT_STICKY
    }

    override fun onBind(intent: Intent?): IBinder? = null

    private fun createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val serviceChannel = NotificationChannel(
                CHANNEL_ID,
                "Download Channel",
                NotificationManager.IMPORTANCE_LOW
            )
            val manager = getSystemService(NotificationManager::class.java)
            manager.createNotificationChannel(serviceChannel)
        }
    }
}
```

**Step 3: Start the Service from a Compose UI**

```kotlin
import android.content.Intent
import android.os.Build
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.platform.LocalContext

@Composable
fun StartServiceButton() {
    val context = LocalContext.current
    Button(onClick = {
        val intent = Intent(context, MyDownloadService::class.java)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            context.startForegroundService(intent)
        } else {
            context.startService(intent)
        }
    }) {
        Text("Start Download Service")
    }
}
```

---

## F. Skill-Building Check

**1. Which component performs long-running operations in the background without a UI?**
A) Activity
B) Service
C) Broadcast Receiver
D) Content Provider
> **Correct Answer: B** (A Service runs in the background without a user interface.)

**2. Which API is the recommended solution for persistent, deferrable background tasks?**
A) `startService()`
B) `IntentService`
C) `WorkManager`
D) `Thread`
> **Correct Answer: C** (WorkManager is the modern recommended solution for deferrable background work.)

**3. True or False: You can start a Foreground Service from the background without restrictions on Android 12+.**
A) True
B) False
> **Correct Answer: B (False)** (Apps targeting Android 12+ are generally not allowed to start foreground services from the background, with a few specific exceptions.)

**4. What must you declare in the manifest for a Foreground Service on Android 14+?**
A) A `foregroundServiceType`
B) A `backgroundServiceType`
C) A `notificationIcon`
D) A `serviceId`
> **Correct Answer: A** (Android 14 requires declaring a `foregroundServiceType` in the manifest.)

**5. What happens if you don't call `startForeground()` within 5 seconds of starting a foreground service?**
A) The service continues as a background service.
B) The app crashes with a `RemoteServiceException`.
C) The notification is delayed.
D) The service automatically stops.
> **Correct Answer: B** (The system throws an exception and crashes the app.)

**6. Which of the following is NOT a type of Service?**
A) Started Service
B) Bound Service
C) Intent Service
D) Foreground Service
> **Correct Answer: C** (IntentService is a deprecated *base class* for a type of Started Service, not a distinct type. The modern types are Started, Bound, and Foreground.)

**7. What is the primary purpose of a Foreground Service's notification?**
A) To display ads.
B) To keep the user informed of ongoing, critical tasks.
C) To replace the app's UI.
D) To save battery.
> **Correct Answer: B** (The notification ensures the user is aware of the background operation.)

**8. Which permission is required to use a Foreground Service?**
A) `FOREGROUND_SERVICE`
B) `BACKGROUND_SERVICE`
C) `SERVICE_PERMISSION`
D) `RUN_IN_BACKGROUND`
> **Correct Answer: A** (The `FOREGROUND_SERVICE` permission is required, along with specific type permissions.)