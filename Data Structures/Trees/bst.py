class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Bst:

    def __init__(self):
        self.root = None
    
    def insert(self, val):
        node = Node(val)

        if(self.root == None):
            self.root = node
        else:
            cur = self.root
            while(True):
                if(val > cur.data):
                    if(cur.right == None):
                        cur.right = node
                        break;
                    else:
                        cur = cur.right
                else:
                    if(cur.left == None):
                        cur.left = node
                        break;
                    else:
                        cur = cur.left
    
    def search(self, val):
        cur = self.root

        while(cur != None):
            if(cur.data == val):
                return True
            elif(cur.data < val):
                cur = cur.right
            else:
                cur = cur.left
        
        return False
    
    def bfs(self):
        '''
        Traverses the tree level by level from left to right
        '''
        cur = self.root
        nodes = []
        if(cur is not None):
            nodes.append(cur)

        while(len(nodes) > 0):
            node = nodes.pop(0)
            print(node.data)
            if(node.left is not None):
                nodes.append(node.left)
            if(node.right is not None):
                nodes.append(node.right)
    
    def inorder(self, root):
        '''
        Traverses left, root, right
        '''
        if(root):
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    
    def preorder(self, root):
        '''
        Traverses root, left, right
        '''
        if(root):
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
    
    def postorder(self, root):
        '''
        Traverses left, right, root
        '''
        if(root):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
    
    def dfs(self, root):
        '''
        Traverses the tree in dfs iteratively
        '''
        stack = [root]
        while(stack):
            cur = stack.pop()
            print(cur.data)
            if(cur.left):
                stack.append(cur.left)
            if(cur.right):
                stack.append(cur.right)


if(__name__ == "__main__"):
    bst = Bst()
    bst.insert(1)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)
    print(bst.search(3))
    bst.bfs()
    print()
    bst.postorder(bst.root)
    print()
    bst.preorder(bst.root)
    print()
    bst.inorder(bst.root)
    print()
    bst.dfs(bst.root)

    