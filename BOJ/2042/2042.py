import sys

#세그먼트 트리만을 활용하는 간단한 문제 세그먼트 트리가 무엇인지 확실하게 알 수 있다
tree = None
def segmentTree(start, end, idx, data):
    if start == end :
        tree[idx - 1] = data[start]
        return tree[idx - 1]
    else:
        mid = (start + end) // 2
        tree[idx - 1] = segmentTree(start, mid, idx * 2, data) + segmentTree(mid + 1, end, idx * 2 + 1, data)
        return tree[idx - 1]

def partialSum(start, end, left, right, idx):
    if right < start or end < left:
        return 0
    elif left <= start and end <= right:
        return tree[idx - 1]
    else:
        mid = (start + end) // 2
        return partialSum(start, mid, left, right, idx * 2) + partialSum(mid + 1, end, left, right, idx * 2 + 1)

def updateTree(start, end, idx, pos, diff):
    if pos < start or end < pos: return
    tree[idx - 1] += diff
    if start == end: return
    
    mid = (start + end) // 2
    updateTree(start, mid, idx * 2, pos, diff)
    updateTree(mid + 1, end, idx * 2 + 1, pos, diff)

if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().split())

    tree = [None for i in range(4 * N)]
    data = []
    for _ in range(N):
        data.append(int(sys.stdin.readline()))
    segmentTree(0, N - 1, 1, data)

    for _ in range(M + K):
        argv = list(map(int, sys.stdin.readline().split()))
        if argv[0] == 1:
            updateTree(0, N - 1, 1, argv[1] - 1, argv[2] - data[argv[1] - 1])
            data[argv[1] - 1] = argv[2]
        else:
            print(partialSum(0, N - 1, argv[1] - 1, argv[2] - 1, 1))
