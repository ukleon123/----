import sys
from itertools import combinations

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    store = []
    customer = []

    for i in range(N):
        tmp = sys.stdin.readline().split()
        
        for j in range(N):
            if tmp[j] == '1':
                customer.append((i, j))
            elif tmp[j] == '2':
                store.append((i, j))

    case = list(combinations(store, M))
    min_r = 1e8
    for i in case:
        result_t = 0
        for j in customer:
            min_c = 1e8
            for k in i:
                dist = abs(j[0] - k[0]) + abs(j[1] - k[1])
                if dist < min_c:
                    min_c = dist
            result_t += min_c

        if result_t < min_r: 
            min_r = result_t
    print(min_r)