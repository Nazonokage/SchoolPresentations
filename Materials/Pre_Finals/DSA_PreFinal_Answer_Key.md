# Data Structures and Algorithms | Pre-Final Periodical Exam: Answer Key

**Total:** 60 points | **Language:** Java | *For instructor use only.*

| Part | Items | Points each | Total |
|---|---|---|---|
| I. Multiple Choice | 1–20 | 1 | 20 |
| II. Identification | 21–35 | 1 | 15 |
| III. Guess the Output | 36–45 | 1 | 10 |
| IV. Coding Problems | 46–48 | 5 | 15 |
| **Total** | **48** | | **60** |

**MC answer distribution:** A = 5, B = 5, C = 5, D = 5.

---

## I. Multiple Choice

| # | Ans | Rationale |
|---|---|---|
| 1 | **C** | The root is the single topmost node; every other node descends from it. |
| 2 | **A** | A binary tree caps every node at two children. |
| 3 | **D** | HTML tags nest inside one another, forming the DOM tree. |
| 4 | **B** | In-order is Left → Root → Right. |
| 5 | **A** | Insert 40, 20, 60, 10, 30: root 40; left 20 (children 10, 30); right 60. Pre-order: 40 20 10 30 60. (D is the level-order trap.) |
| 6 | **D** | Post-order visits both children before the parent, so children are deleted first. |
| 7 | **B** | DFS: A → B → D (D has no neighbors, backtrack) → C (D already visited). Order: A, B, D, C. |
| 8 | **C** | An adjacency list stores only existing edges, so it is the most space-efficient for sparse graphs. |
| 9 | **A** | BFS uses a queue (FIFO). |
| 10 | **D** | DFS uses a stack, or recursion, which uses the call stack. |
| 11 | **B** | low=0, high=6, mid=3 (12); 23 > 12 → low=4. mid=5 (23) → found. Loop body ran 2 times. |
| 12 | **C** | On unsorted data, "target < arr[mid]" no longer implies "target is on the left", so the half holding the target may be discarded. |
| 13 | **A** | `low + (high - low) / 2` cannot overflow, unlike `(low + high) / 2`. |
| 14 | **D** | With no `low > high` base case, the recursion never ends normally and exhausts the call stack (`StackOverflowError`). |
| 15 | **C** | `while (low <= high)` keeps the search alive when only one element remains (`low == high`). |
| 16 | **B** | Larger elements shift one position right to open a gap for the current element. |
| 17 | **D** | On nearly-sorted data, few elements are out of place, so few shifts occur. |
| 18 | **A** | i=1: insert 4 → `{4, 9, 7, 2}`. i=2: insert 7 (9 shifts right) → `{4, 7, 9, 2}`. |
| 19 | **C** | Bubble Sort compares and swaps adjacent pairs over repeated full passes. (Insertion Sort shifts, not swaps.) |
| 20 | **B** | A visited set prevents revisiting vertices, which would loop forever in cyclic graphs. |

---

## II. Identification

| # | Answer | Notes |
|---|---|---|
| 21 | **General Tree** | Nodes may have any number of children. |
| 22 | **Post-order Traversal** | Children are processed before the parent. |
| 23 | **In-order Traversal** | On a BST it yields ascending order. |
| 24 | **Directed Graph (Digraph)** | One-way streets = directed edges. |
| 25 | **Adjacency Matrix** | 2D grid of 1s/0s; O(1) edge lookup. |
| 26 | **Breadth-First Search (BFS)** | Explores neighbors level by level; finds the shortest path in unweighted graphs. |
| 27 | **Binary Search** | Check the middle, discard the half that cannot hold the target. |
| 28 | **`low` and `high`** | The two boundary pointers of the search range. |
| 29 | **Base Case (Base Condition)** | Also accept "terminating condition". |
| 30 | **Infinite Loop** | The range never shrinks because `low = mid` repeats. Accept "infinite loop bug". |
| 31 | **Insertion Sort** | Like sorting a hand of cards. |
| 32 | **Bubble Sort** | Repeated adjacent compare-and-swap passes. |
| 33 | **Left** | 65 > 50 → right to 70; 65 < 70 → go left of 70. |
| 34 | **Iterative** | A `while` loop narrows the range without self-calls. |
| 35 | **DOM Tree** | Document Object Model. |

---

## III. Guess the Output

