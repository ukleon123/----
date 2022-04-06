import sys
import decimal
import math

if __name__ == "__main__":
    X, Y = map(int, sys.stdin.readline().split())
    current = int(decimal.Decimal(Y) / decimal.Decimal(X) * decimal.Decimal(100))
    up = decimal.Decimal((current + 1) * X - (100 * Y))
    down = decimal.Decimal(99 - current)
    if down <= 0:
        print(-1)
    else:
        print(math.ceil(up / down))
    
