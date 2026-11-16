# Complete DSA Reviewer: Big O, Linked Lists, Stacks & Queues

---

# Title & Overview

## Data Structures and Algorithms — Comprehensive Reviewer

This reviewer consolidates four essential topics from a Data Structures and Algorithms (DSA) course: **Big O Notation**, **Linked Lists**, **Stacks (Part 2)**, and **Queues (Part 2)**. The material covers the fundamental concepts of algorithm analysis, linear data structures, their operations, implementations in Java, and real-world applications.

**Learning Objectives:**
- Understand Big O notation and classify algorithms by their growth rates
- Define and implement singly and doubly linked lists
- Explain stack operations (push, pop, peek) and identify underflow conditions
- Differentiate between linear and circular queues
- Apply these data structures to real-world computing problems
- Trace operations step by step through memory diagrams and code

---

# Table of Contents

1. [Big O Notation](#1-big-o-notation)
   - 1.1 What is Big O?
   - 1.2 Reading the Notation
   - 1.3 Growth Families
   - 1.4 Comparison Chart
   - 1.5 How to Calculate Big O — Step by Step
   - 1.6 Worked Examples
2. [Linked Lists](#2-linked-lists)
   - 2.1 What is a Linked List?
   - 2.2 Anatomy of a Node
   - 2.3 Linked List vs. Array
   - 2.4 Singly Linked List
   - 2.5 Doubly Linked List
   - 2.6 java.util.LinkedList
   - 2.7 Operations: Insertion and Deletion
3. [Stacks (Part 2)](#3-stacks-part-2)
   - 3.1 Quick Recap: Push and Pop
   - 3.2 Peek / Top
   - 3.3 Underflow
   - 3.4 Applications of Stacks
4. [Queues (Part 2)](#4-queues-part-2)
   - 4.1 Quick Recap: Enqueue and Dequeue
   - 4.2 Front / Peek
   - 4.3 Linear Queue — The Wasted-Space Problem
   - 4.4 Circular Queue — Reusing Space
   - 4.5 Applications of Queues
5. [Key Takeaways / Summary Box](#5-key-takeaways--summary-box)
6. [Important Terms / Glossary](#6-important-terms--glossary)
7. [Possible Review Questions](#7-possible-review-questions)
8. [Source Notes](#8-source-notes)

---

# 1. Big O Notation

## 1.1 What is Big O?

**Big O notation** is a way to describe how an algorithm's speed (or memory usage) changes as the amount of data (`n`) grows — without getting lost in exact seconds or clock cycles.

### Key Ideas:
- **Big O describes complexity** using algebraic terms — it's a label for how fast the workload grows, not a stopwatch reading.
- **`n`** = the input size (how many items you're working with)
- **`g(n)`** = the function inside `O()` that estimates the workload relative to `n`
- **`O( )`** = "Order of" — the growth family (category label)

### Example: `O(n²)` is read "Big O squared" — if you double the input, the work roughly quadruples.

### Analogy:
Imagine you're a waiter. Instead of timing every table with a stopwatch, you just ask: *"If the restaurant fills up with twice as many guests, does my workload stay the same, double, or explode?"* That question — **"how does effort scale as things grow?"** — is exactly what Big O answers for code.

---

## 1.2 Reading the Notation

| Symbol | What it means | Everyday translation |
|--------|---------------|---------------------|
| `n` | The input size | "How many things am I dealing with?" |
| `g(n)` | Function describing workload vs. `n` | "The recipe for how the effort grows" |
| `O( )` | "Order of" — the growth family | Category label: Small / Medium / Large / XL |
| `O(n²)` | `g(n) = n²` | Double the input → roughly 4x the work |

### Beginner Tip:
You'll almost never need to calculate Big O with a formula by hand. Instead, look at your **loops** — they're the biggest clue:
- One loop over `n` items → usually O(n)
- A loop nested inside another → usually O(n²)
- Loop counter doubles each step → O(log n)

---

## 1.3 Growth Families

### O(1) — Constant Time

**What it means:** The work doesn't grow, no matter how big the input gets.

**Analogy: Vending Machine**
Press B4 on a vending machine and your chips drop out. It doesn't matter if the machine has 10 snacks or 10,000 snacks loaded inside — pressing B4 always takes the same amount of time.

**Java Example:**
```java
public class BigODataExample {
    public static void main(String[] args) {
        int n = 1000;
        System.out.println("Your input is: " + n);
    }
}
```

**Golden Rule:** O(1), O(2), and even O(1000) all mean the exact same thing: constant time. Big O ignores the exact count — it only cares whether it changes with `n`.

---

### O(log n) — Logarithmic Time

**What it means:** Each step cuts the remaining problem in half. Grows very slowly.

**Analogy: Phone Book**
Looking for "Rodriguez" in a phone book, you don't start from page 1. You flip to the **middle**, see you're too early or too late, and jump to the middle of the correct half — again and again. Each step cuts the remaining pages in half.

**Java Example:**
```java
for (int i = 1; i < n; i = i * 2) {
    System.out.println("Opps-I am busy, grinding this thing: " + i);
}
```
- With `n = 8`, it only takes 3 steps because `log₂(8) = 3`
- Spot doubling/halving in a loop → suspect O(log n)

---

### O(n) — Linear Time

**What it means:** The effort grows directly in proportion to the input size.

**Analogy: Checking Every Pocket**
You lost your keys and check your pockets one at a time — jacket, jeans, backpack — until you find them. If you have 4 pockets, that's 4 checks. 8 pockets, 8 checks.

**Java Example:**
```java
for (int i = 0; i < n; i++) {
    System.out.println("Oops - I am busy, grinding this thing: " + i);
}
```

**Golden Rule:** We'd prefer `0.1n` over `1000n + 1000`, but both are still linear. Big O simplifies: `O(2n + 1)` is treated exactly the same as `O(n)`.

---

### O(n²) — Quadratic Time

**What it means:** Work grows by the square of the input size. Double the input → roughly 4x the work.

**Pattern:** Loop inside a loop, both 0→n — outer runs n times; for each lap, inner also runs n times → n × n

---

## 1.4 Comparison Chart

| Growth Rate | Name | As `n` grows |
|-------------|------|--------------|
| O(1) | Constant | Flat forever |
| O(log n) | Logarithmic | Climbs fast, then levels off |
| O(n) | Linear | Steady, straight diagonal |
| O(n²) | Quadratic | Starts calm, then explodes |

**Rule of thumb:** When comparing algorithms for the same job, lower on this chart is better as `n` grows.

---

## 1.5 How to Calculate Big O — Step by Step

Follow these four steps every time you look at a piece of code:

| Step | Action |
|------|--------|
| **① Count** | Count each distinct block of work — a single statement, a loop, or a nested loop. Don't add them yet; just list them. |
| **② Label** | Single statement → O(1), One loop over n → O(n), Loop counter doubles each step → O(log n), Loop inside a loop → O(n²) |
| **③ Add** | If blocks run one after another, add their labels. Example: O(1) + O(n) + O(n) = O(2n + 1). Keep the **dominant (biggest) term** only. |
| **④ Simplify** | Drop constants and lower-order terms. O(2n + 1) → O(n). O(5n² + 3n + 10) → O(n²). O(4) → O(1). |

**Quick Heuristic:** As `n` doubles:
- Does the work stay the same? → O(1)
- Does it roughly double? → O(n)
- Does it roughly quadruple? → O(n²)
- Does it grow much slower than n? → O(log n)

---

## 1.6 Worked Examples

| Code Pattern | What to Notice | Big O Result |
|--------------|---------------|--------------|
| `System.out.println(n);` | One fixed statement, no loop | **O(1)** |
| `for (int i=0; i<n; i++)` | Counter goes 0 → n one step at a time, runs n times | **O(n)** |
| `for (int i=1; i<n; i=i*2)` | Counter doubles each lap → log₂(n) steps | **O(log n)** |
| Loop inside a loop, both 0→n | Outer runs n times; inner also runs n times → n × n | **O(n²)** |
| O(1) block, then O(n) loop | Add: O(1) + O(n) = O(n+1) → drop constant | **O(n)** |
| `O(2n + 1000n + 5)` | Combine coefficients: 1002n + 5 → drop constants | **O(n)** |

### Pattern Cheat-Sheet:
- **O(1)** → no loop, or loop with fixed count
- **O(log n)** → counter multiplies/divides each step
- **O(n)** → single loop 0→n
- **O(n²)** → nested loops both 0→n

---

# 2. Linked Lists

## 2.1 What is a Linked List?

A **linked list** is a linear data structure where elements (**nodes**) are not sitting next to each other in memory. Instead, each node holds the address of the **next** one, like a paper trail: each note tells you where to find the next clue.

### Key Idea:
The nodes themselves are not "in order" in memory — the **pointers** are what create the order.

### Memory Diagram:
```
HEAD → [10] → [20] → [30] → null
```
Each box represents a node stored at a different memory address, connected only by NEXT pointers.

---

## 2.2 Anatomy of a Node

Every node in a **singly linked list** has exactly two parts:

| Component | Description |
|-----------|-------------|
| **DATA** | The actual value being stored — a number, a name, a whole object |
| **NEXT** | A reference (pointer) to the following node. The last node's NEXT is `null` |

### Java Node Class:
```java
class Node {
    int data;
    Node next;
    
    Node(int data) {
        this.data = data;
        this.next = null;
    }
}
```

---

## 2.3 Linked List vs. Array

| Aspect | Array (ArrayList) | Linked List |
|--------|-------------------|-------------|
| **Memory** | One contiguous block | Scattered across memory |
| **Access by index** | Fast O(1) — `arr[2]` | Slow O(n) — must traverse from head |
| **Insertion at beginning** | Slow O(n) — shift elements | Fast O(1) — update one pointer |
| **Insertion at end** | Fast O(1)* | Slow O(n) — must traverse to tail |
| **Memory allocation** | Reserved upfront; resizing expensive | Grabbed one node at a time; no resize |
| **Extra memory** | Minimal | Each node stores a pointer (extra 4-8 bytes) |

*ArrayLists can be O(n) when resizing capacity is exceeded.

---

## 2.4 Singly Linked List

### Characteristics:
- Each node has: `data` + `next` pointer
- Walk **forward only** — no backward view
- Insert/remove is cheap — just re-point pointers
- Need to traverse from head to reach specific positions

### Traversal Code:
```java
void traverse(Node head) {
    Node current = head;
    while (current != null) {
        System.out.print(current.data + " -> ");
        current = current.next;
    }
    System.out.println("null");
}
```

### Insert at Beginning:
```java
Node insertAtBeginning(Node head, int data) {
    Node newNode = new Node(data);
    newNode.next = head;
    head = newNode;
    return head;
}
```
**Only two pointer updates** needed — nothing else shifts.

### Insert at End:
```java
Node insertAtEnd(Node head, int data) {
    Node newNode = new Node(data);
    if (head == null) return newNode;
    
    Node current = head;
    while (current.next != null) {
        current = current.next;
    }
    current.next = newNode;
    return head;
}
```
**Must walk to the last node first** — no direct way to reach the tail.

### Insert at Position:
```java
Node insertAtPosition(Node head, int data, int pos) {
    if (pos == 0) return insertAtBeginning(head, data);
    
    Node newNode = new Node(data);
    Node current = head;
    for (int i = 0; i < pos - 1 && current != null; i++) {
        current = current.next;
    }
    if (current == null) return head;
    
    newNode.next = current.next;
    current.next = newNode;
    return head;
}
```

### Deletion:
```java
Node deleteNode(Node head, int value) {
    if (head == null) return null;
    if (head.data == value) return head.next;
    
    Node current = head;
    while (current.next != null && current.next.data != value) {
        current = current.next;
    }
    if (current.next != null) {
        current.next = current.next.next;
    }
    return head;
}
```
**Deletion doesn't erase memory** — it just makes the previous node's `next` skip over the target.

---

## 2.5 Doubly Linked List

### Characteristics:
- Each node has: `data` + `next` + `previous` pointers
- Walk **forward or backward**
- More memory per node (extra pointer)
- Used when you need to traverse in both directions

### Node Class:
```java
class Node {
    String photo;
    Node next;
    Node previous;
    
    Node(String photo) {
        this.photo = photo;
        this.next = null;
        this.previous = null;
    }
}
```

### Real-World Analogy: Photo Gallery Viewer
Swiping a gallery, you can go **Next** or **Previous**. The current photo needs to know both neighbors.

```
null ← [Photo A] ↔ [Photo B] ↔ [Photo C] → null
```

---

## 2.6 java.util.LinkedList

Java's built-in **doubly linked list** implementation.

### Common Methods:
| Method | Description |
|--------|-------------|
| `add(E e)` | Adds to the end |
| `addFirst(E e)` | Inserts at the beginning |
| `addLast(E e)` | Inserts at the end |
| `remove(Object o)` | Removes first occurrence |
| `get(int index)` | Returns element at position (O(n)) |
| `size()` | Returns number of elements |

### Example:
```java
import java.util.LinkedList;

LinkedList<String> tasks = new LinkedList<>();
tasks.add("Reply to emails");
tasks.addFirst("Fix production bug");  // O(1)
tasks.addLast("Plan next sprint");     // O(1)
tasks.remove("Review pull request");
```

---

## 2.7 Operations: Insertion and Deletion

### Insertion at Beginning (Singly):
```
BEFORE: HEAD → [10] → [20] → [30] → null
AFTER:  HEAD → [5] → [10] → [20] → [30] → null
```
Step 1: `newNode.next = head`
Step 2: `head = newNode`

### Insertion at End:
```
BEFORE: HEAD → [10] → [20] → [30] → null
AFTER:  HEAD → [10] → [20] → [30] → [40] → null
```
Step 1: Walk to last node (where `next == null`)
Step 2: `current.next = newNode`

### Insertion at Position:
```
BEFORE: HEAD → [10] → [20] → [30] → null
AFTER:  HEAD → [10] → [20] → [15] → [30] → null
```
Step 1: Walk to node before target position
Step 2: `newNode.next = current.next`
Step 3: `current.next = newNode`

### Deletion:
```
BEFORE: HEAD → [10] → [20] → [30] → null
AFTER:  HEAD → [10] → [30] → null
```
Step 1: Find node before target
Step 2: `current.next = current.next.next`

---

# 3. Stacks (Part 2)

## 3.1 Quick Recap: Push and Pop

A stack follows **Last-In, First-Out (LIFO)**:
- `push()` — adds to the top
- `pop()` — removes from the top

Access only ever happens at one end (the top).

```
TOP
  ↓
[English]   ← pushed last, sits on TOP
[Science]
[Math]      ← pushed first
```

---

## 3.2 Peek / Top

**`peek()`** looks at the top element **without removing it**. The stack is completely unchanged afterward — useful whenever you need to check what's on top before deciding what to do next.

### Java Example:
```java
Stack<String> books = new Stack<>();
books.push("Math");
books.push("Science");
books.push("English");

String top = books.peek();
System.out.println(top);           // English
System.out.println(books.size());  // 3 -- unchanged!
```

**Key Point:** `peek()` only looks. Only `pop()` actually removes the top element.

---

## 3.3 Underflow

**Underflow** happens when you try to `pop()` or `peek()` a stack that has nothing in it.

### In Java:
The built-in `Stack` class throws an `EmptyStackException`.

### Prevention:
```java
Stack<String> empty = new Stack<>();

if (!empty.isEmpty()) {
    empty.pop();
} else {
    System.out.println("Cannot pop - stack is empty (underflow)!");
}
```

**Golden Rule:** Always call `isEmpty()` before `pop()` or `peek()` if you're not certain the stack has something in it.

---

## 3.4 Applications of Stacks

### 1. The Call Stack (Function Calls)

Every time a method calls another method, the program pushes a new **stack frame**. When that call finishes, its frame pops off and control returns to whoever called it — pure LIFO.

**Example: Recursive Factorial**
```java
int factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}
```

**Stack Growth:**
```
factorial(0)   ← returns 1, pops off
factorial(1)   ← calls factorial(0)
factorial(2)   ← calls factorial(1)
factorial(3)   ← calls factorial(2)
```

**Important:** A recursive function with no base case crashes with a **stack overflow** — too many pushes, and the frames never get a chance to pop.

---

### 2. Undo / Redo

Every action you take gets `push()`ed onto an undo stack. Pressing **Ctrl+Z** simply `pop()`s the most recent one off and reverses it.

```
UNDO STACK (before):                UNDO STACK (after Ctrl+Z):
[Inserted Image]    ← top           [Made text Bold]    ← top
[Made text Bold]                    [Typed 'Hello']
[Typed 'Hello']
```

---

### 3. Expression Evaluation (Bracket Matching)

To check if brackets are balanced:
- Push every opening bracket (`(`, `[`, `{`)
- On a closing bracket, pop and make sure it matches
- If stack ever runs dry on a closing bracket → unbalanced
- If stack isn't empty at the end → unbalanced

**Bracket Matching Algorithm:**
```java
boolean isBalanced(String expr) {
    Stack<Character> stack = new Stack<>();
    for (char c : expr.toCharArray()) {
        if (c == '(' || c == '[' || c == '{') {
            stack.push(c);
        } else if (c == ')' || c == ']' || c == '}') {
            if (stack.isEmpty()) return false; // underflow!
            char open = stack.pop();
            if (!matches(open, c)) return false;
        }
    }
    return stack.isEmpty();
}
```

**Tracing `"{[()]}"`:**
| Char | Action | Stack after |
|------|--------|-------------|
| `{` | push | `{` |
| `[` | push | `{ [ ` |
| `(` | push | `{ [ ( ` |
| `)` | pop, matches ( | `{ [ ` |
| `]` | pop, matches [ | `{` |
| `}` | pop, matches { | empty |

---

### 4. Backtracking

When solving a maze, a puzzle, or any "try this, and if it fails, go back" problem:
- Each step taken gets pushed
- Hit a dead end? **Backtrack** — pop the last step off and try a different move

**Used in:** Solving Sudoku, N-Queens, maze navigation, and puzzle solving.

---

# 4. Queues (Part 2)

## 4.1 Quick Recap: Enqueue and Dequeue

A queue follows **First-In, First-Out (FIFO)**:
- `enqueue()` (or `add()`) — joins at the rear
- `dequeue()` (or `poll()`) — leaves from the front

Just like a line at a counter.

```
FRONT                    REAR
  ↓                       ↓
[Alice] → [Bob] → [Charlie] → null
```

---

## 4.2 Front / Peek

**`peek()`** looks at the front element **without removing it** — the line stays exactly the same.

### Java Example:
```java
Queue<String> customers = new LinkedList<>();
customers.add("Alice");
customers.add("Bob");
customers.add("Charlie");

String next = customers.peek();
System.out.println(next);          // Alice
System.out.println(customers.size()); // 3 -- unchanged!
```

**Key Point:** `peek()` only looks. Only `poll()` (or `remove()`) actually removes the front element.

---

## 4.3 Linear Queue — The Wasted-Space Problem

A queue built on a fixed-size array only ever moves its rear pointer **forward**. Once rear reaches the last slot, the queue reports "full" — even if slots at the front are sitting empty after being served.

### Example:
```
Index:     0      1      2      3      4
         [A]    [B]    [C]    [D]    [E]
                   ↑             ↑
              (served)         REAR
              ↓
         FRONT = 3  (A, B, C already served)
```

**Problem:** Three whole slots are free (0, 1, 2), yet a plain linear queue has no way to reuse them. The queue is "full" even though space exists.

---

## 4.4 Circular Queue — Reusing Space

A **circular queue** treats the last slot as if it connects back to slot 0. When rear needs to move past the end, it wraps around (using modulo) and reuses whatever's been freed.

### Enqueue in a Circular Queue:
```java
int enqueue(int[] queue, int rear, int capacity, int value) {
    int newRear = (rear + 1) % capacity;
    queue[newRear] = value;
    return newRear;
}
```

**The trick is `% capacity`.** Once rear reaches the last index, adding 1 and wrapping with modulo sends it right back to 0.

### Visual:
```
     Slot 0: [F]
     Slot 1: [G]     ← REAR
     Slot 2: empty
     Slot 3: [D]     ← FRONT
     Slot 4: [E]

F and G wrapped around into slots 0 & 1 — space served by A, B, C is reused.
```

### Comparison: Linear vs. Circular Queue

| Aspect | Linear Queue | Circular Queue |
|--------|--------------|----------------|
| Rear movement | Only forward | Wraps back to index 0 |
| Freed space | Wasted once passed | Reused automatically |
| Implementation | Simple | Slightly more logic (modulo) |
| Good fit for | Short-lived, one-shot queues | Long-running queues (buffers, schedulers) |

---

## 4.5 Applications of Queues

### 1. CPU Scheduling

Programs waiting for CPU time sit in a **ready queue**. In simple First-Come-First-Served scheduling, the CPU just keeps dequeuing the front process and running it.

```java
Queue<String> readyQueue = new LinkedList<>();
readyQueue.add("P1");
readyQueue.add("P2");
readyQueue.add("P3");

while (!readyQueue.isEmpty()) {
    String current = readyQueue.poll();
    System.out.println("CPU is now running: " + current);
}
```

**FIFO means:** Whoever has been in the queue the longest (the front) gets served first.

---

### 2. Printer Spooling

When several documents get sent to one printer, they line up in a **print queue (spool)** so they come out in the exact order they were submitted.

```java
Queue<String> printQueue = new LinkedList<>();
printQueue.add("Resume.pdf");
printQueue.add("Report.docx");
printQueue.add("Photo.png");

while (!printQueue.isEmpty()) {
    String job = printQueue.poll();
    System.out.println("Printing: " + job);
}
```

**Output:**
```
Printing: Resume.pdf
Printing: Report.docx
Printing: Photo.png
```

---

# 5. Key Takeaways / Summary Box

1. **Big O** describes how algorithm performance scales with input size — O(1) is constant, O(log n) is logarithmic, O(n) is linear, O(n²) is quadratic.

2. **A Node** is the building block of linked lists — it stores data and a reference to the next node (and previous for doubly linked lists).

3. **Linked lists** trade direct index access (arrays) for flexible, no-resize growth.

4. **Singly linked lists** only point forward; **doubly linked lists** point both ways.

5. **java.util.LinkedList** is Java's ready-made doubly linked list implementation.

6. **Stacks** follow LIFO (Last-In, First-Out) — `push`, `pop`, and `peek` are the core operations.

7. **Underflow** occurs when you try to pop or peek an empty stack — always check `isEmpty()` first.

8. **Applications of stacks:** call stack (function calls), undo/redo, bracket matching, backtracking.

9. **Queues** follow FIFO (First-In, First-Out) — `enqueue`, `dequeue`, and `peek` are the core operations.

10. **Circular queues** solve the wasted-space problem of linear queues by wrapping rear back to index 0 using modulo.

11. **Applications of queues:** CPU scheduling (ready queue), printer spooling (print queue).

12. **The trade-off between arrays and linked lists** is the central decision: arrays give you fast random access but slow insert/delete in the middle; linked lists give you fast insert/delete anywhere but slow random access.

---

# 6. Important Terms / Glossary

| Term | Definition |
|------|------------|
| **Algorithm** | A set of steps to solve a problem — like a recipe |
| **Big O Notation** | A mathematical notation that describes the limiting behavior of a function when the argument tends towards infinity |
| **Constant Time (O(1))** | Algorithm whose runtime does not change with input size |
| **Logarithmic Time (O(log n))** | Algorithm whose runtime grows logarithmically — each step halves the problem |
| **Linear Time (O(n))** | Algorithm whose runtime grows directly proportional to input size |
| **Quadratic Time (O(n²))** | Algorithm whose runtime grows by the square of input size |
| **Linked List** | A linear data structure where nodes are connected by pointers |
| **Node** | A unit in a linked list containing data and a pointer to the next node |
| **Head** | A pointer that marks the first node in a linked list |
| **Null** | A value that indicates the end of a linked list (no more nodes) |
| **Traversal** | The process of visiting each node from the head until reaching null |
| **Singly Linked List** | A linked list where each node points only to the next node |
| **Doubly Linked List** | A linked list where each node points to both the next and previous nodes |
| **Stack** | A LIFO data structure where elements are added and removed from the top |
| **Push** | Adding an element to the top of a stack |
| **Pop** | Removing an element from the top of a stack |
| **Peek / Top** | Looking at the top element without removing it |
| **Underflow** | Trying to pop or peek from an empty stack |
| **Queue** | A FIFO data structure where elements are added at the rear and removed from the front |
| **Enqueue** | Adding an element to the rear of a queue |
| **Dequeue** | Removing an element from the front of a queue |
| **Front / Peek** | Looking at the front element without removing it |
| **Linear Queue** | A queue where rear only moves forward, wasting freed space |
| **Circular Queue** | A queue where rear wraps back to index 0 using modulo, reusing space |
| **Call Stack** | The stack that manages function calls, automatically following LIFO |
| **Backtracking** | A problem-solving technique that undoes the last step upon hitting a dead end |
| **Printer Spooling** | A queue-based system ensuring documents print in submission order |
| **CPU Scheduling** | A queue-based system deciding which waiting process runs next |

---

# 7. Possible Review Questions

### Multiple Choice

1. **What does O(n) represent?**
   - A) Constant time complexity
   - B) Linear time complexity
   - C) Logarithmic time complexity
   - D) Exponential time complexity

2. **A loop that runs a fixed number of times, no matter the size of `n`, is:**
   - A) O(1)
   - B) O(n)
   - C) O(n²)
   - D) O(log n)

3. **In `for (int i = 1; i < n; i = i * 2)`, why is this logarithmic?**
   - A) The loop runs n times
   - B) The counter doubles each time, so steps grow much slower than n
   - C) The loop never ends
   - D) It always runs a constant number of times

