# DSA Prelims Reviewer
### Modules 1–4: Foundations, Type Casting, Sorting & Recursion, Big O Notation
### + Java Quick-Syntax Appendix

> Tip: Read a section, then re-type its code sample from memory. If you can explain the *why* behind each line, you're ready for that topic on the exam.

---

## MODULE 1 — Introduction to Data Structures & Algorithms

### 1.1 The Core Idea
- **Data Structure** — the container/format that *holds* your data (organizes it in memory).
- **Algorithm** — the set of steps used to *solve a problem* using that data.
- Analogy: a cabinet with drawers is a data structure. How you search, sort, or arrange the drawers is the algorithm.

### 1.2 How Data Lives in Memory
Every variable lives in a numbered memory address — like a locker in a hallway:
1. Computer finds an **empty locker** (free memory slot)
2. That slot gets a unique **address**
3. The **value** is placed inside it (`int score = 10;`)
4. The **address is remembered** so the value can be fetched later

This is why structure affects speed:
- **Arrays** = adjacent lockers → fast index access
- **Linked Lists** = scattered lockers, each holding a note (pointer) to the next

### 1.3 Stack — LIFO (Last In, First Out)
🍽️ Analogy: a stack of plates — you only add/remove from the **top**.
Real use: **Undo (Ctrl+Z)** — every action is pushed; undo pops the most recent one first.

| Operation | Meaning |
|---|---|
| `push` | add item to top |
| `pop` | remove item from top |

**Pseudocode (Tagalog structural names, English logic):**
```
STRUCTURE Tumpok (Stack)
  LIST mgaSalansan
  FUNCTION walangLaman()
    RETURN true IF empty
  FUNCTION ipasok(halaga)
    ADD halaga to end
  FUNCTION ipakita()
    PRINT all items
END STRUCTURE
```

**Java:**
```java
class Tumpok {
    ArrayList<Integer> mgaSalansan = new ArrayList<>();
    boolean walangLaman() {
        return mgaSalansan.isEmpty();
    }
    void ipasok(int halaga) {
        mgaSalansan.add(halaga);
    }
    void ipakita() {
        System.out.println(mgaSalansan);
    }
}
```

**C++:**
```cpp
class Tumpok {
    vector<int> mgaSalansan;
    bool walangLaman() {
        return mgaSalansan.empty();
    }
    void ipasok(int halaga) {
        mgaSalansan.push_back(halaga);
    }
    void ipakita() {
        for (int x : mgaSalansan)
            cout << x << " ";
    }
};
```

**Dart:**
```dart
class Tumpok {
    List<int> mgaSalansan = [];
    bool walangLaman() {
        return mgaSalansan.isEmpty;
    }
    void ipasok(int halaga) {
        mgaSalansan.add(halaga);
    }
    void ipakita() {
        print(mgaSalansan);
    }
}
```
> Same method names, same logic — only syntax changes across languages. This is the pattern you'll see all through this reviewer.

### 1.4 Queue — FIFO (First In, First Out)
🚌 Analogy: a jeepney line — first to queue is first to board.
Real use: **printer queues** — first document sent is first printed.

| Operation | Meaning |
|---|---|
| `enqueue` | join the back of the line |
| `dequeue` | leave from the front |

### 1.5 Linear Search
Checks every item one by one until the target is found or the list ends.

- **Best case:** `O(1)` — target is the first item
- **Worst case:** `O(n)` — target is last or not present

```java
// Java
int linearSearch(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}
```
```cpp
// C++
int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}
```
```dart
// Dart
int linearSearch(List<int> arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}
```
All three: return the index if found, `-1` if not.

---

## MODULE 2 — Primitive Conversions, Type Casting & Language Nuances

### 2.1 Data Structure Refresher (with mechanics)

| Structure | Analogy | Mechanic |
|---|---|---|
| **Array** | Numbered wall of P.O. boxes | Instant index access; fixed size once built |
| **Linked List** | Scavenger hunt (each note points to next) | Elements scattered in memory, linked by pointers |
| **Stack** | Spring-loaded plate dispenser | LIFO — access only the top |
| **Queue** | Cinema box-office line | FIFO — insert at rear, remove at front |

### 2.2 Implicit vs Explicit Conversion

**Implicit (Widening) Conversion**
- Automatically converts a *smaller* type → *larger* type
- Zero risk of data loss → compiler does it silently

| Source | Target | Safety |
|---|---|---|
| `int` (32-bit) | `double` (64-bit) | 100% safe |

**Explicit (Narrowing) Conversion**
- Manually forces a *larger* type into a *smaller* container
- Risk of losing precision (e.g., decimal places) → must be declared explicitly with `(type)`

