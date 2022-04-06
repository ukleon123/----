import sys

if __name__ == "__main__":
    number = int(sys.stdin.readline())
    drink = [0]

    for i in range(number):
        drink.append(int(sys.stdin.readline()))
    cache = [0 for i in range(number + 1)]
    cache [1] = drink[1]
    if number > 1: 
        cache [2] = cache[1] + drink[2]

    for i in range(3, number + 1):
        first = cache[i - 2] + drink[i]
        second = cache[i - 3] + drink[i - 1] + drink[i]
        
        cache[i] = first if second < first else second
        cache[i] = cache[i] if cache[i - 1] < cache[i] else cache[i - 1]
    print(cache[-1])
