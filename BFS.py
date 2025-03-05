BFSgraph = {
    'A': ['S', 'D'],
    'B': ['S', 'E'],
    'C': ['S', 'F'],
    'D': ['A', 'G'],
    'E': ['B', 'G'],
    'F': ['C', 'G'],
    'G': ['D', 'E', 'F'],
    'S': ['A', 'B', 'C']
}

def bfs(graph, src):
    visited = []
    queue = [src]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            childs = graph[node]

            for child in childs:
                queue.append(child)
    return visited  

print(bfs(BFSgraph, 'A'))