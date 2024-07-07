from sys import stdin


if __name__ == "__main__":
    T = int(stdin.readline())
    
    result = 0
    DP = [1, 1]
    
    for Idx in range(T):
        P, Q = map(int, stdin.readline().split())
        try:
            result = DP[P - 1] % Q
        except:
            for i in range(len(DP), P):
                DP.append((DP[i - 1] + DP[i - 2]))
            result = DP[P - 1] % Q
        print("Case #" + str(Idx + 1) + ":", result)

# easy to python