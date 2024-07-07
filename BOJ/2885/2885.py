import sys
import math

if __name__ == "__main__":
    K = int(sys.stdin.readline())

    exponential = math.ceil(math.log2(K))

    base = 1 << exponential

    binary = bin(K)
    result = 0
    for idx, value in enumerate(list(reversed(binary))[: -2]):
        if value == '1':
            result = exponential - idx
            break
    print(base, result)

    
    pass