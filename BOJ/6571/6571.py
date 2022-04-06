import sys

if __name__ == "__main__":
    dp = [1]
    N = int(sys.stdin.readline())

    for i in range(1, N):
        if (i + 1) % 2:
            dp.append((sum(dp[:i]) + 1) % 10007)
        else:
            dp.append((sum(dp[:i]) + 2) % 10007)
    print(dp[N - 1])