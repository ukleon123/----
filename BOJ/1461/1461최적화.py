import sys

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    points = list(map(int, sys.stdin.readline().split()))
    
    pos = []
    neg = []
    for i in points: pos.append(i) if i > 0 else neg.append(i)

    
    pos.sort(key = lambda x : -x)
    neg.sort()

    result = 0
    try: tmp = pos if pos[0] > -neg[0] else neg
    except: tmp = pos if pos else neg
    
    result += tmp[0]; tmp = tmp[M:] if len(tmp) >= M else tmp
    
    pos = pos[::M]
    neg = neg[::M]
    for i in pos:
        result += i * 2
    for i in neg:
        result += i * -2
    print(result)
