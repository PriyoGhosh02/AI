# Function to take graph input from the user
def graph():
    graph = {}
    nodes = int(input("Enter number of nodes: "))

    for i in range(nodes):
        node = input("Enter node: ")
        neighbors = list(map(str, input(f"Enter neighbors of vertex {i} (space-separated): ").split()))
        graph[node] = neighbors
    return graph

print(f"Graph: {graph()}")


# another way to do this

# def get_graph(V):
#     #V = number of node
#     graph = {}
#     for i in range(V):
#         edges = list(map(int, input(f"Enter neighbors of vertex {i} (space-separated): ").split()))
#         graph[i] = edges
#     return graph

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
