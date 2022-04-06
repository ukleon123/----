from sys import stdin
from collections import deque


if __name__ == "__main__":
    N = int(stdin.readline())
    f, s = map(int, stdin.readline().split())

    R = int(stdin.readline())
    graph = [set() for i in range(N)]
    
    for i in range(R):
        p, c = map(int, stdin.readline().split())
        graph[p - 1].add(c)
        graph[c - 1].add(p)
    
    flag = 1
    queue = deque()
    visited = [f]
    for i in graph[f - 1]:
        queue.append((i, 1))
    
    while queue:
        curr, level = queue.popleft()
        visited.append(curr)
        if curr == s:
            flag = 0
            print(level)
            break
        for i in graph[curr - 1]:
            if i not in visited and i not in queue:
                queue.append((i, level + 1))
    if flag:
        print(-1)

#bfs를 사용하여 최단경로를 탐색하는 문제