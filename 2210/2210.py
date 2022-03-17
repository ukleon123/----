import sys

def search(p, level = 5, seq = ''):
    if level:
        if p[0] - 1 >= 0:
            current  = seq + data[p[0] - 1][p[1]]
            search((p[0] - 1, p[1]), level - 1, current)
        if p[0] + 1 <= 4:
            current  = seq + data[p[0] + 1][p[1]]
            search((p[0] + 1, p[1]), level - 1, current)
        if p[1] - 1 >= 0:
            current  = seq + data[p[0]][p[1] - 1]
            search((p[0], p[1] - 1), level - 1, current)
        if p[1] + 1 <= 4:
            current  = seq + data[p[0]][p[1] + 1]
            search((p[0], p[1] + 1), level - 1, current)
    else:
        sequences.add(seq)
        return
        

if __name__ == "__main__":
    data = []
    sequences = set()
    for i in range(5):
        data.append(list(sys.stdin.readline().split()))
    for i in range(5):
        for j in range(5):
            search((i,j), seq = data[i][j])
    print(len(sequences))
    
