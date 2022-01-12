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
    print()

    pass 