import sys
import math
import heapq

def makeGraph(V):
    idx = 1
    offset = 0
    graph = {}
    for i in range(V):
        row = list(map(int, sys.stdin.readline().split()))
        for j in range(V):
            graph[idx] = {}
            if i > 0:
                graph[idx][idx - V] = row[j]
            if j > 0:
                graph[idx][idx - 1] = row[j]
            if i < V - 1:
                graph[idx][idx + V] = row[j]
            if j < V - 1:
                graph[idx][idx + 1] = row[j]
            elif i == V - 1 and j == V - 1:
                offset = row[j]
            graph[idx][idx] = 0
            idx += 1
    return graph, offset

def dijkstra(V, graph):
    priorityQueue = []
    distance = [math.inf for i in range(V ** 2)]
    distance[0] = 0
    heapq.heappush(priorityQueue, (0, 1))
    while priorityQueue:
        dist, curr = heapq.heappop(priorityQueue)
        if dist <= distance[curr - 1]:
            try:
                for node in graph[curr]:
                    nodeDist = dist + graph[curr][node]
                    if nodeDist < distance[node - 1]:
                        distance[node - 1] = nodeDist
                        heapq.heappush(priorityQueue, (nodeDist, node))
            except:
                pass

    return distance

if __name__ == "__main__":
    i = 1
    while True:
        N = int(sys.stdin.readline())
        if not N:
            break
        graph, offset = makeGraph(N)
        result = dijkstra(N, graph)
        print("Problem %d:" %i, result[-1] + offset)
        i += 1