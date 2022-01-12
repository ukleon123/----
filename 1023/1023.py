import sys

def makelist(num):
    unit = "01"
    ret = [unit]
    for i in range(num - 1):
        tmp_l = []
        for j in ret:
            for k in range(3):
                tmp_s = list(unit)
                tmp_s.insert(k, j)
                tmp_l.append("".join(tmp_s))
            tmp_l = set(tmp_l)
            tmp_l = list(tmp_l)
        ret = tmp_l
    return ret

if __name__ == "__main__":
    N, K = list(map(int, sys.stdin.readline().split()))
    res = ""
    if N % 2:
        res = bin(K)
    else:

