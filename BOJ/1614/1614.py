import sys


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    result = 0
    if n in [2, 3, 4]:
        if N % 2:
            result += 4 + 5 - n
        else:
            result += n - 1
        result += (N // 2) * 8
    else:
        if n == 1:
            result += N * 8
        else:
            result += N * 8 + 4
    print(result)