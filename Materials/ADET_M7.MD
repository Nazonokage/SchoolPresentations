Here is the updated and modernized version of Module 7, revised to align with current Android development standards.

---

# Android Intents & Modern App Navigation

---

## A. Lesson Preview & Review

In previous modules, you built single-screen applications and made them interactive. But modern apps are rarely static; they are dynamic and responsive, often requiring multiple screens. How do apps move from a login screen to a profile screen, and how is data passed between them?

Historically, **Intents** were the primary mechanism for both navigating within an app and communicating with other apps. Today, the landscape has evolved. While Intents are still crucial for inter-app communication, Google now recommends using the **Jetpack Navigation Component** (specifically Navigation Compose) for navigating between screens within your own app.

> **Quick Recap:** An **Activity** represents a single screen. An **Application** is a collection of Activities. Moving between these screens requires a structured navigation approach.

**Learning Targets:**
By the end of this module, you will be able to:
1. Understand the role of Intents for inter-app communication.
2. Differentiate between Explicit and Implicit Intents.
3. Implement modern in-app navigation using Jetpack Navigation Compose.
4. Use the Activity Result API to receive data back from another screen or app.

![Navigating between app screens](https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&q=80&w=800)

---

## B. Main Lesson

### Understanding Android Intents
An **Intent** is a messaging object you can use to request an action from another app component. Think of it as a "blast email" to the Android system: you state what you want to do, and the system finds the right component to handle it. There are three fundamental use cases:
1.  **Starting an activity:** Launching a new screen.
2.  **Starting a service:** Performing an operation in the background.
3.  **Delivering a broadcast:** Sending a message that any app can receive.

#### Intent Structure
An Intent consists of primary and secondary attributes:
*   **Action:** The general action to be performed (e.g., `ACTION_VIEW`, `ACTION_SEND`).
*   **Data:** The data to operate on, expressed as a `Uri` (e.g., a web URL).
*   **Category, Type, Component, Extras:** Secondary attributes that provide more context or carry additional data (like a Bundle of strings).

#### Types of Intents
1.  **Explicit Intents:** Specify the exact target component by its class name. You typically use these to start components within your own app, as you know the class name of the activity you want to launch.
2.  **Implicit Intents:** Do not name a specific component but declare a general action. The Android system resolves this by searching for an app on the device that can handle the action. For example, `ACTION_VIEW` with a web URL will open a web browser.

> **Modern Shift:** With Jetpack Compose, explicit intents are rarely used for in-app navigation because the **Navigation Component** handles it more efficiently. Explicit intents are still used for cross-app deep links or launching system components.

---

### The Activity Result API (Modern Result Handling)
When you launch another activity (or another app, like the Camera), you often need a result back. The old methods `startActivityForResult()` and `onActivityResult()` are **deprecated** because they struggle with lifecycle issues and memory constraints.

The modern approach is the **Activity Result API**. It decouples the result callback from the place where you launch the activity, ensuring it can survive configuration changes.

*   **In Compose:** You use `rememberLauncherForActivityResult()` to get a result. This API registers a callback and provides a launcher to trigger the action, making it lifecycle-aware and easy to use in a declarative UI.

```kotlin
// Modern Compose Activity Result Example
val launcher = rememberLauncherForActivityResult(
    contract = ActivityResultContracts.GetContent()
) { uri: Uri? ->
    // Handle the returned Uri (e.g., display the selected image)
}

// Trigger the launcher
Button(onClick = { launcher.launch("image/*") }) {
    Text("Load Image")
}
```

---

### Modern Multi-Screen Navigation with Jetpack Compose
**Navigation Compose** is the modern, declarative API for navigating between composables (screens) in a Compose app. It is the recommended approach for building multi-screen apps.

#### Key Concepts:
*   **`NavHost`:** A composable that defines a navigation graph. It acts as a container that maps routes (destinations) to specific composable functions.
*   **`NavController`:** The central navigation object. It allows you to orchestrate transitions, handle the back stack, and pass data between screens.

#### How It Works:
1.  **Define a Route:** Routes are usually defined as serializable objects or strings.
2.  **Set up a NavHost:** Inside your `NavHost`, you declare a `composable` block for each screen, specifying its route and the UI content.
3.  **Navigate:** You call `navController.navigate(route)` to move to a new screen.

```kotlin
// Modern Navigation Compose Example
@Composable
fun MyAppNavHost(navController: NavHostController) {
    NavHost(navController, startDestination = "home") {
        composable("home") {
            HomeScreen(onNavigateToProfile = { navController.navigate("profile") })
        }
        composable("profile") {
            ProfileScreen(onNavigateBack = { navController.popBackStack() })
        }
    }
}
```

---

### The Evolution of Fragments
Historically, **Fragments** represented a reusable portion of an app's UI. They allowed you to build multi-pane layouts (like a master-detail view on a tablet) within a single Activity.

> **Important Modern Context:** In a **Compose-first architecture**, the recommended end goal is to **replace Fragments entirely** with screen-level composables managed by Navigation Compose. While Fragments are still supported (and you can use Compose inside a Fragment), new apps should not be built using Fragments. They are considered legacy View-system components.

---

## C. Analogies and Use Cases

