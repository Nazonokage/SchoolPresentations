# ☕ PRELIM EXAM — ANSWER KEY
### *"The Java Roastery: Brew Your Brain a Little"* (Modules 1–4)
**Total: 60 points**

---

## PART I — Multiple Choice (27 items, 1 pt each)

| # | Answer | Why |
|---|---|---|
| 1 | **C** | An object is an instance of a *class*, not a method or program. |
| 2 | **B** | The class is the cookie cutter (template); objects are the cookies made from it. |
| 3 | **B** | `class` is the keyword used to define a class in Java. |
| 4 | **C** | `adidas` is the object/instance created from the `Sapatos` class. |
| 5 | **B** | `new` creates a new instance (object) of a class. |

| 6 | **C** | The 4 pillars are Abstraction, Encapsulation, Inheritance, Polymorphism — "Compilation" isn't one of them. |
| 7 | **B** | Encapsulation bundles data + methods and protects data from outside tampering. |
| 8 | **B** | Polymorphism = same method name, different behavior per object/class. |
| 9 | **B** | A constructor is a special method that runs automatically when an object is created. |
| 10 | **B** | A constructor's name must match its class name exactly. |

| 11 | **B** | `this` refers to the current object. |
| 12 | **A** | Python uses `self` where Java/JS use `this` and PHP uses `$this`. |
| 13 | **C** | Python doesn't use `new` — you just call `ClassName(...)`. |
| 14 | **B** | A field is also called an attribute or instance variable. |
| 15 | **A** | A local variable is declared inside a method/block and scoped only to it. |

| 16 | **B** | The dot operator accesses an object's fields/methods. |
| 17 | **A** | Nothing's wrong — this is correct dot-operator usage on an object instance. |
| 18 | **B** | State refers to the data an object holds (its fields' values). |
| 19 | **B** | Behavior refers to what an object does — defined by its methods. |
| 20 | **C** | `int x;` is a Data Member (a field). The others involve `{}` runnable code, making them Function Members. |

| 21 | **B** | `public` allows access from anywhere in the project. |
| 22 | **B** | A getter returns/reads a private field's value. |
| 23 | **B** | Getters/setters let you control and validate access to data (encapsulation). |
| 24 | **B** | An unset `int` field defaults to `0` in Java. |
| 25 | **C** | `bark`, `meow`, `quack` are behaviors/methods — the actions the objects (Dog, Cat, Duck) perform. |
| 26 | **B** | A compiler translates source code into machine-readable instructions. |
| 27 | **B** | Java's "write once, run anywhere" comes from the JVM interpreting compiled bytecode on any platform. |

---

## PART II — Identification (7 items, 1 pt each)

1. **Constructor**
2. **Identity** (the unique reference/memory address the JVM uses to distinguish objects)
3. **Field** (also accepted: attribute / instance variable)
4. **private**
5. **Instantiation**
6. **Getter** (accessor method)
7. **JVM** (Java Virtual Machine)

---

## PART III — Guess the Output (3 items, 2 pts each)

**1.**
```
Bruno says Woof!
```
*Trace:* `d1.name` is reassigned from `"Bantay"` to `"Bruno"` **before** `bark()` is called, so `bark()` prints the updated value.

**2.**
```
Total: 65
```
*Trace:* `10 + 25 + 30 = 65`. The loop adds each element of the array to `total` one index at a time (`sales[0]`, `sales[1]`, `sales[2]`).

**3.**
```
Balance: 50.0
```
*Trace:* `setBalance(-20)` is called, but the setter's `if (amount >= 0)` check rejects negative values, so `balance` stays at its original value of `50`. `getBalance()` then returns that unchanged value. *(Accept "Balance: 50" without the decimal — either is correct.)*

---

## PART IV — Coding Problems (4 items, 5 pts each)

> **Grading guide:** 5 pts total for each item — award partial credit for correct structure even if minor syntax slips occur (e.g., missing semicolon but correct logic). Suggested breakdown noted per item.

### 1. Barista Class — Constructor (5 pts)
```java
public class Barista {
    String name;
    int yearsExperience;

    public Barista(String name, int yearsExperience) {
        this.name = name;
        this.yearsExperience = yearsExperience;
    }

    public static void main(String[] args) {
        Barista b1 = new Barista("Ana", 3);
        System.out.println(b1.name);
    }
}
```
**Rubric:** Constructor with correct parameters (2 pts) · correct `this.field = param` assignment (1 pt) · object creation with `new` (1 pt) · correct print statement (1 pt).

---

### 2. MenuItem — Getter & Setter (5 pts)
```java
public class MenuItem {
    private double price;

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        if (price >= 0) {
            this.price = price;
        }
    }
}
```
**Rubric:** Getter returns the field correctly (2 pts) · setter exists with correct parameter (1 pt) · negative-value validation (`if (price >= 0)` or equivalent) (2 pts).

---

### 3. Coffee Class — Constructor + Method (5 pts)
```java
public class Coffee {
    String size;
    String roastLevel;

    public Coffee(String size, String roastLevel) {
        this.size = size;
        this.roastLevel = roastLevel;
    }

    public void describe() {
        System.out.println("This is a " + size + " cup with a " + roastLevel + " roast.");
    }

    public static void main(String[] args) {
        Coffee c1 = new Coffee("Medium", "Light");
        Coffee c2 = new Coffee("Large", "Dark");
        c1.describe();
        c2.describe();
    }
}
```
**Rubric:** Constructor with both fields set (2 pts) · `describe()` method printing both values (2 pts) · two objects instantiated and both called correctly (1 pt).

---

### 4. SalesTracker — Array Edition (5 pts)
```java
public class SalesTracker {

    public static int getTotal(int[] arr) {
        int total = 0;
        for (int i = 0; i < arr.length; i++) {
            total = total + arr[i];
        }
        return total;
    }

    public static double getAverage(int[] arr) {
        return (double) getTotal(arr) / arr.length;
    }

    public static void main(String[] args) {
        int[] sales = {120, 95, 200, 150, 175};

        System.out.println("Total Sales: " + getTotal(sales));
        System.out.println("Average Sales: " + getAverage(sales));
    }
}
```
**Expected Output:**
```
Total Sales: 740
Average Sales: 148.0
```
**Rubric:** Array declared correctly with 5 values (1 pt) · `getTotal()` loops and returns correct sum (2 pts) · `getAverage()` correctly reuses `getTotal()` instead of recalculating (1 pt) · correct output printed in `main` (1 pt).
*(Accept `int` division giving `148` instead of `148.0` if the student didn't cast to `double` — deduct 0.5 pt for the imprecise average logic, not a full miss, since the loop/reuse structure is what's being tested.)*

---

## 📊 Scoring Summary

| Part | Items | Pts each | Total |
|---|---|---|---|
| I. Multiple Choice | 27 | 1 | 27 |
| II. Identification | 7 | 1 | 7 |
| III. Guess the Output | 3 | 2 | 6 |
| IV. Coding Problems | 4 | 5 | 20 |
| **TOTAL** | **41 items** | | **60 pts** |

☕ *End of Answer Key.*
