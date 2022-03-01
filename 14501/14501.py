import sys


if __name__ == "__main__":
    
    
    time = []
    price = []
    N = int(sys.stdin.readline())
    dp = [0 for i in range(N + 1)]

    for i in range(N):
        t, p = map(int, sys.stdin.readline().split())
        time.append(t)
        price.append(p)
    for i in range(N + 1):
        dp[i]
    print(max(dp))
    
    
