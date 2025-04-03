from collections import deque

def find_shortest_path(n, edges, availability, start_provider, target_equipment):
    # Build the graph
    graph = {i: [] for i in range(1, n + 1)}
    for providerA, providerB in edges:
        graph[providerA].append(providerB)
        graph[providerB].append(providerA)
    
    # BFS setup
    queue = deque([[start_provider]])
    visited = set()
    visited.add(start_provider)
    
    while queue:
        path = queue.popleft()
        current = path[-1]
        
        # Check if current provider has the required equipment
        if target_equipment in availability.get(current, []):
            return path
        
        # Traverse neighbors
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    
    return -1  # No provider found

if __name__ == "__main__":
    
    
    n = 5
    edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
    availability = {
        1: ["excavator"],
        2: [],
        3: ["bulldozer"],
        4: ["excavator"],
        5: ["crane"]
    }
    start_provider = 2
    target_equipment = "excavator"
    
    result = find_shortest_path(n, edges, availability, start_provider, target_equipment)
    
    if result == -1:
        print("No provider found with the required equipment.")
    else:
        print("Shortest path:", result)
