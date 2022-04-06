import sys
def select(past, idx):
    ret = past[idx-1] if past[idx - 1] > past[idx] else past[idx]
    return ret

if __name__ == "__main__":
    story = int(sys.stdin.readline())
    
    triangle = []
    for i in range(story):
        triangle.append(list(map(int, sys.stdin.readline().split())))
        past = triangle[0]
        current = []
    for i in range(1, story):
        target = triangle[i]
        size = len(target)
        for j in range(size):
            if j == 0:
                current.append(past[j] + target[j])
            elif 0 < j < size - 1:
                current.append(select(past, j) + target[j])
            else:
                current.append(past[j-1] + target[j])
        past = current[:]
        current = []
    print(max(past))      
    pass