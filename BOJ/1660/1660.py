import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    
    
    th = []
    dp = [0]

    for i in range(1, N + 1):
        tmp = i * (i + 1) * (i + 2) // 6
        if tmp <= N:
            th.append(tmp)
        dp.append(i)

    for i in range(N + 1):
        for j in th:
            if j < i:
                dp[i] = dp[i] if dp[i] < dp[i - j] + 1 else dp[i - j] + 1
            elif j == i:
                dp[i] = 1
                break
            else:
                break
    print(dp[N])