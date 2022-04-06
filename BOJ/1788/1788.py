import sys

if __name__ == "__main__":


    N = int(sys.stdin.readline())
    amt = abs(N)
    dp = [0 for i in range(amt + 1)]
    
    dp[0] = 0

    if N > 0:
        dp[1] = 1
        for i in range(2, N + 1):
            dp[i] = (dp[i - 2] + dp[i - 1]) % int(1e9)
    elif N < 0:
        dp[1] = 1
        for i in range(2, amt + 1):
            if dp[i - 2] - dp[i - 1] < 0:
                dp[i] = ((dp[i - 2] - dp[i - 1]) % int(1e9)) - int(1e9)
            else :
                dp[i] = ((dp[i - 2] - dp[i - 1]) % int(1e9))
    if dp[amt] < 0:
        print(-1)
    elif dp[amt] > 0: 
        print(1)
    else:
        print(0)
    print(abs(dp[amt]))
