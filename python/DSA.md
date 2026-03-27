# Data Structure
# stack
## **What is a Stack?**
- A Stack is a linear data structure that stores elements in a sequential order
- Insertion and Deletion of elements happen only from one end, called the top of the stack
- Follows the LIFO (Last In First Out) principle:
  - When an element is inserted, it is the last element in the stack
  - When an element is removed, it is the first one to be removed from the stack

## 5.2 -Common Operation

- Push ()
- Pop ()
- Peek ()
- isEmpty ()
- isFull ()
- top variable 

## 5.3 - Implementation

**In Python, Stacks can be implement in 3 different ways:**

- Lists/ Array
- collections
- Linked Lists


### Stack Implementation Using Array

stack implemented with an array stores elements in contiguous memory and uses a variable called top to track the index of the last inserted element.

**Core idea**

- `top = -1` → stack is empty
- When inserting → `top = top + 1`
- When removing → `top = top - 1`

#### Operations Logic
#### 1. **Push (Insert Element)**

 **Goal:** add element to the top

 **Steps**

   1. Check if stack is full
   2. Increase top
   3. Insert value at `stack[top]`

  **Push Algorithm**

       if top == size-1
           Stack Overflow
       else
          top = top + 1
          stack[top] = value

#### 2. **Pop (Remove Element)**

**Goal:** remove the top element

**Steps**

1. Check if stack is empty
2. Read element at top
3. Decrease top

    **Pop Algorithm**

       if top == -1
           Stack Underflow
       else
           value = stack[top]
           top = top - 1


### Stack Implementation Using Linked List

In this implementation, a stack is built using a linked list instead of an array.
Each element is stored in a node.

Each node contains:

> [ data | next ]

- data → value stored in the stack

- next → pointer to the next node

The top of the stack is the head of the linked list.

#### Core Stack Operations

#### 1. Push (Insert Element)

Insert a new node at the beginning of the linked list.

**Logic**

1. Create a new node
2. Store value in node
3. Point node.next to current top
4. Move top to new node
  

   **Push Algorithm**

      create newNode
      newNode.data = value
      newNode.next = top
      top = newNode

#### 2. Pop (Remove Element)

Remove the node from the top.

**Logic**

1. Check if stack is empty
2. Store top value
3. Move top to next node
4. Delete old node

**Pop Algorithm**

      if top == NULL
          Stack Underflow
      else
          temp = top
          top = top.next
          delete temp

### Array Stack vs Linked List Stack

| Feature        | Array Stack                             | Linked List Stack                       |
|----------------|-----------------------------------------|-----------------------------------------|
| Memory         | Fixed size                              | Dynamic size                            |
| Overflow       | Possible when array is full             | Rare (only when system memory is full)  |
| Implementation | Simple to implement                     | Slightly complex                        |
| Memory Usage   | Efficient (no extra memory per element) | Uses extra memory for pointer/reference |

## 5.4 - Complexity Analysis

Operations:

- Push   O(1)
- Pop    O(1)
- Peek   O(1)
- isEmpty O(1)
- isFull O(1)

## 5.5 - Applications

- Undo/Redo functionality in Text Editors
- Browser navigation (forward/backward)
- Function calls in programming
- Parentheses/Bracket matching


## 5.6 - Pros & Cons

### Advantages:

- Efficient Memory Management: Since data is added and removed only from one end, top
- Useful in Backtracking Problems: Allows navigation to previous states
- Prevents Data Inconsistency
- Ideal for Reversing Data

### Disadvantages:
- Limited Access: Can't reach middle or lower elements since only top is available
- Limited usability: Not suitable for random access or sorting
- Difficult to Traverse/Search: Since only the top element is readily accessible

## Monotonic Stack Pattern

A **Monotonic Stack** is a stack where elements are maintained in a specific sorted order.

### Types of Monotonic Stack

| Type                           | Order Maintained                        |
|--------------------------------|-----------------------------------------|
| **Monotonic Increasing Stack** | Elements increase from **bottom → top** |
| **Monotonic Decreasing Stack** | Elements decrease from **bottom → top** |

### Key Idea

The stack **removes elements that break the order** before pushing a new element.  
This ensures the stack always maintains the required monotonic property.

- **Increasing stack:** remove larger elements before pushing.
- **Decreasing stack:** remove smaller elements before pushing.

