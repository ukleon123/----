import sys

if __name__ == "__main__":
    
    result = []
    visited = []
    location = []
    tmp = 0
    N = int(sys.stdin.readline())
    
    for i in range(N):
        location.append(list(map(int, list(sys.stdin.readline())[:-1])))    
        pass
    for i in range(N):
        for j in range(N): 
            stack = []
            if location[i][j] and (i,j) not in visited:
                stack.append((i, j))
                while stack:
                    c_x, c_y = stack[-1]
                    if (c_x, c_y) not in visited:
                        visited.append((c_x, c_y))

                    del stack[-1]
                    tmp_x = {c_x - 1, c_x + 1} if 0 < c_x < N - 1 else {c_x + 1} if c_x == 0 else {c_x - 1}
                    tmp_y = {c_y - 1, c_y + 1} if 0 < c_y < N - 1 else {c_y + 1} if c_y == 0 else {c_y - 1}
                    for x in tmp_x:
                        if (x, c_y) not in visited and location[x][c_y]:
                            stack.append((x, c_y))
                    for y in tmp_y:
                        if (c_x, y) not in visited and location[c_x][y]:
                            stack.append((c_x, y))
                result.append(len(visited) - tmp)
                tmp = len(visited)
    print(len(result))
    result.sort()
    for i in result:
        print(i)

    pass