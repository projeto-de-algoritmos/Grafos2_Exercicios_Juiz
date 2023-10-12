import heapq

mst = []
usedVertices = set()

n_buildings = int(input())
n_paths = int(input())

edges = [[] for _ in range(n_buildings)]
for _ in range(n_paths):
    path = input()
    edge = tuple(map(int, path.split()))
    if edge[0] == edge[1]: continue
    heapq.heappush(edges[edge[0]-1], (edge[2], edge[1]-1))
    heapq.heappush(edges[edge[1]-1], (edge[2], edge[0]-1))

cost, dest = 0, 1
while len(usedVertices) < n_buildings:
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

print(mst)
