import heapq

mst = []
usedVertices = set()
with open("sasassas") as f:
    numVertices = int(f.readline())
    edges = [[] for _ in range(numVertices)]
    for line in f.readlines():
        edge = tuple(map(int, line.split("")))
        if edge[0] == edge[1]: continue
        heapq.heappush(edges[edge[0]],(edge[2], edge[1]))
        heapq.heappush(edges[edge[1]],(edge[2], edge[0]))

cost, dest = 0, 1
while len(usedVertices) < numVertices:
    vertexWithSmallestEdge = 0
    for vertex in usedVertices:
        while len(edges[vertex]) > 0 and edges[vertex][0][dest] in usedVertices:
            heapq.heappop(edges[vertex])

        if len(edges[vertex]) == 0: continue

        if len(edges[vertexWithSmallestEdge]) == 0 or edges[vertex][0][cost] < edges[vertexWithSmallestEdge][0][cost]:
            vertexWithSmallestEdge = vertex

    edge = heapq.heappop(edges[vertexWithSmallestEdge])
    mst.append((vertexWithSmallestEdge, edge[dest], edge[cost]))
    usedVertices.add(vertexWithSmallestEdge)
    usedVertices.add(edge[dest])

    print(mst)
