---
marp: true
theme: default
paginate: true
---

# Introduction to Object-Oriented Programming (OOP)
### Java • Python • JavaScript • PHP

---

## What is OOP?

Object-Oriented Programming (OOP) is a programming style that organizes code around **objects** rather than just functions and logic.

- An object is a real-world "thing" with **properties** (data) and **behaviors** (actions).
- A **class** is the blueprint used to create objects.
- OOP makes code more organized, reusable, and easier to maintain as projects grow.

---

## The Shoe Analogy

Think of a **class** as a shoe design/template, and the **objects** as actual pairs of shoes made from that design.

- **Class:** `Sapatos` (Shoe) — defines what a shoe generally has: a color, a size, a brand, and things it can do (like being worn or laced up).
- **Objects:** `Adidas`, `Nike`, `Puma` — these are actual instances created from the `Sapatos` blueprint. Each one has its own specific brand, color, and size, but they all follow the same shoe structure.

This is exactly why a class is called a **template**, and an object is called an **instance** of that class — just like the car illustration (class `car` → objects `Toyota`, `Honda`, `Ford`).

---

## Why Use OOP? (Facts & Use Cases)

- **Reusability** – Write a class once, create as many objects as you need (e.g., one `Sapatos` class → unlimited shoe objects).
- **Encapsulation** – Keeps data safe by bundling it with the methods that use it.
- **Scalability** – Large applications (banking systems, games, e-commerce sites) are easier to manage when broken into classes/objects.
- **Real-world modeling** – OOP mirrors how we naturally think about things: cars, shoes, animals, users, products.
- **Used in industry** – Most modern languages (Java, Python, JS, PHP, C#, C++) support OOP because it's the standard for building maintainable software like mobile apps, websites, and enterprise systems.

---

## The 4 Basic Principles of OOP (Preview)

1. **Abstraction** – hiding complex details, showing only what's needed
2. **Encapsulation** – bundling data and methods, protecting data
3. **Inheritance** – a class can inherit properties/behavior from another class
4. **Polymorphism** – the same method can behave differently depending on the object

*(These will be explored in detail in later slides/topics — this deck focuses on the introduction.)*

---

## OOP in Java ☕

Java is a **class-based**, strongly-typed OOP language. Every piece of code lives inside a class.

```java
public class Sapatos {
    // mga katangian (attributes/properties)
    String kulay;
    int sukat;

    // constructor - gumagawa ng bagong sapatos object
    public Sapatos(String kulay, int sukat) {
        this.kulay = kulay;
        this.sukat = sukat;
    }

    // method - kilos/galaw ng object
    public void takbo() {
        System.out.println("Ang sapatos na " + kulay + " ay tumatakbo!");
    }

    public static void main(String[] args) {
        // paggawa ng mga object mula sa class na Sapatos
        Sapatos adidas = new Sapatos("itim", 42);
        Sapatos nike = new Sapatos("puti", 41);

        adidas.takbo();
        nike.takbo();
    }
}
```

**Explanation:** The class `Sapatos` (Shoe) defines two attributes, `kulay` (color) and `sukat` (size), plus a method `takbo()` (run). In `main()`, two objects (`adidas` and `nike`) are created from the same class using the `new` keyword and the constructor. Each object holds its own independent data, but shares the same behavior defined by the class.

---

## OOP in Python 🐍

Python OOP is simpler in syntax, using `class` and `self` to refer to the current object.

```python
class Sapatos:
    # constructor - tumatakbo tuwing may bagong object
    def __init__(self, kulay, sukat):
        self.kulay = kulay   # katangian: kulay (color)
        self.sukat = sukat   # katangian: sukat (size)

    # method - galaw ng object
    def takbo(self):
        print(f"Ang sapatos na {self.kulay} ay tumatakbo!")

# paggawa ng mga object
adidas = Sapatos("itim", 42)
puma = Sapatos("kulay abo", 40)

adidas.takbo()
puma.takbo()
```

**Explanation:** `__init__` is Python's constructor — it runs automatically whenever a new `Sapatos` object is created, setting its `kulay` and `sukat`. The `self` parameter always refers to the specific object calling the method, which is how each object (`adidas`, `puma`) keeps its own separate data even though they share the same class definition.

---

## OOP in JavaScript 🟨

Modern JavaScript uses `class` syntax (ES6+), though it's built on prototypes under the hood.

```javascript
class Sapatos {
    // constructor - gumagawa ng bagong object
    constructor(kulay, sukat) {
        this.kulay = kulay;   // katangian: kulay
        this.sukat = sukat;   // katangian: sukat
    }

    // method - galaw ng object
    takbo() {
        console.log(`Ang sapatos na ${this.kulay} ay tumatakbo!`);
    }
}

// paggawa ng mga object
const adidas = new Sapatos("itim", 42);
const nike = new Sapatos("puti", 41);

adidas.takbo();
nike.takbo();
```

**Explanation:** The `Sapatos` class has a `constructor` that runs when `new Sapatos(...)` is called, setting up `kulay` and `sukat` for that specific object. `this` refers to the current object instance, so `adidas.takbo()` and `nike.takbo()` produce different output even though they call the exact same method.

---

## OOP in PHP 🐘

PHP is widely used for web development and fully supports class-based OOP, similar to Java.

```php
<?php
class Sapatos {
    // mga katangian (properties)
    public $kulay;
    public $sukat;

    // constructor
    public function __construct($kulay, $sukat) {
        $this->kulay = $kulay;
        $this->sukat = $sukat;
    }

    // method
    public function takbo() {
        echo "Ang sapatos na " . $this->kulay . " ay tumatakbo!\n";
    }
}

// paggawa ng mga object
$adidas = new Sapatos("itim", 42);
$puma   = new Sapatos("kulay abo", 40);

$adidas->takbo();
$puma->takbo();
?>
```

**Explanation:** `__construct()` is PHP's constructor method, automatically called when a new `Sapatos` object is instantiated. The `$this->` syntax accesses the current object's own properties, and `->` (arrow operator) is used to call methods on an object, e.g. `$adidas->takbo()`.

---

## Quick Comparison

| Language   | Constructor        | "Current object" keyword | Object creation      |
|------------|--------------------|---------------------------|-----------------------|
| Java       | `Sapatos(...)`      | `this`                    | `new Sapatos(...)`    |
| Python     | `__init__(self,...)`| `self`                    | `Sapatos(...)`        |
| JavaScript | `constructor(...)`  | `this`                    | `new Sapatos(...)`    |
| PHP        | `__construct(...)`  | `$this`                   | `new Sapatos(...)`    |

---

## Key Takeaway

- All four languages follow the **same OOP concept**: a class is a blueprint, an object is an instance.
- Syntax differs, but the logic is identical — this is why learning OOP once makes it easier to pick up **any** OOP language.
- Just like `Sapatos` → `Adidas`, `Nike`, `Puma`, or `car` → `Toyota`, `Honda`, `Ford`: **one class, many unique objects.**
