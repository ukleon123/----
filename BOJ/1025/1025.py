import sys
import math
#this problem is brute force problem
#코드 진짜 더럽게도 짠다

result = -1

def search(current : str, pos : tuple, off : tuple) -> int:
    global result
    nextX = pos[0] + off[0]
    nextY = pos[1] + off[1]
    if   0 > nextX or nextX > N - 1 or 0 > nextY or nextY > M - 1:
        return current
    current += str(dataMatrix[nextX][nextY])

    ret = check(int(current))
    if ret and int(current) > result:
        result = int(current)
    ret = check(int(current[::-1]))
    if ret and int(current[::-1]) > result:
            result = int(current[::-1])

    return search(current, (nextX, nextY), off)

def check(data : int):
    if math.sqrt(data).is_integer():
        return True
    return False

if __name__ == "__main__":

    N, M = map(int, sys.stdin.readline().split())
    dataMatrix = []
    for _ in range(N):
        dataMatrix.append(list(map(int, sys.stdin.readline()[:-1])))
    
    # starting points
    for i in range(N):
        for j in range(M):
            #step offset
            for k in range(N):
                for l in range(M):
                    if k or l:
                        if check(dataMatrix[i][j]) and dataMatrix[i][j] > result:
                            result = dataMatrix[i][j]
                        search(str(dataMatrix[i][j]), (i, j), (k,l))
                        search(str(dataMatrix[i][j]), (i, j), (- k, l))
                    elif N == 1 and M == 1:
                        if check(dataMatrix[i][j]):
                            result = dataMatrix[i][j]
    
    print(result)

