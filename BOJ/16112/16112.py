import sys


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())

    data = list(map(int, sys.stdin.readline().split()))
    data.sort()
    res = 0
    for i in range(N):
        multi =  i if i < K else K
        res += data[i] * multi
    print(res)