# Android Activities & User Interfaces

---

## A. Lesson Preview & Review

Welcome back! Today we are diving into the core of Android application development: the **Activity**. Most of your journey as an Android developer will revolve around designing, managing, and transitioning between Activities. 

> **Quick Recap:** In the previous module, you were introduced to the Android Stack and the IDE. You learned that an app is built using a combination of code and layout resources.

**Learning Targets:**
By the end of this module, you will be able to:
1. Define what an Activity is and its role in an application.
2. Identify the four main Android application components.
3. Understand and trace the modern Android Activity Lifecycle.
4. Build a basic user interface using modern tools like Jetpack Compose or traditional layouts.

![Woman ordering food on a mobile app](https://images.unsplash.com/photo-1522869635100-9f4c5e86aa37?auto=format&fit=crop&q=80&w=800)

---

## B. Main Lesson

### Activity and Application
An **Activity** is a single, focused screen with which the user can interact. It is the window where you place UI components like buttons, text boxes, and images. Think of it as a blank, transparent canvas where you paint your masterpiece. When you drag controls onto a design surface, you are dragging them onto an Activity.

An **Application** (or App) is a collection of one or more Activities. It is defined via the Android Manifest file (`AndroidManifest.xml`). An Android app is composed of four major components: **Activities**, **Services**, **Content Providers**, and **Broadcast Receivers**.

### Application Components

| Component | Description | Key Characteristics |
| :--- | :--- | :--- |
| **1. Activities** | Presents a visual UI for one focused task a user can undertake. | Single screen of UI. Each activity is isolated. Different apps can invoke activities of other apps (if permitted). |
| **2. Services** | Runs in the background for an indefinite period. | Performs long-running operations. No user interface. |
| **3. Content Providers** | Stores and retrieves data, making it accessible to all apps. | Shared set of application data (Filesystem, SQLite, Web, etc.). |
| **4. Broadcast Receivers** | Receives and reacts to broadcast announcements. | Used for alerts. Can use status bar for notification. No user interface. |

### The Activity Lifecycle
If you are familiar with C, C++, or Java, you know a program starts from the `main()` function. Similarly, the Android system initiates its program within an Activity, starting with a call to the `onCreate()` callback method. 

As a user navigates through, out of, and back into your app, the Activity instances transition through different states in their lifecycle. To manage these transitions, the `Activity` class provides six core callbacks: `onCreate()`, `onStart()`, `onResume()`, `onPause()`, `onStop()`, and `onDestroy()`.

![Android Activity Lifecycle Diagram](https://developer.android.com/static/images/activity_lifecycle.png)

**The 7 Core Callbacks:**
1.  **`onCreate()`**: Called when the activity is first created. This is where you perform setup, like initializing the UI.
2.  **`onStart()`**: Called when the activity becomes visible to the user.
3.  **`onResume()`**: Called when the user starts interacting with the application.
4.  **`onPause()`**: The paused activity does not receive user input and cannot execute any code. Called when the current activity is being paused, and the previous is resuming.
5.  **`onStop()`**: Called when the activity is no longer visible.
6.  **`onDestroy()`**: Called before the activity is destroyed by the system.
7.  **`onRestart()`**: Called when the activity restarts after being stopped.

### Activity States and App Visibility
*   **Created** (not visible yet)
*   **Started** (visible)
*   **Resumed** (visible)
*   **Paused** (partially invisible)
*   **Stopped** (hidden)
*   **Destroyed** (gone from memory)

### Activity Instance State
**State information** (e.g., a counter, user text, animation progression) is created while the activity is running. This state is lost when the device is rotated, the language changes, the back button is pressed, or the system clears memory. To save this data, you use `onSaveInstanceState()`.

---

## C. Analogies and Use Cases

### Analogy: The Theater Stage
Think of an Activity as a **stage in a theater**.
*   **`onCreate()`**: Building the set and bringing in props (setting up the UI).
*   **`onStart()`**: The curtain rises, and the audience can see the stage.
*   **`onResume()`**: The actors begin performing, and the audience is fully engaged.
*   **`onPause()`**: An actor steps off the stage for a moment, but the scene isn't over. The stage is partially obscured.
*   **`onStop()`**: The curtain falls. The audience can't see the stage anymore.
*   **`onDestroy()`**: The set is torn down, and the play is finished.

### Real-World Use Case
**Food Delivery App:** You are browsing a restaurant menu (Activity A). You tap a dish to see details (Activity B). Activity A goes to `onPause()`. When you hit the back button, Activity B is destroyed, and Activity A comes back to the foreground via `onRestart()` and `onStart()`.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   An **Activity** is a single screen with a user interface.
*   An **Application** is a collection of Activities defined in the `AndroidManifest.xml`.
*   The **Activity Lifecycle** manages how an app behaves when it moves between the foreground and background.
*   Modern Android development **highly recommends Kotlin** over Java and **Jetpack Compose** over XML layouts for building user interfaces.

### Frequently Asked Questions

**1. Why is Android so popular?**
It is free and open source. This is why many programmers develop apps for Android phones and why many phone companies use the Android OS in their products.

**2. What if I develop an app for more than one version of the Android OS? What do I need to consider?**
Develop your app using the highest API level (e.g., Android 17) to cover most existing Android smartphones. You can also design multiple types of device screens using responsive layouts.

**3. Is Java still used for Android development?**
Yes, Java is still supported. However, Google announced Kotlin as the **preferred language** for Android development in 2019. All new tools, documentation, and samples are written with Kotlin in mind.

**4. What is the latest version of Android?**
As of 2026, the latest major release is **Android 17**.

**5. What is Jetpack Compose?**
Jetpack Compose is Android's modern, **declarative UI toolkit** for building native interfaces. It simplifies and accelerates UI development on Android, replacing the traditional XML-based view system.

---

## E. Guided Drills / Code Projects

### Skill Building Activity: Creating a Login UI (Modern Approach)

While the original module used XML and Java, modern Android development uses **Jetpack Compose** and **Kotlin**. Let's build a simple login screen using the modern approach.

**Step 1: Set Up Your Project**
1. Open Android Studio and click **New Project**.
2. Choose **Empty Activity** (which uses Compose).
3. Name it `LoginApp`, choose **Kotlin** as the language, and set the Minimum SDK to API 24 (or higher).
4. Click **Finish**.

**Step 2: Write the Compose UI**
Open `MainActivity.kt`. Replace the contents with the following code to create a login form:

```kotlin
package com.example.loginapp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                LoginScreen()
            }
        }
    }
}

@Composable
fun LoginScreen() {
    var username by remember { mutableStateOf("") }
    var password by remember { mutableStateOf("") }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(text = "Login", style = MaterialTheme.typography.headlineLarge)
        Spacer(modifier = Modifier.height(16.dp))
        OutlinedTextField(
            value = username,
            onValueChange = { username = it },
            label = { Text("Enter your Username Here") }
        )
        Spacer(modifier = Modifier.height(8.dp))
        OutlinedTextField(
            value = password,
            onValueChange = { password = it },
            label = { Text("Enter your Password Here") },
            visualTransformation = PasswordVisualTransformation()
        )
        Spacer(modifier = Modifier.height(16.dp))
        Button(onClick = { /* Handle login */ }) {
            Text("LOG IN")
        }
    }
}
```

**Step 3: Run the App**
Click the **Run** button on the toolbar. Your app will launch on the emulator, showing a clean login UI built entirely with Kotlin code—no XML layout files required!

---

## F. Skill-Building Check

**1. What is an Activity in Android?**
A) A background process that fetches data.
B) A single screen with a user interface.
C) A database for storing app data.
D) A notification manager.
> **Correct Answer: B** (An Activity presents a visual UI for one focused task.)

