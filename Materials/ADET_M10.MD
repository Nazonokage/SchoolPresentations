Here is the updated and modernized module on Android Notifications and Dialogs, revised to reflect current best practices like runtime permissions and Jetpack Compose.

---

# Android Notifications & Dialogs: Modern Implementation

## A. Lesson Preview & Review

Have you ever used an app that felt "dead"? You tap a button, and nothing happens. You wait for a message, but no alert arrives. As a developer, you need to make your app feel alive by communicating with the user. **Notifications** and **Dialogs** are the primary tools for this.

> **Quick Recap:** In previous modules, you built UI screens (Activities/Composables) and made them interactive with event listeners. Now, we will handle asynchronous communication.

**Learning Targets:**
By the end of this module, you will be able to:
1. Understand the anatomy of an Android notification.
2. Request the `POST_NOTIFICATIONS` runtime permission (Android 13+).
3. Create and manage Notification Channels.
4. Build and display notifications using `NotificationCompat.Builder`.
5. Implement modern, state-driven dialogs using Jetpack Compose's Material 3 `AlertDialog`.

![Person using a smartphone with notification bubbles](https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&q=80&w=800)

---

## B. Main Lesson

### Part 1: Android Notifications
A **Notification** is a message that Android displays outside your app's UI. It provides the user with reminders, communication from other people, or other timely information. Users can tap the notification to open your app or take an action directly from it.

#### Modern Notification Anatomy
A standard notification is composed of three main areas:
1.  **Header Area:** Contains the app icon (small, monochrome), app name, timestamp, and an expand indicator.
2.  **Content Area:** Contains the content title, content text, and a large icon (optional).
3.  **Action Area:** Contains up to three action buttons (e.g., "Reply", "Archive") that appear when the notification is expanded.

