"""
Generates: DSA_Reviewer_Modules_8-13.docx
A complete reviewer covering Trees, Traversals & BST, Graphs,
Binary Search, Iterative vs Recursive Search, and Insertion Sort.
"""

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

DOC = Document()

# ---------- global styles ----------
styles = DOC.styles
normal = styles['Normal']
normal.font.name = 'Calibri'
normal.font.size = Pt(10.5)

for lvl, size, color in [(1, 22, (0x1F, 0x3A, 0x5F)),
                         (2, 16, (0x1F, 0x3A, 0x5F)),
                         (3, 13, (0x2E, 0x5A, 0x88))]:
    st = styles[f'Heading {lvl}']
    st.font.name = 'Calibri'
    st.font.size = Pt(size)
    st.font.bold = True
    st.font.color.rgb = RGBColor(*color)


def H(text, level=1):
    DOC.add_heading(text, level=level)


def P(text='', bold=False, italic=False, size=None):
    p = DOC.add_paragraph()
    r = p.add_run(text)
    r.bold = bold
    r.italic = italic
    if size:
        r.font.size = Pt(size)
    return p


def BULLET(text):
    DOC.add_paragraph(text, style='List Bullet')


def NUMBER(text):
    DOC.add_paragraph(text, style='List Number')


def CODE(text):
    """Monospace shaded code block."""
    p = DOC.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(8)
    for i, line in enumerate(text.split('\n')):
        if i:
            p.add_run().add_break()
        r = p.add_run(line)
        r.font.name = 'Consolas'
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
    # light gray shading
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:fill'), 'F2F2F2')
    pPr.append(shd)
    return p


def NOTE(label, text):
    p = DOC.add_paragraph()
    r = p.add_run(label + ' ')
    r.bold = True
    p.add_run(text)
    p.paragraph_format.left_indent = Inches(0.2)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(6)
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:fill'), 'FFF7E6')
    pPr.append(shd)
    return p


def TABLE(headers, rows):
    t = DOC.add_table(rows=1, cols=len(headers))
    t.style = 'Light Grid Accent 1'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = ''
        run = hdr[i].paragraphs[0].add_run(h)
        run.bold = True
        run.font.size = Pt(10)
    for row in rows:
        cells = t.add_row().cells
        for i, val in enumerate(row):
            cells[i].text = ''
            r = cells[i].paragraphs[0].add_run(str(val))
            r.font.size = Pt(9.5)
    DOC.add_paragraph()
    return t


def DIVIDER():
    p = DOC.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run('• • •').font.color.rgb = RGBColor(0x99, 0x99, 0x99)
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)


def PAGE_BREAK():
    DOC.add_page_break()


# =====================================================================
# COVER PAGE
# =====================================================================
title = DOC.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = title.add_run('DATA STRUCTURES & ALGORITHMS')
r.bold = True
r.font.size = Pt(28)
r.font.color.rgb = RGBColor(0x1F, 0x3A, 0x5F)

sub = DOC.add_paragraph()
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = sub.add_run('Complete Reviewer — Modules 8 to 13')
r.font.size = Pt(16)
r.italic = True
r.font.color.rgb = RGBColor(0x2E, 0x5A, 0x88)

DOC.add_paragraph()
cover_items = [
    ('Module 8', 'Trees — Fundamentals'),
    ('Module 9', 'Trees, Part 2 — Traversals & Binary Search Trees'),
    ('Module 10', 'Graphs — Representation & Traversal (BFS / DFS)'),
    ('Module 11', 'Binary Search'),
    ('Module 12', 'Searching, Part 2 — Iterative vs. Recursive'),
    ('Module 13', 'Sorting, Part 1 (cont.) — Insertion Sort'),
]
t = DOC.add_table(rows=0, cols=2)
t.style = 'Light List Accent 1'
t.alignment = WD_TABLE_ALIGNMENT.CENTER
for mod, topic in cover_items:
    cells = t.add_row().cells
    cells[0].text = mod
    cells[1].text = topic

DOC.add_paragraph()
p = DOC.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('Prelims • Java • Lecture + Mini Project + Quiz')
r.italic = True
r.font.size = Pt(10.5)
r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

