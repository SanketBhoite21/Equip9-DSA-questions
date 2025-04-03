from collections import deque

def find_shortest_path(n, edges, availability, start_provider, target_equipment):

    graph = {i: [] for i in range(1, n+1)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
  
    queue = deque()
    queue.append((start_provider, [start_provider]))  
    visited = set()
    visited.add(start_provider)
    
    while queue:
        current_provider, path = queue.popleft()
        
        
        if current_provider in availability and target_equipment in availability[current_provider]:
            return path
        
      
        for neighbor in graph[current_provider]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
    
    return -1


n = 5
edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
availability = {1: [], 2: [], 3: ["bulldozer"], 4: ["excavator"], 5: ["crane"]}
start_provider = 2
target_equipment = "excavator"

print(find_shortest_path(n, edges, availability, start_provider, target_equipment))  