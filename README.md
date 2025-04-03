# Equip9-DSA-questions



1. Equipment Rental Availability (Graph Algorithm – BFS/DFS)
Problem Statement:
Equip9 manages a network of equipment rental providers. Each provider has connections with other providers, allowing customers to rent equipment even if their preferred provider does not have availability. Given a list of providers and their connections, determine the shortest path to find the nearest available equipment of a given type.
Input:
n (number of rental providers)
edges (list of connections between providers as [providerA, providerB])
availability (a dictionary {provider: [equipment_type1, equipment_type2, ...]})
start_provider (the provider where the customer is searching)
target_equipment (equipment type the customer needs)
Output:
Return the shortest path (minimum number of provider connections) to a provider that has the requested equipment. If no provider has it, return -1.
Example Input:
n = 5
edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
availability = {1: ["excavator"], 2: [], 3: ["bulldozer"], 4: ["excavator"], 5: ["crane"]}
start_provider = 2
target_equipment = "excavator"

Example Output:
[2, 3, 4]  # Shortest path to provider 4 with an excavator


2. Optimal Equipment Deal Matching (Heap/Priority Queue)
Problem Statement:
Equip9 allows buyers to place requests for specific equipment, and sellers list their available stock with a price. The goal is to match a buyer’s request with the best-priced seller offering the requested equipment. Implement a system that efficiently finds the seller with the lowest price for each incoming request.
Input:
requests (list of [equipment_type, max_price] requested by buyers)
sellers (list of [equipment_type, price] for available inventory)
Output:
Return a list where each request is matched with the lowest-priced seller (if available). If no seller meets the request criteria, return None for that request.
Example Input:
requests = [("excavator", 50000), ("bulldozer", 70000)]
sellers = [("excavator", 45000), ("bulldozer", 68000), ("excavator", 48000)]

Example Output:
[45000, 68000]  # Matches lowest available prices


3. Maintenance Log Analysis (Segment Tree or Fenwick Tree)
Problem Statement:
Equip9 tracks equipment maintenance history. Each piece of equipment has a maintenance log with records of maintenance costs over time. Given multiple queries asking for the total maintenance cost in a specific date range, implement an efficient way to process these queries.
Input:
n (number of maintenance records)
maintenance_logs (list of [equipment_id, date, cost] sorted by date)
queries (list of [start_date, end_date] asking for total cost in that range)
Output:
Return a list of total maintenance costs for each query.
Example Input:
maintenance_logs = [(101, "2024-01-01", 500), (102, "2024-01-10", 300), (101, "2024-01-15", 700)]
queries = [("2024-01-01", "2024-01-10"), ("2024-01-01", "2024-01-15")]

Example Output:
[800, 1500]  # Total maintenance cost in the given date range


