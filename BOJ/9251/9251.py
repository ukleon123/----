import sys

if __name__ == "__main__":
    A = sys.stdin.readline()
    B = sys.stdin.readline()
    l_A = len(A)
    l_B = len(B)
    dp = [[0 for i in range(l_B)] for i in range(l_A)]
    for i in range(1, l_A):
        for j in range(1, l_B):
            if A[i - 1] == B[j - 1] :
                dp[i][j] = dp[i - 1][j - 1] + 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
    print(dp[l_A - 1][l_B - 1])