### Why Monotonic Stack is Used

This pattern is used when problems ask for:

- Next Greater Element
- Next Smaller Element
- Previous Greater Element
- Previous Smaller Element

## 5.7 -Coding Problems
1. **Valid Parentheses**

   Given a string containing ()[]{}, determine if the parentheses are valid.

2. **Next Greater Element**

   For each element in an array, find the next greater element on the right.

3. **Largest Rectangle in Histogram**

   Given bar heights, find the largest rectangle area.

4. **Daily Temperatures**

   Find how many days you must wait for a warmer temperature.

5. **Reverse a Stack**

   Reverse the elements of a stack without using another stack.

6. **Implement Stack Using Queue**
 
    Create a stack using only queue operations.
   
7. **Min Stack**

    Design a stack that supports:

      - push()
      - pop()
      - top()
      - getMin()

8. **Remove Adjacent Duplicates**

    Remove adjacent duplicates in a string.

9. **valuate Reverse Polish Notation**

    Evaluate postfix expression.
     
10. **Next Smaller Element**
    Find the next smaller element to the right.

---
# 6. Queues
- A Queue is a linear data structure that follows the FIFO (First In, First Out) principle —the first element added to the queue is the first one to be removed •

## Basic Queue Operations

| Operation | Meaning                                           |
|-----------|---------------------------------------------------|
| Enqueue   | Insert element at the rear (end)                  |
| Dequeue   | Remove element from the front                     |
| FrontPeek | View the first element without removing it        |
| isEmpty   | Check if the queue is empty                       |
| isFull    | Check if the queue is full (array implementation) |
| rearPeek  | View last element                                 |

## Queue Implementation Methods
Queues can be implemented using:

1. Array
2. Linked List
3. collections
4. **heapq:** Used for implementing Priority Queues
5. **queue:** Handles locking and blocking; suitable for cross-thread communication
6. **asyncio:** Suitable for async/await contexts

>  NOTE: The modules - queue and asyncio implementations aren't much used in DSA/CP context

### 1. Queue Using Array (Concept)

Two pointers are used:

1. front
2. rear

### 2. Queue Using Linked List

Each node contains:

> [data | next]

## Types of Queue

1. Simple Queue (Basic FIFO structure.)
2. Circular Queue (Used to reuse empty spaces in arrays.)
3. Priority Queue (Elements processed based on priority, not order.)
4. Deque (Double Ended Queue) (nsertion and deletion allowed at both ends.)

## 6.4 - Complexity Analysis
- Enqueue:     O(1)
- Dequeue:     O(1)
- FrontPeek:   O(1)
- RearPeek:    O(1)
- isEmpty:     O(1)

##  6.5 - Coding Problems

1. Implement Queue using Stack
   Design a queue using only stack operations.

    **Operations required**  
      - enqueue(x)
      - dequeue()
      - peek()
      - empty()
2. **First Non-Repeating Character in Stream**

   Given a stream of characters, return the first non-repeating character at each step.

3. **Sliding Window Maximum**

   Find the maximum element in every window of size k.

4. **Number of Recent Calls**

   Design a class that counts requests within last 3000 milliseconds.

5. **Rotting Oranges (BFS)**

   Grid problem where rotten oranges spread each minute.

6. **Circular Queue**

   Design a queue that wraps around when the end of array is reached.
   
   **Operations**
   - enQueue()
   - deQueue()
   - Front()
   - Rear()
   - isEmpty()
   - isFull()
   
7. **Task Scheduler**

   Given tasks with cooldown period n, find minimum time to finish tasks.

8. **Binary Tree Level Order Traversal**
   
   Traverse tree level by level.

9. **Moving Average from Data Stream**

   Return moving average of last `k` elements.

10. **Generate Binary Numbers**

   Generate first `n` binary numbers.


---

---

# 7. **Searching**

- Linear Search
- Binary Search
- Exponential Search
## 7.1 - Linear Search

- Linear search, also known as sequential search, is a fundamental search algorithm used to find a specific element within a data 
structure (array, linked list, etc.)

- It operates by sequentially examining each element in the collection until either the target element is found or the end of the 
collection is reached
-  **idea:** Check each element one by one until the target is found.


#### Steps

