import sys


if __name__ == "__main__":
    tmp = 1
    dp = [False, True, False, True]
    N = int(sys.stdin.readline())
    for i in range(4, N):
        dp.append(not(dp[i - 1] and dp[i - 3] and dp[i - 4]))
    print("SK") if dp[N - 1] else print("CY")

