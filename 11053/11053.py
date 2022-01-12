import sys

if __name__ == "__main__":
    number = int(sys.stdin.readline())
    sequence = list(map(int, sys.stdin.readline().split()))
    cache = [1 for i in sequence]
    for i in range(number):
        long = 0
        for j in range(i):
            if sequence[i] > sequence[j]:
                if cache[j] > long:
                    long = cache[j]
        cache[i] += long
    print(max(cache))
    pass    