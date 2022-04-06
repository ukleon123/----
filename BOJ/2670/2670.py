import sys

if __name__ == "__main__":
    dp = []
    N = int(sys.stdin.readline())
    for i in range(N):
        dp.append(float(sys.stdin.readline()))
    for i in range(1, N):
        if dp[i - 1] * dp[i] > dp[i]:
            dp[i] = dp[i - 1] * dp[i]
    print("{:.3f}".format(round(max(dp), 3)))