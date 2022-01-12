import sys


if __name__ == "__main__":
    
    N = int(sys.stdin.readline())
    dp = [0 for i in range(N + 1)]
    
    dp[0] = 1
    
    for i in range(N + 1):
        for j in range(i):
            dp[i] += dp[i-(j+1)] * dp[j]

    print(dp[N])