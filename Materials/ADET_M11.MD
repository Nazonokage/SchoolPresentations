# Android Broadcast Receivers: System-Wide Event Handling

---

## A. Lesson Preview & Review

A mobile device relies on countless background programs to function properly. From network connectivity changes to battery alerts and SMS arrivals, the system constantly broadcasts events. To build robust applications, you need to listen for these system-wide events and react accordingly.

> **Quick Recap:** In previous modules, you learned about **Intents** (messages used to request actions). A **Broadcast Receiver** is a component that *receives* these Intents when they are broadcast by the system or other apps.

**Learning Targets:**
By the end of this module, you will be able to:
1.  Differentiate between static (manifest) and dynamic (context) receivers.
2.  Understand Android 8.0+ background execution limits and Android 14 export flag requirements.
3.  Register and unregister dynamic receivers safely using the `DisposableEffect` and `LifecycleStartEffect` APIs in Compose.
4.  Build a functional broadcast receiver that listens for system connectivity changes.

![Broadcast receiver concept illustration](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&q=80&w=800)

---

## B. Main Lesson

### What is a Broadcast?
A **Broadcast** is an Android-wide event that occurs when the device state changes (e.g., boot completes, airplane mode toggles, network connects, SMS arrives). **Broadcast Receivers** are components that allow your app to register for these events. When the event fires, the system notifies your receiver.

### Static vs. Dynamic Receivers (The Modern Reality)

| Feature | Static (Manifest) Receivers | Dynamic (Context) Receivers |
| :--- | :--- | :--- |
| **Registration** | Declared in `AndroidManifest.xml` | Registered at runtime via `registerReceiver()` |
| **Lifespan** | Works even if the app is closed (app process may be started). | Only works while the registering component (Activity/Service) is active. |
| **Android 8.0+ Restrictions** | **Highly restricted.** Apps targeting API 26+ **cannot** use manifest receivers for most *implicit* broadcasts (broadcasts not targeted specifically at your app). | **Recommended.** For most system events, you must register the receiver at runtime in code. |

> **Important:** Because of background execution limits introduced in Android 8.0 (API 26), **dynamic registration is the modern standard** for listening to system broadcasts like connectivity changes or airplane mode. Static manifest registration is reserved for a few specific exemptions (like `BOOT_COMPLETED` or `ACTION_NEW_OUTGOING_CALL`) or app-specific custom broadcasts.

### Android 14 (API 34) Runtime Export Flags
If you are targeting Android 14 (API 34) or higher, you must explicitly declare whether your dynamically registered receiver is exported to other apps on the device.

*   **`RECEIVER_EXPORTED`:** Your receiver can receive broadcasts from other apps.
*   **`RECEIVER_NOT_EXPORTED`:** Your receiver can only receive broadcasts from your own app or the system.

> **Pro Tip:** The easiest way to handle this compatibility requirement is to use `ContextCompat.registerReceiver()` from the AndroidX library, which automatically applies the correct flags based on the device's API level.

### Implementing a Receiver in Modern Jetpack Compose
In Compose, you don't have `onCreate`/`onStart`/`onStop` lifecycle methods directly in the composable. Instead, you use **Effects** to manage the receiver's lifecycle:
*   **`DisposableEffect`:** Perfect for registering the receiver when the composable enters the composition and unregistering it when it leaves.
*   **`LifecycleStartEffect`:** Ideal for pairing start/stop operations. It registers the receiver when the lifecycle hits `ON_START` and unregisters it on `ON_STOP`.

**Example: Listening for Airplane Mode Changes**

