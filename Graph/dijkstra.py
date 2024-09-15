import heapq


def dijkstra(graph, source_node):
    distances = {}
    for node in graph:
        distances[node] = float("inf")
    distances[source_node] = 0
    min_heap = [(0, source_node)]
    heapq.heapify(min_heap)

    while min_heap:
        cur_cost, node = heapq.heappop(min_heap)

        for neighbour, cost in graph[node].items():
            cost += cur_cost
            if cost < distances[neighbour]:
                distances[neighbour] = cost
                heapq.heappush(min_heap, (cost, neighbour))
    return distances


# Example graph represented as an adjacency list
graph = {
    "A": {"B": 5, "C": 9},
    "B": {"A": 5, "D": 2},
    "C": {"A": 9, "D": 1},
    "D": {"B": 2, "C": 1},
}

start_node = "A"
distances = dijkstra(graph, start_node)
print(f"Shortest distances from {start_node}: {distances}")
