# Design and Analysis of Algorithms (DAA) -- Practical Programs

A collection of Python implementations for the DAA practical
assignments. There are **five assignment topics and six Python files**
because the 0/1 Knapsack problem is implemented using two different
strategies: Dynamic Programming and Branch and Bound.

## 1. How to Run the Programs on Linux

### Requirements

-   Linux (Ubuntu, Fedora, Debian, etc.)
-   Python 3
-   A terminal

The programs use only Python's standard library. **No external packages
or `pip install` commands are required.** The Huffman Coding program
uses Python's built-in `heapq` module.

### Check that Python 3 is installed

Open a terminal and run:

``` bash
python3 --version
```

If Python 3 is not installed, install it using your distribution's
package manager. For Ubuntu/Debian:

``` bash
sudo apt update
sudo apt install python3
```

### Open the project directory

If the files are in a folder named `DAA`, for example:

``` bash
cd path/to/DAA
```

Check that the six files are present:

``` bash
ls
```

You should see:

``` text
01Knapsack_BranchNbound.py
01Knapsack_DP.py
Fibonacci_Hanoi.py
Fractional_Knapsack_Greedy.py
Huffman_Coding.py
NQueens.py
```

### Run a program

Use `python3` followed by the filename:

``` bash
python3 Fibonacci_Hanoi.py
```

For the other programs:

``` bash
python3 Huffman_Coding.py
python3 Fractional_Knapsack_Greedy.py
python3 01Knapsack_DP.py
python3 01Knapsack_BranchNbound.py
python3 NQueens.py
```

Each program takes input through the terminal. Read the prompts and
enter the requested values. To stop a menu-based program, select its
Exit option. For the other programs, follow the prompts until the
program finishes.

> **Tip:** Linux filenames are case-sensitive. Type each filename
> exactly as shown. If a filename contains spaces, put it in quotes;
> these filenames do not contain spaces.

------------------------------------------------------------------------

## 2. Programs at a Glance

  -----------------------------------------------------------------------
  File                                Problem / Algorithm
  ----------------------------------- -----------------------------------
  `Fibonacci_Hanoi.py`                Fibonacci sequence using recursion
                                      and iteration; Tower of Hanoi using
                                      recursion

  `Huffman_Coding.py`                 Huffman encoding and decoding using
                                      a greedy strategy and a min-heap

  `Fractional_Knapsack_Greedy.py`     Fractional Knapsack using a greedy
                                      strategy

  `01Knapsack_DP.py`                  0/1 Knapsack using Dynamic
                                      Programming

  `01Knapsack_BranchNbound.py`        0/1 Knapsack using Branch and Bound

  `NQueens.py`                        N-Queens using backtracking, with
                                      the first queen fixed by the user
  -----------------------------------------------------------------------

## 3. Problem Statements and How the Solutions Work

### A. Fibonacci Sequence and Tower of Hanoi

**File:** `Fibonacci_Hanoi.py`

**Problem statement**

1.  Generate the Fibonacci sequence using both recursive and
    non-recursive (iterative) methods, and compare their execution times
    and complexities.
2.  Solve the Tower of Hanoi problem for a given number of disks using
    recursion.

**How the solution works**

-   **Recursive Fibonacci:** For `n > 1`, calculate each term as
    `fib(n - 1) + fib(n - 2)`. The base cases are `fib(0) = 0` and
    `fib(1) = 1`.
-   **Iterative Fibonacci:** Start with `0` and `1`, print the current
    term, and update the two values in a loop. This avoids repeated
    recursive calls.
-   **Tower of Hanoi:** Move `n - 1` disks from the source peg to the
    auxiliary peg, move the largest disk to the destination peg, and
    then move the `n - 1` disks from the auxiliary peg to the
    destination peg. The program counts and prints the moves.

