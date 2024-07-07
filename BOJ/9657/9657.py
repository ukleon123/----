import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    data = [0, 1, 0, 0]
    mapped = ["SK", "CY"]
    for i in range(4, N):
        if data[i - 1] or data[i - 3] or data[i - 4]:
            data.append(0)
        else:
            data.append(1)
    print(mapped[data[N - 1]])

    

# N = 1 => 1 SK
# N = 2 => 2 CY 1 1 
# N = 3 => 1 SK 3
# N = 4 => 1 SK 4
# N = 5 => 3 SK 3 1 1
# N = 6 => 3 SK 4 1 1 
# N = 7 => 4 CY 1 4 1 1
# N = 8 => 5 SK 1 1 4 1 1 
# 1, 3, 4 이전의 값들에 하나라도 상대가 이기는 값이 있으면 SK승 아니면 CY