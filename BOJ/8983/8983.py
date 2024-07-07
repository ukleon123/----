import sys


if __name__ == "__main__":
    M, N, L = map(int, sys.stdin.readline().split())
    count = 0
    point = sorted(list(map(int, sys.stdin.readline().split())))

    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        if y <= L:
            start, end = 0, M - 1
            while (start <= end):
                if abs(point[(start + end) // 2] - x) <= L - y:
                    count += 1
                    break
                elif point[(start + end) // 2] - x < L - y :
                    start = (start + end) // 2 + 1
                else :
                    end = (start + end) // 2 - 1
    print(count)