import sys


if __name__ == "__main__":
    
    N = int(sys.stdin.readline())
    dp = [1 for i in range(N + 1)]
    
    dp[0] = 0
    
    for i in range(2, N + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    
    print(dp[N])