### Analogy: The Hotel Reception
*   **Intent:** You walk up to the receptionist and say, "I'd like to order room service." You don't know who the chef is or how the kitchen works; you just state your request. The system finds the right person to fulfill it.
*   **Explicit Intent:** You say, "I need to speak to John Smith in Room 204." You are targeting a specific person (class).
*   **Implicit Intent:** You say, "Can someone help me with my luggage?" The system finds whoever is available and capable of handling that task.

### Real-World Use Case: The Social Media App
*   **Sharing a Post (Implicit Intent):** A user taps "Share." The app creates an `ACTION_SEND` intent with the image data. The Android system presents a chooser showing WhatsApp, Gmail, Instagram, etc.
*   **Navigating to Profile (Navigation Compose):** A user taps their avatar. Instead of an Intent, the `NavController` navigates to the `ProfileScreen` composable route.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   **Intents** are messaging objects used to request actions from other apps or components.
*   **Explicit Intents** target a specific class; **Implicit Intents** declare a general action for the system to resolve.
*   The **Activity Result API** is the modern replacement for the deprecated `startActivityForResult` for handling results.
*   **Navigation Compose** is the modern, declarative way to navigate between screens within a Compose application, replacing Fragments.

### Frequently Asked Questions

**1. What is the difference between an Intent and Navigation Compose?**
Use **Intents** to communicate with external apps or system components (e.g., sharing, opening a camera). Use **Navigation Compose** to move between screens *inside* your own app.

**2. Can I still use Fragments?**
Yes, you can, especially in older codebases. However, for new development, Google recommends using screen-level Composables managed by Navigation Compose.

**3. How do I pass data with Navigation Compose?**
You pass data by adding arguments to your routes (e.g., `"profile/{userId}"`) and retrieving them from the `NavBackStackEntry` in the destination composable.

**4. What is a `NavController`?**
It is the central object in Navigation Compose that allows you to navigate between destinations, handle the back stack, and observe navigation state.

**5. Why was `startActivityForResult` deprecated?**
It had lifecycle issues and was prone to errors when the activity or process was destroyed while waiting for a result. The Activity Result API is lifecycle-aware and more robust.

---

## E. Guided Drills / Code Projects

### Skill Building Activity: Multi-Screen Navigation

**The Task:** Create an app with two screens: a Home screen and a Profile screen. Use Navigation Compose to navigate between them.

**Implementation (Jetpack Compose):**

```kotlin
import androidx.compose.material3.*
import androidx.navigation.compose.*

@Composable
fun NavigationExample() {
    // 1. Create a NavController
    val navController = rememberNavController()

    // 2. Set up the NavHost
    NavHost(navController = navController, startDestination = "home") {
        composable("home") {
            HomeScreen(
                onNavigateToProfile = { navController.navigate("profile") }
            )
        }
        composable("profile") {
            ProfileScreen(
                onNavigateBack = { navController.popBackStack() }
            )
        }
    }
}

@Composable
fun HomeScreen(onNavigateToProfile: () -> Unit) {
    Column {
        Text("Home Screen")
        Button(onClick = onNavigateToProfile) {
            Text("Go to Profile")
        }
    }
}

@Composable
fun ProfileScreen(onNavigateBack: () -> Unit) {
    Column {
        Text("Profile Screen")
        Button(onClick = onNavigateBack) {
            Text("Go Back")
        }
    }
}
```

---

## F. Skill-Building Check

**1. What is the primary modern use case for Intents in Android development?**
A) In-app screen navigation.
B) Inter-app communication and system actions.
C) Managing Activity lifecycle.
D) UI layout positioning.
> **Correct Answer: B** (While Intents can launch activities within the same app, their primary modern role is for cross-app communication, sharing, and system actions.)

**2. Which Intent type specifies the exact target component by its class name?**
A) Implicit Intent
B) Explicit Intent
C) Broadcast Intent
D) System Intent
> **Correct Answer: B** (Explicit Intents explicitly name the target component class.)

**3. What is the modern replacement for `startActivityForResult()`?**
A) `ActivityResultLauncher`
B) `rememberLauncherForActivityResult()`
C) The Activity Result API
D) All of the above
> **Correct Answer: D** (All of these are part of the modern Activity Result API ecosystem.)

**4. In Navigation Compose, what component acts as a container for mapping routes to screens?**
A) `NavController`
B) `NavHost`
C) `NavGraph`
D) `Route`
> **Correct Answer: B** (`NavHost` is the composable that defines the navigation graph.)

**5. What is the recommended modern replacement for Fragments in new app development?**
A) Multiple Activities.
B) Screen-level Composables managed by Navigation Compose.
C) WebViews.
D) DialogFragments.
> **Correct Answer: B** (Fragments are legacy; the modern standard is to use Composables for screens.)

**6. True or False: You need an Intent to navigate between two Composable screens in a Compose app.**
A) True
B) False
> **Correct Answer: B (False)** (You use the Navigation Component's `NavController` to navigate between Composable destinations, not Intents.)

**7. What is the purpose of `rememberLauncherForActivityResult()`?**
A) To remember the last Intent used.
B) To launch an activity and handle its result in a lifecycle-aware way within a Composable.
C) To create a new Activity.
D) To manage the back stack.
> **Correct Answer: B** (It provides a launcher for an activity result and a callback to handle the result, surviving recomposition and lifecycle changes.)