from sys import stdin


if __name__ == "__main__":
    N = int(stdin.readline())
    DP = [0, 1, 1, 2, 2, 1, 2, 1]

    for i in range(8, N + 1):
        DP.append(min([DP[i - 1], DP[i - 2], DP[i - 5], DP[i - 7]]) + 1)
    print(DP[N])