import sys
def val(p):
    return rect[p[1]][p[0]]

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    
    result = 1
    rect = []
    for i in range(N):
        tmp = list(sys.stdin.readline()[:M])
        rect.append(tmp)
    
    lim = N if N < M else M
    
    for i in range(1, lim):
        p1 = [0, 0]; p2= [0, i]; p3 = [i, 0]; p4 = [i, i]
        for j in range(M - i):
            for k in range(N - i):
                if val(p1) == val(p2) and val(p2) == val(p3) and val(p3) == val(p4):
                    result = (i + 1) ** 2
                p1[1] += 1; p2[1] += 1; p3[1] += 1; p4[1] += 1
            p1[0] += 1; p2[0] += 1; p3[0] += 1; p4[0] += 1
            p1[1] = 0; p2[1] = i; p3[1] = 0; p4[1] = i
    
    print(result)