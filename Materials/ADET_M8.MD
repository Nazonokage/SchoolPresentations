# Android Resources: Modern Asset Management & Theming

---

## A. Lesson Preview & Review

Good day, everyone! 

In previous modules, you learned how to structure your app's UI using layouts and make it interactive with event handling. But building a great app is not just about writing code. It's also about how you organize the static content your code uses—images, colors, strings, and animations. 

This module focuses on **Android Resources**. A well-organized app keeps its code separate from its resources. This separation is crucial for localization (supporting multiple languages) and for adapting to different screen sizes and device configurations.

> **Quick Recap:** A project's `res/` directory is where all non-code files (like images, colors, and strings) are stored. These are known as **Resource Files**.

**Learning Targets:**
By the end of this module, you will be able to:
1.  Identify the common resource folders in an Android project (e.g., `drawable`, `layout`, `values`).
2.  Add and modify images, colors, and strings using modern best practices.
3.  Understand how to use Vector Drawables to ensure sharp graphics on all screen densities.
4.  Access resources using both traditional XML and modern Jetpack Compose APIs.

![Mobile app design and file organization](https://images.unsplash.com/photo-1586281380349-632531db7ed4?auto=format&fit=crop&q=80&w=800)

---

## B. Main Lesson

### The Android `res/` Directory
Android resources are kept separate from your Java/Kotlin source code in the `res/` folder. This design allows the Android system to automatically select the appropriate resource for the current device configuration (e.g., screen size, language, or orientation). 

Here are the key resource folders:

| Folder | Purpose |
| :--- | :--- |
| **`res/drawable/`** | Contains graphics (images, shapes). **Modern Best Practice:** Prefer XML **Vector Drawables** over raster images (PNG, JPEG) so they scale cleanly across all screen densities without pixelation. |
| **`res/layout/`** | Contains XML files that define the user interface structure (e.g., `activity_main.xml`). |
| **`res/mipmap/`** | Contains launcher icons for your app. These are kept separate from drawables because they have different density requirements. |
| **`res/values/`** | Contains XML files that define simple values like strings, colors, and dimensions. |

> **Image Density Adaptation:** Historically, you had to provide multiple versions of a raster image (e.g., `drawable-hdpi`, `drawable-xhdpi`, `drawable-xxhdpi`). Modern Android development strongly recommends using **Vector Drawables** (`VectorDrawable`), which are resolution-independent. If you must use raster images, **WebP** is the preferred modern format for its smaller file sizes and lossless quality.

---

### The `res/values/` Folder
This folder stores the core values used throughout your app. It contains several important XML files:

#### 1. `colors.xml`
Stores your app's color palette. Historically, this file defined `colorPrimary`, `colorPrimaryDark`, and `colorAccent`. In modern **Material Design 3**, the color system is much more sophisticated. It uses a system of **tonal palettes** where colors are mapped to specific roles (e.g., `primary`, `onPrimary`, `surface`, `onSurface`). This enables powerful features like **Dynamic Color** (Material You), which derives a custom color scheme from the user's wallpaper on Android 12+.

```xml
<resources>
    <!-- Legacy Colors -->
    <color name="purple_200">#FFBB86FC</color>
    <color name="purple_500">#FF6200EE</color>
    
    <!-- Modern M3 Role-based Colors -->
    <color name="md_theme_light_primary">#476810</color>
    <color name="md_theme_light_onPrimary">#FFFFFF</color>
</resources>
```

#### 2. `strings.xml`
This is one of the most important files. It stores all user-facing text. Storing strings here makes it easy to translate your app into different languages. **Best Practice:** Never hardcode text directly in your layouts or code. Always reference it from `strings.xml`.

```xml
<resources>
    <string name="app_name">My Workshop App</string>
    <string name="hello_message">Hello, welcome to the app!</string>
    <string name="action_settings">Settings</string>
</resources>
```

#### 3. `dimens.xml`
Used to define reusable dimensions (margins, padding, text sizes). Using a `dimens.xml` file is a good coding practice because if you ever need to change a standard margin size, you only have to change it in one place.

```xml
<resources>
    <dimen name="activity_horizontal_margin">16dp</dimen>
    <dimen name="activity_vertical_margin">16dp</dimen>
</resources>
```

#### 4. `styles.xml` / `themes.xml`
This is where you define the visual theme for your app. In the modern era, your base theme is typically derived from **Material 3**. The theme defines the default color scheme, typography, and shapes for your entire application.

```xml
<resources>
    <!-- Base application theme. -->
    <style name="Theme.MyApp" parent="Theme.Material3.DayNight.NoActionBar">
        <!-- Customize your theme here. -->
    </style>
</resources>
```

---

### Accessing Resources in Jetpack Compose
The traditional way to access resources was through the generated `R` class (e.g., `R.string.app_name`). In Jetpack Compose, you use specialized composable functions that are **lifecycle-aware**. They automatically update when the device configuration (like language or dark mode) changes, ensuring your UI always reflects the latest values.

*   **Strings:** `stringResource(id = R.string.app_name)`
*   **Images:** `painterResource(id = R.drawable.my_image)`
*   **Colors:** `colorResource(id = R.color.my_color)`

**Example in Compose:**

```kotlin
import androidx.compose.foundation.Image
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.res.stringResource

@Composable
fun MyResourceScreen() {
    // Loading a string from res/values/strings.xml
    Text(text = stringResource(id = R.string.hello_message))
    
    // Loading a drawable from res/drawable/
    Image(
        painter = painterResource(id = R.drawable.ic_launcher_foreground),
        contentDescription = stringResource(id = R.string.app_name)
    )
}
```

---

### Adding Images: Vector Assets vs. Raster Images
**Method 1: Vector Asset Studio (Recommended)**
This is the modern way to add images. Android Studio can convert SVG files or Google Material Icons into `VectorDrawable` XML files. These scale perfectly to any screen resolution without needing multiple density buckets.
1.  Right-click the `res` folder -> **New** -> **Vector Asset**.
2.  Select **Clip Art** (for Material icons) or a local **SVG** file.
3.  Android Studio generates an XML file in the `res/drawable/` folder.

**Method 2: Adding Raster Images**
If you are working with a raster image (like a photograph), you place it in the `res/drawable/` folder. However, you must provide multiple versions for different screen densities (e.g., `drawable-mdpi`, `drawable-hdpi`, `drawable-xhdpi`) to ensure it looks sharp on all devices.

---

## C. Analogies and Use Cases

### Analogy: The Library System
Think of your app as a library. 
*   **Code (Kotlin/Java)** is the librarian who knows how to do things.
*   **Resources (`res/`)** are the books and media. 
*   **`strings.xml`** is the catalog of titles and text. 
*   **`drawable/`** is the media section (pictures, maps). 
*   **`values/colors.xml`** is the interior paint palette.
Instead of the librarian describing every book from memory, they just go to the catalog (resources) and fetch what is needed.

### Real-World Use Case: Localization
Imagine you want your app to be available in English and Spanish. You would create a `values/strings.xml` for English and a `values-es/strings.xml` for Spanish. When a user switches their phone's language to Spanish, the Android system automatically fetches the strings from `values-es/strings.xml`. This is only possible because all strings were externalized into resource files.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   **Resources** (images, strings, colors) are kept in the `res/` folder and are separate from your source code.
*   **Vector Drawables** are the modern standard for icons because they scale cleanly without losing quality.
*   **`strings.xml`** is used to externalize all user-facing text for easy localization.
*   **Material 3 theming** uses a sophisticated color system, including dynamic color, to create a cohesive look across the app.
*   In Compose, always use APIs like **`stringResource`** and **`painterResource`** to access resources in a lifecycle-aware way.

### Frequently Asked Questions

**1. What is the difference between `drawable` and `mipmap`?**
`drawable` is for general images used in your app's UI. `mipmap` is specifically for your app's launcher icon. Android needs launcher icons in different densities for the home screen and app drawer, so they are kept separate.

**2. Why should I use Vector Drawables instead of PNGs?**
Vector Drawables are defined by XML paths, not pixels. This means they can scale to any size without becoming blurry, and they usually result in a much smaller APK size.

**3. What is Dynamic Color?**
Dynamic Color is a feature in Material You (Material 3) available on Android 12+. It allows your app's color scheme to adapt to the user's chosen wallpaper, creating a personalized and cohesive look across the operating system and all apps.

**4. Is `colors.xml` still used in Compose?**
Yes, you can still define colors in `colors.xml` and reference them in Compose using `colorResource()`. However, in a full Compose app, it's common to define colors directly in Kotlin code (e.g., `Color(0xFF476810)`) and use the `MaterialTheme` object to access them.

**5. Do I need to create `drawable-hdpi`, `drawable-xhdpi`, etc., for every image?**
No. If you are using Vector Drawables, you only need a single XML file in the `res/drawable/` folder. For raster images (like photos), providing multiple densities is still best practice, but modern formats like WebP help reduce the file size impact.

---

## E. Guided Drills / Code Projects

### Skill Building Activity: Adding a Custom Vector Icon

**Step 1: Open Vector Asset Studio**
In Android Studio, right-click on the `res` folder and select **New > Vector Asset**.

**Step 2: Configure the Asset**
1.  Choose **Clip Art** and click the "Clip Art" button to browse icons.
2.  Select an icon (e.g., a star or a heart).
3.  Rename the asset to `ic_my_custom_icon`.
4.  Click **Next** and then **Finish**.

**Step 3: Use the Icon in Compose**
Open your `MainActivity.kt` and add an `Icon` composable:

```kotlin
@Composable
fun CustomIconScreen() {
    Icon(
        painter = painterResource(id = R.drawable.ic_my_custom_icon),
        contentDescription = "Custom Icon",
        tint = MaterialTheme.colorScheme.primary
    )
}
```

**Step 4: Run the App**
Run your app to see the new vector icon rendered on the screen. Notice how crisp the edges are, regardless of the emulator's screen density.

---

## F. Skill-Building Check

**1. Which folder is used to store images and graphics in an Android project?**
A) `res/layout`
B) `res/values`
C) `res/drawable`
D) `res/anim`
> **Correct Answer: C** (The `res/drawable` folder contains images and drawable resources.)

