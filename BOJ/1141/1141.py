import sys
def suffix(obj, target):
    try:
        if obj == target[:len(obj)]:
            return 1
        else:
            return 0
    except:
        return 0

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    data = []
    for i in range(N):
        data.append(sys.stdin.readline()[:-1])
    data = list(set(data))

    N = len(data)
    result = N
    for i in range(N):
        for j in range(N):
            if i != j and suffix(data[i], data[j]):
                result += -1
                break

    print(result)