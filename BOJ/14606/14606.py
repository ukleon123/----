import sys


if __name__ == "__main__":
    
    result = 0
    N = int(sys.stdin.readline())    
    
    for i in range(N):
        result += i

    print(result)