PAGE_BREAK()

# =====================================================================
# MODULE 8 — TREES
# =====================================================================
H('MODULE 8 — TREES: FUNDAMENTALS', 1)

H('8.1  What Is a Tree?', 2)
P('Arrays, linked lists, stacks, and queues are all linear — one element leads to exactly one next '
  'element. A tree is non-linear: one node can branch out to several nodes below it, forming a '
  'hierarchy instead of a line.')

H('8.2  Anatomy of a Tree', 2)
TABLE(
    ['Term', 'Definition'],
    [
        ['Root', 'The single topmost node; has no parent.'],
        ['Node', 'Any element in the tree.'],
        ['Edge', 'The connecting line between a parent and a child.'],
        ['Parent', 'A node with at least one node directly below it.'],
        ['Child', 'A node directly below another node.'],
        ['Leaf', 'A node with no children (an endpoint).'],
        ['Subtree', 'Any node plus everything hanging below it.'],
        ['Level', 'How many steps down from the root a node sits (root = Level 0).'],
        ['Height', 'The deepest level in the whole tree.'],
    ]
)
NOTE('Key rule:', 'A tree has exactly one root, no cycles, and every node (except the root) '
                  'has exactly one parent.')

H('8.3  Types of Trees', 2)
TABLE(
    ['Aspect', 'General Tree', 'Binary Tree'],
    [
        ['Children per node', 'Any number', 'At most two (left, right)'],
        ['Shape', 'Flexible, can be wide or deep', 'Predictable, easier to reason about'],
        ['Typical use', 'Org charts, file systems', 'Search structures, expression trees'],
    ]
)

H('8.4  Real-World Applications', 2)
BULLET('File Systems — drives are roots, folders are internal nodes, files are leaves.')
BULLET('Organizational Charts — one person at the root, everyone else below.')
BULLET('HTML Documents — the DOM tree: <html> is the root, tags nest downward.')
BULLET('Decision-Making — each question is a node, each outcome is a leaf.')

H('8.5  Mini Project — Company Org Chart', 2)
CODE(
"""import java.util.ArrayList;
import java.util.List;

class Employee {
    String name;
    List<Employee> reports = new ArrayList<>();

    Employee(String name) { this.name = name; }

    void addReport(Employee e) { reports.add(e); }

    void printChart(int depth) {
        System.out.println("  ".repeat(depth) + name);
        for (Employee report : reports) {
            report.printChart(depth + 1);
        }
    }
}

public class OrgChart {
    public static void main(String[] args) {
        Employee ceo = new Employee("Maria (CEO)");
        Employee cto = new Employee("Liam (CTO)");
        Employee cfo = new Employee("Ana (CFO)");
        Employee dev1 = new Employee("Sam (Developer)");
        Employee dev2 = new Employee("Kai (Developer)");
        Employee dev3 = new Employee("Priya (Developer)");

        ceo.addReport(cto);
        ceo.addReport(cfo);
        cto.addReport(dev1);
        cto.addReport(dev2);
        cto.addReport(dev3);

        ceo.printChart(0);
    }
}"""
)

PAGE_BREAK()

# =====================================================================
# MODULE 9 — TRAVERSALS & BST
# =====================================================================
H('MODULE 9 — TRAVERSALS & BINARY SEARCH TREES', 1)

H('9.1  Why Tree Traversal Is Necessary', 2)
P('A linked list has only one path to walk. A tree branches — so before visiting every node, you '
  'need a rule for when to process the current node versus its children. Change the rule, and you '
  'get a completely different order.')

H('9.2  The Three Traversal Orders', 2)
TABLE(
    ['Traversal', 'Order', 'Use Case'],
    [
        ['In-order', 'Left → Root → Right', 'Produces sorted data on a BST'],
        ['Pre-order', 'Root → Left → Right', 'Copying or saving a tree\u2019s structure'],
        ['Post-order', 'Left → Right → Root', 'Safe deletion, expression evaluation'],
    ]
)

