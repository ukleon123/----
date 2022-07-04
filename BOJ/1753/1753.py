import sys
import math
import heapq

def makeGraph(E):
    graph = {}
    for i in range(E):
        p1, p2, w = map(int, sys.stdin.readline().split())
        try:
            if graph[p1][p2] > w:
                graph[p1][p2] = w
        except:
            try:
                graph[p1][p2] = w
            except:
                graph[p1] = {}
                graph[p1][p2] = w
                graph[p1][p1] = 0
    return graph
    
def dijkstra(V, start, graph):
    priorityQueue = []
    distance = [math.inf for i in range(V)]
    distance[start - 1] = 0
    heapq.heappush(priorityQueue, (0, start))

    while priorityQueue:
        dist, curr = heapq.heappop(priorityQueue)
        if dist <= distance[curr - 1]:
            try:
                for i in graph[curr]:
                    node = i
                    nodeDist = dist + graph[curr][i]
                    if nodeDist < distance[node - 1]:
                        distance[node - 1] = nodeDist
                        heapq.heappush(priorityQueue, (nodeDist, node))
            except:
                pass    
    return distance
 

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    start = int(sys.stdin.readline())
    for i in dijkstra(V, start, makeGraph(E)):
        if i == math.inf:
            print('INF')
        else:
            print(i)
