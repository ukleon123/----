import sys

if __name__ == "__main__":
    while True:
        N = int(sys.stdin.readline())
        if N:
            dp = [0]
            for i in range(1, N + 1):
                tmp = int(sys.stdin.readline())
                dp.append(tmp)
                if dp[i - 1] + tmp > dp[i]:
                    dp[i] = dp[i - 1] + tmp 
            print(max(dp[1:]))
        else:
            break