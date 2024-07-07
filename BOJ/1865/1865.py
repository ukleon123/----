import sys


if __name__ == "__main__":
    test_case = int(sys.stdin.readline())
    for _ in range(test_case):
        graph = {}
        num_node, num_edge, num_hole = list(map(int, sys.stdin.readline().split()))
        for i in range(num_edge + num_hole):
            start, end, weight = list(map(int, sys.stdin.readline().split()))
            try:
                graph[start][end] = weight
            except:
                graph[start] = {}
                graph[start][end] = weight
            
        print(graph)