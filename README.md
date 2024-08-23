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

**Fast and Slow Pointers**

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

## Backtracking

## Dynamic Programming

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

## Heap / Priority Queue

## Greedy Algorithm

## Matrix

## Intervals
