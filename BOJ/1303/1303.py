import sys

def getDirection(pos):
    x = pos[0]
    y = pos[1]
    result = {
        'left' :(x - 1, y), 
        'right': (x + 1, y),
        'up': (x, y - 1),
        'down': (x, y + 1)
        }
    if x == 0:
        del result['left']
    if x == N - 1:
        del result['right']
    if y == 0:
        del result['up']
    if y == M - 1:
        del result['down']
    return result.values()
    

def dfs(start):
    count = 0
    stack = []
    stack.append(start)
    
    while stack:
        current = stack[-1]
        if visited[current[1]][current[0]] == 0:
            count = count + 1
        visited[current[1]][current[0]] = 1
        del stack[-1]
        

        for pos in getDirection(current):
            if visited[pos[1]][pos[0]] == 0 and battlefield[pos[1]][pos[0]] == battlefield[start[1]][start[0]]:
                stack.append(pos)

    return count ** 2

if __name__ == "__main__":
    N, M = list(map(int, sys.stdin.readline().split()))
    battlefield = []
    for i in range(M):
        battlefield.append(list(sys.stdin.readline()[:-1])) 
    
    blue = 0
    white = 0
    visited = [[0 for _ in range(N)]for _ in range(M)]
    for x in range(N):
        for y in range(M):
            if visited[y][x] == 0:
                if battlefield[y][x] == 'W':
                    white = white + dfs((x,y))
                else :
                    blue = blue + dfs((x,y))
        pass
    print(white, blue)
    pass