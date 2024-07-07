from sys import stdin


if __name__ == "__main__":
    N = int(stdin.readline())
    DP = [1, 1]

    for i in range(2, N + 1):
        DP.append((DP[i - 1] + DP[i - 2] + 1) % (10 ** 9 + 7))
    print(DP[N])
#DP[N] = DP[N - 1] + DP[N - 2]