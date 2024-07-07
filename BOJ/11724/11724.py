from sys import stdin
from collections import deque

def dfs(graph : dict, visited : list, start : int) -> list:
    stack = deque()
    stack.append(start)
    while stack:
        current = stack.pop()
        visited[current - 1] = True
        for i in graph[current]:
            if not visited[i - 1] and i not in stack:
                stack.append(i)
        
    return visited

if __name__ == "__main__" :
    Graph = {}
    V, E = map(int, stdin.readline().split())
    for i in range(V):
        Graph[i + 1] = []
    for _ in range(E):
        s, e = map(int, stdin.readline().split())
        Graph[s].append(e)
        Graph[e].append(s)

    result = 0
    Visited = [False for i in range(V)]
    for i in range(1, V + 1):
        if not Visited[i - 1]:
            dfs(Graph, Visited, i)
            result += 1

    print(result)

