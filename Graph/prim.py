import heapq


def prim(graph, source_node):
    visited = set()
    mst_edges = []

    # min_heap keeps track of the cost, current node and parent node
    min_heap = [(0, source_node, None)]
    heapq.heapify(min_heap)

    while min_heap:
        cur_cost, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)

        if parent:
            mst_edges.append([parent, node, cur_cost])

        for neighbour, cost in graph[node].items():
            if neighbour not in visited:
                heapq.heappush(min_heap, (cost, neighbour, node))
    return mst_edges


# Example graph represented as an adjacency list
graph = {
    "A": {"B": 5, "C": 9},
    "B": {"A": 5, "D": 2, "C": 6},
    "C": {"A": 9, "B": 6, "D": 1},
    "D": {"B": 2, "C": 1},
}

start_node = "A"
mst_edges = prim(graph, start_node)

print("Edges in the MST:")
for edge in mst_edges:
    print(f"{edge[0]} -- {edge[1]} == {edge[2]}")
