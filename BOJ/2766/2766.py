import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        N = int(sys.stdin.readline())
        note1 = list(map(int, sys.stdin.readline().split()))
        
        N = int(sys.stdin.readline())
        note2 = list(map(int, sys.stdin.readline().split()))
        
        data = {}
        for i in note1:
            data[i] = i
        for i in note2:
            try:
                data[i]
                print(1)
            except KeyError:
                print(0)