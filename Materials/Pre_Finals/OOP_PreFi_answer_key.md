# EL 101: Pre-Final Periodical Exam — Answer Key

## Section I: Multiple Choice

1. **B** — Declaring a member `static` creates a single copy shared across all class instances.
2. **C** — Static context has no implicit `this` or object instance, resulting in a compile-time error.
3. **A** — The JVM calls `main()` before creating any object instances of the class.
4. **C** — `final` locks a field's value after initialization.
5. **B** — Overriding replaces the superclass implementation using the identical method signature.
6. **C** — Valid array indices run from `0` to `length - 1`; accessing `length` throws `ArrayIndexOutOfBoundsException`.
7. **B** — Java uses `implements` for interfaces and permits implementing multiple interfaces.
8. **A** — Java is strictly pass-by-value; object references are copied when passed into methods.
9. if explained correctly it will be 6 pts
10. **B** — `super()` calls the superclass constructor from inside a subclass constructor.

## Section II: Identification

11. Encapsulation
12. `static`
13. Constructor Chaining (or Constructor Overloading)
14. `extends`
15. Abstract class
16. Field access (array field)
17. `super`
18. Method Overloading
19. `implements`
20. `ArrayIndexOutOfBoundsException`

## Section III: 4 pillars of OOP Enumeration

21. inheritance
22. Abstract
23. Polymorphism
24. Enscapsulation

## Section IV: Guess the Output

25. `101-102-103`
26. `Running `
27. `150.0`
28. `DOC`
29. `10`
30. `25`
31. `int 5`
32. `12`
33. `Compile Error` (non-static field `price` cannot be referenced from a static context)
34. `2 Blue`

## Section V: Coding Problems (Sample Solutions)

### 35. Static Methods & Shared Counter

```java
public class CounterItem {
    private static int itemTracker = 0;
    private String name;

    public CounterItem(String name) {
        this.name = name;
        itemTracker++;
    }

    public static int getItemTracker() {
        return itemTracker;
    }

    public static void main(String[] args) {
        CounterItem c1 = new CounterItem("Alpha");
        CounterItem c2 = new CounterItem("Beta");
        System.out.println(CounterItem.getItemTracker());
    }
}
```

### 36. Abstract Class Implementation

```java
abstract class AbstractLogger {
    public abstract void log(String msg);
}

public class ConsoleLogger extends AbstractLogger {
    @Override
    public void log(String msg) {
        System.out.println("[LOG]: " + msg);
    }

    public static void main(String[] args) {
        AbstractLogger logger = new ConsoleLogger();
        logger.log("System Ready");
    }
}
```

### 37. Inheritance & Super Method Call

```java
class BasePricing {
    public double getPrice() {
        return 100.0;
    }
}

public class DiscountedPricing extends BasePricing {
    @Override
    public double getPrice() {
        return super.getPrice() - 20.0;
    }

    public static void main(String[] args) {
        DiscountedPricing dp = new DiscountedPricing();
        System.out.println(dp.getPrice());
    }
}
```

### 38. Interface Implementation

```java
interface Encryptor {
    void encrypt();
}

public class SimpleEncryptor implements Encryptor {
    @Override
    public void encrypt() {
        System.out.println("Encrypting data...");
    }

    public static void main(String[] args) {
        Encryptor enc = new SimpleEncryptor();
        enc.encrypt();
    }
}
```
total of 55