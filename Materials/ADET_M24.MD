# Android Permissions, Performance & Security: Modern Best Practices

---

## A. Lesson Preview & Review

Welcome! In previous modules, you learned how to build functional, interactive applications. However, an app that is slow, drains the battery, or mishandles sensitive data will quickly be uninstalled (or worse, flagged by Google Play). 

This module focuses on the three pillars of professional Android development: **Permissions** (accessing data safely), **Performance** (keeping the app smooth), and **Security** (protecting the user).

> **Quick Recap:** An Android app is a sandboxed environment. By default, it cannot access system resources or other apps' data. To interact with the outside world, it must request permissions.

**Learning Targets:**
By the end of this module, you will be able to:
1.  Differentiate between Normal and Dangerous permissions and request them at runtime.
2.  Optimize app performance by offloading tasks to background threads.
3.  Identify and prevent common security threats like SQL injection and data leaks.
4.  Implement modern security practices for data storage and networking.

![Smartphone with a security shield](https://images.unsplash.com/photo-1614064641938-3bbee52942c7?auto=format&fit=crop&q=80&w=1000)

---

## B. Main Lesson

### Part 1: Permissions
An Android app is free to use data and resources it creates, but it must get permission to use anything that does not belong to the application (Hardware, Software, User Data).

#### Normal vs. Dangerous Permissions
*   **Normal Permissions:** Actions that do not affect user privacy or expose user data (e.g., `INTERNET`, `ACCESS_NETWORK_STATE`). These are granted automatically at install time.
*   **Dangerous Permissions:** Actions that affect user privacy or data (e.g., `CAMERA`, `LOCATION`, `CONTACTS`). These **must be requested at runtime** (since Android 6.0), and the user can deny them.

#### Modern Best Practices
1.  **Request Contextually:** Don't ask for all permissions on the first screen. Ask for the camera permission only when the user taps the "Take Photo" button.
2.  **Use Intents Instead:** If you just need to take a photo, use the `ACTION_IMAGE_CAPTURE` Intent to launch the device's camera app. You don't need the `CAMERA` permission if you let the camera app do the work!
3.  **Granular Permissions (Android 13+):** Instead of asking for broad `READ_EXTERNAL_STORAGE`, Android 13 requires specific permissions like `READ_MEDIA_IMAGES` or `READ_MEDIA_VIDEO`.

#### Requesting Runtime Permissions in Compose
```kotlin
import android.Manifest
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.platform.LocalContext
import androidx.core.content.ContextCompat
import android.content.pm.PackageManager

@Composable
fun CameraPermissionRequest() {
    val context = LocalContext.current
    
    // 1. Define the permission launcher
    val permissionLauncher = rememberLauncherForActivityResult(
        contract = ActivityResultContracts.RequestPermission()
    ) { isGranted ->
        if (isGranted) {
            // Permission granted, open camera logic here
        } else {
            // Handle denial (e.g., show a message)
        }
    }

    Button(onClick = {
        // 2. Check if we already have it, otherwise request it
        if (ContextCompat.checkSelfPermission(context, Manifest.permission.CAMERA) 
            == PackageManager.PERMISSION_GRANTED) {
            // Already granted
        } else {
            permissionLauncher.launch(Manifest.permission.CAMERA)
        }
    }) {
        Text("Open Camera")
    }
}
```

---

### Part 2: Performance
Mobile devices have limitations: battery life, memory, and processing power. To keep your app smooth, you must respect these limits.

#### 1. Keep Long-Running Tasks Off the Main Thread
The **Main Thread** (UI thread) is responsible for drawing the screen. If you perform a heavy task (like a network request or database read) on the main thread, the app will freeze.
*   **The 16ms Rule:** To achieve 60 frames per second (FPS), the main thread has exactly **16 milliseconds** to process each frame. If it takes longer, the app drops frames and stutters (jank).
*   **Modern Solution:** Use **Kotlin Coroutines** and `Dispatchers.IO` to move tasks to background threads.

#### 2. Simplify Your UI
Complex, deeply nested layouts take longer to render. 
*   **Legacy XML:** Avoid nesting `LinearLayout` inside `LinearLayout` inside `LinearLayout`. Flatten your hierarchy using `ConstraintLayout`.
*   **Modern Compose:** Compose makes layout nesting much less of an issue, but you should still avoid unnecessary components and overlapping views. "Overdraw" occurs when the system draws a pixel multiple times (e.g., a background behind a background).

#### 3. Monitor Performance (Modern Tooling)
The legacy "Profile GPU Rendering" tool is obsolete. Use the **Android Studio Profiler** instead:
*   **CPU Profiler:** See which methods are taking the most time.
*   **Memory Profiler:** Check for memory leaks (objects that are no longer needed but still held in RAM).
*   **Network Profiler:** Inspect the size and speed of your API calls.

---

### Part 3: Security
As a developer, you are the guardian of the user's data. Criminals look for vulnerabilities to steal information or hold data for ransom.

#### 1. Handling User Data
*   **Minimize:** Do not collect or store data you do not need.
*   **Hash it:** If you must store sensitive data (like passwords), use a non-reversible hash (e.g., bcrypt) with a salt. Never store passwords in plain text.
*   **Be careful with Logs:** Historically, `READ_LOGS` was a permission, but it is now restricted. However, malicious apps can still find ways to read logs. **Never log PII (Personally Identifiable Information)** like passwords, emails, or credit card numbers.

#### 2. Secure Storage
*   **Do not use External Storage:** SD cards and external storage are globally readable. Never store sensitive data there.
*   **Internal Storage + Encryption:** For sensitive data, use `EncryptedSharedPreferences` or `EncryptedFile` from the **Jetpack Security** library, which uses the Android Keystore system under the hood.

#### 3. IP Networking & Public Wi-Fi
*   **HTTPS over HTTP:** Always use HTTPS. Since Android 9 (API 28), cleartext (HTTP) traffic is blocked by default.
*   **Certificate Pinning:** To prevent Man-in-the-Middle (MITM) attacks on public Wi-Fi, use **Certificate Pinning** with OkHttp to ensure your app only trusts your specific server's certificate.

#### 4. Validating Input (SQL Injection)
If your app allows users to enter text that is sent to a database, you must guard against **SQL Injection**. 
*   **Modern Solution:** If using a local database, use **Room**. Room uses parameterized queries by default, making SQL injection nearly impossible. If sending data to a backend (like PHP/MySQL), ensure the backend uses prepared statements (PDO).

#### 5. WebViews
A `WebView` renders HTML and JavaScript inside your app. This is a massive security risk if not handled correctly.
*   **Cross-Site Scripting (XSS):** Malicious JavaScript can steal user cookies or execute native app code if the WebView is improperly configured.
*   **Best Practice:** Disable JavaScript unless absolutely necessary (`settings.javaScriptEnabled = false`). Validate every URL before loading it.

---

## C. Analogies and Use Cases

### Analogy: The VIP Club
*   **Normal Permissions:** Showing your ID at the door. Standard check, everyone does it.
*   **Dangerous Permissions:** The bouncer pats you down and asks why you need to bring a giant backpack inside. You need a good reason, and the club manager (the user) has to say "Yes."
*   **Main Thread:** The single-file line to the bar. If one person orders 100 drinks (a long task), the entire line stops moving (UI freezes).

### Real-World Use Case: A Banking App
*   **Permissions:** Requests `USE_BIOMETRIC` (fingerprint) contextually when the user logs in.
*   **Performance:** Uses Coroutines to fetch account balances over the network in the background, keeping the UI scrolling smoothly.
*   **Security:** Enforces HTTPS, uses `EncryptedSharedPreferences` to store the session token, and times out the user after 5 minutes of inactivity.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   **Permissions:** Only ask for what you need, when you need it. Use Intents to delegate tasks to other apps.
*   **Performance:** Keep heavy tasks off the main thread using Coroutines. Simplify layouts.
*   **Security:** Never trust user input. Use HTTPS, encrypt sensitive data, and never log PII.

### Frequently Asked Questions

**1. Why does an app need to ask for permission?**
To protect user privacy and device security. Dangerous permissions allow access to sensitive data (like contacts) or hardware (like the microphone), so the user must explicitly consent.

**2. Why is a permission called "dangerous"?**
Because it grants access to private user data or hardware that could compromise the user's privacy or incur costs (e.g., making phone calls or sending SMS).

**3. How can I ensure users don't get suspicious when installing my app?**
Only declare permissions in the `AndroidManifest.xml` that your app actually needs. If an app requests permissions that don't match its functionality (e.g., a flashlight app requesting access to contacts), users will be suspicious.

**4. What is the effect of putting long-running tasks in the background?**
It prevents the main UI thread from being blocked. This ensures the app remains responsive, animations stay smooth (60 FPS), and the Android system doesn't show an "App Not Responding" (ANR) dialog.

**5. What is the security problem with WebViews?**
WebViews can introduce vulnerabilities like Cross-Site Scripting (XSS) if they render untrusted web content with JavaScript enabled. Malicious scripts can potentially access the user's session or local data.

**6. Why do I need to encrypt user data before transmission?**
Public Wi-Fi networks are easily intercepted (Man-in-the-Middle attacks). Encryption (HTTPS) ensures that even if a hacker intercepts the data packets, they cannot read the contents.

---

## E. Guided Drills / Code Projects

### Skill Building Activity: Secure Logging & Background Task

**The Task:** Create a Compose function that uses Coroutines to simulate a network request in the background and logs the result securely (using a debug-only log).

```kotlin
import android.util.Log
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.rememberCoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

@Composable
fun SecureBackgroundTask() {
    // 1. Create a Coroutine Scope tied to the Composable's lifecycle
    val scope = rememberCoroutineScope()

    Button(onClick = {
        // 2. Launch a coroutine
        scope.launch {
            // 3. Switch to the IO dispatcher for background work
            val result = withContext(Dispatchers.IO) {
                delay(2000) // Simulate network delay
                "Success from server"
            }
            // 4. Log the result (Note: In production, only log in debug builds!)
            if (BuildConfig.DEBUG) {
                Log.d("NetworkTask", "Result: $result")
            }
            
            // UI updates automatically happen on the Main thread after withContext
        }
    }) {
        Text("Start Background Task")
    }
}
```

---

## F. Skill-Building Check

**1. Which permission type grants access to sensitive user data and requires explicit runtime approval?**
A) Normal Permission
B) Dangerous Permission
C) System Permission
D) Root Permission
> **Correct Answer: B** (Dangerous permissions must be requested at runtime).

