from sys import stdin


if __name__ == "__main__":
    
    N, M = map(int, stdin.readline().split())

    DP = [[0 for _ in range(M)] for _ in range(N)]
    DP[0][0] = 1
    for i in range(N):
        for j in range(M):
            if i:
                DP[i][j] += DP[i - 1][j]
            if j:
                DP[i][j] += DP[i][j - 1]
            if i and j:
                DP[i][j] += DP[i - 1][j - 1]
            DP[i][j] = DP[i][j] % (10 ** 9 + 7)
    print(DP[N - 1][M - 1])