import heapq, math

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

graph = {}

n_cities, n_agreements = map(int, input().split())

for x in range(1, n_cities + 1):
    add_node(graph, x)

for i in range(n_agreements):
    node1, node2, n_weight = map(int, input().split())
    add_path(graph, node1, node2, n_weight)
    if node2 in graph[node1] and node1 in graph[node2]:
        graph[node1][node2]=0
        graph[node2][node1]=0

n_cases = int(input())

for j in range(n_cases):
    node_s, node_e = map(int, input().split())
    distances, predecessors = dijkstra(graph, node_s)
    if math.isinf(distances[node_e]):
        print("Nao e possivel entregar a carta")
    else:
        print(distances[node_e])
    print()

