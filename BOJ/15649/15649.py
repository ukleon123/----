import sys
def permutation(std, lub, depth, prev):
    if depth:
        for i in range(lub):
            if i + 1 not in prev:
                if depth == std:
                    prev = []
                prev.append(i + 1)
                permutation(std, lub, depth - 1, prev)
                prev.pop()
                pass
            pass
        pass
    else : 
        for i in prev:
            print(i, end=" ")
        print()
    pass
if __name__ == "__main__":
    lub, num = list(map(int, sys.stdin.readline().split()))
    permutation(num, lub, num, [])