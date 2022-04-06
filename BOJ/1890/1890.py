import sys


if __name__ == "__main__":
    location = []
    N = int(sys.stdin.readline())
    dp = [[0 for i in range(N)]for i in range(N)]

    for i in range(N):
        location.append(list(map(int, sys.stdin.readline().split())))
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            
            for k in range(i):
                if location[k][j] == i - k:
                    dp[i][j] += dp[k][j]
            for k in range(j):
                if location[i][k] == j - k:
                    dp[i][j] += dp[i][k]

    print(dp[N - 1][N - 1])