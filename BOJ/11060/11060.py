import sys
import math


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))

    dp = [math.inf for i in range(N)]
    dp[0] = 0

    for i in range(N):
        for j in range(1, data[i] + 1):
            try:
                dp[i + j] = min(dp[i + j], dp[i] + 1)
            except:
                pass

    print(dp[N - 1]) if dp[N - 1] != math.inf else print(-1)