# Data Structure And Algorithms

## Hashset and Hashmap

- A `hashset` is a data structure that stores unique elements.
- Adding, checking and removal operations have an average of `O(1)` or `constant` time complexity for hashsets.
- A `hashmap` is a data structure that stores key-value pairs.
- Adding, checking and removal operations have an average of `O(1)` or `constant` time complexity for hashmaps.

## Arrays and Strings

**2 Pointers**

- This technique involves using two pointers to iterate through a data structure, typically an array, from different positions (E.g. one from the start and one from the end). The two pointers approach is useful for problems involving searching.
- Can reduce `O(n²)` time to `O(n)` time

**Sliding Window**

- This technique is particularly useful for problems involving subarrays or substrings.
- Involves 2 pointers.

## [Linked List](https://github.com/ricklan/data-structure/tree/main/Linked%20List)

- The **head** of the linked list is the first node.
- The **tail** of the linked list is the last node.

[**Single Linked List (SLL)**](https://github.com/ricklan/data-structure/blob/main/Linked%20List/SingleLinkedList.py)

- Each node has a pointer to the next node.
- The tail points to `None`.
- E.g. [Head] --> [Node 2] --> ... --> [Tail] -->

[**Doubly Linked List (DLL)**](https://github.com/ricklan/data-structure/blob/main/Linked%20List/DoublyLinkedList.py)

- Each node has a pointer to the next node and to the previous node.
- The head's previous pointer points to `None`.
- The tail's next pointer points to `None`.
- E.g. <-- [Head] <--> [Node 2] <--> ... <--> [Tail] -->

[**Circular Linked List (CLL)**](https://github.com/ricklan/data-structure/blob/main/Linked%20List/CircularLinkedList.py)

- Each node has a pointer to the next node.
- The tail points to `head`.

[**Fast and Slow Pointers**](https://github.com/ricklan/data-structure/blob/main/Linked%20List/CycleDetection.py)

- 2 pointers move at different speeds.
- Useful for detecting cycles.

## [Queue](https://github.com/ricklan/data-structure/blob/main/Stack%20%26%20Queue/Queue.py)

- First In First Out (FIFO)
- Can be implemented using an array

## [Stack](https://github.com/ricklan/data-structure/blob/main/Stack%20%26%20Queue/Stack.py)

- Last In First Out (LIFO)
- Can be implemented using an array

## [Binary Search](https://github.com/ricklan/data-structure/blob/main/Binary%20Search/BinarySearch.py)

- Input needs to be sorted.
- (Assuming the input is sorted in non-decreasing order). Have a left pointer at the start, and a right pointer at the end, and get the middle element. If the middle element is the target, return it. If the middle element is less than the target, move the left pointer to be its next element. Otherwise, move the right pointer to be its previous element.
- Time Complexity: O(log(n))

## [Graph](https://github.com/ricklan/data-structure/tree/main/Graph)

- A `node/vertex` represents an element on a graph.
- An `edge` connects 2 nodes.
- A `directed graph` is a graph where edges have a direction.
  E.g. (Node A)-->(Node B)
- An `undirected graph` is a graph where edges do not have a direction.
  E.g. (Node A)---(Node B)
- Two vertices are `adjacent` if they are connected directly by an edge.
- An `adjacency list` is a data structure showing all the nodes that are connected with each node.
- A `path` is a sequence of vertices connected by edges.
- A `simple path` has no repeated vertices.
- A `cycle` is a path that starts and ends at the same vertex.
- Depending on the question, the graph may be in the shape of a matrix or 2-D array
- May need to have an array of directions (E.g. `[(-1,0), (1,0), (0,1), (0,-1)]` representing `[left, right, up, down]`).
- `num_rows = len(graph)`
- `num_columns = len(graph[0])`

[**Breadth First Search (BFS)**](https://github.com/ricklan/data-structure/blob/main/Graph/bfs.py)

- Explores the graph level by level, starting from a given node.
- Useful for finding the shortest path in unweighted graphs.
- Implemented using a queue.

[**Depth First Search (DFS)**](https://github.com/ricklan/data-structure/blob/main/Graph/dfs.py)

- Explores as far as possible along a branch before backtracking.
- Can be implemented recursively or iteratively using a stack.
- Useful for pathfinding and detecting cycles.

[**Dijkstra’s Algorithm**](https://github.com/ricklan/data-structure/blob/main/Graph/dijkstra.py)
- Finds the shortest path between 2 vertices in a graph with non-negative weighted edges. The weight represents the distance or cost between 2 nodes.
- It's a greedy algorithm, as it always chooses the closest node that hasn't been processed yet.
- Algorithm
```
1. Start with a node. This is the source node.
2. Set the distance to all other nodes as infinity (or a large number). The distance to the source node is 0.
3. Mark all nodes as unvisited.
4. Select the unvisited node with the smallest known distance from the source node. Initially, this is the source node itself.
5. For this node, calculate the distance to its neighboring nodes. Update the shortest distance to each neighbor if a shorter path is found.
6. Once all neighbors have been considered, mark this node as visited. A visited node will not be checked again.
7. Repeat steps 4-7  until all nodes have been visited or until the shortest path to the target node is found.
```

[**Prim's Algorithm**](https://github.com/ricklan/data-structure/blob/main/Graph/prim.py)
- Finds the Minimum Spanning Tree (MST) for a connected, undirected graph.
- A **Minimum Spanning Tree (MST)** is a subset of the edges in a graph that connects all the vertices together without any cycles, and with the minimum possible total edge weight.
- Algorithm
```
1. Start with a node. This is the source node.
2. Mark the source node as part of the MST.
3. Initialize a min-heap to store the edges, sorted by their weight.
4. Select the edge with the minimum weight from the min-heap.
5. If the edge connects to a node not yet included in the MST, add it to the MST.
6. Mark this new node as visited, and add all edges connected to this new node to the min-heap (only those that connect to nodes not already in the MST).
7. Repeat steps 4-6 until all nodes are included in the MST.
```

[**Topological Sort**](https://github.com/ricklan/data-structure/blob/main/Graph/topological_sort.py)
- Is an ordering of nodes in a directed acyclic graph (DAG) where for each directed edge (A, B), node A appears before node B in the ordering.
- Topological orderings are not unqiue.
- E.g. If we have `A->B, A->C, B->D`, then one valid topological ordering is A,B,C,D.
- Can be done via DFS or Kahn's Algorithm
- Kahn's Algorithm
```
1. Add all nodes with in-degree 0 to a queue.
2. While the queue is not empty:
    a. Remove a node from the queue and add it to a list.
    b. For each outgoing edge from the removed node, decrement the in-degree of the destination node by 1.
    c. If the in-degree of a destination node becomes 0, add it to the queue.
3. If the queue is empty and there are still nodes in the graph, the graph contains a cycle and cannot be topologically sorted.
4. The nodes in the list represent the topological ordering of the graph.
```

## [Tree](https://github.com/ricklan/data-structure/tree/main/Trees)

- Every tree is a graph.
- Trees are graphs where there are no cycles.
- The `root` is the first node of the tree.
- The node which is a predecessor of any node is the `parent node`.
- The node which is descendant of any node is the `child node`.
- A `leaf` is a node that doesn't have any children.
- `Edges` connect 2 nodes to each other.
- A `path` is the sequence of nodes and edges from 1 node to another.

**Binary Tree**

- Each node has at most 2 children.

**Binary Search Tree**

- A special type of binary tree where the left child is smaller than the parent and the right child is bigger than the parent.

**Trie**

- A trie is a type of tree data structure that is used to store a dynamic set or associative array where the keys are usually strings. It is also known as a "prefix tree" because it is used to efficiently store and retrieve keys that share common prefixes.
- Each node in a trie represents a single character of a key. The root node is usually empty and does not contain any character.
- An edge connects two nodes and represents the transition from one character to the next in a key.
- A path from the root to a node spells out a prefix of some key.
- Nodes can have a flag (or marker) to indicate the end of a valid word or key.

[**Inorder Traversal**](https://github.com/ricklan/data-structure/blob/main/Trees/inorder_traversal.py)

- A type of tree traversal.
- Left, Root, Right
- In a BST, inorder traversal will get you the nodes in increasing order

[**Preorder Traversal**](https://github.com/ricklan/data-structure/blob/main/Trees/preorder_traversal.py)

- A type of tree traversal.
- Root, Left, Right

[**Postorder Traversal**](https://github.com/ricklan/data-structure/blob/main/Trees/postorder_traversal.py)

- A type of tree traversal.
- Left, Right, Root

[**Level Order Traversal/Breadth First Search**](https://github.com/ricklan/data-structure/blob/main/Trees/level_order_traversal.py)

- You traverse the tree level by level, left to right. (Same logic as BFS)

## [Recursion](https://github.com/ricklan/data-structure/tree/main/Recursion)

- The base case is the condition under which the recursion stops. Without a base case, the function would continue to call itself indefinitely, leading to a stack overflow error. The base case is typically a simple, non-recursive solution to the problem.

- The recursive case is where the function calls itself with a modified argument, moving towards the base case. The recursive case should always work towards simplifying the problem.

- E.g. In a recursive function for finding the factorial of a number, n, the base case would be when n is 0. The recursive case is `n * factorial(n-1)`.
  [See example](https://github.com/ricklan/data-structure/blob/main/Recursion/factorial.py)

## [Backtracking](https://github.com/ricklan/data-structure/tree/main/Backtracking)
- An algorithm used to find solutions to problems by incrementally building candidates for solutions and abandoning those candidates as soon as it is determined that they cannot be extended to a valid solution. It is commonly used for problems like permutations, combinations, and puzzles.
- Key Concepts of Backtracking
  1. Choice: Choose an option from the set of possible options.
  2. Constraint: Ensure that the choice is valid according to the problem’s constraints.
  3. oal Check: Check if the current solution is complete and valid.
  4. Backtrack: If the current choice does not lead to a solution, undo the choice and try the next option.
- Psuedo Code
```
def backtrack(candidate):
if find_solution(candidate):
    output(candidate)
    return

# iterate all possible candidates.
for next_candidate in list_of_candidates:
    if is_valid(next_candidate):
        # try this partial candidate solution
        place(next_candidate)
        # given the candidate, explore further.
        backtrack(next_candidate)
        # backtrack
        remove(next_candidate)
```

## [Dynamic Programming](https://github.com/ricklan/data-structure/tree/main/Dynamic%20Programming)
- A method used in computer science and optimization to solve problems by breaking them down into simpler subproblems. It’s particularly useful for problems where the same subproblems are solved multiple times.

- `Top-Down (Memoization):` This approach involves solving the problem by starting with the main problem and breaking it down into smaller subproblems, storing the results of these subproblems to avoid recomputation.

- `Bottom-Up (Tabulation):` This approach starts with the smallest subproblems and builds up the solution to the main problem by combining the solutions of these subproblems.

## [Sorting Algorithms](https://github.com/ricklan/data-structure/tree/main/Sort)

[**Bubble Sort**](https://github.com/ricklan/data-structure/blob/main/Sort/BubbleSort.py)

- Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.
- Time Complexity: `O(n²)`

[**Selection Sort**](https://github.com/ricklan/data-structure/blob/main/Sort/SelectionSort.py)

- Divides the list into a sorted and an unsorted part. Repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the end of the sorted part.
- Time Complexity: `O(n²)`

[**Insertion Sort**](https://github.com/ricklan/data-structure/blob/main/Sort/InsertionSort.py)

- Builds the sorted list one item at a time by repeatedly taking the next element from the unsorted part and inserting it into the correct position in the sorted part.
- Time Complexity: `O(n²)`

[**Merge Sort**](https://github.com/ricklan/data-structure/blob/main/Sort/MergeSort.py)

- A divide-and-conquer algorithm that splits the list into halves, recursively sorts each half, and then merges the sorted halves back together.
- Time Complexity: `O(n log n)`

[**Quick Sort**](https://github.com/ricklan/data-structure/blob/main/Sort/QuickSort.py)

- Uses the divide-and-conquer strategy to sort an array. It selects a "pivot" element and partitions the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.
- Time Complexity: `O(n log n)`

## Heap
- A **heap** is a binary tree-based data structure that follows the heap property. In a heap, the value of each node is compared to the values of its children in a specific way.
- In a **max heap** the root node contains the maximum value, and the values decrease as you move down the tree.
- In a **min heap** the root node contains the minimum value, and the values increase as you move down the tree.
- If you want to find the **top** or **biggest** k elements, use a **min heap**.
- If you want to find the **bottom** or **smallest** k elements, use a **max heap**.

## Greedy Algorithm

## Matrix

## Intervals
