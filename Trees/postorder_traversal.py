from node import Node


def postorder_traversal(node: Node):
    """
    postorder is root --> left --> right
    """
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.val)


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

postorder_traversal(root)
