import sys
import bisect


if __name__ == "__main__":
    N, C = map(int, sys.stdin.readline().split())
    items = list(map(int, sys.stdin.readline().split()))
    
    mid = N // 2
    front, back = [], []

    for i in range(2 ** mid):
        value = 0
        mask = str(bin(i))[2:]
        for idx, c in enumerate(reversed(mask)):
            if c == '1':
                value += items[idx]
        front.append(value)
    for i in range(2 ** (N - mid)):
        value = 0
        mask = str(bin(i))[2:]
        for idx, c in enumerate(reversed(mask)):
            if c == '1':
                value += items[idx + mid]
        back.append(value)
    
    result = 0
    back.sort()
    for val in front:
        limit = C - val
        bound = bisect.bisect_right(back, limit)
        result += bound
    print(result)