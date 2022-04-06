import sys


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    dp = [1, 2, 4]
    for i in range(8):
        dp.append(dp[i + 2] + dp[i + 1] + dp[i])

    for i in range(T):
        N = int(sys.stdin.readline())
        print(dp[N - 1])
