import sys
from collections import deque


def search(x, y, size):
    distance = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    result = []
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if graph[nx][ny] <= size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cur_x][cur_y] + 1
                    if graph[nx][ny] < size and graph[nx][ny] != 0:
                        result.append((nx, ny, distance[nx][ny]))

    return sorted(result, key = lambda x: (-x[2], -x[0], -x[1]))


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    x, y = 0, 0
    cnt, size = 0, 2

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                x, y = i, j

    cnt, res = 0, 0
    while True:
        shark = search(x, y, size)
        if shark.__len__() == 0: break
        nx, ny, dist = shark.pop()

        cnt += 1
        res += dist
        graph[x][y], graph[nx][ny] = 0, 0
        x, y = nx, ny
        if cnt == size:
            size += 1
            cnt = 0
    print(res)