import math
from sys import stdin

def search(current : str, pos : tuple, off : tuple) -> None:
    """
    check recursively if current is square number
    """
    
    global result
    rCurrent = current[::-1]
    
    if check(current) and int(current) > result:
        result = int(current)
    if check(rCurrent) and int(rCurrent) > result:
        result = int(rCurrent)
    
    pos = (pos[0] + off[0], pos[1] + off[1])
    if pos[0] > N - 1 or pos[0] < 0 or pos[1] > M - 1 :
        return
    current = current + dataMatrix[pos[0]][pos[1]]
    search(current, pos, off)
    
    
def check(data : str) -> bool:
    """return true if data is square number"""
    if math.sqrt(int(data)).is_integer():
        return True
    return False

if __name__ == "__main__":
    result = -1
    dataMatrix = []
    N, M = map(int, stdin.readline().split())
    for _ in range(N):
        dataMatrix.append(list(stdin.readline()[:-1]))
    for i in range(N):
        for j in range(M):

            for k in range(N):
                for l in range(M):
                    if N == 1 and M == 1:
                        if check(dataMatrix[0][0]):
                            result = dataMatrix[0][0]
                    elif k or l:
                        search(dataMatrix[i][j], (i, j), (k, l))
                        search(dataMatrix[i][j], (i, j), (-k, l))
    print(result)