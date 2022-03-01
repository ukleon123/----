import sys


if __name__ == "__main__":
    dp = [1, 2]
    N = int(sys.stdin.readline())
    for i in range(2, N):
        dp.append((dp[i - 1] + dp[i - 2]) % 10)
    
    print(dp[N - 1])