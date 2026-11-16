# Android Messaging & Telephony: Modern Intents and Best Practices

---

## A. Lesson Preview & Review

Welcome to our new lesson! Mobile phones have become powerful tools for businesses and individuals to connect globally. According to recent statistics, over 1.5 billion people worldwide send and receive SMS messages, and by 2025, 72.6% of internet users will access the web via mobile phones only. 

As a developer, integrating communication features—SMS, phone calls, and email—is a common requirement. However, the landscape of Android permissions and app policies has changed dramatically. 

> **Quick Recap:** In previous modules, you learned about **Intents** (messaging objects used to request actions from other apps). Today, we will apply Intents to telephony and messaging while adhering to modern security and privacy restrictions.

**Learning Targets:**
By the end of this module, you will be able to:
1.  Understand the **Android 15 restrictions** on the `SEND_SMS` permission.
2.  Use `ACTION_SENDTO` to safely delegate SMS sending to the user's default messaging app.
3.  Use `ACTION_DIAL` to open the phone dialer without requiring sensitive permissions.
4.  Use `ACTION_SENDTO` and `ACTION_SEND` to compose emails with the user's preferred email client.
5.  Implement these intents in **Jetpack Compose**.

![People communicating via smartphones](https://images.unsplash.com/photo-1512428559087-560fa5ceab42?auto=format&fit=crop&q=80&w=800)

---

## B. Main Lesson

### Part 1: Android Telephony Architecture (The Legacy View)
Historically, Android provided a **Telephony API** to monitor phone state, network connections, and use `SmsManager` to send messages directly from the app. The architecture involved:
1.  **Communication Processor:** Wireless module drivers in the Linux kernel.
2.  **Radio Interface Layer (RIL):** Handles communication between the telephony services and the radio hardware.
3.  **Android Telephony Services:** Manages phone state and network info.
4.  **High-Level Telephony Applications:** The apps (Dialer, Contacts, Messaging) you interact with.

#### The Modern Reality: Restricted Permissions
In modern Android development (especially targeting **Android 15+**), the rules have changed:

*   **`SEND_SMS` is Restricted:** The `SEND_SMS` permission is now a "restricted permission." It is only granted to apps that are actively registered as the **default SMS app** (e.g., Google Messages) or to system apps. A regular app attempting to use `SmsManager` to silently send messages will fail.
*   **The Solution: Delegation:** The modern, recommended approach is to **delegate** communication tasks to the user's preferred apps using **Implicit Intents**. This is safer, requires no dangerous permissions, and respects user privacy.

---

### Part 2: Sending SMS (Modern Approach)
Instead of sending messages silently (which is heavily restricted and often flagged as spam), you should use an implicit intent to open the user's default messaging app with a pre-filled message and phone number.

*   **Action:** `Intent.ACTION_SENDTO`
*   **Data URI:** `smsto:` followed by the phone number.
*   **Extras:** `sms_body` for the message text.

> **Important:** The older method of using `Intent.ACTION_VIEW` with type `vnd.android-dir/mms-sms` is deprecated. Always use `ACTION_SENDTO` with the `smsto:` scheme.

```kotlin
// Modern Kotlin function to open SMS app
fun sendSms(context: Context, phoneNumber: String, message: String) {
    val intent = Intent(Intent.ACTION_SENDTO).apply {
        data = Uri.parse("smsto:$phoneNumber") // The smsto: scheme
        putExtra("sms_body", message)
    }
    // Verify an app can handle the intent before launching
    if (intent.resolveActivity(context.packageManager) != null) {
        context.startActivity(intent)
    }
}
```

---

### Part 3: Making Phone Calls
*   **`ACTION_DIAL` (Recommended):** Opens the phone dialer app with the number pre-filled. **Requires NO permissions.** The user must press the call button.
*   **`ACTION_CALL` (Requires Permission):** Directly initiates a call. This requires the `CALL_PHONE` permission, which is a dangerous permission. It is generally discouraged unless you are building a dialer replacement app.

```kotlin
// Modern Kotlin function to open the dialer
fun dialPhoneNumber(context: Context, phoneNumber: String) {
    val intent = Intent(Intent.ACTION_DIAL).apply {
        data = Uri.parse("tel:$phoneNumber")
    }
    if (intent.resolveActivity(context.packageManager) != null) {
        context.startActivity(intent)
    }
}
```

---

### Part 4: Sending Emails
To send an email, you can use the `ACTION_SENDTO` intent with the `mailto:` URI scheme. This ensures that only email apps (not social media or SMS apps) handle the intent.

*   **Action:** `Intent.ACTION_SENDTO`
*   **Data URI:** `mailto:`
*   **Extras:** `EXTRA_EMAIL` (recipients), `EXTRA_SUBJECT`, `EXTRA_TEXT`.

```kotlin
// Modern Kotlin function to compose an email
fun composeEmail(context: Context, addresses: Array<String>, subject: String, body: String) {
    val intent = Intent(Intent.ACTION_SENDTO).apply {
        data = Uri.parse("mailto:") // Only email apps handle this
        putExtra(Intent.EXTRA_EMAIL, addresses)
        putExtra(Intent.EXTRA_SUBJECT, subject)
        putExtra(Intent.EXTRA_TEXT, body)
    }
    if (intent.resolveActivity(context.packageManager) != null) {
        context.startActivity(intent)
    }
}
```

---

## C. Analogies and Use Cases

### Analogy: The Restaurant Concierge
Imagine you are at a hotel. 
*   **SmsManager (Legacy):** You sneak into the kitchen and cook your own meal. This is messy, dangerous, and the hotel (Android system) will stop you because you don't have permission.
*   **Implicit Intents (Modern):** You tell the concierge, "I'd like to order a pizza." The concierge (the Android system) finds the best pizza place (the user's default SMS app) and places the order for you. You get the result without ever entering the kitchen.

### Real-World Use Case: The E-Commerce App
When a user completes a purchase, the app provides a "Contact Support" button.
*   **SMS:** Clicking it opens the user's messaging app with a pre-filled message: "I need help with order #12345."
*   **Email:** Clicking it opens Gmail with the subject "Order #12345 Inquiry" and the body pre-filled.
*   **Call:** Clicking it opens the dialer with the support number pre-filled, ready for the user to tap call.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   **Android 15+** heavily restricts apps from silently sending SMS. The `SEND_SMS` permission is reserved for default SMS apps.
*   **Best Practice:** Use **Implicit Intents** (`ACTION_SENDTO` for SMS, `ACTION_DIAL` for calls, `ACTION_SENDTO` with `mailto:` for email) to delegate tasks to the user's preferred apps.
*   **No Permissions Needed:** Using `ACTION_DIAL` and `ACTION_SENDTO` for SMS/Email does not require dangerous runtime permissions.
*   Always call `resolveActivity()` before starting an intent to prevent `ActivityNotFoundException`.

### Frequently Asked Questions

**1. Can I access the SMS inbox of the phone?**
Accessing the SMS inbox requires the `READ_SMS` permission, which is heavily restricted. Google Play policy only allows apps that are default SMS handlers (or specific exceptions like backup apps) to use this permission. For most apps, this is not permitted.

**2. Can I access the phone's contacts?**
Yes, but it requires the `READ_CONTACTS` permission. You must request this permission at runtime. However, for simply sending a message, you don't need contact access; you can use the `ACTION_PICK` intent to let the user select a contact.

**3. What does "native app" mean in the context of messaging?**
A native app is an app installed on the phone (like the default SMS app) that was downloaded from the store. When you use an Intent, you are leveraging these native apps to do the work for you.

**4. Why is `ACTION_CALL` discouraged?**
Because it requires the `CALL_PHONE` permission, which allows an app to make calls without user interaction (potentially incurring charges). `ACTION_DIAL` is safer as it requires the user to explicitly press the call button.

**5. What happens if the user has no email app installed?**
If no app can handle the `ACTION_SENDTO` intent with `mailto:`, the `resolveActivity()` check will return `null`. Your code should handle this gracefully, perhaps by showing a Toast message informing the user that no email app was found.

---

## E. Guided Drills / Code Projects

### Skill Building Activity: Unified Communication Screen

**The Task:** Create a Compose screen with three buttons: "Send SMS", "Call Support", and "Email Support". Use implicit intents to launch the respective apps.

**Implementation:**

```kotlin
import android.content.Context
import android.content.Intent
import android.net.Uri
import android.widget.Toast
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp

@Composable
fun CommunicationScreen() {
    val context = LocalContext.current
    val supportNumber = "+1234567890"
    val supportEmail = "support@example.com"

    Column(
        modifier = Modifier.fillMaxSize().padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        Button(onClick = {
            sendSms(context, supportNumber, "I need help with my order.")
        }) {
            Text("Send SMS")
        }

        Button(onClick = {
            dialPhoneNumber(context, supportNumber)
        }) {
            Text("Call Support")
        }

        Button(onClick = {
            composeEmail(context, arrayOf(supportEmail), "App Support", "Hello, I have a question about...")
        }) {
            Text("Email Support")
        }
    }
}

// Modern Kotlin functions (as defined in the Main Lesson)
fun sendSms(context: Context, phoneNumber: String, message: String) {
    val intent = Intent(Intent.ACTION_SENDTO).apply {
        data = Uri.parse("smsto:$phoneNumber")
        putExtra("sms_body", message)
    }
    if (intent.resolveActivity(context.packageManager) != null) {
        context.startActivity(intent)
    } else {
        Toast.makeText(context, "No SMS app found", Toast.LENGTH_SHORT).show()
    }
}

fun dialPhoneNumber(context: Context, phoneNumber: String) {
    val intent = Intent(Intent.ACTION_DIAL).apply {
        data = Uri.parse("tel:$phoneNumber")
    }
    if (intent.resolveActivity(context.packageManager) != null) {
        context.startActivity(intent)
    }
}

fun composeEmail(context: Context, addresses: Array<String>, subject: String, body: String) {
    val intent = Intent(Intent.ACTION_SENDTO).apply {
        data = Uri.parse("mailto:")
        putExtra(Intent.EXTRA_EMAIL, addresses)
        putExtra(Intent.EXTRA_SUBJECT, subject)
        putExtra(Intent.EXTRA_TEXT, body)
    }
    if (intent.resolveActivity(context.packageManager) != null) {
        context.startActivity(intent)
    }
}
```

---

## F. Skill-Building Check

**1. Which permission is heavily restricted and generally only available to default SMS apps in modern Android (especially Android 15+)?**
A) `INTERNET`
B) `READ_CONTACTS`
C) `SEND_SMS`
D) `CALL_PHONE`
> **Correct Answer: C** (`SEND_SMS` is now a restricted permission reserved for default SMS handlers.)

