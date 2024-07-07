import sys
from collections import defaultdict


if __name__ == "__main__":

    N, K = map(int, sys.stdin.readline().split())
    result = 0
    current = 0
    counts = defaultdict(int, {0 : 1})
    for v in map(int, sys.stdin.readline().split()):
        current += v
        result += counts[current - K]
        counts[current] += 1
    print(result)
    