import sys

def combination(N, R, li = [], p = 0):
    result = 0
    if R:
        for i in range(p, N):
            if N - p >= R :
                tmp = combination(N, R - 1, li + [data[i]], i + 1)
                result += tmp
    else:
        return 1 if S == sum(li) else 0
    return result


if __name__ == "__main__":
    N, S = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))
    
    result = 0
    for j in range(1, N + 1):
        result += combination(N, j)

    print(result)
