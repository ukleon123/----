import sys

if __name__ == "__main__":
    number = int(sys.stdin.readline())
    cache = [100 for i in range(number + 1)]
    cache[1] = 0
    size = len(cache)
    for i in range(1, size - 1):
        if i * 2 < size and cache[i] + 1 < cache[i*2]:
            cache[i*2] = cache[i] + 1
        if i * 3 < size and cache[i] + 1 < cache[i*3]:
            cache[i*3] = cache[i] + 1
        if  cache[i] + 1 < cache[i + 1]:
            cache[i + 1] = cache[i] + 1
        pass
    print(cache[number])
    pass