def get_graph_from_file(filename):
    with open(filename, 'r') as file:
        V = int(file.readline().strip())
        adj = {}
        for i in range(V):
            edges = list(map(int, file.readline().strip().split()))
            adj[i] = edges
    return adj, V

print("Graph Coloring using Greedy Algorithm")
filename = input("Enter the filename containing the graph data: ")
graph,V=get_graph_from_file(filename)
print(f"Vertex: {V} Graph:{graph}")