| # | Output | Trace |
|---|---|---|
| 36 | `0` | New node `b` has an empty children list (it is a leaf). |
| 37 | `50 30 20 70 ` | Pre-order: 50, then left subtree (30, then its left child 20), then right 70. |
| 38 | `2 0` | `g.get("A")` has 2 items; `getOrDefault("Z", …)` returns an empty list → size 0. |
| 39 | `BC` | After `poll()` removes A, the second `poll()` returns B; `peek()` returns C without removing. String concatenation gives `BC`. |
| 40 | `1 false` | A set ignores the duplicate "A" (size 1); "Z" was never added. |
| 41 | `2 3` | Pass 1: mid=2 (15), 22 > 15 → low=3, steps=1. Pass 2: mid=3 (22) → steps=2, break. `low` stays 3. |
| 42 | `7` | 5 + (10 − 5) / 2 = 5 + 2 (integer division) = 7. |
| 43 | `2 1` | Pass 1: mid=1 (8), 10 > 8 → low=2. Pass 2: mid=2 (15), 10 < 15 → high=1. Loop ends (low > high) without finding the target. |
| 44 | `[3, 5, 8]` | i=1: 8 shifts right, 3 placed first → `{3, 8, 5}`. i=2: 8 shifts right, 5 placed at index 1 → `{3, 5, 8}`. |
| 45 | `1 3 4` | Only i=3 shifts (4 moves right once, so shifts = 1). After the sort, `arr[2]=3`, `arr[3]=4`. |

---

## IV. Coding Problems

### 46. Iterative Binary Search (5 pts)

```java
// 1. Calculate mid safely
int mid = low + (high - low) / 2;

// 2. Eliminate the right half
high = mid - 1;

// 3. Eliminate the left half
low = mid + 1;
```

**Rubric**

| Criterion | Points |
|---|---|
| `int mid = low + (high - low) / 2;` (must be the overflow-safe form, with declaration) | 2 |
| `high = mid - 1;` | 1.5 |
| `low = mid + 1;` | 1.5 |

Deduct 1 pt if `(low + high) / 2` is used. Deduct 1 pt for `mid` (without ±1) in either update, since it can loop forever. Missing semicolons: −0.5 total.

### 47. Breadth-First Search (5 pts)

```java
void bfs(String start, Map<String, List<String>> graph) {
    Queue<String> queue = new LinkedList<>();
    Set<String> visited = new HashSet<>();

    queue.add(start);
    visited.add(start);

    while (!queue.isEmpty()) {
        String current = queue.poll();
        System.out.print(current + " ");

        for (String neighbor : graph.getOrDefault(current, new ArrayList<>())) {
            if (!visited.contains(neighbor)) {
                visited.add(neighbor);   // mark BEFORE enqueuing
                queue.add(neighbor);
            }
        }
    }
}
```

**Rubric**

| Criterion | Points |
|---|---|
| Declares a `Queue` (e.g., `LinkedList`) and a visited `Set` (e.g., `HashSet`) | 1 |
| Adds `start` to both the queue and the visited set | 1 |
| `while (!queue.isEmpty())` with `poll()` and printing the vertex | 1 |
| Loops over neighbors using `getOrDefault` (or an equivalent null check) | 1 |
| Checks `!visited.contains(...)`, marks visited, and enqueues the neighbor | 1 |

Accept `offer`/`add`, and `ArrayDeque`. Deduct 1 pt if the vertex is marked visited only when polled (allows duplicates in the queue) unless a visited check after polling prevents re-processing.

### 48. Insertion Sort (5 pts)

```java
void insertionSort(int[] arr) {
    for (int i = 1; i < arr.length; i++) {
        int current = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > current) {
            arr[j + 1] = arr[j];   // shift right
            j--;
        }
        arr[j + 1] = current;      // insert into gap
    }
}
```

**Rubric**

| Criterion | Points |
|---|---|
| Outer `for` loop from index 1 to `arr.length - 1` | 1 |
| `current = arr[i]` and `j = i - 1` | 1 |
| Correct `while` condition: `j >= 0 && arr[j] > current` (order matters: the bounds check comes first) | 1 |
| Shift `arr[j + 1] = arr[j]` and `j--` inside the loop | 1 |
| `arr[j + 1] = current;` after the loop | 1 |

Deduct 1 pt if the conditions are reversed (`arr[j] > current && j >= 0`), since this can cause `ArrayIndexOutOfBoundsException`.
