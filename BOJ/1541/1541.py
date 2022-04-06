import sys

if __name__ == "__main__":
    string = list(sys.stdin.readline())[ : -1]
    syntax = list()
    tmp = ""
    for i in string:
        if i not in "+-":
            tmp += i
        else:
            syntax.append(tmp)
            syntax.append(i)
            tmp = ""
    syntax.append(tmp)
    tmp = 0
    result = 0
    negative = 0
    for i in syntax:
        if i == '-':
            result += tmp
            tmp = 0
            negative = 1
        elif negative and i != "+":
            tmp -= int(i)
        elif i != "+":
            tmp += int(i) 
    result += tmp
    print(result)
    pass 
"""
-뒤에 얼마나 많은 수가 올 수 있는지 확인하는 간단한 그리디
"""