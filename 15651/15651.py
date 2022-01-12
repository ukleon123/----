import sys
def prnt(num, lim , array):
    if num :
        for i in range(1, lim + 1):
            if len(array) and i < array[-1]:
                pass
            else:
                prnt(num - 1, lim, array + [i])
    else :
        for i in array:
            print(i, end = ' ')
        print()
    return
if __name__ == "__main__":
    N, M = list(map(int, sys.stdin.readline().split()))
    prnt(M, N, [])
    pass