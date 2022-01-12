import sys
from collections import deque

if __name__ == "__main__":
    M, N, H  = list(map(int, sys.stdin.readline().split()))
    R = 0
    num = 0
    bias = 0 
    value = deque()
    queue = deque()
    location = []
    
    for i in range(H):
        tmp = []
        for i in range(N):
            tmp.append(list(map(int, sys.stdin.readline().split())))
        location.append(tmp)
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if location[i][j][k] == 1:
                    queue.append((i, j, k))
                    value.append(0)
                elif location[i][j][k] == -1:
                    bias += 1
    while queue:
        v = value.popleft()
        z, y, x = queue.popleft()

        num += 1

        R = v if v > R else R

        tmp = []
        if  0 <= z < H - 1 and location[z + 1][y][x] == 0:
            tmp.append((z + 1, y, x))
        if  0 < z <= H - 1 and location[z - 1][y][x] == 0:
            tmp.append((z - 1, y, x))
        if  0 <= y < N - 1 and location[z][y + 1][x] == 0:
            tmp.append((z, y + 1, x))
        if  0 < y <= N - 1 and location[z][y - 1][x] == 0:
            tmp.append((z, y - 1, x))
        if  0 <= x < M - 1 and location[z][y][x + 1] == 0:
            tmp.append((z, y, x + 1))
        if  0 < x <= M - 1 and location[z][y][x - 1] == 0:
            tmp.append((z, y, x - 1))
        for i in tmp:
            queue.append(i)
            value.append(v + 1)
            location[i[0]][i[1]][i[2]] = -1
        pass
    
    if M * N * H == bias + num:
        print(R)
    else :
        print(-1)
    