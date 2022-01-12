import sys
def insert_edge(primary, secondary):
    try:
        graph[primary].add(secondary)
    except:
        graph[primary] = set()
        graph[primary].add(secondary)

def dfs(graph, start):
    stack, result = list(), list()
    for i in graph:
        graph[i].reverse()
    try: 
        graph[start]
    except:
        return start
    stack.append(start)
    while stack:
        current = stack.pop()
        for i in graph[current]:
            if i not in result:
                stack.append(i)
        if current not in result:
            result.append(current)
    return result

def bfs(graph, start):
    queue, result = list(), list()
    queue.append(start)
    try: 
        graph[start]
    except:
        return start
    while queue:
        current = queue.pop(0)
        for i in graph[current]:
            if i not in result:
                queue.append(i)
        if current not in result:
            result.append(current)
    return result
if __name__ == "__main__":
    graph = dict()
    N, R, S = list(map(int, sys.stdin.readline().split()))
    
    for i in range(R):
        s, e = list(map(int, sys.stdin.readline().split()))
        insert_edge(s, e)
        insert_edge(e, s)
    for i in graph:
        graph[i] = list(graph[i])
        graph[i].sort()
    answer_bfs = bfs(graph, S)
    answer_dfs = dfs(graph, S)
    if S in graph:
        for i in answer_dfs:
            print (i, end=' ')
        print()
        for i in answer_bfs:
            print (i, end=' ')
        print()
    else:
        print(S)
        print(S)
    pass
