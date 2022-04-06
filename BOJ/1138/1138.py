import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))

    check = [i for i in range(N)]
    result = [0 for i in range(N)]
    for i in range(N):
        tmp = 0
        while tmp < li[i]: 
            tmp += 1

        result[check[tmp]] = str(i + 1)
        del check[tmp]

    print(" ".join(result))
        