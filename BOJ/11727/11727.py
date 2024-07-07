import sys

if __name__ == "__main__":
    n : int = int(sys.stdin.readline())
    prev : int = 1
    next : int = 1
    for i in range(n - 1):
        if i % 2 :
            next = (prev * 2 - 1) % 10007
        else:
            next = (prev * 2 + 1) % 10007
        prev = next
    print(next)
#숏코딩
# n=int(input())+1
# print((2**n+(1%n))//3%10007)