import sys

if __name__ == "__main__":

    idx = []
    T = int(sys.stdin.readline())

    for i in range(T):
        idx.append(int(sys.stdin.readline()))
    
    N = max(idx)
    dp = [[1 for i in range(10)]for j in range(N)]

    for i in range(1, N):
        for j in range(10):
            dp[i][j] = sum(dp[i - 1][j:10])

    for i in idx: 
        print(sum(dp[i-1]))