![Notification Anatomy Diagram](https://developer.android.com/static/images/ui/notifications/notification_anatomy.png)

#### The Crucial First Step: Runtime Permissions (Android 13+)
Starting with **Android 13 (API level 33)**, apps must request the `POST_NOTIFICATIONS` runtime permission before they can send non-exempt notifications. This is a crucial change. 

1.  **Declare in Manifest:** Add `<uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>` to your `AndroidManifest.xml`.
2.  **Request in Compose:** Use `rememberLauncherForActivityResult()` with the `ActivityResultContracts.RequestPermission()` contract to prompt the user.

#### Notification Channels (Android 8.0+)
On Android 8.0 (API level 26) and higher, all notifications must be assigned to a **Channel**. A channel allows the user to control the behavior of a specific *type* of notification (e.g., "Chat messages" vs. "Promotional offers"). You must create the channel before posting any notifications.

#### Building the Notification
To ensure compatibility across all Android versions, you must use the `NotificationCompat.Builder` class from the AndroidX library, not the platform's `Notification.Builder`. 

**Key Methods:**
*   `setSmallIcon()`: Required. The icon in the status bar.
*   `setContentTitle()` / `setContentText()`: The basic text content.
*   `setContentIntent()`: A `PendingIntent` that fires when the user taps the notification.
*   `setAutoCancel(true)`: Automatically removes the notification when tapped.

---

### Part 2: Android Dialogs
A **Dialog** is a small window that prompts the user to make a decision or enter additional information. It does not fill the screen and is normally used for modal events that require users to take an action before they can proceed.

#### Modern Dialogs with Jetpack Compose
In modern Android development, you don't need to manually inflate a `DialogFragment` or use the legacy `AlertDialog.Builder`. You use the Material 3 `AlertDialog` composable. It is **state-driven**: you control its visibility by showing or hiding the composable based on a `Boolean` state variable.

**Structure of a Compose AlertDialog:**
*   `onDismissRequest`: Called when the user clicks outside the dialog or presses back.
*   `confirmButton`: The Composable for the positive action (e.g., "Yes").
*   `dismissButton`: The Composable for the negative action (e.g., "No").
*   `title` / `text`: The content of the dialog.

---

## C. Analogies and Use Cases

### Analogy: The Restaurant Pager
*   **The Notification Channel:** When you arrive at a restaurant, the host asks, "Do you want a pager for your table?" (Permission). The pager vibrates when your table is ready (Notification).
*   **The Dialog:** You are looking at the menu, and the waiter asks, "Would you like fries with that?" You must choose "Yes" or "No" before the order is placed.

### Real-World Use Case: The Messaging App
When a user receives a new message, the app checks for `POST_NOTIFICATIONS` permission. If granted, it creates a "Messages" channel and posts a notification with a `PendingIntent` to open the specific chat screen. If the user tries to exit the chat with unsent text, a `Dialog` appears asking, "Discard draft?" to prevent accidental data loss.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   **Notifications** appear outside your app's UI to provide timely information.
*   **Android 13+** requires the `POST_NOTIFICATIONS` runtime permission.
*   **Notification Channels** (Android 8.0+) allow users to manage different types of alerts.
*   Always use **`NotificationCompat.Builder`** for backward compatibility.
*   **Dialogs** are small windows for critical decisions, easily built in Compose using the `AlertDialog` composable.

### Frequently Asked Questions

**1. Can I customize the dialog?**
Yes. In Compose, you can pass any Composable to the `title`, `text`, `confirmButton`, or `dismissButton` slots, allowing for fully custom layouts with images, inputs, etc..

**2. Can I connect the dialog to a method?**
Yes. The `confirmButton` and `dismissButton` accept lambdas (`() -> Unit`), so you can directly call any function or update state when the button is clicked.

**3. Can I add an image to a dialog?**
Yes, you can include an `Image` composable inside the `text` or `title` slot of the `AlertDialog`.

**4. What happens if I don't create a Notification Channel?**
On Android 8.0 (API 26) and higher, your notification will fail to post and will not be shown to the user.

**5. How do I request the notification permission in Compose?**
Use `rememberLauncherForActivityResult()` with `ActivityResultContracts.RequestPermission()` and call `launcher.launch(Manifest.permission.POST_NOTIFICATIONS)`.

---

## E. Guided Drills / Code Projects

### Skill Building Activity: Notifications & Dialogs

**The Task:** Create an app with a button that triggers a notification and another button that shows an exit confirmation dialog.

**Implementation (Jetpack Compose):**

```kotlin
import android.Manifest
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.os.Build
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.compose.setContent
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.core.app.NotificationCompat
import androidx.core.app.NotificationManagerCompat

// 1. Define Channel Constants
const val CHANNEL_ID = "my_channel_id"
const val NOTIFICATION_ID = 1

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                MainScreen()
            }
        }
    }
}

@Composable
fun MainScreen() {
    val context = LocalContext.current
    var showExitDialog by remember { mutableStateOf(false) }

    // 2. Setup Permission Launcher
    val permissionLauncher = rememberLauncherForActivityResult(
        contract = ActivityResultContracts.RequestPermission()
    ) { isGranted ->
        if (isGranted) {
            // Permission granted, show notification
            showNotification(context)
        }
    }

    Column(
        modifier = Modifier.fillMaxSize().padding(16.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        // Button to trigger notification
        Button(onClick = {
            permissionLauncher.launch(Manifest.permission.POST_NOTIFICATIONS)
        }) {
            Text("Show Notification")
        }

        Spacer(modifier = Modifier.height(16.dp))

        // Button to trigger dialog
        Button(onClick = { showExitDialog = true }) {
            Text("Exit App")
        }
    }

    // 3. Compose Material 3 AlertDialog
    if (showExitDialog) {
        AlertDialog(
            onDismissRequest = { showExitDialog = false },
            title = { Text("Alert!") },
            text = { Text("Do you want to exit?") },
            confirmButton = {
                TextButton(onClick = {
                    showExitDialog = false
                    // In a real app, you would finish the activity here
                }) {
                    Text("Yes")
                }
            },
            dismissButton = {
                TextButton(onClick = { showExitDialog = false }) {
                    Text("No")
                }
            }
        )
    }
}

// 4. Notification Helper Functions
fun showNotification(context: Context) {
    createNotificationChannel(context)

    // Create an explicit intent for an Activity (e.g., MainActivity)
    val intent = Intent(context, MainActivity::class.java).apply {
        flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
    }
    val pendingIntent: PendingIntent = PendingIntent.getActivity(
        context, 0, intent, PendingIntent.FLAG_IMMUTABLE
    )

    // Build the notification
    val builder = NotificationCompat.Builder(context, CHANNEL_ID)
        .setSmallIcon(android.R.drawable.ic_dialog_info) // Use a real drawable in production
        .setContentTitle("My notification")
        .setContentText("Hello World!")
        .setPriority(NotificationCompat.PRIORITY_DEFAULT)
        .setContentIntent(pendingIntent)
        .setAutoCancel(true)

    // Show the notification (with permission check)
    with(NotificationManagerCompat.from(context)) {
        if (androidx.core.content.ContextCompat.checkSelfPermission(
                context, Manifest.permission.POST_NOTIFICATIONS
            ) != android.content.pm.PackageManager.PERMISSION_GRANTED
        ) {
            return@with
        }
        notify(NOTIFICATION_ID, builder.build())
    }
}

fun createNotificationChannel(context: Context) {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
        val name = "My Channel"
        val descriptionText = "Channel Description"
        val importance = NotificationManager.IMPORTANCE_DEFAULT
        val channel = NotificationChannel(CHANNEL_ID, name, importance).apply {
            description = descriptionText
        }
        val notificationManager: NotificationManager =
            context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        notificationManager.createNotificationChannel(channel)
    }
}
```

---

## F. Skill-Building Check

**1. What permission is required to send notifications on Android 13 (API 33) and higher?**
A) `SEND_NOTIFICATIONS`
B) `POST_NOTIFICATIONS`
C) `NOTIFICATION_PERMISSION`
D) `ALERT_WINDOW`
> **Correct Answer: B** (Android 13 introduced the `POST_NOTIFICATIONS` runtime permission.)

