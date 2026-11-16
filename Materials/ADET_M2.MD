# Android Platform & Application Development

---

## A. Lesson Preview & Review

Welcome to the world of mobile application development! Today, mobile apps are ubiquitous, changing how we experience computing. Tasks that once required a desktop computer—like checking email, banking, or buying tickets—are now seamlessly done on the go. App developers make this possible.

As an IT professional, you will likely face a society saturated with mobile applications. Your goal will be to develop apps that help companies and individuals complete tasks effectively and efficiently.

**Learning Targets:**
By the end of this module, you will be able to:
1. Identify key terms, personalities, events, and information related to developing an application.
2. Navigate around the Integrated Development Environment (IDE) using the Android platform.

![Person using a mobile app](https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&q=80&w=800)

---

## B. Main Lesson

### Application and Application Development
*   **Application Software (or simply Application):** A type of computer program that performs a specific personal, educational, or business function. It is designed to assist end-users in accomplishing tasks related to productivity, creativity, or communication.
*   **Application Development:** The process of creating a computer program or a set of programs to perform the tasks that a business requires. Every app-building process follows standard steps: gathering requirements, designing prototypes, testing, implementing, and integrating.

Application development can take different forms based on the goal output, such as Custom, Rapid, Database, Enterprise, Web, and **Mobile Application Development**.

### Mobile Application Development and the Android Platform
**Mobile application development** is the process of creating apps that run on mobile platforms like Android and iOS. With mobile development, you can track inventory or make instant updates right from a phone.

**Android** is the platform changing what mobile devices can do. It powers phones, tablets, watches, TVs, and cars. It is the operating system inside 2.5 billion active devices.

#### Key Characteristics of Android:
*   It is a **Linux-based operating system** and programming platform developed by **Google** for mobile phones and other devices (tablets, TVs, wearables).
*   It can run on many different devices from many different manufacturers.
*   It includes a **Software Development Kit (SDK)** that helps you write original code and assemble software modules to create apps.
*   It provides a **marketplace** to distribute apps.
*   Android Inc. was acquired by Google in July 2005.
*   The Open Handset Alliance was formed in November 2007 to develop open standards for mobile devices.
*   It became available to the public as open source in October 2008.
*   Android powers over 80% of all smartphones globally.
*   Apps can be packaged easily and sold through stores like **Google Play**, SlideME, Opera Mobile Store, Mobango, F-Droid, and the Amazon Appstore.

### The Android Environment and Key Components

| Component | Description |
| :--- | :--- |
| **Operating System** | Android App Development requires Microsoft Windows XP (or later), Mac OS X 10.5.8 (or later), or Linux (including GNU C Library 2.7 or later). |
| **Java** | The language of choice for Android Apps (Java JDK5 or later). |
| **XML** | Used to assist in the layout of the Android emulator and UI. |
| **Android Studio** | The official Android IDE used to develop, run, debug, test, and package apps. |
| **Android Emulator (AVD)** | Used to design, develop, prototype, and test Android apps without using a physical device. |
| **Android Sensors** | Detect users' actions and responses like device contents rotating, walking, or tilting as needed. |
| **Android Development Kit (ADK)** | Used to access all libraries available to develop an Android App/Game. |
| **Android Platform** | Consists of the Android OS, application development tools, and a marketplace. |
| **Package (APK)** | The compiled Android application project file. |
| **Google Play Store** | Official app store and digital distribution service operated by Google. |

### The Android Stack
The Android operating system provides a rich development architecture available for your app to use, known as the **Android Stack**.

1.  **Applications:** The top layer where users interact with apps (Contacts, Camera, Browser, Games, etc.). You will write your applications to be installed here.
2.  **Application Framework:** Provides many higher-level services to applications in the form of Java classes. Developers use these services in their apps (e.g., Activity Manager, Notification Manager, View System).
3.  **Libraries & Android Runtime:** 
    *   **Libraries:** Includes open-source web browser engines (WebKit), SQLite database, and media playback libraries.
    *   **Android Runtime:** Includes Core Libraries and the Dalvik Virtual Machine (DVM), which is designed specifically for Android.
4.  **Linux Kernel:** The foundation. It provides a level of abstraction between the device hardware and contains essential hardware drivers (camera, keypad, display, audio, etc.).

