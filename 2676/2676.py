import sys


if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for i in range(T):
        N, M = map(int, sys.stdin.readline().split())
        print(1 + M * (N - M))
        
