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

def add_node(graph,node):
    if node not in graph:
        graph[node]={}

def add_path(graph,node1,node2,weight):
    if node1 in graph and node2 in graph:
        graph[node1][node2] = weight
        graph[node2][node1] = weight

graph = {}

n_points,n_paths,n_tourist = input().split()

for x in range(1,n_points+1):
    add_node(graph,x)

for i in range(n_paths):
    node1,node2,n_weight = input().split
    add_path(graph,node1,node2,n_weight)



first_node = 1
distances, predecessors = dijkstra(graph, first_node)

print("Shortest Distances:")
for node, distance in distances.items():
    print(f"From {first_node} to {node}: {distance}")

print("\nPredecessors:")
for node, predecessor in predecessors.items():
    print(f"Predecessor of {node}: {predecessor}")