**Complexity to remember**

  Method                         Time complexity          Auxiliary space
  --------------------- ------------------------ ------------------------
  Recursive Fibonacci     `O(2^n)` (upper bound)                   `O(n)`
  Iterative Fibonacci                     `O(n)`                   `O(1)`
  Tower of Hanoi                        `O(2^n)`   `O(n)` recursion stack

**Practical note:** The program uses input limits to keep the recursive
Fibonacci calculation and the printed Hanoi moves manageable.

### B. Huffman Coding

**File:** `Huffman_Coding.py`

**Problem statement**

Construct Huffman codes for the characters in a given text, encode text
into binary form, and decode a binary string back into text.

**How the solution works**

1.  Count how many times each character occurs in the input text.
2.  Insert each character and its frequency into a min-heap.
3.  Remove the two nodes with the smallest frequencies and combine them
    into a new node. Insert the combined node back into the heap.
4.  Repeat until one tree remains. This is the Huffman tree.
5.  Generate codes by traversing the tree: going left adds `0`, and
    going right adds `1`.
6.  **Encoding:** Replace each input character with its Huffman code.
7.  **Decoding:** Follow the tree according to each bit. A `0` means
    left and a `1` means right. Whenever a leaf is reached, append its
    character and return to the root.

The program has a menu to build the tree, encode text, decode binary
input, or exit. It also handles the special case where the input
contains only one distinct character by assigning that character the
code `0`.

**Complexity to remember**

-   Building the Huffman tree: `O(k log k)`, where `k` is the number of
    distinct characters.
-   Generating codes: `O(k)` tree traversal.
-   Encoding: proportional to the input length plus the length of the
    generated output.
-   Decoding: `O(b)`, where `b` is the number of input bits.

**Viva points:** Huffman Coding is a greedy algorithm. It repeatedly
combines the two least-frequent nodes. The min-heap efficiently
retrieves the smallest frequencies.

### C. Fractional Knapsack

**File:** `Fractional_Knapsack_Greedy.py`

**Problem statement**

Given items with profits (values) and weights, and a knapsack with a
maximum capacity, select items to maximize the total profit. Fractions
of an item are allowed.

**How the solution works**

1.  Calculate each item's profit-to-weight ratio:

    `ratio = value / weight`

2.  Sort the items in descending order of this ratio.

3.  Start filling the knapsack with the item having the highest ratio.

4.  If the complete item fits, take it and reduce the remaining
    capacity.

5.  If it does not fit completely, take only the fraction that fits and
    stop.

The total value is the sum of the values of the full items and the value
contributed by the final fraction, if any.

**Complexity to remember**

-   Sorting: `O(n log n)`.
-   Selecting items after sorting: `O(n)`.
-   Overall time: `O(n log n)`.
-   Storing the items: `O(n)` space.

**Viva points:** This is a greedy algorithm because it always chooses
the available item with the highest value-to-weight ratio. Fractions are
allowed, which is why the greedy choice gives an optimal solution for
Fractional Knapsack.

### D. 0/1 Knapsack using Dynamic Programming

**File:** `01Knapsack_DP.py`

**Problem statement**

Given `n` items, each with a value and a weight, find the maximum total
value that can fit in a knapsack of capacity `W`. Each item must either
be selected completely or not selected at all.

**How the solution works**

The program builds a two-dimensional DP table. `dp[i][w]` represents the
maximum value obtainable using the first `i` items with capacity `w`.

For each item, there are two choices:

-   **Exclude the item:** Keep the best value from the previous row,
    `dp[i-1][w]`.
-   **Include the item:** If its weight fits, add its value to the best
    result for the remaining capacity,
    `values[i-1] + dp[i-1][w-weights[i-1]]`.

The program stores the better of these choices. After filling the table,
it traces backwards through the table to identify the selected items.

**Complexity to remember**

-   Time: `O(nW)`.
-   Space: `O(nW)` for the DP table.

Here, `n` is the number of items and `W` is the integer knapsack
capacity. This is pseudo-polynomial time because the running time
depends on the numeric capacity `W`, not just the number of input bits
used to represent it.