H('9.3  Canonical BST Used in All Examples', 2)
P('Root = 50; left subtree = 30 (with children 20, 40); right subtree = 70 (with children 60, 80).')
TABLE(
    ['Traversal', 'Result'],
    [
        ['In-order', '20 → 30 → 40 → 50 → 60 → 70 → 80'],
        ['Pre-order', '50 → 30 → 20 → 40 → 70 → 60 → 80'],
        ['Post-order', '20 → 40 → 30 → 60 → 80 → 70 → 50'],
    ]
)
NOTE('Key insight:', 'Only in-order comes out fully sorted on a BST — that is the whole point of a BST.')

H('9.4  Traversal Code (Java)', 2)
CODE(
"""// In-order: Left -> Root -> Right
void inorder(Node node) {
    if (node == null) return;
    inorder(node.left);
    System.out.print(node.value + " ");
    inorder(node.right);
}

// Pre-order: Root -> Left -> Right
void preorder(Node node) {
    if (node == null) return;
    System.out.print(node.value + " ");
    preorder(node.left);
    preorder(node.right);
}

// Post-order: Left -> Right -> Root
void postorder(Node node) {
    if (node == null) return;
    postorder(node.left);
    postorder(node.right);
    System.out.print(node.value + " ");
}"""
)

H('9.5  The BST Property', 2)
P('A Binary Search Tree adds one strict rule on top of a normal binary tree: at every single node, '
  'everything to the left is smaller, and everything to the right is bigger. The rule applies '
  'recursively, all the way down.')
NOTE('Key rule:', 'left < root < right — at EVERY node, not just the top level.')

H('9.6  Why BSTs Matter', 2)
BULLET('Sorted output for free — in-order traversal is always ascending.')
BULLET('Faster searching — each comparison eliminates an entire side.')
BULLET('Supports insertion, searching, and deletion with the same left/right rule.')
BULLET('One rule, everywhere — the property is recursive.')

H('9.7  BST Insertion', 2)
P('Start at the root and keep comparing: go left if smaller, right if larger, until you fall off '
  'the tree — that empty spot is where the new node belongs.')
P('Example: insert 65 into the canonical BST.', bold=True)
TABLE(
    ['Compare 65 to…', 'Decision'],
    [
        ['50', '65 > 50 → go right'],
        ['70', '65 < 70 → go left'],
        ['60', '65 > 60, and 60 has no right child → insert here'],
    ]
)

H('9.8  Mini Project — A BST That Sorts Itself', 2)
CODE(
"""class BSTNode {
    int value;
    BSTNode left, right;
    BSTNode(int value) { this.value = value; }
}

class BST {
    BSTNode root;

    void insert(int value) { root = insertNode(root, value); }

    BSTNode insertNode(BSTNode node, int value) {
        if (node == null) return new BSTNode(value);
        if (value < node.value) {
            node.left = insertNode(node.left, value);
        } else {
            node.right = insertNode(node.right, value);
        }
        return node;
    }

    void inorderPrint(BSTNode node) {
        if (node == null) return;
        inorderPrint(node.left);
        System.out.print(node.value + " ");
        inorderPrint(node.right);
    }
}

public class BSTDemo {
    public static void main(String[] args) {
        BST tree = new BST();
        int[] values = {50, 30, 70, 20, 40, 60, 80};
        for (int v : values) tree.insert(v);
        tree.inorderPrint(tree.root);   // 20 30 40 50 60 70 80
    }
}"""
)

H('9.9  Real-Life Scenarios', 2)
BULLET('In-order ↔ a sorted bookshelf (reading left to right).')
BULLET('Pre-order ↔ a backup tool (folder before its contents).')
BULLET('Post-order ↔ safely deleting a folder (contents before the folder).')
BULLET('BST ↔ a dictionary lookup (jump, don\u2019t scan).')

PAGE_BREAK()

# =====================================================================
# MODULE 10 — GRAPHS
# =====================================================================
H('MODULE 10 — GRAPHS', 1)

H('10.1  What Is a Graph?', 2)
P('A graph is a set of points (vertices) connected by lines (edges). Unlike a tree, a graph has no '
  'required starting point, and its connections are allowed to loop back and form cycles.')