4. **Is O(1000n + 1000) a different complexity class than O(n)?**
   - A) True — the constants change the class
   - B) False — both are linear, O(n)

5. **What does peek() do that pop() doesn't?**
   - A) Removes the top element
   - B) Adds a new element
   - C) Returns the top element without removing it
   - D) Empties the whole stack

6. **What is underflow?**
   - A) Pushing too many elements onto a stack
   - B) Trying to pop or peek from an empty stack
   - C) A stack that has grown too large
   - D) An array running out of index space

7. **In a linear queue, what problem can occur even when several front slots are empty?**
   - A) The queue automatically resizes itself
   - B) You still can't enqueue once rear has reached the last physical slot
   - C) Dequeue stops working entirely
   - D) The queue turns into a stack

8. **How does a circular queue solve the linear queue's wasted-space problem?**
   - A) By deleting old data automatically
   - B) By wrapping the rear pointer back to slot 0 once space frees up there
   - C) By doubling its capacity every time
   - D) By using two separate queues

9. **Which data structure follows Last-In, First-Out (LIFO)?**
   - A) Queue
   - B) Stack
   - C) Linked List
   - D) Array

10. **What is the main advantage of a linked list over an array?**
    - A) Faster random access
    - B) Efficient insertion and deletion anywhere
    - C) Less memory usage
    - D) Simpler implementation

