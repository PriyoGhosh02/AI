graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": ["H"],
    "F": ["K"],
    "G": [],
    "H": [],
    "K": [],
}


def bfs(graph, src):
    visited = []
    queue = [src]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited


print(f"BFS:{bfs(graph, 'A')}")