### 2.3 Widening & Narrowing — Java vs C++
```java
// Java
public class CastingDemo {
    public static void main(String[] args) {
        // 1. Implicit Widening (Automatic)
        int simpleInt = 201;
        double implicitDouble = simpleInt;
        System.out.println("Implicit Double: " + implicitDouble); // 201.0

        // 2. Explicit Narrowing (Manual)
        double precisePrice = 99.99;
        int truncatedPrice = (int) precisePrice;
        System.out.println("Truncated Int: " + truncatedPrice);   // 99 (data lost!)
    }
}
```
```cpp
// C++
int main() {
    // 1. Implicit Widening
    int simpleInt = 201;
    double implicitDouble = simpleInt;
    cout << "Implicit Double: " << implicitDouble << endl; // 201

    // 2. Explicit Narrowing (C-style or static_cast)
    double precisePrice = 99.99;
    int truncatedPrice = (int)precisePrice; // or static_cast<int>(precisePrice)
    cout << "Truncated Int: " << truncatedPrice << endl;   // 99 (data lost!)
    return 0;
}
```

### 2.4 Primitive → String (Object) Transformation
```java
public class Module2 {
    public static void main(String[] args) {
        int i = 100;
        String s = String.valueOf(i);     // primitive → String object

        System.out.println(i + 100); // 200   (arithmetic +)
        System.out.println(s + 100); // "100100" (text concatenation)
    }
}
```
```cpp
#include <string>
using namespace std;
int main() {
    int i = 100;
    string s = to_string(i);
    cout << i + 100 << endl;   // 200 (math)
    cout << s + "100" << endl; // "100100" (concatenation)
    return 0;
}
```
**Two Java ways to stringify an int** — both return equal results:
- `String.valueOf(i)` → `"100"`
- `Integer.toString(i)` → `"100"`

### 2.5 Narrowing, Overflow & Char Conversion (deep dive)
```java
// Narrowing double → int (fraction is truncated, not rounded)
public class Narrowing {
    public static void main(String[] args) {
        double pi = 3.14159;
        int intPi = (int) pi;   // explicit cast required
        System.out.println(intPi); // 3
    }
}
```
```java
// Overflow: exceeding int's range wraps around
public class Overflow {
    public static void main(String[] args) {
        int big = 2_000_000_000;
        int overflow = big * 2;          // wraps around
        System.out.println(overflow);    // -294967296
        long safe = (long) big * 2;      // cast BEFORE multiplying
        System.out.println(safe);        // 4000000000
    }
}
```
```java
// char <-> int conversion (via ASCII values)
char c = 'A';
int ascii = (int) c;          // 65
char back = (char) (ascii + 1); // 'B'
```

### 2.6 Type Promotion (mixed-type arithmetic)
```java
public class Promotion {
    public static void main(String[] args) {
        byte b = 10;
        int i = 5;
        double d = 2.5;
        // b + i -> promoted to int, then + d -> promoted to double
        double result = b + i + d;
        System.out.println(result); // 17.5

        // byte + byte -> promoted to int; must cast back to store as byte
        byte b1 = 10, b2 = 20;
        byte sum = (byte) (b1 + b2); // explicit cast needed
    }
}
```
**Binary numeric promotion rule:** convert operands to the *largest* type involved.
- `byte`, `short`, `char` → promoted to `int` when operated on
- if either operand is `long` → result is `long`
- if either operand is `float` → result is `float`
- if either operand is `double` → result is `double`

### 2.7 Language Comparison Cheat Sheet

| Language | Level | Style | Typical Use |
|---|---|---|---|
| **C++** | Low-level, compiled | Procedural + OOP, close to hardware/registers | OS, game engines, browsers |
| **Java** | High-level, OOP | Rich built-in collections (`ArrayList`, `Stack`, `Queue`, `LinkedList`) | Cross-platform apps, enterprise systems |
| **Python/Ruby** | High-level | Readable syntax, abstracted data structures | Rapid development, scripting |

---

## MODULE 2 (cont.) — Sorting & Recursion

### 2.8 Why Sort Data?
Sorting arranges elements in order (ascending/descending) so searches (like Binary Search) go from slow to fast, instead of checking every item.

### 2.9 Bubble Sort — Mechanism
- Compares **adjacent pairs**; swaps them if out of order.
- The largest unsorted item "bubbles up" to the end on every full pass.

**Pseudocode:**
```
FUNCTION ayusinAngLinyahan(array)
  SET n TO length of array
  FOR i FROM 0 TO n - 1
    FOR j FROM 0 TO n - i - 2
      IF array[j] > array[j + 1] THEN
        SWAP array[j] AND array[j + 1]
      END IF
    END FOR
  END FOR
END FUNCTION
```

- **Outer loop** → controls the number of passes
- **Inner loop** → compares/swaps adjacent pairs each pass
- **SWAP** → exchanges two elements when out of order

