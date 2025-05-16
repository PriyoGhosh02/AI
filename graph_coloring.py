def get_graph(V):
    adj = {}
    for i in range(V):
        edges = list(map(int, input(f"Enter neighbors of vertex {i}: ").split()))
        adj[i] = edges
    return adj

def greedyColoring(adj, V):
    result = [-1] * V
    result[0] = 0
    available = [False] * V
    color=["Red", "Green", "Blue"]

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


V = int(input("Enter number of vertices: "))
graph=get_graph(V)
print("Coloring of graph: ")
greedyColoring(graph, V)