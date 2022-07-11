import sys
from collections import deque

def swap(state, num):
    state = list(state)
    state[num], state[num + 1] = state[num + 1], state[num]
    return state

def makeEnd(start, obj):
    e1 = 1
    e2 = 0
    first = []
    second = []
    for i in obj:
        for j in range(i):
            first.append(e1)
            second.append(e2)
        e1, e2 = e2, e1
    ret = []
    if first.count(1) == start.count(1):
        ret.append(first)
    if second.count(1) == start.count(1):
        ret.append(second)
    return ret


def search(state, goal, N):
    visited = {}
    queue = deque()
    queue.append((state, 0))
    while queue:
        currState, num = queue.popleft()
        if(currState in goal):
            return num
        try:
            if visited[str(currState)]:
                continue
        except:
            visited[str(currState)] = 1
            for i in range(N - 1):
                tmp = swap(tuple(currState), i)
                try:
                    if visited[str(tmp)]:
                        pass
                except:
                    queue.append((tmp, num + 1))
            

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    start = list(map(int, sys.stdin.readline().split()))
    object = list(map(int, sys.stdin.readline().split()))
    goal = makeEnd(start, object)
    print(search(start, goal, N))