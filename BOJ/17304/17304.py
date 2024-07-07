import sys
from collections import deque

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    graph = {}
    for _ in range(M):
        l1, l2 = map(int, sys.stdin.readline().split())
        #check L1
        try:
            graph[l1].append(l2)
        except:
            graph[l1] = [l2]
        #check L2
        try :
            graph[l2].append(l1)
        except:
            graph[l2] = [l1]

    if len(graph) != N :
        print("NO")
    else :
        for i in range(N):
            stack = deque()
            stack.append(i)
            visited = [False for _ in range(N)]
            while stack:
                current = stack.pop()
                visited[current] = True
                for j in graph[current]:
                    if not visited[j]:
                        stack.append(j)
                    