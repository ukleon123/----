import sys

if __name__ == "__main__":
    number = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    stack = []
    result = []
    stack.append([0, array[0]])
    del array[0]
    for i in enumerate(array):
        i = list(i)
        i[0] += 1
        while stack and i[1] > stack[-1][1] :
            stack[-1][1] = i[1]
            result.append(stack[-1])
            del stack[-1]
        stack.append(i)
    for i in stack:
        i[1] = -1
        result.append(i)
    result.sort(key= lambda x : x[0])
    for i in result:
        print(i[1], end = ' ')