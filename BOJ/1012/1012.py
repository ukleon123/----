import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for i in range(T):
        W, H, N = list(map(int, sys.stdin.readline().split()))
        location = [[0 for i in range(H)] for i in range(W)]
        for i in range(N):
            x, y = list(map(int, sys.stdin.readline().split()))
            location[x][y] = 1
        
        stack = []
        result = []
        visited = []
        tmp = 0
        for i in range(W):
            for j in range(H):
                if location[i][j] and (i, j) not in visited:
                    stack.append((i, j))
                    while stack:
                        c_x, c_y = stack[-1]
                        visited.append(stack[-1])
                        del stack[-1]
                        tmp_x = {c_x - 1, c_x + 1} if 0 < c_x < W - 1 else {c_x + 1} if c_x == 0 else {c_x - 1}
                        tmp_y = {c_y - 1, c_y + 1} if 0 < c_y < H - 1 else {c_y + 1} if c_y == 0 else {c_y - 1}
                        for x in tmp_x:
                            if (x, c_y) not in visited and location[x][c_y]:
                                stack.append((x, c_y))
                        for y in tmp_y:
                            if (c_x, y) not in visited and location[c_x][y]:
                                stack.append((c_x, y))
                    result.append(len(visited) - tmp)
                    tmp = len(visited)
        print(len(result))
        
        pass
    pass