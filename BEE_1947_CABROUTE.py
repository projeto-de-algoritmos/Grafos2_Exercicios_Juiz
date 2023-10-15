import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    predecessors = {node: None for node in graph}
    distances[start] = 0
    
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, predecessors

def add_node(graph, node):
    if node not in graph:
        graph[node] = {}

def add_path(graph, node1, node2, weight):
    if node1 in graph and node2 in graph:
        graph[node1][node2] = weight
        graph[node2][node1] = weight

graph = {}

n_points, n_paths, n_tourist = map(int, input().split())

for x in range(1, n_points + 1):
    add_node(graph, x)

for i in range(n_paths):
    node1, node2, n_weight = input().split()
    add_path(graph, int(node1), int(node2), int(n_weight))

total_cost = 0
first_node = 1

for j in range(n_tourist):
    start_t, end_t = map(int, input().split())
    distances, predecessors = dijkstra(graph, first_node)
    total_cost += distances[start_t]
    print(f"total cost: {total_cost}")
    first_node = start_t
    print(f"first node: {first_node}")
    distances, predecessors = dijkstra(graph, first_node)
    total_cost += distances[end_t]
    print(f"total cost: {total_cost}")
    first_node = end_t
    print(f"first node: {first_node}")


distances, predecessors = dijkstra(graph, first_node)
total_cost += distances[1]

print(total_cost)

