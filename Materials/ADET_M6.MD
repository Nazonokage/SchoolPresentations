# Event-Driven Programming in Android

---

## A. Lesson Preview & Review

The applications we use daily are tools designed to support us in specific tasks. However, an app is only useful if it can respond to what we do. When you tap a button, swipe a screen, or type a message, you are triggering an **Event**. 

**Event-Driven Programming** is the core paradigm behind Android development. It focuses on the flow of the program being determined by user actions and system events. 

> **Quick Recap:** In previous modules, you learned how to build the visual structure of an app using Layouts and Views (or Composables). Now, it’s time to make those interfaces interactive.

**Learning Targets:**
By the end of this module, you will be able to:
1. Define events, event listeners, and event handlers in the context of Android.
2. Understand the asynchronous nature of event-driven programming.
3. Implement basic event handling using both legacy Java/XML and modern Kotlin/Compose approaches.

![Person tapping on a smartphone screen](https://images.unsplash.com/photo-1551650975-87deedd944c3?auto=format&fit=crop&q=80&w=800)

---

## B. Main Lesson

### Understanding Events and Event Handling
*   **Events:** Actions performed by the user to interact with the application (e.g., pressing a button, touching the screen). The Android framework manages these events in a FIFO (First In, First Out) manner.
*   **Event-Driven Programming:** An asynchronous programming model. Instead of a sequential `top-to-bottom` execution, the program runs an **event loop** that constantly listens for new incoming events. Once an event occurs, the loop decides what to execute and in what order.
*   **Event Handling:** The process of writing code that dictates how the app should respond when a specific event occurs.

### The Core Components of Event Handling
To make an app interactive, three concepts work together:
1.  **Event Listeners:** An interface in the View class that has a single callback method. It "listens" for a specific action on a View.
2.  **Event Handlers:** The method (the actual block of code) responsible for dealing with the event that the listener registered. It performs the desired action.
3.  **Event Listener Registration:** The process that associates a handler with a listener so that the handler is called when the event fires.

> **What is Touch Mode?** When a user interacts with a touch-enabled device, the device enters "Touch Mode." In this mode, focusing on items (like highlighting) is less important, and standard touch interactions (like tapping) take precedence.

### Common Event Listeners
Here are the standard listeners used in the traditional Android View system:

| Listener Interface | Handler Method | Triggered When... |
| :--- | :--- | :--- |
| `OnClickListener()` | `onClick()` | The user clicks, touches, or focuses on a view (Button, Image, etc.). |
| `OnLongClickListener()`| `onLongClick()` | The user presses and holds a widget for one or more seconds. |
| `OnMenuItemClickListener()`| `onMenuItemClick()` | The user selects a menu item. |
| `OnTouchListener()` | `onTouch()` | A movement gesture occurs, or a key is pressed/released. |

---

### The Paradigm Shift: Legacy XML/Java vs. Modern Kotlin/Compose

The way we handle events has evolved significantly. Let's look at how to make a button change text, comparing the old and new methods.

#### Legacy Approach (Java & XML)
In the old system, you had to find the View by its ID, create an anonymous inner class for the listener, and override the handler method.

```java
// Legacy Java Code
Button btn1 = (Button) findViewById(R.id.button1);
TextView tv2 = (TextView) findViewById(R.id.tv1);

btn1.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View view) {
        tv2.setText("Button Clicked");
    }
});
```

#### Modern Approach (Kotlin & Jetpack Compose)
In Jetpack Compose, you don't need `findViewById` or anonymous classes. You pass a **Lambda function** directly to the Composable's `onClick` parameter. The UI and the event logic live in the same place.

```kotlin
// Modern Kotlin Compose Code
var textState by remember { mutableStateOf("Please Click the Button") }

Button(onClick = { textState = "Button Clicked" }) {
    Text("CLICK ME")
}

Text(text = textState) // Automatically updates when textState changes
```

> **Pro Tip:** In Compose, you don't manipulate the UI directly (like calling `setText`). You update the **State**, and Compose automatically redraws the UI for you.

---

## C. Analogies and Use Cases

### Analogy: The Restaurant Order
Think of Event-Driven programming like dining at a restaurant:
*   **The Event:** You deciding you are ready to order.
*   **The Event Listener:** The waiter who is constantly watching the tables (the Event Loop).
*   **The Event Handler:** The chef in the kitchen who receives the order slip and cooks the food.
*   **Registration:** The waiter taking your menu and saying, "I'll put that right in for you."

### Real-World Use Case: The E-Commerce Cart
When you tap the "Add to Cart" button on a shopping app:
1.  The **Event** (a touch/click) is registered by the `OnClickListener`.
2.  The **Handler** (`onClick`) executes the logic to add the item to the cart database.
3.  The UI reacts by updating the cart icon badge number using **State Management**.

---

## D. Lesson Wrap-Up / FAQs

### Summary
*   **Event-Driven Programming** is asynchronous; the flow depends on user actions.
*   **Event Listeners** listen for actions (like clicks), and **Event Handlers** execute the response.
*   In modern Android development, event handling is declarative. You pass lambda functions (e.g., `onClick = { ... }`) to Composables rather than creating separate listener objects.

### Frequently Asked Questions

**1. Is it required to make objects of each XML component present in the application?**
No. You only need to create a reference (object) for components that are involved in an event or action. If you don't need to read data from a TextView or modify a Button, you don't need a reference to it. *(Note: In Jetpack Compose, `findViewById` and object creation for UI elements are eliminated entirely).*

**2. What happens if an Android Application has no Events?**
Without events, an application is essentially a static poster. It would be non-interactive, unappealing, and likely useless as a tool because it cannot respond to user input.

**3. What is a Lambda function?**
In Kotlin, a lambda is a concise way to write an anonymous function. It's why you can write `onClick = { /* code here */ }` instead of creating a whole class just to handle one click.

**4. What is "State" in Compose?**
State is any value that can change over time. When state changes (due to an event), Compose re-renders the UI components that rely on that state.

---

## E. Guided Drills / Code Projects

### Skill Building Activity: Event Handling Application

**The Task:** Create an application with a TextView and 6 Buttons. Apply `onClick` logic to each button to perform the following actions:
1.  **Show Message 1:** Changes the text to "Mabuhay!"
2.  **Show Message 2:** Changes the text to "Hello World!"
3.  **Clear:** Erases the text.
4.  **Large Text:** Sets the text size to 24sp.
5.  **Regular Text:** Sets the text size to 14sp.
6.  **Red Text:** Changes the text color to red.

**Implementation (Jetpack Compose):**

```kotlin
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun EventHandlingApp() {
    // State variables to hold the current text, size, and color
    var displayText by remember { mutableStateOf("Hi! Welcome to My Page!") }
    var textSize by remember { mutableStateOf(16.sp) }
    var textColor by remember { mutableStateOf(Color.Black) }

    Column(modifier = Modifier.padding(16.dp)) {
        // The TextView equivalent
        Text(
            text = displayText,
            fontSize = textSize,
            color = textColor,
            modifier = Modifier.padding(bottom = 16.dp)
        )

        // Row 1
        Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            Button(onClick = { displayText = "Mabuhay!" }) { Text("SHOW MESSAGE 1") }
            Button(onClick = { textSize = 24.sp }) { Text("LARGE TEXT") }
        }
        
        Spacer(modifier = Modifier.height(8.dp))

        // Row 2
        Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            Button(onClick = { displayText = "Hello World!" }) { Text("SHOW MESSAGE 2") }
            Button(onClick = { textSize = 14.sp }) { Text("REGULAR TEXT") }
        }

        Spacer(modifier = Modifier.height(8.dp))

        // Row 3
        Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            Button(onClick = { displayText = "" }) { Text("CLEAR") }
            Button(onClick = { textColor = Color.Red }) { Text("RED TEXT") }
        }
    }
}
```

---

## F. Skill-Building Check

**1. What is the model that event-driven programming follows?**
A) Sequential execution
B) Parallel execution
C) Asynchronous execution
D) Synchronous execution
> **Correct Answer: C** (Event-driven programming is asynchronous, relying on an event loop to listen for and respond to actions as they happen.)