```kotlin
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.provider.Settings
import android.widget.Toast
import androidx.compose.runtime.*
import androidx.compose.ui.platform.LocalContext
import androidx.core.content.ContextCompat

@Composable
fun AirplaneModeListener() {
    val context = LocalContext.current

    // Use DisposableEffect to tie the receiver to the composable's lifecycle
    DisposableEffect(Unit) {
        val airplaneModeReceiver = object : BroadcastReceiver() {
            override fun onReceive(context: Context?, intent: Intent?) {
                if (intent?.action == Intent.ACTION_AIRPLANE_MODE_CHANGED) {
                    // Check the current state of airplane mode
                    val isAirplaneModeOn = Settings.Global.getInt(
                        context?.contentResolver,
                        Settings.Global.AIRPLANE_MODE_ON, 0
                    ) != 0

                    val message = if (isAirplaneModeOn) "Airplane Mode ON" else "Airplane Mode OFF"
                    Toast.makeText(context, message, Toast.LENGTH_SHORT).show()
                }
            }
        }

        val filter = IntentFilter(Intent.ACTION_AIRPLANE_MODE_CHANGED)

        // Register the receiver safely using ContextCompat (handles API 34 flags automatically)
        ContextCompat.registerReceiver(
            context,
            airplaneModeReceiver,
            filter,
            ContextCompat.RECEIVER_EXPORTED // Or RECEIVER_NOT_EXPORTED if only listening to your own app's broadcasts
        )

        // Cleanup block: Unregister the receiver when the composable is destroyed
        onDispose {
            context.unregisterReceiver(airplaneModeReceiver)
        }
    }
}
```

### Important System Broadcasts (Examples)
*   `android.intent.action.BATTERY_LOW`: Indicates low battery condition.
*   `android.intent.action.BOOT_COMPLETED`: System has finished booting (requires static registration).
*   `android.net.conn.CONNECTIVITY_CHANGE`: Network or Wi-Fi connection changed.
*   `android.intent.action.AIRPLANE_MODE_CHANGED`: Airplane mode switched on or off.

---

## C. Analogies and Use Cases

### Analogy: The Radio Station
Think of a **Broadcast** as a radio station transmitting a signal. A **Broadcast Receiver** is a radio tuned to that specific frequency (the `IntentFilter`). If you turn on your radio (register the receiver), you hear the broadcast. If you turn it off (unregister), you miss it. Static receivers are like a radio with an always-on alarm; dynamic receivers are like a portable radio you only turn on when you are in the room.

### Real-World Use Case: The E-Commerce App
When a user is browsing a product page and loses internet connection, you can register a dynamic receiver for `CONNECTIVITY_CHANGE`. When the broadcast fires, your receiver checks if the network is lost and displays a prominent "You are offline" banner using Compose state, preventing the user from attempting to purchase.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   **Broadcast Receivers** allow your app to listen for system-wide or app-specific events.
*   Due to **Android 8.0 (API 26)** background limits, **dynamic registration** is required for most implicit system broadcasts.
*   **Android 14 (API 34)** requires runtime receivers to specify an export flag (`RECEIVER_EXPORTED` or `RECEIVER_NOT_EXPORTED`).
*   Use `ContextCompat.registerReceiver()` for backward compatibility.
*   In **Jetpack Compose**, manage the receiver's lifecycle using `DisposableEffect` or `LifecycleStartEffect` to avoid memory leaks.

### Frequently Asked Questions

**1. Are there any changes or considerations for system broadcasts?**
Yes, as the Android platform evolves, it changes how system broadcasts behave. Apps targeting Android 8.0 (API 26) or higher can no longer declare most implicit broadcasts in the manifest. Also, apps targeting Android 14 must specify export flags for dynamically registered receivers.

**2. Why did Android 8.0 restrict implicit broadcasts?**
To improve battery life and device performance. Allowing every app to wake up in the background for every system broadcast (like connectivity changes) severely degraded battery life.

**3. What is the difference between `RECEIVER_EXPORTED` and `RECEIVER_NOT_EXPORTED`?**
`RECEIVER_EXPORTED` means your receiver can receive broadcasts from other apps. `RECEIVER_NOT_EXPORTED` means it only listens to broadcasts from your own app or the system. For system broadcasts like airplane mode, use `RECEIVER_EXPORTED`.

**4. Can I register a receiver in a Composable without `DisposableEffect`?**
Technically, you could register it in a `LaunchedEffect`, but `DisposableEffect` is specifically designed for setup and teardown logic. It guarantees the `onDispose` block runs when the composable leaves the screen, preventing `IntentReceiverLeaked` errors.

**5. Is static registration completely dead?**
No, but it is highly restricted. Static registration is still used for app-specific broadcasts, explicit broadcasts, and a small list of exempt system broadcasts (like `BOOT_COMPLETED`).

---

## E. Guided Drills / Code Projects

### Skill Building Activity: Network Connectivity Monitor

**The Task:** Create a Composable that listens for network connectivity changes and updates the UI to show whether the device is connected to Wi-Fi or Mobile Data.

**Implementation:**