H('10.2  Directed vs. Undirected', 2)
TABLE(
    ['Type', 'Meaning', 'Example'],
    [
        ['Undirected', 'Edge works both ways (A ↔ B)', 'Friendship, two-way street'],
        ['Directed', 'Edge only goes one way (A → B, not B → A)', 'Follow, one-way street'],
    ]
)

H('10.3  Representing Graphs', 2)
P('Adjacency Matrix', bold=True)
BULLET('A grid of 0s and 1s sized vertices × vertices.')
BULLET('Instant "are X and Y connected?" lookup — but uses O(V²) space.')
BULLET('Best for small, densely connected graphs.')

P('Adjacency List', bold=True)
BULLET('Each vertex stores only its own list of neighbors.')
BULLET('Less space for large, sparse graphs (most real-world networks).')
BULLET('Best for most practical situations.')
CODE(
"""Map<String, List<String>> graph = new HashMap<>();
graph.put("A", Arrays.asList("B", "C"));
graph.put("B", Arrays.asList("A", "D"));
graph.put("C", Arrays.asList("A", "D"));
graph.put("D", Arrays.asList("B", "C", "E", "F"));
graph.put("E", Arrays.asList("D", "F"));
graph.put("F", Arrays.asList("D", "E"));"""
)

H('10.4  BFS — Breadth-First Search', 2)
P('Visits level by level, like ripples in a pond. Uses a Queue (FIFO). Good for the shortest path '
  'in unweighted graphs.')
CODE(
"""void bfs(String start, Map<String, List<String>> graph) {
    Queue<String> queue = new LinkedList<>();
    Set<String> visited = new HashSet<>();

    queue.add(start);
    visited.add(start);          // GOLDEN RULE: mark when queued

    while (!queue.isEmpty()) {
        String current = queue.poll();
        System.out.print(current + " ");
        for (String neighbor : graph.get(current)) {
            if (!visited.contains(neighbor)) {
                visited.add(neighbor);
                queue.add(neighbor);
            }
        }
    }
}"""
)

H('10.5  DFS — Depth-First Search', 2)
P('Dives as deep as possible down one path before backtracking. Uses a Stack (or recursion). Good '
  'for exploring every path, like solving a maze.')
CODE(
"""void dfs(String current,
         Map<String, List<String>> graph,
         Set<String> visited) {
    visited.add(current);
    System.out.print(current + " ");
    for (String neighbor : graph.get(current)) {
        if (!visited.contains(neighbor)) {
            dfs(neighbor, graph, visited);   // dive in
        }
    }
}"""
)

H('10.6  Canonical Graph Trace (start at A)', 2)
TABLE(
    ['Algorithm', 'Visit Order', 'Strategy'],
    [
        ['BFS (Queue)', 'A → B → C → D → E → F', 'Level by level (wide)'],
        ['DFS (Stack/Recursion)', 'A → B → D → C → E → F', 'Branch by branch (deep)'],
    ]
)

H('10.7  Golden Rule of BFS', 2)
P('Always mark a vertex as visited at the exact moment you add it to the queue — not later when '
  'you finally pull it out. Otherwise the same neighbor can be added twice.')

H('10.8  Real-World Applications', 2)
BULLET('Social Networks — people are vertices; follows are directed edges, friendships undirected.')
BULLET('Maps & Navigation — intersections are vertices, roads are edges.')
BULLET('The Internet — routers and connections.')
BULLET('Recommendation systems — "people who liked X also liked Y."')

PAGE_BREAK()

# =====================================================================
# MODULE 11 — BINARY SEARCH
# =====================================================================
H('MODULE 11 — BINARY SEARCH', 1)

H('11.1  The One Requirement: Sorted Data', 2)
P('Binary Search makes a bet at every step: "the target, if it exists, must be on this side, '
  'because everything is in order." That bet only pays off if the data is sorted.')

H('11.2  What Happens If It Isn\u2019t Sorted?', 2)
P('If the data isn\u2019t sorted, "smaller than mid" doesn\u2019t mean "must be on the left" — and the '
  'algorithm can eliminate the exact half holding the answer.')

