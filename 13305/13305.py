import sys

if __name__ == "__main__":
    num  = int(sys.stdin.readline())
    route = list(map(int, sys.stdin.readline().split()))
    cost = list(map(int, sys.stdin.readline().split()))
    min = cost[0]
    res = 0 
    for i in range(num - 1):
        idx = 0
        if min > cost[i]:
            min = cost[i]
        res += min * route[i]
        idx  += 1
    print(res)
    pass