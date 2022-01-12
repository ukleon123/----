import sys


if __name__ == "__main__":
    H, W = list(map(int, sys.stdin.readline().split()))
    location = []
    for i in range(H):
        location.append(list(map(int, list(sys.stdin.readline())[:-1])))
        pass
    dist = []
    queue = []
    visited = []
    dist.append(1)
    queue.append((0, 0))
    while queue:
        v = dist[0]
        y, x = queue[0]
        del dist[0]
        del queue[0]
        visited.append((y, x))
        tmp_x = []
        tmp_y = []
        if 0 <= x < W - 1:
            tmp_x.append(x + 1)
        if 0 < x <= W - 1:
            tmp_x.append(x - 1)
        if 0 <= y < H - 1:
            tmp_y.append(y + 1)
        if 0 < y <= H - 1:
            tmp_y.append(y - 1)
        for i in tmp_x:
            if location[y][i]:
                if (y, i) not in queue and (y, i) not in visited:
                    if (y, i) == (H - 1, W - 1):
                        print(v + 1)
                        exit()
                    dist.append(v + 1)
                    queue.append((y, i))
        for i in tmp_y:
            if location[i][x]:
                if (i, x) not in queue and (i, x) not in visited:
                    if (i, x) == (H - 1, W - 1):
                        print(v + 1)
                        exit()
                    dist.append(v + 1)
                    queue.append((i, x))

        pass
