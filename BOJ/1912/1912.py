import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    
    dp = data
    for i in range(1, N):
        if dp[i] < dp[i] + dp[i - 1]:
            dp[i] += dp[i - 1]
    print(max(dp)) 