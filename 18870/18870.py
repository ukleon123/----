import sys

if __name__=="__main__":
    number = int(sys.stdin.readline())
    points = list(map(int, sys.stdin.readline().split()))
    tmp  = sorted(list(set(points)))
    size = len(tmp)
    
    compressed= dict()
    for i in range(size):
        compressed[tmp[i]] = i

    del tmp, size
    for point in points:
        print(compressed[point], end=' ')
    pass