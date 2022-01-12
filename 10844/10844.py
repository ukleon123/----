import sys
def findNumber(number, step, cache):
    ret = 0
    if cache[step][number] != -1 :
        return cache[step][number]
    if step > 1:
        if 0 < number < 9:
            ret += findNumber(number - 1, step - 1, cache)
            ret += findNumber(number + 1, step - 1, cache)
        elif number == 0:
            ret += findNumber(number + 1, step - 1, cache)
        elif number == 9:
            ret += findNumber(number - 1, step - 1, cache)
    elif step == 1:
        ret = 1
    cache[step][number] = ret
    return ret
    
if __name__ == "__main__":
    number = int(sys.stdin.readline())
    cache = [[-1 for i in range(10)] for i in range(number + 1)]
    
    result = 0 
    for i in range(1, 10):
        result += findNumber(i, number, cache)
    print(result % 1000000000)