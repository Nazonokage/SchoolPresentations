Good timing — this gives us the real syllabus skeleton to check our prelims reviewer against. Quick heads up: the numbering in this master document (Module 01–14) doesn't line up with the module numbers in your earlier slide decks — this syllabus treats **Linked Lists** as its own Module 02 and **Stacks** as Module 03, whereas your earlier materials bundled stack/queue into "Module 1" and sorting/recursion/casting into "Module 2." So I'm matching by **topic**, not by label.

## ✅ Topics we've already covered (current prelims reviewer)

| Topic | Source | Depth |
|---|---|---|
| Data Structure vs Algorithm (definitions, how they work together) | Module 01 equivalent | Solid |
| Memory model basics (how variables/addresses work) | Module 01 equivalent | Solid |
| Stack (LIFO) — push, pop | Module 03 equivalent | **Partial** — push/pop done, but no peek, underflow, or applications |
| Queue (FIFO) — enqueue/add, dequeue/poll | Module 04 equivalent | **Partial** — basic add/remove done, no front/peek, no linear-vs-circular |
| Linear Search | Module 08 equivalent | Solid |
| Type casting — implicit widening / explicit narrowing, promotion, primitive→String | Not in this syllabus at all (language-nuance side topic) | Solid |
| Bubble Sort | Module 10 equivalent | **Partial** — mechanics & performance done, no formal Big-O labels (per your request), no comparison to Insertion Sort |
| Recursion — base case, recursive case, call stack, stack overflow | Spread across Module 09 (recursive search) | Solid intro, not yet tied to recursive binary search |
| Algorithm characteristics (unambiguous, finite, feasible, etc.) | Module 01 equivalent | Solid |
| Java syntax basics (variables, methods, loops, classes) | Not a DSA module — general language support | Solid |

## ❌ Topics not yet covered (per this document)

| Module | Topic | Notes |
|---|---|---|
| **02 — Linked Lists** | Node structure (data + next), head, traversal, insertion (beginning/end/position), deletion | **Biggest gap for prelims** — mentioned only as an analogy so far, never taught as its own structure |
| **03 — Stacks (rest)** | Peek/top, underflow, applications (call stack, undo/redo, expression evaluation, backtracking) | We have push/pop; the "why it matters" applications are missing |
| **04 — Queues (rest)** | Front/peek, linear vs circular queue, applications (CPU scheduling, printer spooling) | We have enqueue/dequeue only |
| **05 — Graphs** | Vertices/edges, directed vs undirected, adjacency matrix vs list, BFS/DFS | Not touched at all |
| **06 — Trees** | Root/node/edge/parent/child/leaf, general vs binary trees, applications | Not touched at all |
| **07 — Trees Pt. 2** | In-order/pre-order/post-order traversal, Binary Search Trees | Not touched at all |
| **08 — Searching Pt. 1 (rest)** | Binary Search (steps, requirement of sorted data) | Only Linear Search done |
| **09 — Searching Pt. 2** | Iterative vs recursive Binary Search, common bugs | Not touched at all |
| **10 — Sorting Pt. 1 (rest)** | Insertion Sort, Bubble vs Insertion comparison | Only Bubble Sort done |
| **11 — Sorting Pt. 2** | Quick Sort (pivot/partition), Merge Sort (divide/merge) | Not touched at all |
| **12 — Hashing Pt. 1** | Hash functions, hash tables, collisions | Not touched at all |
| **13 — Hashing Pt. 2** | Separate chaining, linear probing, load factor, rehashing | Not touched at all |
| **14 — Final Project** | System design combining searching/sorting/hashing/stack | Capstone — depends on everything above |

## 📅 Suggested split for the rest of the semester

**Finish out prelims (add now):**
- Linked Lists — full module (this is the clearest gap given the syllabus explicitly makes it its own prelim-scope module)
- Round out Stack (peek, underflow, real applications) and Queue (front, circular queue, applications) since they're prelim-scope topics too

**Midterms (Modules 05–09):**
- Graphs (components, representation, BFS/DFS)
- Trees + Trees Pt. 2 (traversals, BST)
- Searching Pt. 1 & 2 (Binary Search, iterative vs recursive)

**Finals (Modules 10–14):**
- Sorting Pt. 1 & 2 (Insertion, Quick, Merge — plus a full comparison table with Bubble)
- Hashing Pt. 1 & 2 (hash tables, collisions, chaining, probing, load factor, rehashing)
- Final Project prep (tying searching + sorting + hashing + stack into one system demo)

Want me to go ahead and add the **Linked Lists** section (plus the missing Stack/Queue pieces) to the prelims reviewer now, since that's the real gap before the exam?