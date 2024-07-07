import sys
def kmpTable (S : str) -> list:
    j = 0
    result = [0]
    for i in range(1, len(S) - 1):
        while(j > 0 and S[j] != S[i]):
            j = result[j - 1]
        if S[j] == S[i]:
            j += 1
            result.append(j)
        else:
            result.append(0)
        
    return result

def KMP(target : str, keyword : str, pi : list) -> int:
    
    pass
if __name__ == "__main__":
    T = sys.stdin.readline()[:-1]
    K = sys.stdin.readline()[:-1]
    Pi = kmpTable(K)
    print(KMP(T, K, Pi))
    pass