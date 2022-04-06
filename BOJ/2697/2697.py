from sys import stdin

def swap(case):
    tmp = S[case[0]]
    S[case[0]] = S[case[1]]
    S[case[1]] = tmp

if __name__ == "__main__":
    N = int(stdin.readline())
    for i in range(N):
        case = []
        S = list(stdin.readline()[:-1])
        
        for i in range(1, len(S) + 1):
            for j in range(1, i):
                if S[-j] > S[-i]:
                    case.append((-i, -j))
        if not case:
            print("BIGGEST")
        else:
            case.sort(key = lambda x: (-x[0], -x[1]))
            std = case[0][0]
            swap(case[0])
            while case:
                case = []
                for i in range(1, -std):
                    for j in range(1, i):
                        if S[-j] < S[-i]:
                            case.append((-i, -j))
                if case:
                    case.sort(key = lambda x: (-x[0], -x[1]))
                    swap(case[0])
            print("".join(S))

        
# 구현, 정렬을 통한 그리디 문제 간단하지만 에제를 잘못봐서 계속 오답을 제출함