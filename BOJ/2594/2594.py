import sys

def trans(time1, time2):
    ret = 0
    if time1 - time2 > 0:
        ret += (time1 // 100 - time2 // 100) * 60
        tmp = time1 % 100 - time2 % 100
        if tmp < 0:
            tmp = 60 + tmp
            ret -= 60
        ret += tmp
    else:
        ret = 0
    return ret

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    data  = [[1000, 1000]]
    for i in range(N):
        data.append(list(map(int, sys.stdin.readline().split())))
    data.sort(key = lambda x : x[1])
    data.append([2200, 2200])
    result = 0
    for i in range(N + 1):
        tmp = trans(data[i + 1][0], data[i][1])
        tmp = tmp - 10 if i == 0 or i == N else tmp - 20
        tmp += 10 if N == 0 else 0
        if result < tmp:
            result = int(tmp)
    print(result) 

# 정렬 방향을 생각해야 하는 문제