1. Start from the first element.
2. Compare it with the target value.
3. If equal → element found.
4. If not → move to the next element.
5. Repeat until the end of the data.

#### Working:

- The search begins at the first element of the data structure
- Each element is compared to the target value
- If a match is found, the index of the element is returned, and the search terminates
- If no match is found after checking all elements, the algorithm indicates that the element is not present
#### Characteristics:

- **Simplicity:** Linear search is easy to understand and implement
- **No Sorting Required:** It does not require the data to be sorted, making it suitable for unordered lists
- **Time Complexity:** In the worst-case scenario (element not present or at the very end), linear search has a time complexity of O(n)
- **Space Complexity:** It has a space complexity of O(1) as it only requires a constant amount of extra space

#### Time Complexity

| Case    | Complexity |
|---------|------------|
| Best    | O(1)       |
| Average | O(n)       |
| Worst   | O(n)       |


## 7.2 -Binary Search

- Binary Search is an efficient algorithm used to find the position of a target value within a sorted array or list 
- It works on the principle of "divide and conquer," repeatedly dividing the search interval in hal
- **Idea:** Works only on sorted data.
- Divide the array into halves repeatedly.

**Steps**

1. Find the middle element.
2. Compare it with the target.
3. If equal → found.
4. If target smaller → search left half.
5. If target larger → search right half.
6. Repeat.

#### Time Complexity

| Case    | Complexity |
|---------|------------|
| Best    | O(1)       |
| Average | O(log n)   |
| Worst   | O(log n)   |

#### Working:

- **Initialize Pointers:** Set a low pointer to the beginning of the array and a high pointer to the end of the array 
- **Calculate Midpoint:** Calculate the middle index mid as `low + (high -low) / 2` (to prevent potential integer overflow) 
- **Compare and Adjust:** 
    - If the element at `mid` is equal to the target value, the search is successful, and `mid` is returned ○
    - If the element at `mid` is less than the target value, the target must be in the right half of the array; Update `low` to `mid + 1` 
    - If the element at `mid` is greater than the target value, the target must be in the left half of the array; Update `high` to `mid -1` 
- **Repeat:**Continue steps 2 and 3 until the target is found or the low pointer crosses the `high` pointer (indicating the target is not in the array)

#### Characteristics:
- **Sorted Data Requirement:** Binary Search is only applicable to data structures that are sorted (ascending or descending) 
- **Time Complexity:** It has a time complexity of O(log N), making it significantly faster than linear search (O(N)) for large datasets 
- **Space Complexity:** It has a space complexity of O(1) as it only requires a few variables to store pointers

## 7.3 Exponential Search

- Exponential Search is a searching algorithm used to find an element in a sorted array.
- It works well when the size of the array is unknown or very large.
- Exponential Search, also known as Doubling Search or Galloping Search, is a search algorithm particularly efficient for sorted arrays 
- Most useful when the array is very large or its size is unknown (unbounded arrays)

**The idea:**

- Find a range where the element may exist by increasing the index exponentially.
- Once the range is found, apply Binary Search in that range.

**Steps**

1. Check the first element.
2. If target ≠ first element, start increasing index exponentially.
3. Stop when:
    - the index exceeds array size, or
    - the array value becomes greater than the target.
4. Now the element must lie between:
   > (i/2)  →  i
5. Perform Binary Search in that range.

**Working:** Operates in 2 main stages
1. **Finding the Range:**
   - The algorithm starts by checking the first element of the array; If it's the target, the search ends 
   - Otherwise, it iteratively doubles the index (bound = 1, then 2, 4, 8, etc.) as long as the element at the currentboundindex is less than the target value and 
the `bound` remains within the array limits
   - This stage aims to find a range[bound/2, min(bound, n-1)]wherenis the array size, such that the target element, if present, must lie within this range •
2. **Binary Search within the Range:** 
   - Once the appropriate range is identified, a standard Binary Search algorithm is applied within this narrowed-down range to locate the exact position of the 
   target element

**Characteristics:**
   - Efficient for very large or unbounded sorted arrays, especially when the target is near the beginning •
   - Better worst-case performance than linear search for large arrays

## Jump Search
## Interpolation Search

##  Coding Problems

1. **Find Element in Array**

   Given an array and a target value, return the index of the target element. Array: [4, 2, 7, 1, 9]  Target: 7

