# graph = {
#     "A": ["B", "C"],
#     "B": ["D", "E"],
#     "C": ["F", "G"],
#     "D": [],
#     "E": ["H"],
#     "F": ["K"],
#     "G": [],
#     "H": [],
#     "K": [],
# }

def take_graph():
    n=int(input("Enter the number of node: "))
    graph={}
    for i in range(n):
        node=input("Enter node: ")
        naighbor=list(map(str, input(f"Enter {node} naighbor: ").split()))
        graph[node]=naighbor
    print("Graph: ", graph)
    return graph

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
            childs = reversed(graph.get(node, []))
            i += 1

            for child in childs:
                stack.append(child)
                if child not in level:
                    level[child] = i

    return visited


print(f"DFS:{dfs(take_graph(), 'a')}")
print(level)
