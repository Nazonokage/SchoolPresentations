Here is the modernized, 2026-ready version of Module 25, updated to reflect the required Android App Bundle (AAB) format, Play Console testing mandates, and contemporary monetization models.

---

# Android App Publishing & Modern Monetization

## A. Lesson Preview & Review

Welcome! You have built a functional, secure, and performant application. The final step is getting it into the hands of users and potentially generating revenue.

> **Important Paradigm Shift:** The legacy methods of publishing—generating an APK and uploading it directly—are obsolete. Since August 2021, Google Play **requires** the **Android App Bundle (AAB)** format. Furthermore, new developer accounts face mandatory testing phases, and monetization has shifted toward subscriptions and hybrid models.

**Learning Targets:**
1.  Understand the mandatory **Android App Bundle (AAB)** format and **Play App Signing**.
2.  Navigate the modern **Google Play Console** testing tracks (Internal, Closed, Open) and the 14-day testing requirement for new personal accounts.
3.  Identify modern **monetization models** (Subscriptions, Freemium, IAP, Hybrid).
4.  Generate a signed release AAB and complete the Play Store release workflow.

![Publishing and uploading concept](https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&q=80&w=1000)

---

## B. Main Lesson

### Part 1: Preparing for Release (The AAB Format)

#### 1. The Android App Bundle (AAB)
The legacy `.apk` file contained all resources for all device types, resulting in unnecessarily large downloads. The **AAB** is a publishing format that includes all your app’s compiled code and resources, but **defers APK generation and signing to Google Play**.
*   **Dynamic Delivery:** Google Play uses the AAB to generate optimized APKs containing only the resources needed for the specific device (e.g., only the `xxhdpi` images, only the `arm64-v8a` native libraries). This reduces download sizes by **15-30%**.
*   **Play Feature Delivery:** You can modularize features so users only download them when they are needed.

#### 2. Modern Release Signing
*   **Play App Signing:** Google manages your app's signing key. You sign the AAB with an **upload key**. If your upload key is compromised, Google can reset it without losing your app's identity.
*   **Code Shrinking (R8):** Ensure `isMinifyEnabled = true` and `isShrinkResources = true` in your `build.gradle.kts` release block. This obfuscates code and removes unused resources, making the app smaller and harder to reverse-engineer. You must upload the `mapping.txt` file to Play Console to deobfuscate crash reports.

#### 3. Generating the AAB
In Android Studio, go to **Build > Generate Signed Bundle / APK**. Select **Android App Bundle** and follow the prompts to create or use an existing keystore. The output will be an `app-release.aab` file.

---

### Part 2: The Google Play Console Workflow

#### 1. The 14-Day Closed Testing Rule (New Personal Accounts)
If you created a personal Google Play developer account **after November 13, 2023**, you cannot publish to production immediately. You must:
1.  Run a **Closed Test** with at least **12 testers** who remain opted in **continuously for 14 days**.
2.  Apply for production access after meeting this requirement. This is to ensure apps are tested before reaching a wider audience.

#### 2. Modern Testing Tracks
*   **Internal Testing:** Up to 100 testers. Fastest way to get a build to QA.
*   **Closed Testing (Alpha):** Limited number of chosen testers. Required for new personal accounts.
*   **Open Testing (Beta):** Anyone can join via the Play Store listing.
*   **Production:** Available to all users.

#### 3. Store Listing & App Content
Before rollout, you must complete:
*   **Store Listing:** High-res icon (512x512), Feature Graphic (1024x500), screenshots, short description (80 chars), and full description (4000 chars).
*   **App Content:** Privacy Policy URL (required for all apps), Data Safety form, Content Rating questionnaire, and Target Audience declaration.

#### 4. Rollout & Review
Submit the release for review. Reviews can take **up to 7 days**. Once approved, you can do a **staged rollout** (e.g., 5% -> 20% -> 50% -> 100%) to catch critical bugs early.

---

### Part 3: Modern Monetization Models

The legacy "Paid App" model is largely obsolete. Modern strategies focus on user acquisition and lifetime value.

#### 1. Freemium
The app is free to download, but premium features (e.g., ad-free experience, advanced tools, extra storage) are locked behind a paywall.
*   **Best for:** Broad-audience tools, games.

#### 2. Subscriptions (The Recurring-Revenue Engine)
Users pay a recurring fee (monthly or annual) for ongoing access to content or services. This is the dominant revenue model for productivity, fitness, and media apps.
*   **Best Practice:** Offer a **free trial** (e.g., 7 days) and an **annual discount** (e.g., "Save 50%") to improve retention. Subscription revenue grew by **105% YoY** in Q1 2026.

#### 3. In-App Purchases (IAP)
Users buy virtual goods or currency (e.g., gems, coins, skins) within the app. This is the primary model for mobile games.
*   **Platform Cut:** Google takes **15%** on the first $1M of annual revenue, and **30%** after that. Subscriptions after 12 months drop to 15%.

