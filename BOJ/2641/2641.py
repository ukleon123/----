from sys import stdin


def generate(seq, overlap):  
    ret = []; tmp = []
    rev = reversed(seq)
    for i in rev:
        tmp.append((i + 2) % 4 if (i + 2) % 4 else 4)
    rev = tmp; tmp = []
    for i in range(N):
        seq.append(seq.pop(0))
        rev.append(rev.pop(0))
        tmp.append(seq[:])
        tmp.append(rev[:])
    
    cnt = 0
    for i in overlap:
        if i in tmp:
            ret.append(i); cnt += 1
    return cnt, ret

if __name__ == "__main__":
    N = int(stdin.readline())
    seq = list(map(int, stdin.readline().split()))

    M = int(stdin.readline())
    overlap = []
    for i in range(M):
        overlap.append(list(map(int, stdin.readline().split())))

    case = generate(seq, overlap)
    print(case[0])
    for i in case[1]:
        print(" ".join(map(str, i)))


# 구현문제이지만 굳이 따지자면 탐색쪽에 가까운 문제로 생각함
# 구현 문제를 해결하는 경우네는 꼼꼼하게 문제 조건을 파악해야 함