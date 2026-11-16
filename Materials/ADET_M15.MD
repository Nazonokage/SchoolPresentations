The provided source material relies on heavily outdated integration methods—such as embedded third-party SDKs, deprecated APIs like the old Twitter v1.1, and requesting sensitive runtime permissions. Today’s Android ecosystem enforces strict privacy sandboxing, restricts background SMS/Phone access, and prioritizes standardized system UI. 

Below is the modernized, best-practice approach for sharing content to social platforms and external apps in 2025/2026.

---

# Android Social Media Integration & Modern System Sharing

## A. Lesson Preview & Review

Most users expect seamless sharing, but modern Android security policies no longer allow apps to freely control other applications or post silently. Modern integration relies on **Implicit Intents**, the **Android Sharesheet** (system UI), and **Deep Links (App Links)**.

> **Key Paradigm Shift:** Historically, developers bundled heavy, proprietary SDKs (like old Twitter4J or Facebook Share SDK) directly into their apps. Today, the best practice is to leverage Android’s native **Sharesheet** via `ACTION_SEND` for universal compatibility, and use **App Links** to route users back to specific content.

**Learning Targets:**
1. Implement generic social sharing using the **Android Sharesheet** (`ShareCompat` / `Intent.createChooser`).
2. Integrate platform-specific intents (e.g., Instagram Feed, X/Twitter intent).
3. Utilize **Android App Links** for seamless deep linking.
4. Build secure, sandboxed sharing flows in Jetpack Compose.

![System Share Sheet Interface](https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&q=80&w=1000)

---

## B. Main Lesson

### 1. The Android Sharesheet (Universal Sharing)
The **Android Sharesheet** is the standard system UI that appears when a user shares content. It predicts the user's preferred contacts and apps. You should use it for *any* general content-sharing flow, as it eliminates the need for app-specific SDKs.

*   **Single Content:** Use `Intent.ACTION_SEND`. Provide the MIME type (`text/plain`, `image/*`) and attach data using `Intent.EXTRA_TEXT` or `Intent.EXTRA_STREAM`.
*   **Multiple Contents:** Use `Intent.ACTION_SEND_MULTIPLE` and pass an `ArrayList<Uri>` of images/videos.
*   **Helper Class:** Use `ShareCompat.IntentBuilder` to construct these intents cleanly.

```kotlin
// Sharing text and a link
val shareIntent = ShareCompat.IntentBuilder(context)
    .setType("text/plain")
    .setChooserTitle("Share via")
    .setText("Check out this awesome app!")
    .createChooserIntent()

context.startActivity(shareIntent)
```

### 2. Platform-Specific Integrations & Intents

While the Sharesheet is universal, some platforms have specific intent schemes for better UX:

*   **Instagram (Feed & Stories):** Instagram does not accept generic `text/plain` or pre-filled captions. To share media to the Feed, use an implicit `ACTION_SEND` with `EXTRA_STREAM` set to a `content://` URI and MIME type `image/*` or `video/*`. For Stories, use the explicit intent action `com.instagram.share.ADD_TO_STORY`.
*   **X (formerly Twitter):** The old Twitter4J SDK is deprecated. To share text and URLs, use the standard X web intent URL: `https://twitter.com/intent/tweet?text=...&url=...`. For full API posting, use the **X API v2** via HTTP REST (`POST /2/tweets`) with OAuth 2.0, utilizing community libraries like `twitter4j-v2` or `KTweet`.
*   **Facebook:** The Facebook Android SDK (v18+) remains useful for **Login** and **Analytics**. For **Sharing**, it is highly recommended to use the native Android Sharesheet or the Facebook web share dialog (`https://www.facebook.com/dialog/share`) rather than embedding the Facebook Share SDK, as the native app handles the UI securely without requiring extra SDK configuration.

### 3. App Links & Deep Linking (Bringing Users Back)
To integrate social media *into* your app (e.g., clicking a link in a Facebook post opens your app), you must implement **Android App Links**.
*   **App Links vs. Deep Links:** Deep links are any URI that opens your app. **App Links** are verified deep links that leverage `Digital Asset Links` (`assetlinks.json` hosted on your domain) to prove ownership.
*   **Dynamic App Links (Android 15+):** You can now define specific URL paths, query parameters, and exclusions directly in the `assetlinks.json` file, allowing you to route users to specific app screens without pushing app updates.

### 4. Uploading to YouTube
For uploading videos to YouTube, use the **YouTube Data API v3**.
*   You must authenticate using **OAuth 2.0** (using the Google API Client Library for Android or REST endpoints).
*   Uploads are performed via the `videos.insert` endpoint. For mobile, use **resumable uploads** to handle network interruptions gracefully.

---

## C. Analogies and Use Cases

### Analogy: The Universal Postal Service vs. Private Couriers
*   **The Android Sharesheet** is like a universal postal service. You hand them a package (the content), and they present a list of couriers (apps) to deliver it. You don't need to know how each courier operates.
*   **Implicit Intents (e.g., Instagram intent)** are like hiring a specific courier. You know they have special capabilities (e.g., adding stickers to Stories), but if that courier isn't available on the device, the delivery fails unless you provide a fallback.

### Real-World Use Case
**E-Commerce App:** A user finds a product and wants to share it via WhatsApp. The app uses the **Sharesheet** with `ACTION_SEND` and `text/plain`, allowing WhatsApp to handle the preview card. If the user wants to share an image of the product, the app uses `ACTION_SEND` with `image/*` and `EXTRA_STREAM`. Both flows require **zero** third-party SDKs and respect user privacy.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   **System Sharesheet:** The preferred method for all sharing. Use `ACTION_SEND` or `ACTION_SEND_MULTIPLE`.
*   **Platform Intents:** Use for specific features (e.g., Instagram Stories `com.instagram.share.ADD_TO_STORY`).
*   **App Links:** Verify domain ownership with `assetlinks.json` to securely route links into your app.
*   **YouTube:** Use the Data API v3 with OAuth 2.0 for uploads.

