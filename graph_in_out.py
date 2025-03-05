# Function to take graph input from the user
def get_graph():
    graph = {}
    nodes = int(input("Enter number of nodes: "))

    for _ in range(nodes):
        node = input("Enter node: ").strip()
        neighbors = input(f"Enter neighbors of {node} (space-separated): ").strip().split()
        graph[node] = neighbors

    return graph


print(f"Graph: {get_graph()}")

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
