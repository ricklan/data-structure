from node import Node


def inorder_traversal(node: Node):
    """
    inorder is left --> root --> right
    """
    if node:
        inorder_traversal(node.left)
        print(node.val)
        inorder_traversal(node.right)


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

inorder_traversal(root)