![Android Architecture Diagram](https://developer.android.com/static/images/platform/google-play-services/overview.png)

### Navigating the Android Studio IDE
Android Studio is the official Integrated Development Environment (IDE) for Android development. It is made up of different logical areas:

1.  **Toolbar:** Lets you carry out a wide range of actions, including running your app and launching Android tools.
2.  **Navigation Bar:** Helps you navigate through your project and open files for editing. It provides a more compact view of the structure visible in the Project window.
3.  **Editor Window:** Where you create and modify code. Depending on the file type, it changes (e.g., a layout file displays the Layout Editor).
4.  **Tool Window Bar:** Runs around the outside of the IDE window and contains buttons that allow you to expand or collapse individual tool windows.
5.  **Tool Windows:** Give you access to specific tasks like project management, search, and version control.
6.  **Status Bar:** Displays the status of your project, the IDE itself, and any warnings or messages.

#### Understanding the Project Window Structure
When you create a new project, the **Project Window** (`app` folder) contains crucial files:
*   **java /:** Contains the `.java` source files (e.g., `MainActivity.java`), which is the default activity class that runs when the app is launched.
*   **res/drawable-hdpi /:** Directory for drawable objects designed for high-density screens.
*   **res/layout /:** Directory for files that define your app's user interface (e.g., `activity_main.xml`).
*   **res/values /:** Directory for XML files containing resources like strings and color definitions.
*   **AndroidManifest.xml:** The manifest file that describes fundamental characteristics of the app and defines its components.
*   **build.gradle:** Auto-generated file containing compile SDK version, build tools version, application ID, minimum SDK version, target SDK version, version code, and version name.

---

## C. Analogies and Use Cases

### Analogy: Building a House (The Android Stack)
Think of the Android Stack as building a house:
*   **Linux Kernel (Foundation):** The concrete foundation and structural framework. It interacts directly with the ground (hardware).
*   **Libraries & Runtime (Plumbing & Electrical):** The internal systems that make the house functional (water pipes, electrical wiring).
*   **Application Framework (Rooms & Layout):** The walls and rooms that give structure to the house and dictate how you move through it.
*   **Applications (Furniture & Decor):** The things you actually interact with and use daily (the sofa, the TV, the apps on your phone).

### Real-World Use Case
**Retail Inventory Management:** A local boutique uses a custom mobile app built on Android. Staff use their smartphones to scan barcodes (using the phone's camera sensor) to track inventory in real-time, updating the central SQLite database and syncing with their enterprise system without needing a desktop computer.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   Android is a **Linux-based, open-source operating system** developed by Google.
*   It dominates the mobile market, powering over 80% of smartphones.
*   Android Studio is the official **IDE** used to write code (Java), design layouts (XML), and test apps.
*   The **Android Stack** represents the layers of the operating system, from the Linux Kernel at the bottom to user Applications at the top.
*   Apps are distributed via marketplaces like the Google Play Store.

### Frequently Asked Questions

**1. Why choose Android over other platforms?**
Android gives you a lot of flexibility. You can customize your device interface, choose from a variety of themes, icons, fonts, and keyboards, and personalize your device. It is highly customizable and open-source.

**2. What is the latest version of Android?**
As of the module's creation, the latest version was Android 13 (codename 'Tiramisu'). Historically, Android versions are named alphabetically after desserts (e.g., Android 9: Pie, Android 11: Red Velvet Cake, Android 12: Snow Cone).

**3. Do I need a physical Android phone to build and test apps?**
No. You can use the **Android Emulator (Android Virtual Device - AVD)** built into Android Studio. It simulates a real device on your computer screen.

**4. What language is used to build Android apps?**
While Java has historically been the primary language (and is used in this course), Kotlin is now the preferred language for Android development. XML is used for designing the layouts.

---

## E. Guided Drills / Code Projects

### Skill-Building Activity: Creating Your First Android Application

**Step 1: Setup**
Ensure your Android development environment is set up. Double-click the Android Studio icon to open it.

**Step 2: Create a New Project**
On the Welcome screen, click **New Project**. Select **Phone and Tablet**, choose **Basic Activity**, and click **Next**.

**Step 3: Configure the Project**
*   **Name:** `MyApplication`
*   **Language:** `Java`
*   **Minimum SDK:** `API 23: Android 6.0 (Marshmallow)`
Click **Finish** and wait for all components to load.

**Step 4: Explore the Code**
Open `MainActivity.java` in the `java` folder. You will see the base code for the application:

```java
package com.example.myapplication;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;
import androidx.appcompat.widget.Toolbar;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });
    }
}
```

**Step 5: View the Layout**
Open `activity_main.xml` in the `res/layout` folder to view the UI Editor. You will see a basic screen with a floating action button.

**Step 6: Create an Emulator (AVD)**
1. On the Toolbar, click the **Device Manager** icon.
2. Click **Create Device**.
3. Choose a phone (e.g., Pixel 2) and click **Next**.
4. Download a system image (e.g., API 33) and click **Next**.
5. Finish the configuration.

**Step 7: Run the App**
Click the **Run (Play icon)** button on the toolbar. Select your newly created emulator. Wait for the emulator to boot, and your app will automatically install and launch!

---

## F. Skill-Building Check

**1. What is the original developer of Android?**
A) Google
B) Apple
C) Android Inc.
D) Microsoft
> **Correct Answer: C) Android Inc.** (Android Inc. was acquired by Google in 2005).

**2. On what operating system is Android based?**
A) Windows
B) macOS
C) Linux
D) Unix
> **Correct Answer: C) Linux** (The bottom layer of the Android Stack is the Linux Kernel).

**3. How many percent of devices does Android power globally?**
A) 50%
B) 65%
C) 80%
D) 95%
> **Correct Answer: C) 80%** (The text states it powers over 80% of all smartphones).

**4. What is one of the primary programming languages used for Android development?**
A) Python
B) C++
C) Swift
D) Java
> **Correct Answer: D) Java** (While Kotlin is now preferred, Java is the foundational language taught in this module).

**5. What do you mean by APK?**
A) Android Platform Kit
B) Application Package
C) Android Programming Kernel
D) App Process Key
> **Correct Answer: B) Application Package** (It is the compiled Android application project file).

**6. Which component detects the user's actions and responses (like tilting or walking)?**
A) Android Emulator
B) Android Sensors
C) Android Runtime
D) Android Framework
> **Correct Answer: B) Android Sensors**

**7. What is Google's official IDE for developing Android apps?**
A) Eclipse
B) Xcode
C) Android Studio
D) Visual Studio Code
> **Correct Answer: C) Android Studio**

**8. What is Google's official app store for Android?**
A) Amazon Appstore
B) F-Droid
C) Google Play Store
D) Opera Mobile Store
> **Correct Answer: C) Google Play Store**