**2. What is the modern, recommended action for opening the default SMS app with a pre-filled message?**
A) `Intent.ACTION_VIEW` with type `vnd.android-dir/mms-sms`
B) `Intent.ACTION_SENDTO` with the `smsto:` URI
C) `Intent.ACTION_CALL`
D) `Intent.ACTION_SEND`
> **Correct Answer: B** (`ACTION_SENDTO` with the `smsto:` scheme is the correct modern approach.)

**3. Which intent action should you use to open the phone dialer with a number pre-filled, without requiring any dangerous permissions?**
A) `Intent.ACTION_CALL`
B) `Intent.ACTION_DIAL`
C) `Intent.ACTION_PHONE`
D) `Intent.ACTION_VIEW`
> **Correct Answer: B** (`ACTION_DIAL` opens the dialer without needing the `CALL_PHONE` permission.)

**4. To ensure an email intent is only handled by email apps (and not SMS or social media apps), what should you do?**
A) Use `ACTION_SEND` with type `text/plain`.
B) Use `ACTION_SENDTO` with the `mailto:` URI.
C) Use `ACTION_VIEW` with a web URL.
D) Set the package name to Gmail.
> **Correct Answer: B** (`ACTION_SENDTO` with `mailto:` ensures only email apps handle it.)

**5. What is the purpose of `resolveActivity()` before calling `startActivity()`?**
A) To check if the user has granted permissions.
B) To ensure an app exists on the device that can handle the intent.
C) To validate the phone number.
D) To check if the device has an internet connection.
> **Correct Answer: B** (`resolveActivity()` prevents `ActivityNotFoundException` by checking for a handler.)

**6. Which permission is required to use `Intent.ACTION_CALL`?**
A) `CALL_PHONE`
B) `PHONE_CALL`
C) `DIAL_PHONE`
D) No permission is required.
> **Correct Answer: A** (`ACTION_CALL` requires the `CALL_PHONE` permission.)

**7. How do you pre-fill the message body in an SMS intent?**
A) `putExtra(Intent.EXTRA_TEXT, message)`
B) `putExtra("sms_body", message)`
C) `setData(Uri.parse("sms:$message"))`
D) `putExtra(Intent.EXTRA_MESSAGE, message)`
> **Correct Answer: B** (`sms_body` is the standard extra for SMS message text.)

**8. True or False: You can access the user's SMS inbox simply by declaring the `READ_SMS` permission in the manifest.**
A) True
B) False
> **Correct Answer: B (False)** (`READ_SMS` is a restricted permission; declaring it in the manifest is not enough, and Google Play policy heavily restricts its use to default SMS apps.)