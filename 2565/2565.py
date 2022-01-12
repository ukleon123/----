import sys

if __name__ == "__main__":
    data = []
    cache = [0]
    N = int(sys.stdin.readline())
    for i in range(N):
        tmp = 0
        l, r = list(map(int, sys.stdin.readline().split()))
        for i in data:
            if not (((i[0] < l and i[1] < l) and (i[0] < r and i[1] < r)) or ((i[0] < l and i[1] < l) and (i[0] < r and i[1] < r))):
                tmp += 1
        if tmp >= cache[i]:
            cache.append(cache[i] + 1)
        data.append((l,r))