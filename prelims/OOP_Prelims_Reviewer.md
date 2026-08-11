# 🧠 OOP Prelims Reviewer (Modules 1–4)
### Object-Oriented Programming • Java-focused (with Python/JS/PHP side-by-side)

> Covers: Programming Logic & Algorithms → Introduction to OOP → Java Crash Course → Classes & Objects → Java Objects & Class Members.
> **Note:** Static vs Instance Methods (Module 5) and the deep-dive on Access Modifiers/`final`/`abstract` (Module 6) are **not** included — this reviewer stops at Module 4.
> Code blocks marked 🔁 show the SAME concept in Java, Python, JS, and PHP so you can see the pattern.

---

## 📑 Table of Contents

1. [Foundations: Programming Logic & Algorithms](#1-foundations-programming-logic--algorithms)
2. [Introduction to OOP](#2-introduction-to-oop)
3. [Java Crash Course (Syntax Basics)](#3-java-crash-course-syntax-basics)
4. [Classes & Objects](#4-classes--objects)
5. [Java Objects & Class Members (State, Behavior, Identity)](#5-java-objects--class-members)
6. [Cross-Language Cheat Sheet](#6-cross-language-cheat-sheet)
7. [Glossary of Key Terms](#7-glossary-of-key-terms)
8. [Practice Quiz Bank + Answer Key](#8-practice-quiz-bank--answer-key)

---

## 1. Foundations: Programming Logic & Algorithms

**Programming Logic** — the reasoning/thinking process behind how code is structured to perform a task. It's the "why" behind the "what."

**Algorithm** — a sequence of well-defined steps that solve a problem. Same input → same output, every time. (Analogy: a recipe. Follow the same steps, get the same dish.)

- Algorithms describe **what to do**, not the deep mechanical "how" (e.g., "bake for 30 mins" doesn't explain oven thermodynamics).

### The 10 Basic Programming Concepts (building blocks)

| # | Concept | One-liner |
|---|---------|-----------|
| 1 | Algorithm | Steps to accomplish a task |
| 2 | Source Code | The actual text of the program |
| 3 | Compiler | Converts source code → machine-readable bytecode |
| 4 | Data Type | Classification of values (int, String, etc.) |
| 5 | Variable | Container for data |
| 6 | Conditionals | Decision-making (`if/else`) |
| 7 | Array | Collection of similar elements |
| 8 | Loop | Repeating a block of code |
| 9 | Function/Method | Reusable block of code |
| 10 | Class | Blueprint for objects |

### How a computer works (quick facts)
- **Input devices** (keyboard, mouse, mic, scanner...) feed data in.
- **Memory** stores information so it isn't lost while processing.
  - **RAM** (Random Access Memory) — fast, **volatile** (wiped when power is off).
  - **ROM** (Read-Only Memory) — **non-volatile**, stores startup instructions permanently.

### Compiler vs Source Code
- **Source code**: what YOU write (text — letters, numbers, symbols).
- **Compiler**: translates that human-readable source code into machine-readable instructions.
- Java specifically compiles into **bytecode**, which the **JVM (Java Virtual Machine)** interprets — this is *why Java is cross-platform* (write once, run anywhere: Windows, Linux, macOS).

---

## 2. Introduction to OOP

### What is OOP?
Object-Oriented Programming organizes code around **objects** instead of just loose functions/logic.

- **Object** = a real-world "thing" with **properties** (data) and **behaviors** (actions).
- **Class** = the blueprint/template used to create objects.

### The Classic Analogy (Class = Template, Object = Instance)

| Analogy | Class (blueprint) | Objects (instances) |
|---|---|---|
| Shoes | `Sapatos` (Shoe) | `Adidas`, `Nike`, `Puma` |
| Cars | `Car` | `Toyota`, `Honda`, `Ford` |
| Cookies | Cookie cutter | The actual cookies |
| Cats | `Cat` | Fred, Stella (individual cats) |

Each object shares the same **structure** (defined by the class) but holds its **own independent data**.

### Why Use OOP?
- **Reusability** — write a class once, make unlimited objects from it.
- **Encapsulation** — bundles data with the methods that use it, protecting it from outside tampering.
- **Scalability** — big systems (banking, games, e-commerce) are easier to manage when split into classes/objects.
- **Real-world modeling** — mirrors how we naturally think (cars, users, products, animals).
- **Industry standard** — Java, Python, JS, PHP, C#, C++ all support OOP.

### The 4 Pillars of OOP (preview — good to know, tested lightly)
1. **Abstraction** – hide complex details, show only what's needed.
2. **Encapsulation** – bundle data + methods together; protect data (commonly via `private` fields + `public` getters/setters). *(This one you'll use a lot — see Section 4.)*
3. **Inheritance** – a class can inherit properties/behavior from another class.
4. **Polymorphism** – the same method name behaves differently depending on the object.

### 🔁 Same Concept, 4 Languages: A `Sapatos` (Shoe) Class

**Java**
```java
public class Sapatos {
    String kulay;   // color
    int sukat;      // size

    public Sapatos(String kulay, int sukat) {
        this.kulay = kulay;
        this.sukat = sukat;
    }

    public void takbo() {  // "run"
        System.out.println("Ang sapatos na " + kulay + " ay tumatakbo!");
    }

    public static void main(String[] args) {
        Sapatos adidas = new Sapatos("itim", 42);
        Sapatos nike   = new Sapatos("puti", 41);
        adidas.takbo();
        nike.takbo();
    }
}
```

**Python**
```python
class Sapatos:
    def __init__(self, kulay, sukat):
        self.kulay = kulay
        self.sukat = sukat

    def takbo(self):
        print(f"Ang sapatos na {self.kulay} ay tumatakbo!")

adidas = Sapatos("itim", 42)
puma = Sapatos("kulay abo", 40)
adidas.takbo()
puma.takbo()
```

**JavaScript**
```javascript
class Sapatos {
    constructor(kulay, sukat) {
        this.kulay = kulay;
        this.sukat = sukat;
    }
    takbo() {
        console.log(`Ang sapatos na ${this.kulay} ay tumatakbo!`);
    }
}

const adidas = new Sapatos("itim", 42);
const nike = new Sapatos("puti", 41);
adidas.takbo();
nike.takbo();
```

**PHP**
```php
<?php
class Sapatos {
    public $kulay;
    public $sukat;

    public function __construct($kulay, $sukat) {
        $this->kulay = $kulay;
        $this->sukat = $sukat;
    }

    public function takbo() {
        echo "Ang sapatos na " . $this->kulay . " ay tumatakbo!\n";
    }
}

$adidas = new Sapatos("itim", 42);
$puma   = new Sapatos("kulay abo", 40);
$adidas->takbo();
$puma->takbo();
?>
```

### Quick Comparison Table

| Language | Constructor | "Current object" keyword | Creating an object |
|----------|-------------|---------------------------|---------------------|
| Java | `Sapatos(...)` (matches class name) | `this` | `new Sapatos(...)` |
| Python | `__init__(self, ...)` | `self` | `Sapatos(...)` (no `new`) |
| JavaScript | `constructor(...)` | `this` | `new Sapatos(...)` |
| PHP | `__construct(...)` | `$this` | `new Sapatos(...)` |

**Key takeaway:** All four languages follow the *same OOP logic* — a class is a blueprint, an object is an instance. Syntax differs, logic doesn't. Learn it once, apply it everywhere.

---

## 3. Java Crash Course (Syntax Basics)

### Setup
- **JDK (Java Development Kit)** — lets you write and run Java programs.
- **IDE (Integrated Development Environment)** — like "MS Word for code": auto-complete, error detection, running programs. (e.g. Eclipse, IntelliJ IDEA)

### The `main` Method — Entry Point of Every Java Program
```java
public static void main(String[] args) {
    // Your code goes here!
}
```
| Keyword | Meaning |
|---|---|
| `public` | Accessible from anywhere |
| `static` | Can be called without creating an object |
| `void` | Returns nothing |
| `main` | The special method name Java looks for to start the program |
| `String[] args` | Command-line arguments |

### Variables
A variable is a **container that stores data** — has a **type**, **name**, and **value**.

```java
type variableName = value;

int myInt = 7;
System.out.println(myInt); // prints 7
```

### Primitive Data Types (8 total in Java — lowercase, "building blocks")

| Type | Description | Example |
|---|---|---|
| `int` | Whole numbers | `int age = 25;` |
| `double` | Decimal numbers | `double price = 19.99;` |
| `char` | A single character | `char initial = 'J';` |
| `boolean` | True or False | `boolean isRaining = false;` |

### `String` — Not Primitive (starts with capital `S`)
```java
String myName = "John";

System.out.println(myName.length());       // 4
System.out.println(myName.toUpperCase());  // JOHN
```
Strings have built-in **methods**, accessed with a dot `.`

### Arrays — Storing Multiple Values
```java
int[] sales = {10, 25, 30};
String[] fruits = {"grape", "guava", "banana"};

System.out.println(sales[0]);      // 10 (index starts at 0)
System.out.println(sales.length);  // 3
```
- Access elements by **index** (starts at `0`).
- `.length` gives the number of elements — no parentheses, it's a field, not a method.

### Operators
```java
int myInt = 7;
double shoeSize = 9.5;
System.out.println(myInt * shoeSize); // 66.5
```
`+` add · `-` subtract · `*` multiply · `/` divide

### Methods (functions) — Declaring, Parameters, Return Values
```java
// No parameters, no return value
private static void burp() {
    System.out.println("Burp!");
}

// With parameters
private static void printName(String name, int number) {
    System.out.println("My name is " + name + " and my number is " + number);
}

// With a return value
private static String getName() {
    return "My name is John";
}

public static void main(String[] args) {
    burp();
    printName("John", 7);
    String result = getName();
    System.out.println(result);
}
```
- Change `void` → an actual type (`String`, `int`, etc.) once your method needs to give something back.
- Use the `return` keyword.
- A method can **call another method** inside it (e.g., an "average" method calling a "total" method) — very handy for arrays.

### Conditionals (`if / else if / else`)
```java
String name = "John";

if (name.equals("John")) {
    System.out.println("This guy is awesome!");
} else if (name.equals("Larry")) {
    System.out.println("This guy is okay, I guess.");
} else {
    System.out.println("I don't know this guy at all.");
}
```
⚠️ **Use `.equals()` for String comparison — NOT `==`.**
`==` is for numbers/primitives (and assignment is single `=`, comparison is double `==`).

### Loops
```java
for (int i = 0; i < 10; i++) {
    System.out.println("These pretzels are making me thirsty!");
}
```
1. `int i = 0;` — start
2. `i < 10;` — condition (keep looping while true)
3. `i++` — increment after each pass

**Looping through an array (very common combo):**
```java
int[] nums = {1, 2, 3, 4, 10};
int total = 0;

for (int i = 0; i < nums.length; i++) {
    total = total + nums[i];
}
System.out.println("Total: " + total);
```

---

## 4. Classes & Objects

### Class vs Constructor
```java
public class Car_show {
    Car_show() {   // constructor — runs when object is created
        // initialization code
    }
}
```
- **Instantiating a class** = creating an object (an instance) using the `new` keyword: `new Car_show();`

### Types of Variables in a Class

| Type | Where declared | Scope |
|---|---|---|
| **Fields** | Directly inside a class (outside methods) | Define the object's *state* |
| **Local variables** | Inside a method/block | Only accessible in that scope |
| **Parameters** | In a method's declaration | Receive values when method is called |

**Field declaration order:** `modifier → type → name` (e.g. `public int cadence;`)

```java
public class Bicycle {
    public int cadence;
    public int gear;
    public int speed;
}
```

### Identifying Objects & Behaviors (in plain sentences)
> "A customer can have more than one bank account." → Objects: `customer`, `account`
> "Dogs bark, cats meow, ducks quack." → Objects: `Dog`, `Cat`, `Duck` · Behaviors: `bark()`, `meow()`, `quack()`

💡 **Tip:** Nouns → potential objects/classes. Verbs → potential methods/behaviors.

### Worked Example: Animals that "Say Hello" Differently
```java
class Dog {
    public void sayHello() {
        System.out.println("Arf! Arf! Arf!");
    }
}

class Cat {
    public void sayHello() {
        System.out.println("Meow! Meow!");
    }
}

class Duck {
    public void sayHello() {
        System.out.println("Quack! Quack!");
    }
}

public class HelloWorld {
    public static void main(String[] args) {
        Dog animal1 = new Dog();
        Cat animal2 = new Cat();
        Duck animal3 = new Duck();
        animal1.sayHello();
        animal2.sayHello();
        animal3.sayHello();
    }
}
```
This is a sneak peek at **polymorphism** — same method name (`sayHello`), different behavior per class.

### `toString()` — Overriding
```java
class Person {
    String name;

    Person(String name) {
        this.name = name;
    }

    public String toString() {  // overriding built-in method
        return "Person: " + name;
    }
}
```
**Override** = redefine an existing method with the same name so it behaves differently for your class.

### Encapsulation: Getters & Setters
```java
public class Person {
    private String name;
    private int age;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age > 0) {   // ✅ validation before storing
            this.age = age;
        }
    }
}
```
**Why encapsulation matters:**
- Protects data from unauthorized/invalid access.
- Allows validation before setting a value.
- Hides implementation details.
- Easier long-term maintenance.

### `private` vs `public` (as much as we need for now)
| Modifier | Visible from |
|---|---|
| `public` | Anywhere |
| `private` | Same class only |

**Rule of thumb:** Keep fields `private`, and use `public` getters/setters to control access. This is the core habit behind encapsulation.

---

## 5. Java Objects & Class Members

### Class = Logical only. Object = Logical + Physical.
- A **class** exists only "on paper" — no memory used until you create an object.
- An **object** is the real thing built from the blueprint — it lives in memory with actual data.

> "A class is the cookie cutter — an object is the actual cookie. You bake as many as you need."

### The 3 Characteristics of Every Java Object

| Characteristic | Question it answers | Defined by | Car example |
|---|---|---|---|
| **State** | "What it has" | Fields | `model="Mustang", color="Red", year=1969` |
| **Behavior** | "What it does" | Methods | `fullThrottle()`, `brake()`, `honk()` |
| **Identity** | "Who it is" | Unique memory reference (JVM) | Two red Mustangs = same state, different memory address |

📌 You'll work with **State** and **Behavior** most often in code.

### Class Members — The 4 Building Blocks

| Member | Runs when? | Purpose |
|---|---|---|
| **Field** | Exists as long as the object lives | Store data (state) |
| **Method** | Explicitly called | Define behavior |
| **Constructor** | Automatically on `new ClassName()` | Initialize state |
| **Property** (getter/setter) | Explicitly called | Safe, controlled field access |

```java
public class Data {
    // ① Fields (Data Members)
    public int x;
    public boolean check;

    // ② Constructor
    public Data() {
        check = true;  // sets initial state
    }

    // ③ Method (Function Member)
    public void printCheck() {
        if (this.check) {
            System.out.println("Check is true");
        }
    }
}
```
**Two categories of members:**
- **Data Members** — Fields (e.g. `x`, `check`)
- **Function Members** — Methods + Constructors (e.g. `Data()`, `printCheck()`)

**Easy test:** If it stores a value → Data Member. If it has `{}` with runnable code → Function Member.

### The Dot `.` Operator — Accessing Members
```java
// Access a field
objectName.fieldName;

// Call a method
objectName.methodName();
```
**3 steps:**
1. Create an object → `Car myCar = new Car();`
2. Type object name + dot → `myCar.`
3. Add the field/method → `myCar.model` or `myCar.fullThrottle();`

⚠️ **Common mistake:** The dot operator works on **objects (instances)**, not the class name itself.
```java
// ❌ Wrong
Car.model = "Mustang";
// ✅ Correct
myCar.model = "Mustang";
```

### Full Example — Two Independent Objects, Same Blueprint
```java
public class Car {
    public String model;
    public String color;
    public int year;

    public void fullThrottle() {
        System.out.println(model + " is going as fast as it can!");
    }
}

public class MainProgram {
    public static void main(String[] args) {
        Car ford = new Car();
        ford.model = "Mustang";
        ford.color = "red";
        ford.year  = 1969;

        Car honda = new Car();
        honda.model = "Brio";
        honda.color = "orange";
        honda.year  = 2019;

        System.out.println(ford.model);   // Mustang
        System.out.println(honda.model);  // Brio
        honda.fullThrottle();             // "Brio is going as fast as it can!"
    }
}
```
`ford` and `honda` are **completely independent** — changing `ford.model` never affects `honda.model`.

### Default Values (if you don't set a field yourself)
| Type | Default |
|---|---|
| `int` / `double` | `0` / `0.0` |
| `boolean` | `false` |
| `String` / any object | `null` |

---

## 6. Cross-Language Cheat Sheet

### Creating a Class + Object

| Concept | Java | Python | JavaScript | PHP |
|---|---|---|---|---|
| Define a class | `class Sapatos { }` | `class Sapatos:` | `class Sapatos { }` | `class Sapatos { }` |
| Constructor name | Same as class | `__init__(self, ...)` | `constructor(...)` | `__construct(...)` |
| Self-reference | `this` | `self` | `this` | `$this` |
| Create object | `new Sapatos(...)` | `Sapatos(...)` | `new Sapatos(...)` | `new Sapatos(...)` |
| Access member | `obj.field` | `obj.field` | `obj.field` | `$obj->field` |
| Call method | `obj.method()` | `obj.method()` | `obj.method()` | `$obj->method()` |

### Field vs Method vs Constructor vs Property
```
Field       → stores a value                    (int x;)
Method      → runnable behavior                 (void run() { } )
Constructor → runs automatically on `new`       (ClassName() { } )
Property    → getter/setter, controlled access  (getX() / setX())
```

### Access Modifiers Covered So Far
```
private → class only
public  → everywhere
```

---

## 7. Glossary of Key Terms

- **Object** — an instance of a class; a real "thing" with data + behavior.
- **Class** — the blueprint/template that defines an object's structure.
- **Instance / Instantiation** — creating an object from a class using `new`.
- **Field / Attribute / Instance Variable** — a variable that stores an object's state.
- **Method** — a block of code (behavior) that runs when called.
- **Constructor** — special method that initializes an object when it's created.
- **State** — the data an object holds (its fields' current values).
- **Behavior** — what an object can do (its methods).
- **Identity** — the unique reference the JVM uses to tell objects apart.
- **Encapsulation** — bundling data + methods, restricting direct access to protect data integrity.
- **Abstraction** — hiding complex implementation, exposing only what's necessary.
- **Inheritance** — a class acquiring properties/behavior from a parent class.
- **Polymorphism** — same method name, different behavior depending on the object.
- **Access Modifier** — keyword controlling visibility (`private`, `public`, for now).
- **Override** — redefining a method (same name) in a subclass or with new logic.
- **Dot Operator (`.`)** — used to access an object's fields/methods.
- **Array** — a collection that stores multiple values of the same type, accessed by index.
- **JVM (Java Virtual Machine)** — runs compiled Java bytecode on any platform.
- **Bytecode** — the compiled, intermediate form of Java source code.

---

## 8. Practice Quiz Bank + Answer Key

### Part A — Multiple Choice

**1.** What is an object?
A. Instance of an object B. Instance of a method C. Instance of a class D. Instance of a program

**2.** Which keyword is used to create a class in Java?
A. `class` B. `MyClass` C. `className` D. `class()`

**3.** What is the correct way to create an object `myObj` of `MyClass`?
A. `class MyClass = new myObj();` B. `MyClass myObj = new MyClass();` C. `new myObj = MyClass();` D. `class myObj = new MyClass();`

**4.** Which keyword ensures a variable/method is accessible only within its defining class?
A. `public` B. `private` C. `protected` D. `static`

**5.** What does `State` refer to in an object?
A. Its unique memory address B. The data it holds C. Its method names D. Its class name

### Part B — Code Tracing

**6.** What does this program print?
```java
class Student {
    int id;
    String name;
}

public class TestStudent2 {
    public static void main(String args[]) {
        Student s1 = new Student();
        s1.id   = 101;
        s1.name = "Juan Cruz";
        System.out.println(s1.id + " " + s1.name);
    }
}
```
A. `101 JuanCruz` B. `101 Juan Cruz` C. `id: 101 name: Juan Cruz` D. Compilation Error

### Part C — Short Answer
**7.** Explain the difference between a **field** and a **property** in your own words.
**8.** Why does `private` support encapsulation better than `public`?
**9.** Give one real-life analogy each for: Class, Object, Constructor.
**10.** Loop through the array `int[] nums = {2, 4, 6};` — what would `total` equal after summing all elements in a `for` loop?

---

### ✅ Answer Key

1. **C** — An object is an instance of a *class* (not a method or program).
2. **A** — `class` is the keyword; `MyClass`/`className` would just be the name you choose.
3. **B** — Correct syntax is `ClassName objectName = new ClassName();`
4. **B** — `private` restricts access to the declaring class only.
5. **B** — State = the data an object holds, defined by its fields.
6. **B — `101 Juan Cruz`.** Trace: `s1.id` → `101`, then `" "`, then `s1.name` → `"Juan Cruz"` (the space is already inside that string). Concatenation with `+` joins them left to right: `101 + " " + "Juan Cruz"` → `"101 Juan Cruz"`. (Not A — the name already has its own space. Not C — Java prints raw values, no auto-labels. Not D — the code is syntactically valid.)
7. A **field** is the raw variable that stores data inside a class (often `private`). A **property** is a getter/setter pair that gives *controlled* access to that field — it can validate or transform the value before it's read/written. Analogy: a field is a safe; a property is the combination lock on the safe.
8. Because `private` hides the field from *any* outside code, forcing all access to go through your own methods (getters/setters). This lets you validate input, prevent invalid states, and change the internal implementation later without breaking other code that uses the class.
9. Sample analogies: **Class** = cookie cutter / car blueprint. **Object** = the actual cookie / a specific car like a red 1969 Mustang. **Constructor** = the baking process that turns cutter + dough into an actual cookie.
10. `total` = `12` (2 + 4 + 6).

---

*Good luck sa prelims! Focus on: class vs object, the 4 pillars (light), encapsulation with getters/setters, state/behavior/identity, arrays + loops, and being able to trace/predict output of small Java programs — that's usually where most exam points come from.* ☕
