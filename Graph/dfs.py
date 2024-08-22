def dfs_iterative(graph):
    visited = set()
    rows = len(graph)
    cols = len(graph[0])
    stack = [(0, 0)]
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while stack:
        r, c = stack.pop()
        visited.add((r, c))
        print(graph[r][c])
        for x, y in directions:
            new_r = r + x
            new_c = c + y
            if (
                0 <= new_r < rows
                and 0 <= new_c < cols
                and (new_r, new_c) not in visited
            ):
                visited.add((new_r, new_c))
                stack.append((new_r, new_c))


visited = set()
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def dfs_recursive(graph, row, column):
    rows = len(graph)
    cols = len(graph[0])
    visited.add((row, column))
    print(graph[row][column])
    for x, y in directions:
        new_r = row + x
        new_c = column + y
        if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited:
            visited.add((new_r, new_c))
            dfs_recursive(graph, new_r, new_c)


graph = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
"""
A B C
D E F
G H I
"""
print("Iterative DFS")
dfs_iterative(graph)
print("Recursive DFS")
dfs_recursive(graph, 0, 0)
