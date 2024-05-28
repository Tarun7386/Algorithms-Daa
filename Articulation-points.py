def find_articulation_points(graph):
    ids = {}
    low = {}
    visited = set()
    articulation_points = set()
    id_counter = [0]

    def dfs(at, parent, out_edge_count):
        visited.add(at)
        ids[at] = low[at] = id_counter[0]
        id_counter[0] += 1
        children = 0

        for to in graph[at]:
            if to == parent:
                continue
            if to not in visited:
                children += 1
                dfs(to, at, out_edge_count + 1)
                low[at] = min(low[at], low[to])

                if parent is not None and low[to] >= ids[at]:
                    articulation_points.add(at)

                if parent is None and children > 1:
                    articulation_points.add(at)
            else:
                low[at] = min(low[at], ids[to])

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex, None, 0)

    return list(articulation_points)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C', 'E'],
    'E': ['D']
}

articulation_points = find_articulation_points(graph)

print("Articulation points:", articulation_points)
