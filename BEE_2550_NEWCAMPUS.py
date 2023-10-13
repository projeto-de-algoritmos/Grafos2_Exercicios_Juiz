import queue

while True:
    mst = []
    usedVertices = set()

    try:
        n_buildings, n_paths = map(int, input().split())
    except EOFError:
        break

    edges = [[] for _ in range(n_buildings)]
    min_edges = [float('inf')] * n_buildings 

    for _ in range(n_paths):
        edge = tuple(map(int, input().split()))
        if edge[0] == edge[1]: continue
        edges[edge[0]-1].append((edge[2], edge[1]-1))
        edges[edge[1]-1].append((edge[2], edge[0]-1))

        if edge[2] < min_edges[edge[0]-1]:
            min_edges[edge[0]-1] = edge[2]
        if edge[2] < min_edges[edge[1]-1]:
            min_edges[edge[1]-1] = edge[2]

    pq = queue.PriorityQueue()
    for i in range(1, n_buildings):
        pq.put((min_edges[i], i))

    total_cost = 0
    while not pq.empty():
        cost, vertex = pq.get()
        if vertex in usedVertices:
            continue
        usedVertices.add(vertex)
        total_cost += cost

        for edge_cost, neighbor in edges[vertex]:
            if neighbor not in usedVertices:
                pq.put((edge_cost, neighbor))

    print(total_cost)