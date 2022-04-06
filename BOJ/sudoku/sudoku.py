import sys
data = []
square = [[] for i in range(9)]
vertical = [[] for i in range(9)]
horizontal = [[] for i in range(9)]

def check(num, array):
    global data
    global square
    global vertical
    global horizontal
    s = data[len(array)][2]
    v = data[len(array)][1]
    h = data[len(array)][0]

    S = square[s][:]
    V = vertical[v][:]
    H = horizontal[h][:]
    if num in S or num in H or num in V:
        return 0

    for i in range(len(array)):
        if s == data[i][2]:
            if array[i] == num:
                return
        if v == data[i][1]:
            if array[i] == num:
                return 0
        elif h == data[i][0]:
            if array[i] == num:
                return 0
    return 1

def search(depth, limit, array):
    ret = []
    if depth:
        for i in data[len(array)][3]:
            if check(i, array):
                ret = search(depth - 1, limit, array + [i])
                if len(ret) == limit:
                    return ret
        return ret
    else :
        return array
    
if __name__ == "__main__":
    num = 0
    
    pr = [[] for i in range(9)]
    
    for i in range(9):
        N = list(map(int, sys.stdin.readline().split()))
        for j in range(len(N)):
            w_x = i//3
            w_y = j//3
            k = w_y * 3 + w_x
            pr[i].append(N[j])
            if N[j]:
                square[k].append(N[j])
                vertical[j].append(N[j])
                horizontal[i].append(N[j])
            elif N[j] == 0:
                num += 1 
                std = set([i for i in range(1, 10)])
                loop = std - set(square[k])
                loop = loop &(std - set(vertical[j]))
                loop = loop &(std - set(horizontal[i]))
                loop = list(loop)
                data.append((i, j, k, loop))
    result = search(num, num, [])
    for i in pr:
        for j in i:
            if j == 0:
                print(result[0], end = ' ')
                del result[0]
            else:
                print(j, end = ' ')
        print()
    pass