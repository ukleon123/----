import sys

def eea(a, b):
    r0, r1 = a, b
    t0, t1 = 0, 1

    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - r1 * q
        t0, t1 = t1, t0 - t1 * q
    return r0, t0

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        A, B = map(int, sys.stdin.readline().split())
        gcd, result = eea(A, B)
        if gcd == 1:
            if B == 1:
                result = A + B
            else:
                if A == 1:
                    result = A
                else:
                    result = A + result if result < 0 else result
        else:
            result = 0
        
        if result == 0 or result > 1e9:
            print("IMPOSSIBLE")
        else:
            print(result)

                