**2. Which class should you use to build notifications for maximum backward compatibility?**
A) `Notification.Builder`
B) `NotificationManager`
C) `NotificationCompat.Builder`
D) `NotificationChannel`
> **Correct Answer: C** (Always use `NotificationCompat.Builder` from the AndroidX library to handle differences across Android versions.)

**3. True or False: You must create a Notification Channel on Android 8.0 (API 26) and higher before posting a notification.**
A) True
B) False
> **Correct Answer: A (True)** (Notifications will fail to post if a channel is not created on API 26+.)

**4. In Jetpack Compose, which component is used to create a modal dialog?**
A) `DialogFragment`
B) `AlertDialog.Builder`
C) `AlertDialog` composable
D) `ModalBottomSheet`
> **Correct Answer: C** (The Material 3 `AlertDialog` composable is the modern way to create dialogs in Compose.)

**5. Which parameter of `NotificationCompat.Builder` sets the action when a user taps the notification?**
A) `setAction()`
B) `setContentIntent()`
C) `setTapAction()`
D) `setPendingIntent()`
> **Correct Answer: B** (`setContentIntent()` accepts a `PendingIntent` that fires when tapped.)

**6. What is the purpose of `setAutoCancel(true)` in a notification?**
A) It prevents the notification from showing.
B) It removes the notification automatically when the user taps it.
C) It hides the notification after 5 seconds.
D) It requires no permissions.
> **Correct Answer: B** (`setAutoCancel(true)` dismisses the notification upon user interaction.)

**7. In a Compose `AlertDialog`, which parameter is used to handle clicks outside the dialog or back presses?**
A) `onDismissRequest`
B) `confirmButton`
C) `dismissButton`
D) `title`
> **Correct Answer: A** (`onDismissRequest` is called when the user tries to dismiss the dialog without a button press.)

**8. Which of the following is NOT part of a standard notification's anatomy?**
A) Small icon
B) App name
C) Timestamp
D) App's main activity layout
> **Correct Answer: D** (The notification anatomy includes the header, content, and action areas, not the app's underlying Activity layout.)