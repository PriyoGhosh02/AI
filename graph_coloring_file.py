def get_from_file(filename):
    with open(filename, 'r') as file:
        V = int(file.readline().strip())
        graph = {}
        for i in range(V):
            edges = list(map(int, file.readline().strip().split()))
            graph[i] = edges
    return graph, V

def greedyColoring(adj, V):
    result = [-1] * V
    result[0] = 0
    available = [False] * V
    color = ["Red", "Green", "Blue"]

    for u in range(1, V):
        for i in adj[u]:
            if result[i] != -1:
                available[result[i]] = True

        cr = 0
        while cr < V:
            if not available[cr]:
                break
            cr += 1
        
        result[u] = cr

        for i in adj[u]:
            if result[i] != -1:
                available[result[i]] = False

    for u in range(V):
        print("Vertex", u, "--->  Color", color[result[u]])

filename = input("Enter the filename: ")
print("Graph Coloring: ")
graph, vertices = get_from_file(filename)
greedyColoring(graph, vertices)
