import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    dp = [1 for i in range(N)]
    for i in range(3,N):
        dp[i] = dp[i - 1] + dp[i - 3]
    print(dp[N - 1])