#### 4. In-App Advertising (IAA)
Integrating ads (e.g., Google AdMob) into the app. This model is most effective for high-engagement, mass-audience apps.
*   **Best Practice:** Use rewarded video ads (users watch an ad to get an in-game benefit) rather than intrusive banner ads.

#### 5. The Hybrid Model
Most successful apps use a **hybrid** of two or more models. For example, a free tier with ads, plus a subscription to remove ads and unlock features, plus occasional IAP for premium content.

---

## C. Analogies and Use Cases

### Analogy: The Modern Supermarket
*   **APK (Legacy):** You order a box containing every item in the store, even if you only need milk.
*   **AAB (Modern):** You order milk, and the store delivers only the milk to your door. This is Dynamic Delivery.

### Real-World Use Case: The Fitness App
A fitness app uses the **Freemium** model. Users can access basic workouts for free with ads. A **Subscription** unlocks advanced programs, offline access, and an ad-free experience. This hybrid approach maximizes both user acquisition (free tier) and revenue (paid tier).

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   **AAB is mandatory** for Google Play. It reduces app size via Dynamic Delivery.
*   **Play App Signing** secures your app's identity.
*   New personal accounts must run a **14-day closed test with 12 testers** before production.
*   **Subscriptions and hybrid models** are the dominant modern monetization strategies.
*   Always complete the **Data Safety** form and provide a **Privacy Policy**.

### Frequently Asked Questions

**1. Can I still publish an APK to Google Play?**
No. Since August 2021, new apps and updates must use the Android App Bundle (AAB) format.

**2. What is the 15% platform fee?**
Google Play charges a 15% service fee on the first $1 million in revenue each year. After that, it is 30%. For subscriptions, the fee drops to 15% after 12 months of active subscription.

**3. Do I need a Privacy Policy?**
Yes. Google Play requires a privacy policy URL in the Play Console for all apps, even if they do not collect data.

**4. What is a staged rollout?**
A staged rollout releases your app to a small percentage of users (e.g., 5%) so you can monitor crash rates and feedback before releasing to 100% of users.

**5. What happens if my app is rejected during review?**
You will receive an email explaining the policy violation. You must fix the issue, increment the `versionCode`, and resubmit the app for review.

---

## E. Guided Drills / Code Projects

### Skill Building Activity: Generate a Signed AAB

**Step 1: Configure Build File**
Ensure your `build.gradle.kts` has release signing and R8 enabled.

```kotlin
android {
    signingConfigs {
        create("release") {
            storeFile = file("your_keystore.jks")
            storePassword = "your_store_password"
            keyAlias = "your_key_alias"
            keyPassword = "your_key_password"
        }
    }
    buildTypes {
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            signingConfig = signingConfigs.getByName("release")
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
}
```

**Step 2: Build the Bundle**
In Android Studio, go to **Build > Generate Signed Bundle / APK**. Select **Android App Bundle** and follow the wizard. The output `app-release.aab` will be in `app/build/outputs/bundle/release/`.

---

## F. Skill-Building Check

**1. What is the mandatory publishing format for Google Play?**
A) APK
B) AAB (Android App Bundle)
C) ZIP
D) EXE
> **Correct Answer: B** (AAB is required for all new apps and updates.)

**2. What is the primary benefit of the AAB format?**
A) It is easier to email.
B) It reduces app download sizes via Dynamic Delivery.
C) It replaces Kotlin.
D) It automatically creates screenshots.
> **Correct Answer: B** (Dynamic Delivery optimizes the APK for the specific device.)

**3. For new personal developer accounts (post-Nov 2023), what is required before production access?**
A) A $1000 fee.
B) A closed test with 12 testers for 14 days.
C) A YouTube trailer.
D) A physical office address.
> **Correct Answer: B** (Google requires this testing period to ensure app quality.)

**4. Which monetization model is the "recurring-revenue engine"?**
A) Paid App
B) Subscriptions
C) In-App Purchases
D) Ads
> **Correct Answer: B** (Subscriptions provide recurring revenue.)

**5. What is the Google Play commission on the first $1M of annual revenue?**
A) 0%
B) 15%
C) 30%
D) 50%
> **Correct Answer: B** (15% on the first $1M, then 30%.)

**6. What is Play App Signing?**
A) A way to sign PDFs.
B) Google manages your app's signing key, you use an upload key.
C) A requirement to sign in with Google to use the app.
D) A tool to generate icons.
> **Correct Answer: B** (It secures the app's identity and allows key resets.)

**7. What file must you upload to Play Console to get deobfuscated crash reports?**
A) `proguard-rules.pro`
B) `mapping.txt`
C) `build.gradle`
D) `AndroidManifest.xml`
> **Correct Answer: B** (`mapping.txt` is generated by R8 and maps obfuscated code back to original names.)

**8. True or False: A Privacy Policy is optional if your app is free.**
A) True
B) False
> **Correct Answer: B (False)** (A Privacy Policy is required for all apps.)