**Viva points:** 0/1 means an item cannot be divided. Dynamic
Programming stores results of smaller subproblems and reuses them to
avoid solving the same subproblem repeatedly.

### E. 0/1 Knapsack using Branch and Bound

**File:** `01Knapsack_BranchNbound.py`

**Problem statement**

Solve the same 0/1 Knapsack problem, maximizing the total value without
exceeding the capacity, while either taking each item completely or
leaving it out.

**How the solution works**

1.  Sort items in descending order of value-to-weight ratio.
2.  Explore the decision for each item: include it if it fits, or
    exclude it.
3.  Maintain the best valid profit found so far.
4.  Calculate an **upper bound** on the profit that could be obtained
    from a search branch. The bound uses the fractional-knapsack idea:
    after taking as many remaining whole items as possible, it estimates
    the next item's fractional contribution.
5.  If this upper bound is no better than the best profit already found,
    stop exploring that branch. It cannot improve the current answer.
6.  Continue exploring promising branches and return the best valid
    selection.

The fractional estimate is used only to calculate an optimistic upper
bound. The final selected items still obey the 0/1 rule; no fractional
item is included in the final answer.

**Complexity to remember**

-   Sorting: `O(n log n)`.
-   Worst-case search: exponential; a conservative bound for this
    implementation is `O(n · 2^n)` because bound calculation can inspect
    remaining items at each search node.
-   Recursion space: `O(n)`, in addition to the storage for the items.

**Viva points:** Branch and Bound explores choices but prunes branches
that cannot beat the current best answer. The bound helps avoid
exploring every possible subset in many cases, but the worst case is
still exponential.

### F. N-Queens with the First Queen Fixed

**File:** `NQueens.py`

**Problem statement**

Place `n` queens on an `n × n` chessboard so that no two queens attack
each other. The first queen is already placed at a position entered by
the user. Use backtracking to place the remaining queens and generate a
final board.

**How the solution works**

1.  Create an `n × n` board, initially filled with `0`.
2.  Ask the user for the row and column of the first queen and place it
    there. The entered position is 1-based.
3.  Consider the remaining rows one by one.
4.  For each row, try each column. Before placing a queen, check whether
    the position is safe:
    -   no other queen is in the same row;
    -   no other queen is in the same column;
    -   no other queen is on either diagonal.
5.  If the position is safe, place the queen and recursively process the
    next row.
6.  If a later row has no safe position, remove the previously placed
    queen and try another column. This is **backtracking**.
7.  Stop when all rows have a queen, or report that no solution exists
    for the fixed first-queen position.

The board uses `1` for a queen and `0` for an empty square. The program
also prints intermediate placement and backtracking steps.

**Complexity to remember**

-   The search has a factorial worst-case bound, commonly described as
    `O(n!)` for the row-by-row placement search.
-   Each safety check in this implementation scans rows, columns, and
    diagonals, taking `O(n)` time.
-   A conservative overall time bound is `O(n · n!)`.
-   Board space: `O(n²)`, with `O(n)` additional recursion depth.

**Viva points:** Backtracking builds a solution step by step. When a
choice makes the remaining problem impossible, it undoes that choice and
tries another. Since the first queen is fixed, a valid solution is not
guaranteed for every starting position.

------------------------------------------------------------------------

## 4. Important Differences to Remember

### Fractional Knapsack vs. 0/1 Knapsack

  -----------------------------------------------------------------------
  Fractional Knapsack                 0/1 Knapsack
  ----------------------------------- -----------------------------------
  Fractions of items are allowed.     Items are either fully selected or
                                      not selected.

  Greedy by value/weight ratio gives  A simple greedy choice is not
  an optimal solution.                guaranteed to give an optimal
                                      solution.

  This repository solves it using     This repository provides DP and
  Greedy.                             Branch and Bound implementations.
  -----------------------------------------------------------------------

