# Data Structure And Algorithms

## Arrays and Strings

**2 Pointers**

**Fast and Slow Pointers**

**Sliding Window**

## [Linked List](https://github.com/ricklan/data-structure/tree/main/Linked%20List)

- The **head** of the linked list is the first node.
- The **tail** of the linked list is the last node.

**Single Linked List (SLL)**

- Each node has a pointer to the next node.
- The tail points to `None`.
- E.g. [Head] --> [Node 2] --> ... --> [Tail] -->

**Doubly Linked List (DLL)**

- Each node has a pointer to the next node and to the previous node.
- The head's previous pointer points to `None`.
- The tail's next pointer points to `None`.
- E.g. <-- [Head] <--> [Node 2] <--> ... <--> [Tail] -->

**Circular Linked List (CLL)**

- Each node has a pointer to the next node.
- The tail points to `head`.

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

## Graph

## Tree

- Every tree is a graph.
- Trees are graphs where there are no cycles.
- The root is the first node of the tree.
- The node which is a predecessor of any node is the parent node.
- The node which is descendant of any node is the child node.
- A leaf is a node that doesn't have any children.
- Edges connect 2 nodes to each other.
- A path is the sequence of nodes and edges from 1 node to another.

**Binary Tree**

- Each node has at most 2 children.

**Binary Search Tree**

- A special type of binary tree where the left child is smaller than the parent and the right child is bigger than the parent.

**Trie**

- A trie is a type of tree data structure that is used to store a dynamic set or associative array where the keys are usually strings. It is also known as a "prefix tree" because it is used to efficiently store and retrieve keys that share common prefixes.
- Nodes: Each node in a trie represents a single character of a key. The root node is usually empty and does not contain any character.
- Edges: An edge connects two nodes and represents the transition from one character to the next in a key.
- Paths: A path from the root to a node spells out a prefix of some key.
- End of Word Marker: Nodes can have a flag (or marker) to indicate the end of a valid word or key.

**Inorder Traversal**

- A type of tree traversal.
- Left, Root, Right
- In a BST, inorder traversal will get you the nodes in increasing order

**Preorder Traversal**

- A type of tree traversal.
- Root, Left, Right

**Postorder Traversal**

- A type of tree traversal.
- Left, Right, Root

**Level Order Traversal/Breadth First Search**

- You traverse the tree level by level, left to right. (Same logic as BFS)

## Heap / Priority Queue

## [Recursion](https://github.com/ricklan/data-structure/tree/main/Recursion)

- The base case is the condition under which the recursion stops. Without a base case, the function would continue to call itself indefinitely, leading to a stack overflow error. The base case is typically a simple, non-recursive solution to the problem.

- The recursive case is where the function calls itself with a modified argument, moving towards the base case. The recursive case should always work towards simplifying the problem.

- E.g. In a recursive function for finding the factorial of a number, n, the base case would be when n is 0. The recursive case is `n * factorial(n-1)`.
  [See example](https://github.com/ricklan/data-structure/blob/main/Recursion/factorial.py)

## Backtracking

## Dynamic Programming

## Sorting Algorithms
