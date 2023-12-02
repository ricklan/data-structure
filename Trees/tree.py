class Node:

    def __init__(self, val=0):
        self.data = val
        self.left = None
        self.right = None

def bfs(root):
    queue = [root]
    tmp = []
    while(queue):
        node = queue.pop(0)
        if(node):
            print(node.data)
            tmp.append(node.left)
            tmp.append(node.right)
        if(not queue):
            print('-----------')
            queue = tmp
            tmp = []
    

def dfs(root):
    if(not root):
        return

    print(root.data)
    dfs(root.left)
    dfs(root.right)
    print('-----------------')

def dfs_iterative(root):
    stack = [root]
    while(stack):
        node = stack.pop()
        if(node):
            print(node.data)
            stack.append(node.right)
            stack.append(node.left)
    print('-----------------')

if(__name__ == "__main__"):
    head = Node(1)
    node1 = Node(2)
    node2 = Node(3)
    node3 = Node(4)
    node4 = Node(5)
    head.left = node1
    head.right = node2
    node1.left = node3
    node1.right = node4
    bfs(head)
    dfs(head)
    dfs_iterative(head)
    