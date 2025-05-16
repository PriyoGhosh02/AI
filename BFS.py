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

def in_graph():
    graph={}
    nodes=int(input("Enter the number of nodes: "))
    for i in range(nodes):
        node=input("Enter node: ")
        naighbor=list(map(str, input(f"Enter {node} naighbor: ").split()))
        graph[node]=naighbor
    print("Graph: ", graph)
    return graph
    

def bfs(graph, src):
    visited = []
    queue = [src]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph.get(node, []))  #queue.extend(graph[node])
    return visited


print(f"BFS: {bfs(in_graph(), 'A')}")