### Identification / Fill in the Blank

1. The letter that represents input size in Big O notation is **_____** .

2. A loop whose counter doubles each iteration (e.g., `i = i * 2`) has complexity **_____** .

3. The pointer that always marks the starting node of a linked list is called the **_____** .

4. The process of visiting each node from the head until reaching null is called **_____** .

5. The two components every singly-linked-list node contains are **_____** and **_____** .

6. The stack operation that returns the top element without removing it is called **_____** .

7. The error condition that occurs when popping or peeking an empty stack is called **_____** .

8. The queue type where rear can't wrap back around, wasting freed-up space, is called a **_____** queue.

9. The queue type where rear wraps back to index 0 once space frees up is called a **_____** queue.

10. The data structure that manages function calls and automatically follows LIFO order is called the **_____** .

### True or False

1. Big O notation measures the exact time an algorithm takes to run. (False)
2. O(2n + 1) can be simplified to O(n). (True)
3. In a singly linked list, you can easily traverse backward. (False)
4. A stack's peek() operation removes the top element. (False)
5. A circular queue uses modulo to wrap rear back to the beginning. (True)
6. java.util.LinkedList is Java's built-in singly linked list. (False — it's doubly linked)
7. Printer spooling uses a queue to ensure documents print in submission order. (True)
8. Underflow happens when you push too many elements onto a stack. (False — underflow is popping from empty)
9. Backtracking uses a stack to undo the last step upon hitting a dead end. (True)
10. CPU scheduling uses a queue to decide which process runs next. (True)

