import sys

def nextNode(start, length):
    goal = len(data)
    result = []
    std1 = (goal - start) // data[start - 1]
    std2 = start - 1 // data[start - 1]

    for i in range(-std2, std1 + 1):
        tmp = start + i * length
        if 0 < tmp and tmp <= N:
            result.append(start + i * length)
    return result 


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    start, end = map(int, sys.stdin.readline().split())

    flag = 1
    queue = [(0, start)]
    
    visited = [0 for i in range(N)]
    visited[start - 1] = -1
    while queue:
        jump, current = queue.pop(0)
        if current != end:
            for i in nextNode(current, data[current - 1]):
                if -1 < visited[i - 1]:
                    queue.append((jump + 1, i))
                    visited[i - 1] = -1
        else:
            print(jump)
            flag = 0
            break
    if flag:
        print(-1)
    
# 3 3 1 2 1