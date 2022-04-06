import sys

def dfs(graph):
    stack = []
    result = []
    result.append(1)
    stack += graph[0]
    while stack:
        current = stack[-1]
        del stack[-1]
        result.append(current)
        for i in graph[current - 1]:
            if i not in stack and i not in result:
                stack.append(i)
    return len(result) - 1


if __name__ == "__main__":
    
    node = int(sys.stdin.readline())
    edge = int(sys.stdin.readline())

    graph = [[] for i in range(node)]

    for idx in range(edge):
        start,end = list(map(int, sys.stdin.readline().split()))
        graph[start - 1].append(end)
        graph[end - 1].append(start)
        pass
    print(dfs(graph))
    pass