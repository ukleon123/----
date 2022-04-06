import sys


if __name__ == "__main__":
    dp = [[]for i in range(101)]
    N, M = map(int, sys.stdin.readline().split())

    dp[0].append(1)
    dp[1] = [1, 1]
    for i in range(1, 101):
        for j in range(i + 1):
            if j == 0:
                dp[i].append(1)
            elif j == i:
                dp[i].append(1)
            else:
                dp[i].append(dp[i-1][j - 1] + dp[i - 1][j])
    print(dp[N][M])