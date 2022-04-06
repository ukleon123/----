import sys
def BtoD(arr):
    res = 0
    for i, j in enumerate(arr):
        if j :
            res += 2**i
    return res
if __name__ == "__main__":
    n, k = list(map(int, sys.stdin.readline().split()))
    first = n
    odd_case = [0 for i in range(25)]
    original = [0 for i in range(25)]
    if n > k and 25 > k:
        idx = 0
        while sum(odd_case) + n > k:
            if n == 1:
                break
            if n % 2:
                odd_case[idx] = 1
                original[idx] = 1
            idx += 1
            n = n >> 1
        if sum(odd_case) + n <= k :
            print(0)
        else:
            if k == 1 :
                print( 2**(idx + 1) - first)
            else:
                tmp = k - 1
                pos = 0
                std = sum(odd_case) - tmp + 1
                for i, j in enumerate(odd_case):
                    if j == 1:
                        std -= 1
                    if std == 0:
                        while odd_case[i + 1] != 0:
                            i = i + 1
                        odd_case[i + 1] = 1
                        print(BtoD(odd_case) - BtoD(odd_case[:i + 1]) - BtoD(original))
                        
    elif k >= 25:
        print(0)
    elif k >= n:
        print(0)
    pass
"""
010010010
"""