**2. True or False: You should prefer raster PNG images over Vector Drawables for app icons.**
A) True
B) False
> **Correct Answer: B (False)** (Vector Drawables are preferred for icons because they scale cleanly on all screen densities without losing quality.)

**3. What is the primary purpose of `strings.xml`?**
A) To define the layout structure.
B) To externalize user-facing text for localization.
C) To store images.
D) To define animations.
> **Correct Answer: B** (`strings.xml` is used to store all user-facing text, making it easy to translate the app into different languages.)

**4. In Jetpack Compose, which function is used to load a drawable resource?**
A) `stringResource()`
B) `colorResource()`
C) `painterResource()`
D) `loadDrawable()`
> **Correct Answer: C** (`painterResource()` is the composable function used to load a drawable resource.)

**5. What feature in Material 3 allows the app's color scheme to adapt to the user's wallpaper?**
A) Dark Mode
B) Dynamic Color
C) Color Blindness Mode
D) High Contrast Mode
> **Correct Answer: B** (Dynamic Color, part of Material You, derives custom colors from the user's wallpaper.)

**6. True or False: `res/layout` is where you store launcher icons.**
A) True
B) False
> **Correct Answer: B (False)** (Launcher icons are stored in `res/mipmap`. The `res/layout` folder is for XML UI layout files.)

**7. Which file is used to define reusable dimensions like margins and padding?**
A) `colors.xml`
B) `strings.xml`
C) `dimens.xml`
D) `styles.xml`
> **Correct Answer: C** (`dimens.xml` is used for defining reusable dimensions.)

**8. Why is it better to use `stringResource()` instead of `context.getString()` in Compose?**
A) `stringResource()` is faster.
B) `stringResource()` is lifecycle-aware and automatically updates when the configuration (e.g., language) changes.
C) `stringResource()` uses less memory.
D) There is no difference.
> **Correct Answer: B** (`stringResource()` is a composable function that triggers recomposition when the configuration changes, ensuring the UI reflects the latest values.)