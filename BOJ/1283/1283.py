import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    options = []
    shortKey = []
    for i in range(N):
        tmp = sys.stdin.readline()[:-1]
        while tmp[0] == ' ':
            tmp = tmp[1:]
        idx = 0
        check = 1
        options.append(tmp)
        splitten = tmp.split(' ')
        
        for j in splitten:
            if j[0].lower() not in shortKey and j[0].upper() not in shortKey:
                shortKey.append(j[0]); check = 0
                break
            idx += len(j) + 1
        if check:
            idx = 0
            for j in splitten:
                for k in j:
                    if k.lower() not in shortKey and k.upper() not in shortKey:
                        shortKey.append(k); check = 0
                        break
                    idx += 1
                if not check:
                    break
                idx += 1
            if check:
                idx = None
        for i in range(len(tmp)):
            if idx == i:
                print(f'[{tmp[i]}]', end='')
            else:
                print(tmp[i], end='')
        print()
            
    #모든 조건을 하나 하나 꼼꼼하게 구현해야 함