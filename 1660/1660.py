import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    dp = [0]
    tetra = [1]
    adder = 3
    offset = 3

    idx_dp = 0
    idx_tetra = 0
    for i in range(1, N + 1):
        if i == tetra[idx_tetra]:
            idx_dp = 0
            dp.append(dp[idx_dp] + 1)
            tetra.append(tetra[idx_tetra] + adder)
            adder  += offset
            offset += 1
            idx_dp += 1
            idx_tetra += 1
        else:
            dp.append(dp[idx_dp] + 1)
            idx_dp += 1
    print(dp[-1])