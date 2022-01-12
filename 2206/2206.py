import sys
from collections import deque

if __name__ == "__main__":
    M, N = list(map(int, sys.stdin.readline().split()))

    location = []
    for i in range(M):
        location.append(list(map(int, list(sys.stdin.readline())[:-1])))
    

    queue = deque()
    value = deque()

    value.append((1, 1))
    queue.append((0, 0))
    location[0][0] = -1
    while queue:
        y, x = queue.popleft()
        v, c = value.popleft()

        tmp = []
        if y == M - 1 and x == N - 1: 
            print(v)
            exit()
        if 0 <= x < N - 1:
            tmp.append((y, x + 1))
        if 0 < x <= N - 1:
            tmp.append((y, x - 1))
        if 0 <= y < M - 1:
            tmp.append((y + 1, x))
        if 0 < y <= M - 1:
            tmp.append((y - 1, x))
        for i in tmp:
            if location[i[0]][i[1]] == 0:
                queue.append(i)
                value.append((v + 1, c))
                if c:
                    location[i[0]][i[1]] = -1
                elif c == 0:
                    location[i[0]][i[1]] = -2
            if c and location[i[0]][i[1]] == 1:
                queue.append(i)
                value.append((v + 1, c - 1))
            if c == 0 and location[i[0]][i[1]] == -1:
                queue.append(i)
                value.append((v + 1, c))
                location[i[0]][i[1]] = -3
            if c == 1 and location[i[0]][i[1]] == -2:
                queue.append(i)
                value.append((v + 1, c))
                location[i[0]][i[1]] = -3
            
            if i[0] == M - 1 and i[1] == N - 1:
                print(v + 1)
                exit()
    print(-1) 