H('11.3  The Core Idea: low, high, mid', 2)
TABLE(
    ['Concept', 'Meaning'],
    [
        ['low', 'Left boundary of the current search range.'],
        ['high', 'Right boundary of the current search range.'],
        ['mid', 'Midpoint: mid = low + (high - low) / 2.'],
        ['Compare & eliminate', 'If target < arr[mid], move high left. If larger, move low right.'],
        ['Stop when…', 'Target found, OR low > high (not in array).'],
    ]
)

H('11.4  Worked Example — Searching for 45', 2)
P('Sorted array: [3, 8, 15, 22, 34, 45, 56, 67, 78, 90]')
TABLE(
    ['Step', 'low', 'high', 'mid', 'arr[mid]', 'Compare', 'Result'],
    [
        [1, 0, 9, 4, 34, '45 > 34', 'Search right → low = 5'],
        [2, 5, 9, 7, 67, '45 < 67', 'Search left → high = 6'],
        [3, 5, 6, 5, 45, '45 == 45', 'FOUND at index 5'],
    ]
)
NOTE('Payoff:', 'Just 3 comparisons to find 45 in a 10-element array. Linear Search would need up to 10.')

H('11.5  Binary Search in Java', 2)
CODE(
"""int binarySearch(int[] arr, int target) {
    int low = 0;
    int high = arr.length - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;   // safer than (low + high) / 2

        if (arr[mid] == target) {
            return mid;
        } else if (target < arr[mid]) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return -1;   // not found
}"""
)

H('11.6  Linear Search vs. Binary Search', 2)
TABLE(
    ['Aspect', 'Linear Search', 'Binary Search'],
    [
        ['Data requirement', 'None — works on any list', 'Must already be sorted'],
        ['How it moves', 'One element at a time', 'Jumps to the middle, halves the range'],
        ['Comparisons (10-item example)', 'Up to 10', '3'],
        ['Best fit for', 'Small or frequently-changing lists', 'Large, already-sorted lists'],
    ]
)

H('11.7  Real-Life Scenarios', 2)
BULLET('Dictionaries and phone books — flip to the middle, jump to the right half.')
BULLET('"Guess the number" games — every "higher or lower" hint is one BS comparison.')
BULLET('Library catalogs — jump to the right shelf by call number.')
BULLET('Sorted contact lists — tap a letter instead of scrolling from A.')

PAGE_BREAK()

# =====================================================================
# MODULE 12 — ITERATIVE VS RECURSIVE
# =====================================================================
H('MODULE 12 — SEARCHING, PART 2: ITERATIVE VS. RECURSIVE', 1)

H('12.1  Iterative Binary Search', 2)
P('A while loop keeps narrowing the range by reassigning low and high. No extra memory needed '
  'beyond a few variables.')
CODE(
"""int binarySearchIterative(int[] arr, int target) {
    int low = 0;
    int high = arr.length - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) {
            return mid;
        } else if (target < arr[mid]) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return -1;
}"""
)

H('12.2  Recursive Binary Search', 2)
P('The method calls itself on a smaller range. It needs two base conditions: found, or low > high '
  '(not found).')
CODE(
"""int binarySearchRecursive(int[] arr, int target, int low, int high) {
    if (low > high) {
        return -1;                       // BASE CASE 1: not found
    }
    int mid = low + (high - low) / 2;
    if (arr[mid] == target) {
        return mid;                      // BASE CASE 2: found
    } else if (target < arr[mid]) {
        return binarySearchRecursive(arr, target, low, mid - 1);
    } else {
        return binarySearchRecursive(arr, target, mid + 1, high);
    }
}"""
)

H('12.3  Same Logic, Different Control Flow', 2)
TABLE(
    ['Aspect', 'Iterative', 'Recursive'],
    [
        ['Progress tracked by', 'Reassigning low and high in a loop', 'Passing a smaller range into the next call'],
        ['Stops when', 'low > high (loop ends)', 'low > high (base case hit)'],
        ['Memory', 'A few variables', 'One stack frame per call'],
        ['Readability', 'Slightly more moving parts', 'Often reads closer to the plain definition'],
        ['Main risk', 'Forgetting to update low / high', 'Missing the low > high base case'],
    ]
)

H('12.4  Three Common Bugs', 2)

