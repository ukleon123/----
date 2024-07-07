import sys
import math


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    data = []
    for i in range(N):
        data.append(list(map(int, sys.stdin.readline().split())))
    
    DP = [[[] for _ in range(M)] for _ in range(N)]

    for i in range(M):
        for j in range(3):    
            DP[0][i].append(data[0][i])
    
    for i in range(1, N):
        for j in range(M):
            if j != M - 1:
                DP[i][j].append(min([DP[i - 1][j + 1][1], DP[i - 1][j + 1][2]]))
            else:
                DP[i][j].append(math.inf)

            DP[i][j].append(min([DP[i - 1][j][0], DP[i - 1][j][2]]))
            if j != 0:
                DP[i][j].append(min([DP[i - 1][j - 1][0], DP[i - 1][j - 1][1]]))
            else:
                DP[i][j].append(math.inf)
            for k in range(3):
                DP[i][j][k] += data[i][j]
    
    result = math.inf
    for i in range(M):
        tmp = min(DP[-1][i])
        if tmp < result:
            result = tmp
            
    print(result)