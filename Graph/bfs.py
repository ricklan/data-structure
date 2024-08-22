def bfs(graph):
    visited = set()
    rows = len(graph)
    cols = len(graph[0])
    queue = [(0, 0)]
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while queue:
        r, c = queue.pop(0)
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
                queue.append((new_r, new_c))


graph = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
"""
A B C
D E F
G H I
"""
bfs(graph)
