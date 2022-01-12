import sys

def w(a, b, c, cache):
    if a <= 0 or b <= 0 or c <= 0:
        if a <= 0: a = 0
        elif a > 20: a = 20
        if b <= 0: b = 0
        elif b > 20: b = 20
        if c <= 0: c = 0
        elif c > 20: c = 20

        if cache[a][b][c] == -1:
            cache[a][b][c] = 1

    elif a > 20 or b > 20 or c > 20:
        a = 20
        b = 20
        c = 20

        if cache[a][b][c] == -1:
            cache[a][b][c] = w(a, b, c, cache)

    elif a < b and b < c:
        if cache[a][b][c - 1] == -1 :
            cache[a][b][c - 1] = w(a, b, c - 1, cache)
        if cache[a][b - 1][c] == -1 :
            cache[a][b - 1][c] = w(a, b - 1, c, cache)
        if cache[a][b - 1][c - 1] == -1 :
            cache[a][b - 1][c - 1] = w(a, b - 1, c - 1, cache)

        cache[a][b][c] = cache[a][b][c-1] + cache[a][b-1][c-1] - cache[a][b-1][c]

    else:
        if cache[a - 1][b][c] == -1 :
            cache[a - 1][b][c] = w(a - 1, b, c, cache)
        if cache[a - 1][b - 1][c] == -1 :
            cache[a - 1][b - 1][c] = w(a - 1, b - 1, c, cache)
        if cache[a - 1][b][c - 1] == -1 :
            cache[a - 1][b][c - 1] = w(a - 1, b, c - 1, cache)
        if cache[a - 1][b - 1][c - 1] == -1 :
            cache[a - 1][b - 1][c - 1] = w(a - 1, b - 1, c - 1, cache)
            
        cache[a][b][c] = cache[a-1][b][c] + cache[a-1][b-1][c] + cache[a-1][b][c-1] - cache[a-1][b-1][c-1]
    return cache[a][b][c]
    

if __name__ == "__main__":

    cache = [[[-1 for i in range(21)]for j in range(21)]for k in range(21)]

    while True:      
        data = list(map(int, sys.stdin.readline().split()))
        result = 0
        string = "w(" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ') ' 
        if data[0] == -1 and data[1] == -1 and data[2] == -1:
            break        
        result = w(data[0], data[1], data[2], cache)   
        print(string + "=", result)
    pass