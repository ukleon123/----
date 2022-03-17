import sys
import math

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    
    test = []
    for i in range(N): 
        test.append(float(sys.stdin.readline()))
    
    flag = 0
    for i in range(1, 1001):
        flag = 0
        for j in test:
            std = int(j * i)
            for k in range(std, std + 3):
                tmp = truncate(k / i , 3)
                if tmp == j:
                    flag += 1
                    break
        if flag == N:
            break
                    
    print(i)

# 소수점을 반올림 없이 정확하게 잘라야 하는 문제