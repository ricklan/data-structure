import collections


def topological_sort(edges):
    ordering = []
    indegrees = collections.defaultdict(int)
    queue = []
    adj_list = collections.defaultdict(list)
    visited = set()

    # [node1, node2] means node1 --> node2
    for node1, node2 in edges:
        if node1 not in indegrees:
            indegrees[node1] = 0

        if node2 not in indegrees:
            indegrees[node2] = 0

        indegrees[node2] += 1
        adj_list[node1].append(node2)

    for node, indegree_val in indegrees.items():
        if indegree_val == 0:
            visited.add(node)
            queue.append(node)

    while queue:
        node = queue.pop(0)
        ordering.append(node)
        for neighbour in adj_list[node]:
            indegrees[neighbour] -= 1

        if not queue:
            for new_node, indegree_val in indegrees.items():
                if indegree_val == 0 and new_node not in visited:
                    visited.add(new_node)
                    queue.append(new_node)

    return ordering


if __name__ == "__main__":
    """
    Graph looks like this
    A --> B --> D
      \--> C
    """
    edges = [["A", "B"], ["A", "C"], ["B", "D"]]
    result = topological_sort(edges)
    print(result)
