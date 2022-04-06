from operator import length_hint
import sys

def check(bulbs):
    ret = 0
    length = len(bulbs)
    for i in range(1, length):
        if bulbs[i - 1] != bulbs[i]:
            ret += 1
    return ret


if __name__ == "__main__":
    bulb = [0 for i in range(4)]
    result = 0
    N = int(sys.stdin.readline())
    
    for _ in range(N):
        current = list(map(int, list(sys.stdin.readline()[:-1])))
        result += check(current)
        if current[0] == 0:
            if current[-1] == 0:
                bulb[0] += 1
            else:
                bulb[1] += 1
        else:
            if current[-1] == 0:
                bulb[2] += 1
            else:
                bulb[3] += 1
    if abs(bulb[1] - bulb[2]) > 1:
        result += abs(bulb[1] - bulb[2]) - 1
    elif bulb[1] == 0 and bulb[2] == 0:
        if bulb[0] and bulb[3]:
            result += 1
    print(result)
        

    