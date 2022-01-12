import sys


if __name__ == "__main__":
    
    N = int(sys.stdin.readline())
    dp = [i for i in range(N + 1)]
    
    for i in range(2, N + 1):
        dp[i] = dp[i-1] + dp[i-2]
        
    print(dp[N])