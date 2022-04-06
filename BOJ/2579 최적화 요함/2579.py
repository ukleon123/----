import sys
def step(cache, stair, index, Step, conti):
    ret = 0
    size = len(stair)
    
    if cache[Step][index][conti] != -1:
        return cache[Step][index][conti]
    
    if index == size - 1 :
        ret = stair[-1]

    elif index < size and Step:
        ret += stair[index]
        if conti == 2:
            ret += step(cache, stair, index + 2, Step - 1, 1)
        else:
            first = step(cache, stair, index + 1, Step - 1, conti + 1)
            second = step(cache, stair, index + 2, Step - 1, 1)
            ret += first if first > second else second 
            
    else : 
        ret = float("-inf")

    cache[Step][index][conti] = ret
    return ret

if __name__ == "__main__":

    Step = 0
    number = int(sys.stdin.readline())
    
    stair = []
    flag = 0
    # odd = once even = double time
    for i in range(number):
        stair.append(int(sys.stdin.readline()))
        Step += 1 if flag == 0 or flag == 1 else 0
        flag += 1 if flag == 0 or flag == 1 else -2

    #cache initialization
    size = len(stair)
    cache = [-1 for i in range(3)]
    cache = [cache for i in range(size + 1)]
    cache = [cache for i in range(Step + 1)]

    first = step(cache, stair, 0, Step - 1, 1)
    second = step(cache, stair, 1, Step - 1, 1)
    result = first if first > second else second
    print(result)
    pass