Here is the modernized, 2026-ready version of Module 22. The content has been updated to reflect the latest API levels (Android 15/16), modern API concepts, and the shift from the deprecated Twitter SDK to OAuth 2.0 / Firebase Authentication.

---

# Android Application Programming Interface: Modern API Integration & Authentication

## A. Lesson Preview & Review

Welcome! In this module, we will explore the **Application Programming Interface (API)**, the crucial set of rules that allows different software applications to communicate with each other. 

> **Quick Recap:** You've learned how to build UIs, handle data, and manage background tasks. Now, we will connect your app to the outside world. We'll replace the outdated Twitter SDK approach with modern, secure authentication using **OAuth 2.0** and **Firebase Authentication**, and review the latest **Android API Levels**.

**Learning Targets:**
1.  Define what an API is and its core features.
2.  Differentiate between Open, Internal, Composite, and Partner APIs.
3.  Understand the modern Android API Levels (Android 15 and Android 16).
4.  Implement secure Twitter/X login using **OAuth 2.0 with PKCE** and the **Firebase Authentication SDK**.

![API integration concept](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&q=80&w=1000)

---

## B. Main Lesson

### What is an API?
An **Application Programming Interface (API)** is a software interface that allows two applications to talk to each other. It acts as a "middleman" that enables applications to exchange data and functionality easily.

#### Types of APIs
*   **Open APIs (Public APIs):** Available to any developer. They help external users access data and services (e.g., weather data, public social media feeds).
*   **Internal APIs (Private APIs):** Exposed only within an organization for internal use, not for external developers.
*   **Composite APIs:** Combine different data and services to speed up execution and improve performance.
*   **Partner APIs:** Require specific rights or licenses to access. They are not available to the public and are used for business-to-business integrations.

### Android API Levels (2026 Update)
In the Android ecosystem, an API Level is an integer that uniquely identifies a version of the Android framework. Every new Android version introduces a new API level with new features and security improvements.

Here is the modern mapping of recent Android versions:

| Android Version | API Level | Version Name / Codename | Year |
| :--- | :--- | :--- | :--- |
| **Android 17 (Beta)** | **Level 37** | Cinnamon Bun | 2026 |
| **Android 16** | **Level 36** | Baklava | 2025 |
| **Android 15** | **Level 35** | Vanilla Ice Cream | 2024 |
| **Android 14** | Level 34 | Upside Down Cake | 2023 |
| **Android 13** | Level 33 | Tiramisu | 2022 |

> **Important Note:** Google Play requires new apps and updates to target **Android 16 (API level 36)** or higher. Existing apps must target at least **Android 15 (API level 35)** to remain available to new users.

### Modern Authentication: Twitter/X Login with Firebase
The legacy `com.twitter.sdk.android:twitter` library is **deprecated and no longer maintained**. It does not support the X API v2 and lacks modern security features. 

Today, to authenticate users with their X (formerly Twitter) account, you should use **OAuth 2.0 with PKCE** (Proof Key for Code Exchange). The easiest way to implement this in Android is via **Firebase Authentication**, which handles the end-to-end sign-in flow for you.

#### Step-by-Step Modern Integration

**Step 1: Configure in the X Developer Portal**
*   Go to the X Developer Console and create an app.
*   Enable **OAuth 2.0** (not OAuth 1.0a). Choose "Native App" as the app type, which uses the **PKCE** flow (public client) and does not require a client secret.
*   Set your Callback URL to your Firebase OAuth redirect URI (e.g., `my-app-12345.firebaseapp.com/__/auth/handler`).

**Step 2: Configure in Firebase Console**
*   Go to Firebase Console > **Authentication** > **Sign-in method**.
*   Enable the **Twitter** provider.
*   Enter your X **API Key** and **API Secret** from the X Developer Portal.

**Step 3: Add Dependencies**
Add the Firebase Authentication library to your app-level `build.gradle.kts`. It's recommended to use the Firebase BoM to manage versions.

```kotlin
dependencies {
    // Import the BoM for the Firebase platform
    implementation(platform("com.google.firebase:firebase-bom:35.0.0"))
    
    // Add the dependency for the Firebase Authentication library
    implementation("com.google.firebase:firebase-auth")
}
```

**Step 4: Implement the Login Flow in Kotlin**
Firebase provides a `OAuthProvider` to handle the Twitter.com provider.

```kotlin
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.OAuthProvider
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase

class AuthManager {
    private val auth: FirebaseAuth = Firebase.auth

    fun signInWithTwitter() {
        // 1. Build the OAuth Provider
        val provider = OAuthProvider.newBuilder("twitter.com")
            .setScopes(listOf("users.read", "tweet.read", "offline.access")) // Request only what you need
            .build()

        // 2. Start the sign-in flow
        auth.startActivityForSignInWithProvider(this, provider)
            .addOnSuccessListener { authResult ->
                // User is signed in successfully
                val user = authResult.user
                println("Signed in as: ${user?.displayName}")
            }
            .addOnFailureListener { e ->
                // Handle error
                println("Sign-in failed: ${e.message}")
            }
    }
}
```

---

## C. Analogies and Use Cases

### Analogy: The Restaurant Menu
Think of an API as a **restaurant menu**. 
*   **You (The App)** are the customer. 
*   **The Kitchen (The Server/Database)** is where the food (data) is made. 
*   **The API is the Menu**. It tells you what you can order and what you will get. You don't need to know how the kitchen works; you just use the menu to get your food.

