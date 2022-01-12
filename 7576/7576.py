import sys
from collections import deque

if __name__ == "__main__":
    W, H = list(map(int, sys.stdin.readline().split()))
    M = 0
    num = 0
    bias = 0 
    value = deque()
    queue = deque()
    location = []
    
    for i in range(H):
        location.append(list(map(int, sys.stdin.readline().split())))
    for i in range(H):
        for j in range(W):
            if location[i][j] == 1:
                queue.append((i, j))
                value.append(0)
            elif location[i][j] == -1:
                bias += 1
    while queue:
        v = value.popleft()
        y, x = queue.popleft()

        num += 1

        M = v if v > M else M

        tmp = []
        if  0 <= y < H - 1 and location[y + 1][x] == 0:
            tmp.append((y + 1, x))
        if  0 < y <= H - 1 and location[y - 1][x] == 0:
            tmp.append((y - 1, x))
        if  0 <= x < W - 1 and location[y][x + 1] == 0:
            tmp.append((y, x + 1))
        if  0 < x <= W - 1 and location[y][x - 1] == 0:
            tmp.append((y, x - 1))
        for i in tmp:
            queue.append(i)
            value.append(v + 1)
            location[i[0]][i[1]] = -1
        pass
    
    if W * H == bias + num:
        print(M)
    else :
        print(-1)
    