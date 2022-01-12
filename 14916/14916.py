import sys

if __name__ == "__main__":
    
    result = 0
    N = int(sys.stdin.readline())
    
    while N >= 2:
        if  N % 5:
            N -= 2
            result += 1

        else :
            result += N//5
            N = 0
            break

    if N :
        print(-1)
    else:
        print(result)
