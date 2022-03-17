import sys


def check():
    check = []
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                check.append((i, j))
    check.sort(key = lambda x : (-x[0], -x[1]))
    try:
        return check[0]
    except:
        return None

def turn(point):

    for i in range(N):
        for j in range(M):
            if i <= point[0] and j <= point[1]:
                board[i][j] = 0 if board[i][j] else 1

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    
    board = []
    for i in range(N):
        tmp = list(map(int, sys.stdin.readline()[:-1]))
        board.append(tmp)
    
    result =  0
    point = check()
    while point:
        turn(point)
        point = check()
        result += 1
    print(result)

    
#좌표가 가장 큰 부분 부터 뒤집으면 되는 문제 Greedy