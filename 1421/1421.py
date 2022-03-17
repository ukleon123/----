import sys

if __name__ == "__main__":
    N, C, W = map(int, sys.stdin.readline().split())
    data = []
    for i in range(N):
        data.append(int(sys.stdin.readline()))
    
    result = 0

    for i in range(1, max(data) + 1):
        tmpRes = 0
        for j in data:
            unit = 0
            cutCnt = 0

            unit  += j // i
            cutCnt += j // i if j % i else j // i - 1
            if i * unit * W - cutCnt * C > 0:
                tmpRes  +=  i * unit * W - cutCnt * C

        if tmpRes > result:
            result = tmpRes
    print(result)

# 조건들에 숨겨진 특징을 꼼꼼하게 구현해야 함
