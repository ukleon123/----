import sys 

if __name__ == "__main__":
    W, H, f, c, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    result = (x2 - x1) * (y2 - y1) * (c + 1)
    tmp = W - f if W - f < f else f
    if  tmp > x1:
        if  tmp < x2:
            result += (tmp - x1) * (y2 - y1) * (c + 1)
        else:
            result += (x2 - x1) * (y2 - y1) * (c + 1)
    print(W * H - result)