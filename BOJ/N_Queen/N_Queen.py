import sys
def check(array, data):
    ret = 1
    for i in array:
        if i[0] == data[0] or i[1] == data[1]:
            return 0
        elif i[0] + i[1] == data[0] + data[1]:
            return 0
        elif i[1] - i[0] == data[1] - data[0]:
            return 0
    return ret 
    
def search(N, depth, array):
    ret = 0
    if depth > 0 :
        for j in range(N):
            if check(array, (depth - 1, j)):
                ret += search(N, depth - 1, array + [(depth - 1, j)])
        return ret
    else :
        ret = 1
        return ret
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    ret = search(N, N, [])
    print (ret)