P('Bug 1: Risky Mid Computation', bold=True)
P('The classic (low + high) / 2 can overflow on very large arrays before the division happens.')
CODE(
"""// Risky:
int mid = (low + high) / 2;

// Safer:
int mid = low + (high - low) / 2;"""
)

P('Bug 2: Forgetting to Shrink the Range', bold=True)
P('Updating low = mid instead of low = mid + 1 can freeze the search in an infinite loop.')
CODE(
"""// Buggy:
if (target > arr[mid]) {
    low = mid;      // BUG: should be mid + 1
}"""
)

P('Bug 3: Missing the Recursive Base Case', bold=True)
P('Without checking low > high, a recursive search that fails to find the target will keep calling '
  'itself with smaller and smaller ranges until the call stack overflows.')

H('12.5  Mini Project — Binary Search Race', 2)
CODE(
"""public class BinarySearchRace {
    static int iterative(int[] arr, int target) {
        int low = 0, high = arr.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] == target) return mid;
            else if (target < arr[mid]) high = mid - 1;
            else low = mid + 1;
        }
        return -1;
    }

    static int recursive(int[] arr, int target, int low, int high) {
        if (low > high) return -1;
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) return mid;
        else if (target < arr[mid]) return recursive(arr, target, low, mid - 1);
        else return recursive(arr, target, mid + 1, high);
    }

    public static void main(String[] args) {
        int[] arr = {3, 8, 15, 22, 34, 45, 56, 67, 78, 90};
        int target = 45;
        System.out.println("Iterative: " + iterative(arr, target));           // 5
        System.out.println("Recursive: " + recursive(arr, target, 0, arr.length - 1)); // 5
    }
}"""
)

PAGE_BREAK()

# =====================================================================
# MODULE 13 — INSERTION SORT
# =====================================================================
H('MODULE 13 — INSERTION SORT', 1)

H('13.1  The Core Idea: Sorting a Hand of Cards', 2)
P('You don\u2019t compare every card to every other card. You pick up the next card, slide it into '
  'the correct spot among the cards you\u2019re already holding in order, and move on.')

TABLE(
    ['Term', 'Meaning'],
    [
        ['Sorted portion', 'Left-hand section already arranged correctly; grows one element at a time.'],
        ['Shifting', 'Larger elements slide right one spot to open a gap; the current element drops in.'],
    ]
)

H('13.2  Worked Example — [8, 3, 5, 2]', 2)
TABLE(
    ['Step', 'Inserting', 'Shifts needed', 'Array after'],
    [
        [1, '8 (by itself)', '0', '[8 | 3, 5, 2]'],
        [2, '3', '1 (8 shifts)', '[3, 8 | 5, 2]'],
        [3, '5', '1 (8 shifts)', '[3, 5, 8 | 2]'],
        [4, '2', '3 (8, 5, 3 shift)', '[2, 3, 5, 8]'],
    ]
)

H('13.3  Insertion Sort in Java', 2)
CODE(
"""void insertionSort(int[] arr) {
    for (int i = 1; i < arr.length; i++) {
        int current = arr[i];     // pick up the next card
        int j = i - 1;

        // Shift larger elements right to open a gap
        while (j >= 0 && arr[j] > current) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = current;     // drop the card into its gap
    }
}"""
)

H('13.4  Swap vs. Shift', 2)
TABLE(
    ['Algorithm', 'Mechanism', 'Behavior'],
    [
        ['Bubble Sort', 'Swap', 'Neighbors trade places, one comparison at a time, over and over.'],
        ['Insertion Sort', 'Shift', 'Elements slide over one spot at a time; current element drops in.'],
    ]
)

H('13.5  Bubble Sort vs. Insertion Sort', 2)
TABLE(
    ['Aspect', 'Bubble Sort', 'Insertion Sort'],
    [
        ['How elements move', 'Multiple swaps', 'Direct insertion (shifting)'],
        ['Number of passes', 'Many', 'Fewer'],
        ['Uses existing order', 'Poorly', 'Effectively'],
        ['Stops early', 'Rarely', 'Naturally'],
        ['Practical efficiency', 'Lower', 'Higher'],
    ]
)