### Frequently Asked Questions

**1. Why should I avoid the Facebook Share SDK?**
The native Android Sharesheet already lists the Facebook app. Using the Sharesheet provides a consistent, secure experience and doesn't require you to add a heavy SDK dependency, manage Facebook App IDs, or deal with SDK version conflicts.

**2. Can I pre-fill an Instagram caption?**
No. Instagram intentionally does not allow third-party apps to pre-fill captions or tags via Intents. The user must write their own caption in the Instagram app.

**3. How do I share a link to X (Twitter)?**
Use the web intent URL: `Intent(Intent.ACTION_VIEW, Uri.parse("https://twitter.com/intent/tweet?text=$text&url=$url"))`. This opens the X app if installed, or the browser.

**4. What is a `content://` URI and why is it necessary?**
Modern Android uses scoped storage. You cannot pass a `file://` URI to another app. You must use a `FileProvider` to generate a secure `content://` URI, granting the target app temporary read permission.

**5. What happens if the user doesn't have Instagram installed?**
Always wrap intent launches in a `resolveActivity()` check or a `try/catch` block to prevent an `ActivityNotFoundException`. You can then fall back to the Sharesheet.

---

## E. Guided Drills / Code Projects

### Skill Building Activity: Multi-Platform Share Button

**The Task:** Implement a Compose button that shares a product image and text via the Android Sharesheet.

**Step 1: Setup FileProvider in `AndroidManifest.xml`**
```xml
<provider
    android:name="androidx.core.content.FileProvider"
    android:authorities="${applicationId}.fileprovider"
    android:exported="false"
    android:grantUriPermissions="true">
    <meta-data
        android:name="android.support.FILE_PROVIDER_PATHS"
        android:resource="@xml/file_paths" />
</provider>
```

**Step 2: Create `res/xml/file_paths.xml`**
```xml
<?xml version="1.0" encoding="utf-8"?>
<paths>
    <cache-path name="images" path="images/" />
</paths>
```

**Step 3: Compose Share Logic**
```kotlin
import android.content.Intent
import android.net.Uri
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.platform.LocalContext
import androidx.core.content.FileProvider
import androidx.core.app.ShareCompat
import java.io.File

@Composable
fun ShareProductButton(imageFile: File) {
    val context = LocalContext.current

    Button(onClick = {
        // Generate a secure content:// URI
        val uri: Uri = FileProvider.getUriForFile(
            context,
            "${context.packageName}.fileprovider",
            imageFile
        )

        // Build the Share Intent using ShareCompat
        val shareIntent = ShareCompat.IntentBuilder(context)
            .setType("image/*")
            .setStream(uri) // Attach the image
            .setText("Check out this product!") // Attach text
            .setChooserTitle("Share Product via")
            .createChooserIntent()
            .addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION) // Crucial for content URIs

        context.startActivity(shareIntent)
    }) {
        Text("Share Product")
    }
}
```

---

## F. Skill-Building Check

**1. What is the recommended modern approach for sharing content to any social media app?**
A) Adding the Facebook SDK
B) Using the Android Sharesheet with `ACTION_SEND`
C) Using the deprecated Twitter4J library
D) Sending a direct SMS
> **Correct Answer: B** (The Sharesheet is universal, secure, and requires no third-party SDKs.)

**2. Which Intent action should you use to share multiple images at once?**
A) `ACTION_SEND`
B) `ACTION_SEND_MULTIPLE`
C) `ACTION_SHARE`
D) `ACTION_VIEW`
> **Correct Answer: B** (`ACTION_SEND_MULTIPLE` is designed for lists of URIs.)

**3. True or False: You can use the Instagram intent to pre-fill a caption for the user.**
A) True
B) False
> **Correct Answer: B (False)** (Instagram intentionally strips pre-filled captions to prevent spam.)

**4. What file must be hosted on your server to verify your Android App Links?**
A) `robots.txt`
B) `assetlinks.json`
C) `applinks.xml`
D) `manifest.json`
> **Correct Answer: B** (`assetlinks.json` proves domain ownership for App Links.)

**5. Which API does X (Twitter) recommend for programmatic posting (e.g., from a backend)?**
A) Twitter API v1.1
B) X API v2
C) Twitter4J SDK
D) Facebook Graph API
> **Correct Answer: B** (The X API v2 is the current standard; v1.1 is deprecated.)

**6. Why is a `content://` URI required when sharing files between apps?**
A) It is faster than a `file://` URI.
B) It prevents unauthorized access by requiring the target app to have explicit read permissions.
C) It automatically compresses the file.
D) It is the only way to share images.
> **Correct Answer: B** (Scoped storage enforces security via `content://` URIs and temporary permissions.)

**7. Which YouTube API should you use to upload a video?**
A) YouTube Player API
B) YouTube Data API v3
C) Google Analytics API
D) YouTube SDK for Android
> **Correct Answer: B** (The Data API v3 handles uploads via `videos.insert`.)

**8. What is the best way to fall back if a user doesn't have Instagram installed?**
A) Crash the app.
B) Show a Toast message and do nothing.
C) Check `resolveActivity()` and fall back to the Android Sharesheet.
D) Open the Instagram website.
> **Correct Answer: C** (Always check for an available handler and provide a graceful fallback.)