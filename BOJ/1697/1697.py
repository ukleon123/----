import sys
from collections import deque

if __name__ == "__main__":
    N, K = list(map(int, sys.stdin.readline().split()))
    
    location = [0 for i in range(int(1e5 + 1))]

    value = deque()
    queue = deque()
    visited = []
    value.append(0)
    queue.append(N)
    location[N] = 1
    while queue:
        v = value.popleft()
        x = queue.popleft()

        tmp = []
        if x == K:
            print(v)
            exit()
        if 0 <= x < 1e5:
            tmp.append(x + 1)
        if 0 < x <= 1e5:
            tmp.append(x - 1)
        if x <= 1e5//2 :
            tmp.append(2 * x) 

        for i in tmp:
            if location[i] == 0:
                if i == K:
                    print(v + 1)
                    exit()
                else:
                    queue.append(i)
                    location[i] = 1
                    value.append(v + 1)
    pass