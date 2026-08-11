# ITE 031: Data Structures and Algorithms — Prelim Exam
## Answer Key (For Instructor Use)

**Total: 50 points** | Part I & II: 40 items (1 pt each) | Part III: 5 coding problems (2 pts each)

---

## Part I. Multiple Choice (Items 1–30)

| # | Answer | Quick Note |
|---|:---:|---|
| 1 | **B** | Data structure = organizing/storing data for efficient access & modification |
| 2 | **B** | Arrays sit in contiguous memory |
| 3 | **C** | Stack = LIFO |
| 4 | **B** | Queue = FIFO |
| 5 | **B** | `int[] arr = new int[5];` |
| 6 | **B** | `nums[1]` → index 1 = second element = `4` |
| 7 | **A** | `java.util.Stack` |
| 8 | **C** | `Queue` interface |
| 9 | **B** | Node = data + pointer to next |
| 10 | **B** | Doubly Linked List has next AND previous pointers |
| 11 | **A** | Loop prints `0 1 2` |
| 12 | **B** | Stack Overflow (pushing onto a full stack) |
| 13 | **B** | Queue Underflow / error (dequeue on empty queue) |
| 14 | **B** | `push()` adds to top of stack |
| 15 | **B** | `dequeue()` / `poll()` removes from front of queue |
| 16 | **B** | `"Juan".length()` = 4 |
| 17 | **C** | Arrays are zero-indexed |
| 18 | **B** | Queue — first to arrive, first served |
| 19 | **B** | Circular Queue reuses freed-up front spaces |
| 20 | **C** | Priority Queue serves by priority, not arrival order |
| 21 | **B** | Recursion = function calling itself on smaller subproblems |
| 22 | **B** | Base case stops infinite recursion |
| 23 | **B** | `5 + 10` = `15` |
| 24 | **C** | Iteration/Repetition = repeats instructions |
| 25 | **B** | Selection = choosing between paths (if/else, switch) |
| 26 | **A** | Sequence = instructions run in order, no branching |
| 27 | **B** | `ArrayList` is dynamically resizable |
| 28 | **B** | `null` next pointer = last node in the list |
| 29 | **B** | `1 + 2 + 3 = 6` |
| **30** | **A** | See note below ⬇️ |

> **Note on Item 30:** This one's not really about tracing code — it's the sequence itself. If a student picked **A**, they just followed the exact steps in order: **stood up, walked to the middle of the room, talked to their teacher, and said thanks.** Wink wink. If your student actually did it, give them full marks *and* a round of applause. 😄

---

## Part II. Identification / Enumeration (Items 31–40)

| # | Answer |
|---|---|
| 31 | **Stack** |
| 32 | **Queue** |
| 33 | **Doubly Linked List** |
| 34 | **Array** |
| 35 | **Singly Linked List** and **Doubly Linked List** |
| 36 | **Stack** |
| 37 | **Queue** |
| 38 | **Circular Linked List** |
| 39 | **Sequence**, **Selection**, and **Iteration** (Repetition) |
| 40 | **Tree** |

*Accept minor spelling variations or the terms written in reverse order (e.g., item 35 or 39) as correct, as long as all required terms are present.*

---

## Part III. Coding Problems (Items 41–50, 2 points each)

Grading guide: **1 point** for correct logic/structure, **1 point** for correct syntax/compilability. Minor syntax slips (missing semicolon, etc.) can be judgment calls — use your discretion.

### 41–42. Tagalog Algorithm → Java (Array Sum)

```java
public class ArraySum {
    public static void main(String[] args) {
        int[] numero = {10, 20, 30, 40, 50};
        int kabuuan = 0;

        for (int i = 0; i < numero.length; i++) {
            kabuuan += numero[i];
        }

        System.out.println("Kabuuan: " + kabuuan);
    }
}
```
**Expected output:** `Kabuuan: 150`

---

### 43–44. Print Array in Reverse Order

```java
public class ReverseArray {
    public static void main(String[] args) {
        int[] nums = {5, 10, 15, 20, 25};

        for (int i = nums.length - 1; i >= 0; i--) {
            System.out.println(nums[i]);
        }
    }
}
```
**Expected output:** `25, 20, 15, 10, 5` (one per line)

---

### 45–46. Stack — Push and Pop Names

```java
import java.util.Stack;

public class StackDemo {
    public static void main(String[] args) {
        Stack<String> names = new Stack<>();
        names.push("Juan");
        names.push("Maria");
        names.push("Pedro");

        while (!names.isEmpty()) {
            System.out.println(names.pop());
        }
    }
}
```
**Expected output (LIFO order):** `Pedro`, `Maria`, `Juan`

---

### 47–48. Queue — Enqueue and Dequeue Tickets

```java
import java.util.LinkedList;
import java.util.Queue;

public class QueueDemo {
    public static void main(String[] args) {
        Queue<String> tickets = new LinkedList<>();
        tickets.add("Ticket1");
        tickets.add("Ticket2");
        tickets.add("Ticket3");

        while (!tickets.isEmpty()) {
            System.out.println(tickets.poll());
        }
    }
}
```
**Expected output (FIFO order):** `Ticket1`, `Ticket2`, `Ticket3`

---

### 49–50. Print Only Even Numbers

```java
public class EvenNumbers {
    public static void main(String[] args) {
        int[] nums = {3, 8, 12, 7, 4};

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 0) {
                System.out.println(nums[i]);
            }
        }
    }
}
```
**Expected output:** `8`, `12`, `4`

---

## Scoring Summary

| Part | Items | Points Each | Max Points |
|---|---|---|---|
| I — Multiple Choice | 1–30 | 1 | 30 |
| II — Identification | 31–40 | 1 | 10 |
| III — Coding Problems | 41–50 (5 problems) | 2 | 10 |
| **Total** | | | **50** |