**Time Complexity**
| Case | Complexity | Why |
|---|---|---|
| Best | `O(n)` | Array already sorted — one pass, no swaps, stops early |
| Worst | `O(n²)` | Array in reverse order — every comparison swaps, nested loops run fully |

> Bubble Sort is great for learning but rarely used in production because of its `O(n²)` worst case.

**Java:**
```java
void ayusinAngLinyahan(int[] array) {
    int n = array.length;
    boolean mayPabago;
    for (int i = 0; i < n - 1; i++) {
        mayPabago = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
                mayPabago = true;
            }
        }
        if (!mayPabago) break; // already sorted -> stop early
    }
}
```
**C++:**
```cpp
void ayusinAngLinyahan(vector<int>& array) {
    int n = array.size();
    bool mayPabago;
    for (int i = 0; i < n - 1; i++) {
        mayPabago = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                swap(array[j], array[j + 1]);
                mayPabago = true;
            }
        }
        if (!mayPabago) break;
    }
}
```
> `mayPabago` ("did it change?") is a change-flag optimization: it lets both versions detect an already-sorted array and stop early, improving best case to `O(n)`.

### 2.10 Recursion — Functions That Call Themselves
Breaks a big problem into smaller versions of the **exact same problem** — like Russian nesting dolls: you must open each outer layer to reach the smallest one.

Every recursive function needs:
1. **Base case** — when to stop
2. **Recursive case** — how to break the problem down further

**Pseudocode:**
```
FUNCTION magbilangPabalik(n)
  IF n == 0 THEN
    RETURN "Tapos na!"
  ELSE
    RETURN magbilangPabalik(n - 1)
  END IF
END FUNCTION
```
**Java:**
```java
String magbilangPabalik(int n) {
    if (n == 0) return "Tapos na!";
    return magbilangPabalik(n - 1);
}
```
**C++:**
```cpp
string magbilangPabalik(int n) {
    if (n == 0) return "Tapos na!";
    return magbilangPabalik(n - 1);
}
```

**The Call Stack:** each call pushes a new *stack frame*. Once the base case is hit, frames pop off in reverse order — **LIFO**, same as the Stack structure from Module 1/2.

⚠️ **Stack Overflow:** too many nested calls without ever reaching a base case → crash. Always make sure your recursion has a clear stopping condition.

---

## MODULE 3 — Algorithms Deep Dive

### 3.1 Algorithm vs Data Structure (recap in context)
- **Data structure** — specialized format for organizing, processing, retrieving, and storing data.
- **Algorithm** — tool to resolve a problem *using* that data (e.g., how Facebook ranks your feed by engagement, not by post time).

### 3.2 The 4 Characteristics of a True Algorithm
A procedure only counts as an algorithm if it satisfies **all** of these:

| Characteristic | Meaning |
|---|---|
| **Clarity / Unambiguous** | Every step, input, and output has exactly one meaning |
| **Independent** | Steps stand on their own — not tied to one specific programming language |
| **Input & Output** | 0+ well-defined inputs, 1+ well-defined outputs |
| **Finiteness** | Must terminate after a *finite* number of steps — can't run forever |
| **Feasibility** | Must be achievable with the resources actually available |

### 3.3 Writing an Algorithm — Example (Add Two Numbers)
**Pseudocode:**
```
01 START
02 Declare three integers a, b, c
03 Define values of a & b
04 Add values of a & b
05 Store output of Step 4 to c
06 Print c
07 STOP
```
**Java:**
```java
public class Module3 {
    public static void main(String args[]) {
        int a, b, c;
        a = 80;
        b = 80;
        c = a + b;
        System.out.println("Value of c is" + " " + c);
    }
}
```

| Pseudocode step | Java line |
|---|---|
| declare a, b, c | `int a, b, c;` |
| define a & b | `a = 80; b = 80;` |
| add a & b | `c = a + b;` |
| print c | `System.out.println(...)` |

### 3.4 Math Expressions & Methods
- A **math expression** combines one or more operators: `+ - * / % && \|\|`
- A **method** is a reusable block of code, callable with `parameters`, so you don't rewrite the same logic repeatedly.
- Java ships a built-in `Math` class with ready-made methods.

| Method | What it does |
|---|---|
| `Math.max(x, y)` | highest number between x and y |
| `Math.min(x, y)` | lowest number between x and y |
| `Math.sqrt(x)` | square root of x |
| `Math.abs(x)` | absolute (positive) value of x |
| `Math.random()` | random number, `0.0` (incl.) to `1.0` (excl.) |

```java
public class Module3_1 {
    public static void main(String args[]) {
        int x = 100;
        int y = 200;
        System.out.println("Maximum data is = " + " " + Math.max(x, y)); // 200
        System.out.println("Minimum data is = " + " " + Math.min(x, y)); // 100
    }
}
```

