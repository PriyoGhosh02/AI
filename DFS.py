graph = {
    'A': ['S', 'D'],
    'B': ['S', 'E'],
    'C': ['S', 'F'],
    'D': ['A', 'G'],
    'E': ['B', 'G'],
    'F': ['C', 'G'],
    'G': ['D', 'E', 'F'],
    'S': ['A', 'B', 'C']
}

level = {}

def dfs(graph, src):
    visited = []
    stack = [src]
    level[src]=0
    i=0;
   
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            childs = reversed(graph[node])
            i+=1
           
            for child in childs:
                stack.append(child)
                if child not in level:
                    level[child]=i
               
    return visited

   
print(dfs(graph,'A'))
print(level)