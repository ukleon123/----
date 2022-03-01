import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    boxes = list(map(int, sys.stdin.readline().split()))

    dp = [1 for i in range(N)]

    for i in range(N):
        for j in range(i):
            if boxes[i] > boxes[j]:
                dp[i] = max([dp[i], dp[j] + 1])
    print(max(dp))