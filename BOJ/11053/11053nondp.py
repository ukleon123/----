import sys
import bisect


if __name__ == "__main__":
    number = int(sys.stdin.readline())
    sequence = list(map(int, sys.stdin.readline().split()))
    cache = []
    for i in sequence:
        if not len(cache) or cache[-1] < i:
            cache.append(i)
        else:
            cache[bisect.bisect_left(cache, i)] = i
        pass
    print(len(cache))
    pass 