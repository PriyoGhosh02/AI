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


# def idfs(graph, src, depth):
#     visited = []
#     stack = [src]
#     level[src] = 0

#     while stack:
#         node, level = stack.pop()
#         if node not in visited:
#             visited.append(node)
#             childs = reversed(graph[node])

#             if level < depth:
#                 for child in childs:
#                     stack.append(child)
#                     level += 1

#     return visited


# print(f"IDFS: {idfs(graph, 'A', 3)}")

def get_graph():
    graph = {}
    nodes = int(input("Enter number of nodes: "))

    for _ in range(nodes):
        node = input("Enter node: ").strip()
        neighbors = input(f"Enter neighbors of {node} (space-separated): ").strip().split()
        graph[node] = neighbors

    return graph

graph = get_graph()

def idfs(graph, src, depth):
    visited = []
    stack = [(src, 0)]  

    while stack:
        node, node_level = stack.pop()  
        if node not in visited:
            visited.append(node)
            childs = reversed(graph[node])  

            if node_level < depth:
                for child in childs:
                    stack.append((child, node_level + 1)) 

    return visited

print(f"Graph: {graph}")
print(f"IDFS: {idfs(graph, 'A', 3)}")  