### Real-World Use Case: The E-Commerce App
An e-commerce app integrates multiple APIs:
*   A **Payment API** (like Stripe or PayPal) to process transactions securely.
*   A **Shipping API** (like FedEx or UPS) to calculate delivery rates and track packages.
*   A **Login API** (like Firebase or Google Sign-In) to authenticate users.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   An **API** is a set of protocols that allows different software components to communicate.
*   **Android API Levels** map to specific Android versions; the current target is **Android 16 (API 36)**.
*   The legacy Twitter SDK is deprecated. Use **OAuth 2.0 with PKCE** for secure authentication.
*   **Firebase Authentication** simplifies the OAuth 2.0 flow, handling token exchange and user session management.

### Frequently Asked Questions

**1. What is the difference between API Key and API Secret?**
An **API Key** is a public identifier for your app. An **API Secret** is a private password and must never be exposed in client-side code. For mobile apps using OAuth 2.0 with PKCE (Native App type), a client secret is not used, which is why PKCE is more secure for mobile.

**2. Can I still use the old `com.twitter.sdk.android` library?**
No. It is deprecated and will not work with the modern X API v2. You must use OAuth 2.0 or Firebase Authentication.

**3. What is OAuth 2.0 PKCE?**
PKCE (Proof Key for Code Exchange) is an extension to OAuth 2.0 designed for public clients (like mobile apps) that cannot securely store a client secret. It uses a dynamically created code verifier and challenge to secure the authorization flow.

**4. Why do I need to specify a SHA-1 fingerprint in Firebase?**
The SHA-1 fingerprint is used to verify the identity of your app when it communicates with Firebase and Google services. It ensures that only your signed app can access the Firebase project.

**5. What happens if I don't target the latest API level?**
Google Play will eventually prevent your app from being published or updated if it doesn't target a recent API level. Additionally, targeting a newer API level ensures your app can access the latest features and security enhancements.

---

## E. Guided Drills / Code Projects

### Skill Building Activity: API Authentication Flow

**The Task:** Implement a Compose UI that triggers the Firebase Twitter sign-in flow and displays the logged-in user's name.

**Step 1: Create the Compose UI**
```kotlin
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.platform.LocalContext
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase

@Composable
fun TwitterLoginScreen() {
    val context = LocalContext.current
    val auth = Firebase.auth
    var userName by remember { mutableStateOf("Not signed in") }

    Button(onClick = {
        // In a real app, you would call an AuthManager here
        val provider = com.google.firebase.auth.OAuthProvider.newBuilder("twitter.com")
            .setScopes(listOf("users.read", "tweet.read"))
            .build()

        auth.startActivityForSignInWithProvider(context as android.app.Activity, provider)
            .addOnSuccessListener { result ->
                userName = result.user?.displayName ?: "Unknown"
            }
            .addOnFailureListener { e ->
                userName = "Error: ${e.message}"
            }
    }) {
        Text("Sign in with X (Twitter)")
    }

    Text(text = "Hello, $userName")
}
```

**Step 2: Run the App**
Run the app and tap the "Sign in with X (Twitter)" button. A Chrome Custom Tab will open, prompting the user to authorize the app. Upon successful authorization, the user's name will be displayed.

---

## F. Skill-Building Check

**1. What is an API?**
A) A type of database.
B) A set of functions that allows applications to access data and interact with external software components.
C) A UI design pattern.
D) A testing framework.
> **Correct Answer: B** (An API is an interface that allows different software applications to communicate.)

**2. Which type of API is available to any developer and helps external users access data?**
A) Internal APIs
B) Composite APIs
C) Open (Public) APIs
D) Partner APIs
> **Correct Answer: C** (Open or Public APIs are available to any developer for external use.)

**3. What is the current target API level requirement for new apps on Google Play (as of 2026)?**
A) Level 33
B) Level 34
C) Level 35
D) Level 36
> **Correct Answer: D** (New apps must target Android 16 / API level 36).

**4. Which Android version corresponds to API Level 35?**
A) Android 13
B) Android 14
C) Android 15
D) Android 16
> **Correct Answer: C** (Android 15 is API level 35).

**5. What modern authentication protocol should you use for mobile apps?**
A) OAuth 1.0a
B) OAuth 2.0 with PKCE
C) Basic Authentication
D) API Key only
> **Correct Answer: B** (OAuth 2.0 with PKCE is the secure standard for mobile apps).

**6. Which Firebase service simplifies the Twitter login flow?**
A) Firebase Realtime Database
B) Firebase Authentication
C) Firebase Cloud Messaging
D) Firebase Hosting
> **Correct Answer: B** (Firebase Authentication handles the OAuth flow).

**7. True or False: The legacy `com.twitter.sdk.android` library is still the recommended way to integrate Twitter login.**
A) True
B) False
> **Correct Answer: B (False)** (It is deprecated and does not support the modern API v2.)

**8. What is the role of the `OAuthProvider` class in Firebase?**
A) It configures the UI theme.
B) It builds the authentication request for a specific provider like Twitter.com.
C) It stores user data locally.
D) It handles network requests.
> **Correct Answer: B** (It is used to construct the OAuth authentication request).