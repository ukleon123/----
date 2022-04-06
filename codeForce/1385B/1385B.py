import sys


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for i in range(T):
        result = []
        N = int(sys.stdin.readline())
        data = list(map(int, sys.stdin.readline().split()))
        for j in range(N * 2):
            if data[j] not in result:
                result.append(data[j])
        print(" ".join(map(str, result)))
