import sys
def upper_permutation(std, lub, depth, prev):
    if depth:
        for i in range(lub):
            if i + 1 not in prev and (not len(prev) or i + 1 > prev[-1]):
                if std == depth:
                    prev = []
                prev.append(i + 1)
                upper_permutation(std, lub, depth - 1, prev)
                prev.pop()
                pass
            pass
        pass
    else:
        for i in prev:
            print(i, end  = " ")
        print()
        
        pass
    pass
if __name__ == "__main__":
    lub, num = list(map(int, sys.stdin.readline().split()))
    upper_permutation(num, lub, num, [])
    pass 