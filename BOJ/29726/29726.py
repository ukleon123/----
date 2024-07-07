import sys
from collections import deque


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))
    suffix_max = []
    suffix_min = []

    data_min, data_max = 1e9, 0
    for i in range(M + 1):
        data_min = min(data_min, data[i])
        data_max = max(data_max, data[-(i + 1)])
        suffix_min.append(data_min)
        suffix_max.append(data_max)
    
    result = data[-1] - data[0]
    for i in range(M + 1):
        tmp = suffix_max[M - i] - suffix_min[i]
        result = max(result, tmp)
    print(result)

