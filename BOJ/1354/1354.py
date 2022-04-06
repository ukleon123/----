import sys
li = {0:1} 
def search(N, P, Q, X, Y):
    result = 0
    try:
        N = 0 if N < 0 else N
        result += li[N]
    except:
        result += search(N // P - X, P, Q, X, Y)
        result += search(N // Q - Y, P, Q, X, Y)
        li[N] = result
    return result

if __name__ == "__main__":
    N, P, Q, X, Y = map(int, sys.stdin.readline().split())
    print(search(N, P, Q, X, Y))