**2. Which method is called when the activity is first created?**
A) `onStart()`
B) `onResume()`
C) `onCreate()`
D) `onDestroy()`
> **Correct Answer: C** (`onCreate()` is the first callback and performs setup.)

**3. Which of the following is NOT one of the four main Android application components?**
A) Activities
B) Services
C) Layouts
D) Broadcast Receivers
> **Correct Answer: C** (Layouts are resources, not application components. The four are Activities, Services, Content Providers, and Broadcast Receivers.)

**4. What is the modern, preferred UI toolkit for Android?**
A) XML Layouts
B) Jetpack Compose
C) JavaFX
D) React Native
> **Correct Answer: B** (Jetpack Compose is the modern declarative UI toolkit for Android.)

**5. Which language did Google announce as the preferred language for Android development?**
A) Java
B) C++
C) Kotlin
D) Python
> **Correct Answer: C** (Google announced Kotlin-first approach in 2019.)

**6. What happens when a user navigates away from an activity, making it no longer visible?**
A) `onCreate()` is called.
B) `onPause()` is called.
C) `onStop()` is called.
D) `onRestart()` is called.
> **Correct Answer: C** (`onStop()` is called when the activity is no longer visible.)

**7. What tool in Android Studio helps you debug by viewing logs?**
A) Logcat
B) Compiler
C) Emulator
D) Gradle
> **Correct Answer: A** (The Logcat window helps you debug your app by viewing logs.)

**8. What is the latest major version of Android as of 2026?**
A) Android 14
B) Android 15
C) Android 16
D) Android 17
> **Correct Answer: D** (Android 17 is the latest stable release as of 2026.)