**2. Which component is responsible for the actual execution of an action when an event occurs?**
A) Event Listener
B) Event Handler
C) Event Registration
D) Event Loop
> **Correct Answer: B** (The Event Handler is the method that executes the desired action, while the listener just waits for the trigger.)

**3. In traditional XML/Java Android development, which method is used to find a view by its ID?**
A) `setContentView()`
B) `findViewById()`
C) `setOnClickListener()`
D) `getView()`
> **Correct Answer: B** (`findViewById()` is the legacy method to link Java code to XML UI elements.)

**4. How do you handle a button click in modern Jetpack Compose?**
A) By calling `findViewById().setOnClickListener()`
B) By passing a lambda function to the `onClick` parameter of the `Button` Composable.
C) By creating an anonymous inner class.
D) By editing the XML file directly.
> **Correct Answer: B** (Compose uses declarative lambdas, e.g., `onClick = { ... }`.)

**5. What happens if an Android application has no event listeners?**
A) The app will crash.
B) The app will run but be completely non-interactive (static).
C) The app will automatically close.
D) The app will run faster.
> **Correct Answer: B** (Without event listeners, the app cannot respond to user gestures, making it a static display.)

**6. Which listener would you use if you want an action to trigger only after a user presses and holds a button for several seconds?**
A) `OnClickListener`
B) `OnTouchListener`
C) `OnLongClickListener`
D) `OnMenuItemClickListener`
> **Correct Answer: C** (`OnLongClickListener` is specifically designed for press-and-hold gestures.)

**7. In Compose, if you want the UI to update automatically when data changes, what must you use?**
A) `findViewById`
B) An Event Handler
C) A State variable (e.g., `mutableStateOf`)
D) `setText()`
> **Correct Answer: C** (Compose observes State. When state variables change, the UI automatically recomposes to reflect the new data.)