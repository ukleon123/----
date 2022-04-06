import sys
import math


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    
    data = [[math.inf for i in range(N)] for i in range(N)]
    for i in range(N):
        friends = sys.stdin.readline()[:-1]
        for j in range(N):
            if friends[j] == 'Y':
                data[i][j] = 1
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if j != k:
                    data[j][k] = min(data[j][k], data[j][i] + data[i][k])
                else :
                    data[j][k] = 0
    
    result = 0
    for i in range(N):
        tmp = 0
        for j in range(N):
            if i != j and data[i][j] <= 2:
                tmp += 1
        if tmp > result:
            result = tmp
    print(result)
