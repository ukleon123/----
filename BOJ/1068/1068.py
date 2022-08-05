import sys
from collections import deque

def remTree(root):
    queue = deque()
    queue.append(root)
    
    while queue:
        current = queue.popleft()
        for i in tree[current]:
            queue.append(i)
        del tree[current]


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    node = int(sys.stdin.readline())

    root = 0
    tree = {}
    for i in range(N):
        tree[i] = []
    for i in range(N):
        if data[i] >= 0:
            tree[data[i]].append(i)
        else:
            root = i
    remTree(node)
    result = 0
    for i in tree.values():
        if i == [] or (len(i) == 1 and i == [node]):
            result += 1
         
    print(result)