```kotlin
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.net.ConnectivityManager
import android.net.NetworkCapabilities
import android.os.Build
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.core.content.ContextCompat

@Composable
fun NetworkMonitorScreen() {
    val context = LocalContext.current
    var networkStatus by remember { mutableStateOf("Checking...") }

    DisposableEffect(Unit) {
        val connectivityReceiver = object : BroadcastReceiver() {
            override fun onReceive(context: Context?, intent: Intent?) {
                if (intent?.action == ConnectivityManager.CONNECTIVITY_ACTION) {
                    val cm = context?.getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
                    val activeNetwork = cm.activeNetwork
                    val capabilities = cm.getNetworkCapabilities(activeNetwork)

                    networkStatus = when {
                        capabilities == null -> "Offline"
                        capabilities.hasTransport(NetworkCapabilities.TRANSPORT_WIFI) -> "Connected to Wi-Fi"
                        capabilities.hasTransport(NetworkCapabilities.TRANSPORT_CELLULAR) -> "Connected to Mobile Data"
                        else -> "Connected via other means"
                    }
                }
            }
        }

        val filter = IntentFilter(ConnectivityManager.CONNECTIVITY_ACTION)
        ContextCompat.registerReceiver(
            context,
            connectivityReceiver,
            filter,
            ContextCompat.RECEIVER_EXPORTED
        )

        onDispose {
            context.unregisterReceiver(connectivityReceiver)
        }
    }

    Column(
        modifier = Modifier.fillMaxSize().padding(16.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(text = "Network Status:", style = MaterialTheme.typography.headlineSmall)
        Text(text = networkStatus, style = MaterialTheme.typography.bodyLarge)
    }
}
```

---

## F. Skill-Building Check

**1. Which component allows an app to listen for system-wide events?**
A) Activity
B) Service
C) Broadcast Receiver
D) Content Provider
> **Correct Answer: C** (Broadcast Receivers are designed to respond to broadcast events.)

**2. True or False: Since Android 8.0 (API 26), apps can declare most implicit broadcasts in the manifest.**
A) True
B) False
> **Correct Answer: B (False)** (Android 8.0 restricted manifest-declared implicit broadcasts to save battery.)

**3. What must dynamically registered receivers specify when targeting Android 14 (API 34)?**
A) A security token
B) An export flag (`RECEIVER_EXPORTED` or `RECEIVER_NOT_EXPORTED`)
C) A static manifest entry
D) A background service
> **Correct Answer: B** (Android 14 requires runtime receivers to explicitly declare their export behavior.)

**4. Which Compose Effect is best suited for registering and unregistering a BroadcastReceiver?**
A) `LaunchedEffect`
B) `DisposableEffect`
C) `SideEffect`
D) `remember`
> **Correct Answer: B** (`DisposableEffect` allows you to register the receiver and clean it up in the `onDispose` block.)

**5. What is the recommended method for registering a receiver to ensure backward compatibility?**
A) `context.registerReceiver()`
B) `ContextCompat.registerReceiver()`
C) `Activity.registerReceiver()`
D) `BroadcastManager.registerReceiver()`
> **Correct Answer: B** (`ContextCompat.registerReceiver()` handles the API level differences and export flags automatically.)

**6. True or False: Registering a BroadcastReceiver in a Composable without unregistering it can lead to memory leaks.**
A) True
B) False
> **Correct Answer: A (True)** (Failing to unregister leaves the receiver attached to the context, leaking the composable or activity.)

**7. Which system broadcast is commonly exempt from the Android 8.0 implicit broadcast restrictions?**
A) `ACTION_AIRPLANE_MODE_CHANGED`
B) `CONNECTIVITY_CHANGE`
C) `BOOT_COMPLETED`
D) `ACTION_POWER_CONNECTED`
> **Correct Answer: C** (`BOOT_COMPLETED` is one of the few broadcasts that can still be received via a manifest-declared receiver.)

**8. What is the correct way to clean up a receiver in Compose?**
A) Call `unregisterReceiver()` in `onDestroy()`.
B) Call `unregisterReceiver()` in the `onDispose` block of a `DisposableEffect`.
C) Let the system clean it up automatically.
D) Call `unregisterReceiver()` in a `LaunchedEffect`.
> **Correct Answer: B** (The `onDispose` block is the correct lifecycle hook for cleanup in Compose.)