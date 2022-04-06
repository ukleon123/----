import sys


if __name__ == "__main__":
    N, p1, p2 = map(int, sys.stdin.readline().split())
    result = 0
    while p1 != p2:
        p1 = (p1 + 1) // 2 if p1 % 2 else p1 // 2
        p2 = (p2 + 1) // 2 if p2 % 2 else p2 // 2
        result += 1
    print(result)