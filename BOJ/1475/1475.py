import sys

if __name__ == "__main__":
    li = list(map(int, list(sys.stdin.readline())[:-1]))

    set = [0 for i in range(10)]
    for i in li:
        set[i] += 1
    
    tmp = (set[6] + set[9])
    if tmp % 2:
        del set[6], set[8]
        set.append(tmp // 2  + 1)
    else:
        del set[6], set[8]
        set.append(tmp // 2)
        
    print(max(set))
        