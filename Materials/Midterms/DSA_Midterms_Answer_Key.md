# DSA — Data Structure & Algorithms Midterms
## Answer Key (Revised)

**Total: 60 pts (+3 bonus) — 43 items**

---

## I. CODING PROBLEMS (15 pts — 5 pts each)

### 1. Singly Linked List — Insertion at Position

```java
public static Node insertAtPosition(Node head, int data, int position) {
    Node newNode = new Node(data);

    // Insert at beginning
    if (position == 0 || head == null) {
        newNode.next = head;
        return newNode;
    }

    Node current = head;
    int index = 0;

    // Traverse to the node just before the insertion point
    while (current.next != null && index < position - 1) {
        current = current.next;
        index++;
    }

    // Insert (handles middle and append-when-position-exceeds)
    newNode.next = current.next;
    current.next = newNode;

    return head;
}
```

### 2. Stack — Balanced Brackets

```java
public static boolean isBalanced(String expression) {
    Stack<Character> stack = new Stack<>();

    for (char c : expression.toCharArray()) {
        if (c == '(' || c == '[' || c == '{') {
            stack.push(c);
        } else if (c == ')' || c == ']' || c == '}') {
            if (stack.isEmpty()) return false;

            char top = stack.pop();
            if ((c == ')' && top != '(') ||
                (c == ']' && top != '[') ||
                (c == '}' && top != '{')) {
                return false;
            }
        }
    }

    return stack.isEmpty();
}
```

### 3. Queue — Print Queue Simulator

```java
import java.util.LinkedList;
import java.util.Queue;

public class PrintQueueSimulator {
    public static void main(String[] args) {
        Queue<String> printQueue = new LinkedList<>();

        // Build queue with at least 5 jobs
        printQueue.add("Document1.pdf");
        printQueue.add("Report.docx");
        printQueue.add("Invoice.xlsx");
        printQueue.add("Photo.png");
        printQueue.add("Presentation.pptx");

        // Peek at what's next
        System.out.println("Next job to process: " + printQueue.peek());

        // Process all jobs in FIFO order
        System.out.println("\nProcessing jobs:");
        while (!printQueue.isEmpty()) {
            String job = printQueue.poll();
            System.out.println("Printing: " + job);
        }

        System.out.println("\nQueue is now empty.");
    }
}
```

---

## II. IDENTIFICATION (5 pts — 1 pt each)

1. **Head** (or Head pointer)
2. **Peek** (or front / element)
3. **Underflow** (or Stack Underflow)
4. **prev** (or previous / prev pointer)
5. **Backtracking**

---

## III. SCENARIO-BASED IDENTIFICATION (5 pts — 1 pt each)

1. **Doubly Linked List**
2. **Stack**
3. **Queue** (or Linear Queue)
4. **Call Stack** (or Stack)
5. **Printer Spooling** (or Queue)

---

## IV. GUESS THE OUTPUT (10 pts — 2 pts each)

1.
```
10
10
2
```

2.
```
C
B
false
```

3. **4**
   *(i = 1 → 2 → 4 → 8; count = 4; stops when i becomes 16)*

4. **10**
   *(head is reassigned to head.next)*

5. **0**
   *((4 + 1) % 5 = 0)*

---

## V. MULTIPLE CHOICE (25 pts — 1 pt each)

| # | Answer | # | Answer |
|---|--------|---|--------|
| 1 | **C) O(1)** | 14 | **B) A Queue (FIFO)** |
| 2 | **B) O(n)** | 15 | **B) Stack** |
| 3 | **C) O(n²)** | 16 | **B) Queue** |
| 4 | **B) A reference to the following node** | 17 | **C) Data, next, and previous pointers** |
| 5 | **B) Points to the first node** | 18 | **B) Efficient insertion/deletion anywhere** |
| 6 | **B) Nodes aren't contiguous, so you must traverse from the head** | 19 | **D) All of the above** |
| 7 | **C) New node's next, then the head pointer** | 20 | **C) null** |
| 8 | **C) Returns the top element without removing it** | 21 | **A) Nothing, this is just a regular question** |
| 9 | **B) Trying to pop/peek an empty stack** | 22 | **A) 0** |
| 10 | **C) The ) — doesn't match the [ on top** | 23 | **B) Stack** |
| 11 | **C) Returns the front element without removing it** | 24 | **B) Traverse to the 2nd-to-last node, set its next to null** |
| 12 | **B) Wraps rear back to slot 0 via modulo** | 25 | **B) The structure contains no elements** |
| 13 | **B) The one waiting the longest** | | |

> **Note on #21:** Easter-egg / trick question (carried over from original #30). Academic answer is **A**. If the instructor counts live action for bonus, **B** applies (+3 bonus, as noted in the total).

---

## Point Distribution Summary

| Section | Items | Points |
|---|---|---|
| I. Coding Problems | 3 | 15 |
| II. Identification | 5 | 5 |
| III. Scenario-Based Identification | 5 | 5 |
| IV. Guess the Output | 5 | 10 |
| V. Multiple Choice | 25 | 25 |
| **Total** | **43** | **60 (+3 bonus)** |

---

***End of Answer Key***
