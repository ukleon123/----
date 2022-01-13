import sys

if __name__ == "__main__":
    num = sum(list(map(int, sys.stdin.readline().split())))
    T = int(sys.stdin.readline())

    check = {}
    testCase = []

    for i in range(T):
        case = list(map(int, sys.stdin.readline().split()))
        certified = case[3]
        partNum = case[0:3]

        if certified == 1:
            for i in partNum:
                check[i] = 1
            T -= 1
        else:
            for i in partNum:
                try:
                    if check[i] != 1:
                        check[i] = 2
                except KeyError:
                    check[i] = 2
            testCase.append(partNum)

    while testCase:
        for i in testCase:
            if check[i[0]] == 1 and check[i[1]] == 1:
                check[i[2]] = 0
            elif check[i[1]] == 1 and check[i[2]] == 1:
                check[i[0]] = 0
            elif check[i[0]] == 1 and check[i[2]] == 1:
                check[i[1]] = 0
        del testCase[-1]

    for i in range(num):
        try:
            print(check[i + 1])
        except KeyError:
            print(2)