2. **Binary Search (Sorted Array)**

    Given a sorted array, find the index of the target element. Array: [1, 3, 5, 7, 9]  Target: 7

3. **First Occurrence of Element** 

    Find the first position of a target element in a sorted array with duplicates. Array: [1,2,2,2,3,4]  Target: 2

4. **Last Occurrence of Element**

    Find the last position of a target element. Array: [1,2,2,2,3]   Target: 2

5. **Count Occurrences**

   Count how many times an element appears in a sorted array.

6. **Find Minimum in Rotated Sorted Array**

   Array is sorted but rotated. Array: [6,7,8,1,2,3,4]

7. **Search in Rotated Sorted Array**

   Find a target in a rotated sorted array. Array: [6,7,8,1,2,3,4]  Target: 2

8. **Find Peak Element**

   Find an element greater than its neighbors.  Array: [1,3,20,4,1,0]

9. Find Square Root (Binary Search)

    Find integer square root of a number.

10. Two Sum (Search Pair)

   Find two numbers that add up to a target.


---

# 8. Sorting
## 8.1 - Introduction
**What is Sorting?**

Sorting is the process of arranging data in a particular format or order (ascending or descending)

**Why Sorting?**

- Helps in efficient searching (e.g., Binary Search)
- Simplifies data visualization and analysis
- Essential in data processing, ranking, and optimization problems

**Classifications of Sorting:**

1. **Based on Implementation:**
   - **Internal Sorting:** Entire data fits in main memory (e.g., Quick Sort, Merge Sort)
   - **External Sorting:** Data stored in external memory (e.g., External Merge Sort)
2. **Based on Stability:**
   - **Stable:** Equal elements maintain their relative order (e.g., Merge Sort, Insertion Sort)
   - **Unstable:** Equal elements may change order (e.g., Quick Sort, Heap Sort)
3. **Based on Time Complexity:**
   - **Quadratic Time (O(n²)):** Bubble, Selection, Insertion
   - **Log-linear Time (O(n log n)):** Merge, Quick, Heap

## 8.2 - Bubble Sort

**Main Ideas:**

- Compare neighboring pairs
- Swap if they’re out of order
- Keep repeating until no swaps are needed
- After each pass, the largest element moves to the end

**Key Points:**

- Very easy to understand and implement
- Inefficient for large lists

**Applications:**
- **Data Validation:** Quickly detect whether data is already sorted
- **Test Case Generation:** Verify correctness of complex sorting implementations

## 8.3 -Selection Sort

**Main Ideas:**
- Find the smallest element in the unsorted part of the list •
- Swap it with the first element of the unsorted section •
- Move the boundary between sorted and unsorted parts one step forward and repeat until the list is sorted


**Key Points:**
- Makes fewer swaps than Bubble Sort •
- Inefficient for large lists since it needs O(n²) comparisons

**Applications:**
- **Flash Memory:** Writes degrade hardware lifespan
- **Firmware & IoT systems:** Sorting configuration tables

## 8.4 -Insertion Sort

**Main Ideas:**
- Start from the second element and compare it with the elements before it 
- Insert the current element into its correct position in the already sorted part of the list 
- Repeat this for all elements until the entire list is sorted 

**Key Points:**
- Works well for small lists or lists that are almost sorted 
- Sorting happens in-place (no extra memory needed) 
- Inefficient for large lists

**Applications:**

- **Real-time streaming systems:** New data arrives continuously
- **Maintaining sorted order incrementally**

## 8.5 -Merge Sort

**Main Ideas:**
- Divide the list into two halves until each sublist has only one element 
- Merge the sublists by comparing elements and combining them in sorted order 
- Repeat merging until one fully sorted list is formed

**Key Points:**
- Based on the Divide and Conquer strategy 
- Very efficient for large datasets, with time complexity O(n log n) 
- Requires extra space for merging (not an in-place  algorithm)

**Applications:**
- External sorting(data > RAM) 
- Distributed computing frameworks 
- Stable sorting requirements

## 8.6 -Quick Sort

Main Ideas:
Choose a pivot element from the list 
Rearrange (partition) the list so that all elements smaller than the pivot are on its left, and all greater elements are on its right 
Recursively apply the same process to the left and right sublists until the list is sorted

