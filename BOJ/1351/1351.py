import sys

#딕셔너리를 사용한 메모이제이션
seq = {0:1}
def search(N, P, Q):
    result = 0 

    try:
        result += seq[N]
    except:
        result += search(N//P, P, Q)
        result += search(N//Q, P, Q)
        seq[N] = result
    return result

if __name__ == "__main__":
    N, P, Q = map(int, sys.stdin.readline().split())

    print(search(N, P, Q))
