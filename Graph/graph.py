class Graph:
    def __init__(self, data):
        self.data = data
        self.adjacent = []
    
    def bfs(self):
        curNode = self
        queue = [curNode]
        visited = []

        while(len(queue) > 0):
            data = queue.pop(0)
            visited.append(data.data)
            for item in data.adjacent:
                if(item.data not in visited):
                    queue.append(item)
        
        print(visited)
    
    def dfs(self, visited):
        print(self.data)
        if(self.data in visited):
            return
        
        visited.append(self.data)
        for item in self.adjacent:
            item.dfs(visited)
        

# Creating the nodes
A = Graph("A")
B = Graph("B") 
C = Graph("C")
D = Graph("D")
E = Graph("E")
F = Graph("F")
G = Graph("G")
N = Graph("N")
I = Graph("I")
J = Graph("J")
K = Graph("K")
H = Graph("H")
 
# Assigning the adjacent nodes
A.adjacent = [B,C,D]
B.adjacent = [E,F]
C.adjacent = [N]
D.adjacent = [G,H]
E.adjacent = []
F.adjacent = [I,J]
I.adjacent = []
J.adjacent = []
N.adjacent = []
G.adjacent = [K]
H.adjacent = []

#                  A  
#              /   |  \  
#            B     C    D
#           / \    /   / \
#          E   F  N   G   H
#             / \      \
#            I   J       K

# DFS
print("DFS")  
A.dfs(visited = [])

print()

# BFS
print("BFS")
A.bfs()
