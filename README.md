# Data Structure And Algorithms

## Arrays and Strings

**2 Pointers**

**Fast and Slow Pointers**

**Sliding Window**

## Linked List

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

## Queue

- First In First Out (FIFO)
- Can be implemented using an array

## Stack

- Last In First Out (LIFO)
- Can be implemented using an array

## [Binary Search](/Binary Search/BinarySearch.py)

- Input needs to be sorted.
- (Assuming the input is sorted in non-decreasing order). Have a left pointer at the start, and a right pointer at the end, and get the middle element. If the middle element is the target, return it. If the middle element is less than the target, move the left pointer to be its next element. Otherwise, move the right pointer to be its previous element.
- Time Complexity: O(log(n))

## Graph

## Tree

**Binary Tree**

**Binary Search Tree**

**Trie**

**Inorder Traversal**

**Preorder Traversal**

**Postorder Traversal**

**Level Order Traversal**

## Heap / Priority Queue

## Recursion

## Backtracking

## Dynamic Programming