Key Points:
Based on the Divide and Conquer strategy 
Faster than Merge Sort in practice for many datasets (average case: O(n log n)) 
In-place sorting algorithm (needs little extra space)

Applications:
Better Applications
System libraries
Low-latency applications
Real-time analytics

8.7 -Counting Sort

Main Ideas:
Count the frequency of each unique element in the input list •
Store these counts in an auxiliary array (called the count array) •
Use the count array to place each element directly in its correct sorted position in the output array

Key Points:
Works best for integers or discrete values within a small range •
Very fast when the range of input values is not much larger than the number of elements (time complexity O(n + k)) •
Not comparison-based and stable (if implemented carefully) •
Requires extra space for the count array, so not ideal for large ranges

Applications:
Better Applications
Voting systems
Telemetry & sensor data
Categorical data processing
Image processing

## 8.8 - Complexity Analysis

### Sorting Algorithms Time Complexity

| Algorithm      | Best Case  | Average Case | Worst Case | Stable |
|----------------|------------|--------------|------------|--------|
| Bubble Sort    | O(n)       | O(n²)        | O(n²)      | Yes    |
| Selection Sort | O(n²)      | O(n²)        | O(n²)      | No     |
| Insertion Sort | O(n)       | O(n²)        | O(n²)      | Yes    |
| Merge Sort     | O(n log n) | O(n log n)   | O(n log n) | Yes    |
| Quick Sort     | O(n log n) | O(n log n)   | O(n²)      | No     |
| Heap Sort      | O(n log n) | O(n log n)   | O(n log n) | No     |
| Counting Sort  | O(n + k)   | O(n + k)     | O(n + k)   | Yes    |

---

# 9. Recursion

## Introduction

**What is Recursion?**
- Programming technique where a function calls itself to solve smaller subproblems of the original problem 
- This process continues until a specific base case(or stopping condition) is met 
- At this point the recursion terminates and the results are combined back up the chain of calls to solve the original problem

**Structure of Recursive Functions:**

*A recursive solution typically has two components*

1. **Base Case:**
   - Stops recursion from continuing infinitely 
   - Should always be reachable 
   - Returns the answer for the smallest version of the problem 
2. **Recursive Case:** 
  - Divides the problem into smaller versions 
  - Should always progress toward base case

**Applications of Recursion:**
- Tree Traversals:Algorithms like in-order, pre-order, and post-order traversal are inherently recursive •
- Graph Algorithms:Depth-First Search (DFS) uses recursion to explore all possible paths in a graph •
- Sorting Algorithms:Quick Sort and Merge Sort are divide-and-conquer algorithms that use recursion to sort subarrays •
- Mathematical Problems:Calculating factorials, Fibonacci sequences, and the Tower of Hanoi puzzle are classic examples solved with recursion •
- Backtracking:Problems like solving a Sudoku puzzle or the N-Queens problem often rely heavily on recursion to explore different possibilities •

**Advantages:**
- Leads to shorter, cleaner, and more intuitive code 
- Ideal for Divide and Conquer algorithms 
- Good for Backtracking 
- Helps model Hierarchical Structures(file system, XML, JSON)

**Disadvantages:**
- High memory usage 
- Risk of Infinite Recursion 
- Harder to debug 
- Not always efficient 
- Limited by Maximum Recursion Depth(Python ~ 1,000 calls) 

**When to Use Recursion?**
- Problem is naturally repetitive 
- Tree/Graph traversal is needed 
- Need for Divide and Conquer algorithm 
- Backtracking/Search problems 
- Code clarity is more important than raw speed

## 9.2 -Internal Working

<b><u>Recursion is managed using aCall Stack, which is a Last-In, First-Out (LIFO) data structure:</b></u>

1.  <p style="color: lightgreen;"> When a function is called, a new stack frame (also known as an activation record) is created and pushed onto the call stack</p>
     - This frame stores the function's local variables, parameters, and the return address
2.  <p style="color: lightgreen;"> As the function recursively calls itself, new stack frames accumulate on top of the previous ones 

3.  <p style="color: lightgreen;"> Once the base case is reached, the functions start returning their results 

     - The top stack frame is popped off, and control returns to the function below it in the stack 
     - The function uses the returned result to perform its remaining calculations and return its own result 
     - This process is called stack <span style="color: lightblue;"> unwinding</span> or the <span style="color: lightblue;"> ascending phase </span>

