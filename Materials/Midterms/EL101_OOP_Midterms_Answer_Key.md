# EL 101 — OOP Midterms Examination
## Answer Key: Java Methods & Access Modifiers

**Time Allotment:** 2 hours · **Total Items:** 43 · **Total Points:** 60

---

## I. CODING PROBLEMS — 15 points

### 1. Access Modifiers — Employee (5 pts)

```java
public class Employee {
    private String name;
    private double salary;

    public Employee(String n) {
        name = n;       // or this.name = n;
        salary = 0;
    }

    public String getName() {
        return name;
    }

    public void raiseSalary(double amount) {
        if (amount > 0) {
            salary = salary + amount;   // or salary += amount;
        }
    }
}
```

**Notes / grading cues**
- `name` and `salary` stay `private`
- Constructor assigns `name` and initializes `salary` to `0`
- `getName()` simply returns `name`
- `raiseSalary` only mutates when `amount > 0` (negative values ignored)

---

### 2. Creating Your Own Methods — Temperature Converter (5 pts)

```java
public class TemperatureConverter {

    public static double celsiusToFahrenheit(double c) {
        return c * 9.0 / 5 + 32;   // or: return c * 9 / 5.0 + 32;
    }

    public void displayTemp(double c) {
        System.out.println(celsiusToFahrenheit(c));
    }

    public static void main(String[] args) {
        TemperatureConverter tc = new TemperatureConverter();
        tc.displayTemp(100);   // prints 212.0
    }
}
```

**Notes / grading cues**
- `celsiusToFahrenheit` is `public static` and returns the formula
- Prefer `9.0` or `5.0` so integer division does not truncate (though `c * 9 / 5` still works when `c` is `double`)
- `displayTemp` is an **instance** method that calls the static helper and prints

---

### 3. Combined — Vehicle (5 pts)

```java
public class Vehicle {
    private String brand;
    private int mileage;

    public Vehicle(String brand) {
        this.brand = brand;
        this.mileage = 0;
    }

    public void drive(int km) {
        if (km > 0) {
            mileage = mileage + km;   // or mileage += km;
        }
    }

    public int getMileage() {
        return mileage;
    }

    public static double milesToKm(double miles) {
        return miles * 1.60934;
    }

    public static void main(String[] args) {
        Vehicle v = new Vehicle("Toyota");  // any brand string is fine
        v.drive(100);
        System.out.println(v.getMileage());      // 100
        System.out.println(Vehicle.milesToKm(50)); // 80.467
        // or: System.out.println(milesToKm(50));
    }
}
```

**Notes / grading cues**
- Both fields `private`; mileage starts at `0`
- `drive` only adds when `km > 0`
- `milesToKm` is `public static`
- `main` creates an object, drives 100 km, prints mileage, then prints the conversion

---

## II. IDENTIFICATION — 5 points

| # | Answer |
|---|--------|
| 1 | **static** |
| 2 | **private** |
| 3 | **default** (package-private / package-level) |
| 4 | **Encapsulation** |
| 5 | **Instance method** (non-static method) |

---

## III. SCENARIO-BASED IDENTIFICATION — 5 points

*Word bank: Static Method · Instance Method · private · default · protected · public · Encapsulation · Class · Object · Field*

| # | Answer |
|---|--------|
| 1 | **Static Method** |
| 2 | **private** |
| 3 | **protected** |
| 4 | **Instance Method** |
| 5 | **public** |

---

## IV. GUESS THE OUTPUT — 10 points (2 pts each)

| # | Output | Brief reason |
|---|--------|--------------|
| 1 | **3** | `increment()` called three times on the shared `static` field `count` |
| 2 | **5** | `size` is private but accessible via the public getter `getSize()` |
| 3 | **Hello, Warrior** | `name` has default (package) access, so `main` can reassign it; `greet()` prints the new value |
| 4 | **50.0** | `100 − 30 − 20 = 50`; private field mutated only through the public method |
| 5 | **15** | Static field `total` updated via class name: `10 + 5 = 15` |

---

## V. MULTIPLE CHOICE — 25 points

| # | Answer | Key idea |
|---|--------|----------|
| 1 | **B** | A method is a block of code that runs when called |
| 2 | **B** | `static` marks a method as belonging to the class |
| 3 | **B** | Call static methods with `ClassName.methodName()` |
| 4 | **C** | Instance methods require an object first (`new`) |
| 5 | **C** | Static methods belong to the class itself |
| 6 | **C** | Instance methods can access instance fields; static methods cannot (without an object reference) |
| 7 | **D** | `private` = class only |
| 8 | **C** | No modifier → default (package-private) |
| 9 | **C** | `protected` = same package + subclasses (even other packages) |
| 10 | **D** | `public` has the widest visibility |
| 11 | **B** | Most → least restrictive: private, default, protected, public |
| 12 | **B** | Direct access to a private member → **compile-time error** |
| 13 | **C** | Private fields + public methods enforce encapsulation |
| 14 | **C** | Subclass in another package needs `protected` or `public` |
| 15 | **B** | Default access is visible package-wide (subclass not required) |
| 16 | **C** | Access modifiers primarily support **Encapsulation** |
| 17 | **B** | Method that belongs to an object = **instance method** |
| 18 | **C** | Yes / Yes / Yes / No pattern = **protected** |
| 19 | **D** | Getters are normally `public` |
| 20 | **C** | Private field is changed from outside only via a public setter |
| 21 | **A** | Wishing does nothing — you must edit the code |
| 22 | **B** | Least privilege = tightest access that still works |
| 23 | **B** | A static field belongs to the class and is shared by all objects |
| 24 | **C** | Static method cannot access instance fields without an object |
| 25 | **C** | Narrowing a public API later is usually harder than starting tight |

---

## Quick Reference (for self-check)

### Static vs Instance
| | Static | Instance |
|---|--------|----------|
| Belongs to | Class | Object |
| Call style | `ClassName.method()` | `obj.method()` |
| Needs `new`? | No | Yes |
| Can touch instance fields? | No (without an object) | Yes |

### Visibility Matrix
| Modifier | Same class | Same package | Subclass (other package) | World |
|----------|------------|--------------|---------------------------|-------|
| **private** | ✓ | ✗ | ✗ | ✗ |
| **default** | ✓ | ✓ | ✗ | ✗ |
| **protected** | ✓ | ✓ | ✓ | ✗ |
| **public** | ✓ | ✓ | ✓ | ✓ |

### Rule of thumb
> Pick the **tightest** access level that still gets the job done.

---

*End of Answer Key — Good luck, and happy brewing ☕*
