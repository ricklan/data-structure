from node import Node


def level_order_traversal(node: Node):
    queue = [root]
    current_level_nodes = []
    next_level_nodes = []
    level = 1

    while queue:
        node = queue.pop(0)
        current_level_nodes.append(node.val)
        if node.left:
            next_level_nodes.append(node.left)
        if node.right:
            next_level_nodes.append(node.right)

        if not queue:
            if current_level_nodes:
                print(f"Level {level} nodes", current_level_nodes)
            queue = next_level_nodes[:]
            next_level_nodes = []
            current_level_nodes = []
            level += 1


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

level_order_traversal(root)
