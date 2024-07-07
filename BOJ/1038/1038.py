import sys
from collections import deque

if __name__ == "__main__":
    
    N = int(sys.stdin.readline())

    # will using bfs with check condition(back tracking)
    count = -1
    queue = deque()
    for i in range(10):
        queue.appendleft([i])
    while (queue):
        curr = queue.pop()
        count = count + 1
        if count == N:
            print("".join(map(str, curr)))
            quit()
        for i in range(0, curr[-1]):
            queue.appendleft(curr + [i])
    print(-1)
