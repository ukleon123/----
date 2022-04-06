import sys
def hanoi(F, M, T, N):
    if N == 1:
        print(F, T)
        return
    hanoi(F, T, M, N - 1)
    print(F, T)
    hanoi(M, F, T, N - 1)
    pass
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    print(2 ** N - 1)
    if N <= 20:
        hanoi(1, 2, 3, N)
    pass