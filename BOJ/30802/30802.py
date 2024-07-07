import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    participants = list(map(int, sys.stdin.readline().split()))
    T, P = tuple(map(int, sys.stdin.readline().split()))

    shirts = 0
    for num in participants:
        if num % T > 0:
            shirts += (num // T) + 1
        else:
            shirts += (num // T)
    
    print(shirts)
    print(N // P, N % P)