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

level = {}


def dfs(graph, src):
    visited = []
    stack = [src]
    level[src] = 0
    i = 0

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            childs = reversed(graph[node])
            i += 1

            for child in childs:
                stack.append(child)
                if child not in level:
                    level[child] = i

    return visited


print(f"DFS:{dfs(graph, 'A')}")
print(level)
