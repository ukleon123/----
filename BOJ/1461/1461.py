import sys

if __name__ == "__main__":
    N, M = list(map(int, sys.stdin.readline().split()))
    points = list(map(int, sys.stdin.readline().split()))

    pos = []
    neg = []
    for i in points: pos.append(i) if i > 0 else neg.append(i)

    pos.sort()
    neg.sort(key = lambda x : -x)
    result = 0
    try:
        tmp = pos if abs(pos[-1]) > abs(neg[-1]) else neg
    except:
        tmp = pos if pos else neg
    result += abs(tmp[-1])
    if len(tmp) >= M:
        for i in range(M):
            tmp.pop()
    else:
        for i in range(len(tmp)):
            tmp.pop()
            
    while pos or neg:
        if len(pos) >= M:
            result += 2 * pos[-1]
            for i in range(M):
                pos.pop(-1)
        elif pos:
            result += 2 * pos[-1]
            for i in range(len(pos)):
                pos.pop(-1)
        if len(neg) > M:
            result += 2 * abs(neg[-1])
            for i in range(M):
                neg.pop(-1)
        elif neg:
            result += 2 * abs(neg[-1])
            for i in range(len(neg)):
                neg.pop(-1)
    print(result)