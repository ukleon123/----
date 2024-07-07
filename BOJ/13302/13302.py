import sys


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    data = set(map(lambda x :int(x) - 1, sys.stdin.readline().split()))

    Inf = 1e9
    dp = [[Inf for _ in range(42)] for _ in range(N + 6)]

    dp[0][0] = 0
    for i in range(N + 1):
        for j in range(40):
            if i in data:
                dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])
            if j > 2 :
                dp[i + 1][j - 3] = min(dp[i + 1][j - 3], dp[i][j])
            dp[i + 1][j] = min(dp[i][j] + 10000, dp[i + 1][j])
            for k in range(3):
                dp[i + k + 1][j + 1] = min(dp[i][j] + 25000, dp[i + k + 1][j + 1])
            for k in range(5):
                dp[i + k + 1][j + 2] = min(dp[i][j] + 37000, dp[i + k + 1][j + 2])

    print(min(dp[N]))