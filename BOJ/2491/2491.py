import sys


if __name__:
    N = int(sys.stdin.readline())

    data = list(map(int, sys.stdin.readline().split()))

    lis1 = [1 for i in range(N)]
    lis2 = [1 for i in range(N)]
    for i in range(1, N):
        if data[i] >= data[i - 1]:
            lis1[i] = lis1[i - 1] + 1
        if data[i] <= data[i - 1]:
            lis2[i] = lis2[i - 1] + 1
    print(max(lis1 + lis2))
         
