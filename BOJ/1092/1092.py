import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    crane = list(map(int, sys.stdin.readline().split()))

    M = int(sys.stdin.readline())
    box = list(map(int, sys.stdin.readline().split()))
    
    box.sort()
    crane.sort()

    flag = 1
    result = 0
    if crane[-1] < box[-1]:
        result = -1
        flag = 0

    while box and flag:
        i = 0
        tmp = []
        result += 1
        
        while i < N:
            try:
                if crane[-(i + 1)] < box[-1]:
                    tmp.append(box.pop())
                else:
                    box.pop()
                    i += 1
            except:
                break
        tmp.reverse()
        box = box + tmp

    print(result)
