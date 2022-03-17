import sys


def check(xc, yc, r, x, y):
    if (x - xc) ** 2 + (y - yc) ** 2 < r ** 2:
        return 1
    else :
        return 0

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    
    for i in range(T):
        result = 0
        xs, ys, xd, yd = map(int, sys.stdin.readline().split())
        
        N = int(sys.stdin.readline())
        for i in range(N):
            xc, yc, r = map(int, sys.stdin.readline().split())
            start = check(xc, yc, r, xs, ys)
            dest = check(xc, yc, r, xd, yd)
            if start != dest:
                result += 1
        
        print(result)