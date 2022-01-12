import sys

if __name__ == "__main__":
    number = int(sys.stdin.readline())
    array_A = list(map(int, sys.stdin.readline().split()))
    array_B = list(map(int, sys.stdin.readline().split()))
    array_A.sort(), array_B.sort(reverse=True)
    
    result = 0
    for i in range(number):
        result += array_A[i] * array_B[i]
    print(result)