H('13.6  Nearly-Sorted Data: The Real Difference', 2)
P('Take [1, 2, 4, 3, 5] — only one pair is out of place.')
TABLE(
    ['Algorithm', 'Comparisons', 'Shifts / swaps'],
    [
        ['Insertion Sort', '4', '1'],
        ['Bubble Sort', '8 (two full passes)', '1'],
    ]
)
NOTE('Key insight:', 'Insertion Sort only touches what\u2019s actually out of place. Bubble Sort still '
                    'sweeps the entire array at least twice.')

H('13.7  Mini Project — Sort My Hand', 2)
CODE(
"""import java.util.Arrays;

public class SortMyHand {
    static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int current = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > current) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = current;
            System.out.println("After inserting " + current + ": " + Arrays.toString(arr));
        }
    }

    public static void main(String[] args) {
        int[] hand = {8, 3, 5, 2};
        insertionSort(hand);
    }
}

// Output:
// After inserting 3: [3, 8, 5, 2]
// After inserting 5: [3, 5, 8, 2]
// After inserting 2: [2, 3, 5, 8]"""
)

PAGE_BREAK()

# =====================================================================
# QUICK REFERENCE CHEAT SHEET
# =====================================================================
H('QUICK REFERENCE — CHEAT SHEET', 1)

H('Trees', 2)
TABLE(
    ['Term', 'One-line definition'],
    [
        ['Root', 'Topmost node, no parent'],
        ['Leaf', 'Node with no children'],
        ['Edge', 'Connection between parent and child'],
        ['Level', 'Steps down from the root (root = 0)'],
        ['Height', 'Deepest level in the tree'],
        ['General tree', 'Any number of children per node'],
        ['Binary tree', 'At most 2 children per node'],
    ]
)

H('Traversals', 2)
TABLE(
    ['Traversal', 'Order'],
    [
        ['In-order', 'Left → Root → Right'],
        ['Pre-order', 'Root → Left → Right'],
        ['Post-order', 'Left → Right → Root'],
    ]
)

H('BST', 2)
BULLET('Property: left < root < right, recursively.')
BULLET('In-order traversal of a BST produces sorted output.')
BULLET('Insertion: compare and step left/right until you find an empty spot.')

H('Graphs', 2)
TABLE(
    ['Concept', 'Note'],
    [
        ['Vertex / Edge', 'Point / connection'],
        ['Directed', 'One-way edge (A → B, not B → A)'],
        ['Adjacency Matrix', 'Grid of 0s and 1s — fast lookup, more space'],
        ['Adjacency List', 'Per-vertex neighbor list — less space for sparse graphs'],
        ['BFS', 'Queue-based, level by level'],
        ['DFS', 'Stack / recursion, dive deep first'],
    ]
)

H('Searching', 2)
TABLE(
    ['Algorithm', 'Requirement', 'Speed'],
    [
        ['Linear Search', 'None', 'Up to n comparisons'],
        ['Binary Search (iterative)', 'Sorted data', 'About log2(n) comparisons'],
        ['Binary Search (recursive)', 'Sorted data + base cases', 'Same as iterative'],
    ]
)

H('Sorting (Insertion)', 2)
BULLET('Grows a sorted portion left-to-right, one element at a time.')
BULLET('Shifts larger elements right; drops the current element into the gap.')
BULLET('Very fast on nearly-sorted data.')

PAGE_BREAK()

# =====================================================================
# PRACTICE QUESTIONS
# =====================================================================
H('PRACTICE QUESTIONS', 1)
P('Answer these on your own, then verify against the modules.', italic=True)