**Examples:**
- Factorial 
- Fibonacci Numbers

## 9.3 - Common Mistakes


- **Forgetting the Base Case:**
   - Leads to infinite recursion
   - Overflow of the memory stack
- **Reducing the problem incorrectly:**
   - May skip base case
   - Could lead to infinite loop
- **Doing extra work in recursive return:**
   - Inefficient code
  
## 9.4 - Recursion vs Iteration

| Feature          | Recursion                                           | Iteration                                                    |
|------------------|-----------------------------------------------------|--------------------------------------------------------------|
| Function calls   | Yes                                                 | No                                                           |
| Memory usage     | Higher (stack)                                      | Lower                                                        |
| Code readability | Often simpler                                       | Sometimes longer                                             |
| Performance      | Sometimes slower                                    | Usually faster                                               |
| Mechanism        | A function calls itself until a "base case" is met. | A set of instructions is repeated using loops (for, while).  |
| Memory           | Uses the Call Stack (each call adds a new "frame"). | Uses a small, fixed amount of memory for loop variables.     |
| Code Style       | Often cleaner and more "mathematical."              | Can become "nested" and harder to read for complex logic.    |
| Risk             | Can lead to a StackOverflowError if too deep.       | Can lead to an infinite loop if the exit condition is wrong. |

# 9.5 -Coding Problems

1. Fibonacci Sequence

    **Task:** Compute the nth Fibonacci number recursively.

    **Skill:** Simple recursion, base case handling.

2. Factorial

    **Task:**  Compute n! recursively.

    **Skill:** Basic recursion, understanding stack growth.

3. Count Ways to Climb Stairs

    **Task:**  You can climb 1 or 2 steps at a time. Count all ways to reach the top.

    **Skill:**Recursion with multiple choices, combinatorics.

4. Reverse a String

    **Task:**  Reverse a string using recursion.

    **Skill:** String manipulation, recursive thinking.

5. Sum of Array Elements

    **Task:**  Recursively sum all elements in an array.

    **Skill:** Array recursion, base cases.

6. Power of a Number

    **Task:**  Compute x^n recursively (without loops).

    **Skill:** Divide and conquer, recursion optimization (optional: implement with O(log n) calls).

7. Subset Sum / All Subsets

    **Task:** Find all subsets of an array whose sum equals target T.

    **Skill:** Backtracking, recursion with arrays.

8. Maze / Rat in a Maze Problem

    **Task:**  Find all paths from top-left to bottom-right in a grid, moving only right or down.

    **Skill:** Backtracking, recursion on 2D arrays.

9. Generate All Permutations of a String / Array

    **Task:**  Return all possible permutations.

    **Skill:** Backtracking, swapping elements, recursion depth management.

10. N-Queens Problem

    **Task:**  Place N queens on an NxN chessboard so no two queens attack each other. Return all solutions.

    **Skill:** Advanced backtracking, recursion, constraints handling.

---

# 10 - Hashing

**What is Hashing?**
- Hashing is a technique that converts a key (string, number, object) into a fixed-size number called a hash value
- Makes use of a hash function to map data keys to a specific index in an array, known as a hash table

**Major Components in Hashing:**
- Key
- Hash Function
- Hash Table

**Common Workflow:**
- Convert key into hash value (hash function)
- Map the hash value to a smaller integer (compression function)
- Insert the key into the index position in array (hash table)

**Applications:**

| APPLICATION           | PURPOSE                 | EXAMPLE                       |
|----------------------|------------------------|-------------------------------|
| Database Indexing     | Fast lookup            | MySQL Hash Index              |
| Password Storage      | Security               | SHA-256, bcrypt               |
| Data Deduplication    | Avoid duplicates       | Dropbox, cloud storage        |
| Data Structures       | Key-value storage      | Python dict, Java HashMap     |
| Data Integrity        | Detect tampering       | MD5/SHA checksums             |
| Load Balancing        | Distribute requests    | Consistent Hashing            |
| Caching               | Quick access           | Web browsers                  |
| Plagiarism Detection  | Detect duplication     | Document Fingerprinting       |
| Networking            | P2P storage            | BitTorrent DHT                |
| Blockchain            | Secure transactions    | Bitcoin, Ethereum             |


# 10.2 - Hashing Function
