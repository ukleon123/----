from sys import stdin
from collections import OrderedDict
    

if __name__ == "__main__":
    N = int(stdin.readline())
    M = int(stdin.readline())
    data = list(map(int, stdin.readline().split()))
    
    candidate = OrderedDict()
    for i in range(M):
        try:
            candidate[data[i]] += 1
        except:
            if len(candidate) < N:
                candidate[data[i]] = 1
            else: 
                index = min(candidate, key=candidate.get)
                del candidate[index]
                candidate[data[i]] = 1
    tmp = list(candidate.keys())
    print(' '.join(map(str, sorted(tmp))))