### 3.5 Writing Your Own Method (custom `max_data`)
```java
public class Module3_2 {
    public static void main(String args[]) {
        int x = 100;
        int y = 200;
        int result = max_data(x, y);
        System.out.println("Max data is + " + " " + result);
    }

    static int max_data(int n1, int n2) {
        if (n1 > n2) {
            return n1;
        } else {
            return n2;
        }
    }
}
```
**Anatomy of a method:**
- `static int` — return type (gives back a whole number)
- `max_data(int n1, int n2)` — name + parameters accepted
- `if / else` — decides which value to return
- `return` — sends the result back to the caller

> This is literally how `Math.max()` works under the hood.

---

## APPENDIX — Java Quick-Syntax Reference
*(from "Java in 15 Minutes" — use this as a fast lookup while reading the modules above)*

### A.1 The `main` Method (entry point)
```java
public static void main(String[] args) {
    // Your code goes here!
}
```
- `public` — accessible from anywhere
- `static` — callable without creating an object
- `void` — returns nothing
- `main` — the method's name
- `String[] args` — command-line arguments

### A.2 Variables & Primitive Types
```java
int myInt = 7;
double shoeSize = 9.5;
char myInitial = 'J';
boolean isJavaFun = true;
```
| Type | Stores |
|---|---|
| `int` | whole numbers |
| `double` | decimal numbers |
| `char` | a single character |
| `boolean` | true / false |

### A.3 Operators
```java
System.out.println(myInt * shoeSize); // 66.5
```
`+` addition · `-` subtraction · `*` multiplication · `/` division

### A.4 Strings (non-primitive, capital `S`)
```java
String myName = "John";
System.out.println(myName.length());        // 4
System.out.println(myName.toUpperCase());   // JOHN
System.out.println(myName.getClass().getSimpleName()); // String
```

### A.5 Methods, Parameters & Return Values
```java
private static void burp() {
    System.out.println("Burp!");
}

private static void printName(String name, int number) {
    System.out.println("My name is " + name + " and my number is " + number);
    System.out.printf("My name is %s and my number is %d\n", name, number);
}

private static String getName() {
    return "My name is John";
}
```

### A.6 Conditionals
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
> Use `.equals()` to compare Strings — **not** `==`.

### A.7 Comparison Operators
`==` equal to · `!=` not equal to · `>` greater than · `<` less than · `>=` greater/equal · `<=` less/equal
> Double equals `==` compares. Single equals `=` assigns.

### A.8 Loops
```java
for (int i = 0; i < 10; i++) {
    System.out.println("These pretzels are making me thirsty!");
}
```
- `int i = 0` — start value
- `i < 10` — loop condition
- `i++` — increment after each pass

### A.9 Classes & Objects
- **Class** = blueprint (a cookie cutter)
- **Object** = actual instance made from that blueprint (the cookie)

```java
public class Cat {
    String name;
    int age;
    public void meow() {
        System.out.println("Meow!");
    }
}

// Creating objects
Cat myCat = new Cat();
myCat.name = "Fred";
myCat.age = 6;
myCat.meow(); // Meow!
```

### A.10 Static vs Non-Static
```java
public class Cat {
    public void meow() {                 // non-static: belongs to an object
        System.out.println("Meow!");
    }
    public static void dingDong() {      // static: belongs to the class itself
        System.out.println("Ding dong!");
    }
}

Cat.dingDong();     // works
Cat myCat = new Cat();
myCat.meow();        // works
// Cat.meow();       // ERROR — can't call non-static on the class
```

---

## FINAL SUMMARY CHEAT SHEET

| Concept | One-liner |
|---|---|
| Data Structure | How data is organized/stored |
| Algorithm | Steps to solve a problem with that data |
| Array | Fixed-size, indexed, instant access |
| Linked List | Scattered, pointer-linked, flexible size |
| Stack | LIFO — push/pop from the top |
| Queue | FIFO — enqueue at back, dequeue at front |
| Implicit (Widening) Cast | Small → big type, automatic, safe |
| Explicit (Narrowing) Cast | Big → small type, manual, risks data loss |
| Type Promotion | Smaller types auto-promoted to the largest type in an expression |
| Bubble Sort | Compare & swap adjacent pairs repeatedly; O(n) best / O(n²) worst |
| Recursion | Function calls itself; needs a base case + recursive case |
| Algorithm characteristics | Unambiguous, independent, defined I/O, finite, feasible |
| O(1) | Constant — vending machine |
| O(log n) | Logarithmic — phone book (halving) |
| O(n) | Linear — checking every pocket |
| O(n²) | Quadratic — nested loops |

**Good luck sa prelims! 💪**