### Short Answer / Essay Questions

1. Explain the trade-off between using an array and using a linked list. When would you choose one over the other?

2. Describe the steps to insert a new node at the beginning of a singly linked list. Include a diagram in your explanation.

3. Compare and contrast singly linked lists and doubly linked lists. What are the advantages and disadvantages of each?

4. Explain how a circular queue works and why it is more efficient than a linear queue.

5. Describe three real-world applications of stacks and explain why a stack is the right data structure for each.

6. Explain the difference between `peek()` and `pop()` for both stacks and queues.

7. Walk through the execution of the bracket matching algorithm on the input `"{[()]}"`. Show the stack after each step.

8. What is a call stack? How does it relate to recursion and stack overflow?

9. Describe the FIFO and LIFO principles and give real-world analogies for each.

10. How would you implement a queue using two stacks?

---

# 8. Source Notes

This reviewer was compiled from the following HTML presentation files:

1. `DSA M4 big-o-notation-slides.html` — Big O Notation: Fundamentals, growth families, calculation methods, and worked examples.

2. `DSA M5 Linked_Lists.html` — Linked Lists: Node anatomy, singly vs. doubly linked lists, operations (insertion, deletion, traversal), and comparison with arrays.

3. `linkedlist_deck.html` — Linked Lists (alternative presentation): Java's `java.util.LinkedList`, real-world analogies, coding examples, and activity problems.

4. `DSA M6 Stacks_Part2.html` — Stacks (Part 2): Peek/top, underflow, applications (call stack, undo/redo, bracket matching, backtracking), and the Balanced Brackets Checker mini-project.

5. `DSA M7 Queues_Part2.html` — Queues (Part 2): Front/peek, linear vs. circular queues, applications (CPU scheduling, printer spooling), and the Print Queue Simulator mini-project.

---

*End of Reviewer*