### Dynamic Programming vs. Branch and Bound

  -----------------------------------------------------------------------
  Dynamic Programming                 Branch and Bound
  ----------------------------------- -----------------------------------
  Stores solutions to subproblems in  Explores include/exclude decisions
  a table.                            as a search tree.

  Uses `O(nW)` time and `O(nW)` table Has exponential worst-case time;
  space.                              uses bounds to prune branches.

  A predictable method for integer    Can avoid many branches when the
  capacity `W`.                       bound is effective.
  -----------------------------------------------------------------------

## 5. Suggested Test Inputs

Use these as quick checks after running the programs. Follow the exact
prompts shown by each program.

### Fibonacci and Tower of Hanoi

-   Fibonacci terms: `7`; expected sequence: `0 1 1 2 3 5 8`.
-   Number of disks: `3`; expected number of moves: `7`.
-   Boundary check: `0` Fibonacci terms and `0` disks should produce no
    terms and no moves.

### Huffman Coding

-   Build a tree from `AAABBC`, encode `AAABBC`, and decode the
    generated bits. The decoded text should be `AAABBC`.
-   Build a tree from `AAAAA`. The single character should receive code
    `0`; encoding `AAAAA` should produce `00000`.
-   Try text containing spaces, such as `HELLO WORLD`, and verify that
    decoding reproduces the original text.
-   Try encoding a character that was not included when the tree was
    built; the program should report that the character is not in the
    tree.

### Fractional Knapsack

Use 3 items:

  Item     Value   Weight
  ------ ------- --------
  1           60       10
  2          100       20
  3          120       30

Capacity: `50`

Expected maximum value: **240.00**. The solution takes items 1 and 2
completely and two-thirds of item 3.

### 0/1 Knapsack -- DP and Branch and Bound

Use the same data in both programs:

  Item     Value   Weight
  ------ ------- --------
  1           60       10
  2          100       20
  3          120       30

Capacity: `50`

Expected maximum value: **220**. Items 2 and 3 are selected. Both
implementations should return the same optimal profit.

### N-Queens

-   `n = 4`, first queen at row `1`, column `2`: a solution exists. One
    valid final board is:

    ``` text
    0 1 0 0
    0 0 0 1
    1 0 0 0
    0 0 1 0
    ```

-   `n = 1`, first queen at row `1`, column `1`: the one-queen board is
    a solution.

-   `n = 2` or `n = 3`: no solution exists.

-   `n = 4`, first queen at row `1`, column `1`: no solution exists for
    that fixed starting position.

## 6. Quick Viva Revision

-   **What is a greedy algorithm?** An approach that makes the
    best-looking local choice at each step.
-   **What is recursion?** A function calling itself to solve smaller
    instances of a problem.
-   **What is backtracking?** Trying a choice, checking whether it can
    lead to a solution, and undoing it if it cannot.
-   **What is Dynamic Programming?** Solving overlapping subproblems and
    storing their results for reuse.
-   **What is Branch and Bound?** Searching possible solutions while
    using bounds to discard branches that cannot improve the best
    solution.
-   **What is a min-heap?** A data structure that gives access to the
    smallest-priority element; Huffman Coding uses it to repeatedly
    select the two least-frequent nodes.
-   **Why are the two knapsack problems different?** Fractional Knapsack
    permits taking part of an item; 0/1 Knapsack does not.
-   **Why can the two 0/1 Knapsack programs be useful together?** They
    solve the same optimization problem using two different algorithmic
    strategies, so their results can be compared.

------------------------------------------------------------------------

## 7. Repository Contents

``` text
.
├── 01Knapsack_BranchNbound.py
├── 01Knapsack_DP.py
├── Fibonacci_Hanoi.py
├── Fractional_Knapsack_Greedy.py
├── Huffman_Coding.py
├── NQueens.py
└── README.md
```

**Note:** This README describes the implementations and filenames in
this project. If you change a program's input prompts, validation rules,
or algorithm, update the corresponding section and test instructions as
well.
