import sys
def binary_insert(new,  data):
    
    tmp = data
    idx = 0
    while len(tmp) > 1:
        if tmp[len(tmp) // 2] == new:
            idx += (len(tmp) // 2) + 1
            break
        elif tmp[len(tmp) // 2] > new:
            idx += (len(tmp) // 2) + 1
            tmp = tmp [idx:]
            pass
        elif tmp[len(tmp) // 2] < new:
            idx += (len(tmp) // 2) + 1
            tmp = tmp [:idx + 1]
            pass
    data.insert(idx, new)
    return data 
    
if __name__ == "__main__":
    num = int(sys.stdin.readline())
    data = list()
    for i in range(num):
        flag = 1
        new = int(sys.stdin.readline())
        if i < 2:
            data.append(new)
            data.sort()
        else:
            binary_insert(new, data)
        if (i + 1) % 2:
            print(data[i // 2])
        else:
            print(data[(i + 1) // 2 - 1])
        flag = 1
    pass