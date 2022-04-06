import sys
from itertools import combinations

#모든 경우를 구한 뒤, 그 값이 결과에 존재하는지 확인하면 되는 문제로 생각할 수 있을 것
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))

    good = 0
    comb = combinations(range(N), 2)

    li_std = {}
    for i in comb:
        try:
            if li_std[li[i[0]] + li[i[1]]]:
                li_std[li[i[0]] + li[i[1]]].append((i[0], i[1]))
        except:
            li_std[li[i[0]] + li[i[1]]] = [(i[0], i[1])]
    for i in range(N):
        try:
            for j in li_std[li[i]]:
                if i not in j:
                    good += 1
                    break
        except:
            pass
    print(good)
            
# 자기 자신을 더해서 구하는 경우는 제외해야 함 + 인덱스가 다르면 다른 수이다.
    