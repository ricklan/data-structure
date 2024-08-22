from node import Node


def preorder_traversal(node: Node):
    """
    preorder is root --> left --> right
    """
    if node:
        print(node.val)
        preorder_traversal(node.left)
        preorder_traversal(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

"""
The tree looks like
            1
        2           3
    4       5   6       7
"""

preorder_traversal(root)