H('Part A — Multiple Choice', 2)
mc = [
    ('What is the topmost node of a tree called?',
     'A) Leaf   B) Root   C) Parent   D) Edge', 'B'),
    ('A node with no children is called a…',
     'A) Root   B) Parent   C) Leaf   D) Subtree', 'C'),
    ('A node in a binary tree can have at most how many children?',
     'A) 1   B) 2   C) 3   D) Unlimited', 'B'),
    ('Which traversal on a BST produces sorted output?',
     'A) Pre-order   B) Post-order   C) In-order   D) Level-order', 'C'),
    ('In a BST, if a value is greater than the current node, where do you go next?',
     'A) Left   B) Right   C) Stop   D) Delete', 'B'),
    ('What are the two core components of a graph?',
     'A) Root and Leaf   B) Vertices and Edges   C) Push and Pop   D) Front and Rear', 'B'),
    ('Which traversal explores as deep as possible before backtracking?',
     'A) BFS   B) DFS   C) In-order   D) Linear search', 'B'),
    ('Which data structure does BFS rely on?',
     'A) Stack   B) Queue   C) Array   D) Tree', 'B'),
    ('Binary Search requires the data to be…',
     'A) An integer array   B) Already sorted   C) Even-length   D) A String array', 'B'),
    ('Which is the safer mid calculation on very large arrays?',
     'A) (low + high) / 2   B) low + (high - low) / 2   C) high - low   D) low * high', 'B'),
    ('What does Insertion Sort do to make room for a new element?',
     'A) Swap pairs   B) Shift larger elements right   C) Delete elements   D) Reverse the array', 'B'),
    ('Which algorithm is generally more efficient on nearly-sorted data?',
     'A) Bubble Sort   B) Insertion Sort   C) Both equal   D) Neither works', 'B'),
]
for i, (q, opts, _) in enumerate(mc, 1):
    P(f'{i}. {q}', bold=True)
    P('    ' + opts, size=10)

H('Part B — Identification', 2)
ids = [
    'The single topmost node of a tree, with no parent of its own.',
    'A node with no children.',
    'The connection between a parent node and a child node.',
    'A tree where each node can have at most two children.',
    'The traversal that visits Left → Root → Right.',
    'The rule that says left subtree values < root < right subtree values.',
    'The points/entities in a graph.',
    'The traversal algorithm that uses a queue.',
    'The Binary Search version that uses a while loop.',
    'The sorting algorithm that uses shifting, not swapping.',
]
for i, q in enumerate(ids, 1):
    P(f'{i}. {q}')

H('Part C — Guess the Output', 2)
P('1. Using the BST (50, 30, 70, 20, 40, 60, 80), what does in-order traversal print?', bold=True)
P('2. Using the same BST, what does pre-order traversal print?', bold=True)
P('3. Using the graph with edges A-B, A-C, B-D, C-D, D-E, D-F, E-F, what does BFS from A print?', bold=True)
P('4. Using the same graph, what does DFS from A print (alphabetical neighbor order)?', bold=True)
P('5. Given [3, 8, 15, 22, 34, 45, 56, 67, 78, 90], what does binarySearch(arr, 45) return?', bold=True)
P('6. Given the same array, what does binarySearch(arr, 100) return?', bold=True)
P('7. Insertion Sort on [8, 3, 5, 2]: what does the array look like after inserting 5?', bold=True)

PAGE_BREAK()

# =====================================================================
# ANSWER KEY
# =====================================================================
H('ANSWER KEY', 1)

H('Part A — Multiple Choice', 2)
for i, (_, _, ans) in enumerate(mc, 1):
    P(f'{i}. {ans}')

H('Part B — Identification', 2)
answers_b = [
    'Root',
    'Leaf',
    'Edge',
    'Binary Tree',
    'In-order Traversal',
    'BST Property',
    'Vertices (Nodes)',
    'Breadth-First Search (BFS)',
    'Iterative Binary Search',
    'Insertion Sort',
]
for i, a in enumerate(answers_b, 1):
    P(f'{i}. {a}')

H('Part C — Guess the Output', 2)
answers_c = [
    '20 30 40 50 60 70 80',
    '50 30 20 40 70 60 80',
    'A B C D E F',
    'A B D C E F',
    '5',
    '-1',
    '[3, 5, 8, 2]',
]
for i, a in enumerate(answers_c, 1):
    P(f'{i}. {a}')

DOC.add_paragraph()
DIVIDER()
p = DOC.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('End of Reviewer — Modules 8 to 13')
r.bold = True
r.font.size = Pt(12)
r.font.color.rgb = RGBColor(0x1F, 0x3A, 0x5F)

# =====================================================================
# SAVE
# =====================================================================
OUT = 'DSA_Reviewer_Modules_8-13.docx'
DOC.save(OUT)
print(f'Saved: {OUT}')