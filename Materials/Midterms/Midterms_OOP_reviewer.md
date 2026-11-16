# Complete Reviewer: Java OOP Module 5 & 6
## Methods & Access Modifiers

---

## 📚 **PART 1: METHODS IN JAVA**

### What is a Method?

A **method** is a block of code that only runs when it is called. Methods are the building blocks of Java programs - they allow you to organize code, avoid repetition, and make programs easier to maintain.

**Key Benefits:**
- ♻️ **Reuse** - Write once, call anywhere
- 📦 **Organization** - Break big problems into small, manageable pieces
- 🔧 **Actions** - Methods perform specific tasks (calculations, printing, updating data)

### Method Syntax Example

```java
int add_number(int num1) {
    return num1 + 1;
}
```

---

## 🔀 **Static vs Instance (Dynamic) Methods**

### The Core Difference

| Feature | **Static Method** | **Instance Method** |
|---------|-------------------|---------------------|
| Belongs to | The **class** itself | An **object** |
| Called via | `ClassName.staticMethod()` | `myObject.instanceMethod()` |
| Object needed? | ❌ No | ✅ Yes |
| Keyword | `static` | No `static` keyword |
| Can access | Only static members | Both static and instance members |

### 📖 Analogy: Mall Escalator vs Smartphone Camera

| **Static = Public Mall Escalator** | **Instance = Your Smartphone Camera** |
|-------------------------------------|----------------------------------------|
| Anyone can use it without owning the mall | You can't take a photo without a phone |
| Belongs to the building (the Class) | First create the object, then use its camera |
| `MallEscalator.goUp()` | `Smartphone myPhone = new Smartphone();` |
| | `myPhone.takePhoto()` |

**Key takeaway:** Static methods don't need objects. Instance methods do.

---

## 💻 **Code Examples**

### Static vs Public Method in Action

```java
public class Sas678 {
    // Static method
    static void myStaticMethod() {
        System.out.println("Static methods can be called without creating objects");
    }

    // Instance method
    public void myPublicMethod() {
        System.out.println("Public methods must be called by creating objects");
    }

    public static void main(String[] args) {
        myStaticMethod(); // works directly

        Sas678 myObj = new Sas678();
        myObj.myPublicMethod(); // needs object
    }
}
```

### Car Class Example

```java
public class Car {
    int power = 2000;
    String model = "Nissan Almera 1.2";

    // Static method
    static void powerUp() {
        for (int q = 1; q <= 10; q++) {
            System.out.print(q + " ");
        }
        System.out.println();
    }

    // Instance method
    public void power_Boost() {
        System.out.println(power + " " + model);
    }

    public static void main(String[] args) {
        powerUp(); 
        Car Tarak2 = new Car();
        Tarak2.power_Boost();
    }
}
```

**Expected Output:**
```
1 2 3 4 5 6 7 8 9 10
2000 Nissan Almera 1.2
```

### FullThrottle and Speed with Parameters

```java
public class Main {
    public void fullThrottle() {
        System.out.println("The car is going as fast as it can!");
    }

    public void speed(int maxSpeed) {
        System.out.println("Max speed is: " + maxSpeed);
    }

    public static void main(String[] args) {
        Main myCar = new Main();
        myCar.fullThrottle();
        myCar.speed(1000);
    }
}
```

**Output:**
```
The car is going as fast as it can!
Max speed is: 1000
```

---

## 📊 **Fields vs Methods - Quick Review**

| **Fields** | **Methods** |
|-----------|-------------|
| Variables inside a class (data/state) | Behaviors/actions the class can perform |
| Store values | Perform operations |
| Can be static or instance | Can be static or instance |

**Best practice:** Keep fields private and access them through methods.

---

## 🎯 **Practice Activities**

### Activity 1 — Static Counter
**Task:** Write a static method `countToFive()` that prints numbers 1 to 5.

```java
public class Counter {
    public static void countToFive() {
        // Your code here
    }
    public static void main(String[] args) {
        countToFive();
    }
}
```

### Activity 2 — Dog Class
**Task:** Create a Dog class with:
- Field: `String name`
- Instance method: `bark()` that prints `"Woof! My name is " + name`

---

## 🔑 **Activity Solutions**

### Solution 1 — Static Counter
```java
public class Counter {
    public static void countToFive() {
        for (int i = 1; i <= 5; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        countToFive(); // Output: 1 2 3 4 5
    }
}
```

### Solution 2 — Dog Class
```java
public class Dog {
    String name;

    public Dog(String dogName) {
        this.name = dogName;
    }

    public void bark() {
        System.out.println("Woof! My name is " + name);
    }

    public static void main(String[] args) {
        Dog myDog = new Dog("Buddy");
        myDog.bark();
    }
}
```

---

# 🔐 **PART 2: ACCESS MODIFIERS**

## The Four Access Modifiers

Access modifiers control **who can access** your classes, fields, and methods. They enforce **encapsulation** - one of the four pillars of Object-Oriented Programming.

### 🔒 **private** (Class-level)
- Restricted only to the class where it's declared
- Like a barista's personal recipe notebook nobody else touches

### 📦 **default** (Package-level)
- No modifier written = visible only to classes in the same package
- The "house blend" shared among staff on the same shift

### 👪 **protected** (Package & Subclass)
- Accessible within the same package AND by subclasses anywhere
- The "family recipe" passed down to every franchise branch

### 🌍 **public** (World-level)
- Accessible from anywhere in the project
- The menu board everyone walking in can read

---

## 📊 **Visibility Matrix**

