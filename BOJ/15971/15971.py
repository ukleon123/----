import sys
from collections import deque
from collections import defaultdict


if __name__ == "__main__":
    N, R1, R2 = map(int, sys.stdin.readline().split())
    # 한 지점에서 다른 지점으로 가는 경로는 1개
    path = defaultdict(int)
    graph = defaultdict(defaultdict)
    for _ in range(N - 1):
        n1, n2, d = map(int, sys.stdin.readline().split())
        graph[n1][n2] = d 
        graph[n2][n1] = d
    
    start = R1
    visited = {start}
    queue = deque([start])
    visited.add(start)
    while queue:
        current = queue.popleft()
        if current == R2:
            break
        for node in graph[current].keys():
            if node not in visited:
                path[node] = current
                queue.append(node)
                visited.add(node)
    
    queue.clear()
    current = R2
    while current != R1:
        queue.append(graph[current][path[current]])
        current = path[current]
    result = 0
    while queue.__len__() > 1:
        if queue[0] <= queue[-1]:
            result += queue.popleft()
        else:
            result += queue.pop()
    print(result)  