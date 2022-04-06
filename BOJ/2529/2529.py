import sys


def check(curr, next, idx):
    if case[idx] == '<':
        return 1 if curr < next else 0 
    else:
        return 1 if curr > next else 0 
def search(depth, seq):
    if depth:
        for i in range(10):
            if i not in seq and check(seq[-1], i, N - depth):
                search(depth - 1, seq + [i])
    else:
        result.append(seq)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    case = sys.stdin.readline().split()
    result = []
    for i in range(10):
        search(N , [i])
        try:
            if result[0] is not result[-1]: 
                result = [result[0], result[-1]]
            else:
                result = [result[0]]
        except:
            result = []
    result.sort(key=lambda x : -x[0])
    for i in result:
        print("".join(map(str, i)))