**2. What is the "Main Thread" responsible for in Android?**
A) Handling network requests.
B) Drawing the UI and handling user input.
C) Running background services.
D) Managing the database.
> **Correct Answer: B** (The main thread draws the UI. Blocking it causes jank and ANRs).

**3. What is the recommended time budget to render a single frame to achieve 60 FPS?**
A) 1 millisecond
B) 16 milliseconds
C) 100 milliseconds
D) 1 second
> **Correct Answer: B** (16ms is the standard frame budget for 60Hz displays).

**4. Which of the following is a modern, secure way to store sensitive data locally?**
A) Plain text in `SharedPreferences`
B) External Storage (SD Card)
C) `EncryptedSharedPreferences` from Jetpack Security
D) A simple text file in internal storage
> **Correct Answer: C** (Jetpack Security uses the Android Keystore for encryption).

**5. True or False: You should use `HTTP` instead of `HTTPS` to save data bandwidth.**
A) True
B) False
> **Correct Answer: B (False)** (HTTP is insecure and blocked by default since Android 9. Always use HTTPS).

**6. What is SQL Injection?**
A) A performance optimization for databases.
B) A technique where malicious users inject SQL commands into input fields to compromise the database.
C) A way to back up SQL databases.
D) A method to encrypt SQL queries.
> **Correct Answer: B** (SQL injection is a critical security vulnerability).

**7. Why is it a bad practice to log user data (like passwords or emails) to Logcat?**
A) It slows down the app.
B) Other malicious apps with legacy permissions might read the logs, exposing user data.
C) It causes the app to crash.
D) Logcat has a limited size.
> **Correct Answer: B** (Logs can be a vector for data leaks).

**8. Which modern Android Studio tool helps you identify memory leaks and CPU bottlenecks?**
A) Profile GPU Rendering
B) Logcat
C) The Android Studio Profiler
D) The Layout Inspector
> **Correct Answer: C** (The Profiler provides real-time CPU, Memory, Network, and Energy data).