| Access Level | Same Class | Same Package | Subclass (different package) | World (everywhere) |
|--------------|------------|--------------|------------------------------|-------------------|
| **private** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **default** (no modifier) | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| **protected** | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No |
| **public** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |

---

## 💻 **Access Modifier Code Examples**

### ❌ Private Access — Direct Access Fails
```java
public class NumberClass {
    private int number = 10;
}

public class Program {
    public static void main(String[] args) {
        NumberClass num = new NumberClass();
        // COMPILE ERROR: number has private access in NumberClass
        System.out.println(num.number);
    }
}
```

### ✅ Private Access — Access via Method
```java
class HelperClass {
    private int power = 1;

    public HelperClass() {
        displayPower();
    }

    public void displayPower() {
        // Allowed: inside the same class
        System.out.println("Power value: " + this.power);
    }
}

public class Main {
    public static void main(String[] args) {
        HelperClass example = new HelperClass();
    }
}
```

---

## 🌐 **Public Access — The Open Menu**

```java
public class ReturnNumber {
    public int x = 105;

    public static void main(String[] args) {
        ReturnNumber num = new ReturnNumber();
        // Allowed: x is public
        System.out.println("Public field value: " + num.x);
    }
}
// Output: Public field value: 105
```

**Key Points:**
- `public` is the **widest** visibility level
- Great for constants and API entry points
- Use deliberately - over-exposure breaks encapsulation

---

## 📦 **Default (Package-Level) Access**

```java
// Both classes live in the same package
class InventoryItem {
    int stockCount = 42; // no modifier -> default (package-private)
}

public class WarehouseDesk {
    public static void main(String[] args) {
        InventoryItem item = new InventoryItem();
        // Allowed: WarehouseDesk is in the SAME package
        System.out.println("Stock on hand: " + item.stockCount);
    }
}
// Output: Stock on hand: 42
```

**What Changes If the Package Differs?**
```
error: stockCount is not public in InventoryItem; 
cannot be accessed from outside package
```

---

## 👪 **Protected Access — The Franchise Recipe**

```java
// Parent class in package A
package com.roastery.recipes;

public class HouseBlendRecipe {
    protected String secretRatio = "70% Arabica, 30% Robusta";
}

// Subclass in package B
package com.roastery.franchise;
import com.roastery.recipes.HouseBlendRecipe;

public class FranchiseBranch extends HouseBlendRecipe {
    public void printRecipe() {
        // Allowed: protected reaches subclasses
        System.out.println("Our secret ratio: " + secretRatio);
    }
}
```

**Key difference from default:** A plain, unrelated class in the same package that does **not** extend `HouseBlendRecipe` still couldn't touch `secretRatio`.

---

## 🎯 **Real-Life Analogies for Access Modifiers**

| Modifier | Analogy | Description |
|----------|---------|-------------|
| **private** | 📓 Personal Notebook | A barista's personal recipe notebook - nobody else touches it |
| **default** | 🏠 House Blend | The house blend recipe shared among everyone working that location |
| **protected** | 🏢 Franchise Recipe | The family recipe passed down to every franchise branch |
| **public** | 📋 The Menu Board | Anyone walking in off the street can read it |

---

## 🔍 **Guided Drill: BankAccount**

**Task:** Keep `balance` private, add `deposit()` and `showBalance()`, then test it by depositing 500.

### Pseudocode
```
CLASS BankAccount
    PRIVATE balance = 0
    METHOD deposit(amount)
        balance = balance + amount
    END METHOD
    METHOD showBalance()
        PRINT "Balance: " + balance
    END METHOD
END CLASS
```

### Java Solution
```java
class BankAccount {
    private double balance = 0;

    public void deposit(double amount) {
        balance = balance + amount;
    }

    public void showBalance() {
        System.out.println("Balance: " + balance);
    }

    public static void main(String[] args) {
        BankAccount account = new BankAccount();
        account.deposit(500);
        account.showBalance();
    }
}
// Output: Balance: 500.0
```

---

## 📝 **Check for Understanding**

### Q1: What is a method?
**A:** A block of code that performs a specific task when called.

### Q2: What's the difference between static and instance methods?
**A:** Static belongs to class and doesn't need an object. Instance belongs to object and requires an object to be created.

### Q3: List the four access modifiers in order from most restrictive to least restrictive.
**A:** `private` → `default` → `protected` → `public`

### Q4: What's the default access modifier if you don't specify one?
**A:** `default` (package-level) - accessible only within the same package.

### Q5: When would you use `protected` instead of `default`?
**A:** When you want subclasses in different packages to be able to access the member.

---

## 🎯 **Key Takeaways**

### Methods
1. Methods are reusable blocks of code that perform specific tasks
2. **Static methods** belong to the class → `ClassName.methodName()`
3. **Instance methods** belong to objects → `object.methodName()`
4. Methods can accept parameters and return values

### Access Modifiers
1. **private** → Class only
2. **default** → Package only
3. **protected** → Package + Subclasses
4. **public** → Everyone

### Rule of Thumb
**Pick the tightest level that still gets the job done.** You can always widen access later - narrowing it after other code depends on it is much harder.

---

## 📚 **Summary**

Understanding **methods** and **access modifiers** is fundamental to writing clean, maintainable, and secure Java code:

- Methods organize code into reusable actions
- Static vs Instance determines how methods are called
- Access modifiers control visibility and enforce encapsulation
- Use the principle of **least privilege**: give access only where needed

> *"OOP is not hard. Practice makes it click. Keep coding!"*

---

*End of Reviewer*