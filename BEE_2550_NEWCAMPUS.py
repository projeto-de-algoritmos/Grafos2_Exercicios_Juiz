import heapq

while True:
    mst = []
    usedVertices = set()

    try:
        n_buildings, n_paths = map(int, input().split())
    except EOFError:
        break
    
    edges = [[] for _ in range(n_buildings)]
    for _ in range(n_paths):
        edge = tuple(map(int, input().split()))
        if edge[0] == edge[1]: continue
        heapq.heappush(edges[edge[0]-1], (edge[2], edge[1]-1))
        heapq.heappush(edges[edge[1]-1], (edge[2], edge[0]-1))

    cost, dest = 0, 1
    while len(usedVertices) < n_buildings: #change required here
        vertexWithSmallestEdge = 1
        for vertex in usedVertices:
            while len(edges[vertex]) > 0 and edges[vertex][0][dest] in usedVertices:
                heapq.heappop(edges[vertex])

            if len(edges[vertex]) == 0: continue

            if len(edges[vertexWithSmallestEdge]) == 0 or edges[vertex][0][cost] < edges[vertexWithSmallestEdge][0][cost]:
                vertexWithSmallestEdge = vertex

        edge = heapq.heappop(edges[vertexWithSmallestEdge])
        mst.append((vertexWithSmallestEdge+1, edge[dest]+1, edge[cost]))  # Adding 1 to vertex numbers
        usedVertices.add(vertexWithSmallestEdge)
        usedVertices.add(edge[dest])
    total_cost = sum(edge[2] for edge in mst)
    print(total_cost)
