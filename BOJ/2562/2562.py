import sys

if __name__ == "__main__":
    max = 0
    max_idx = 0
    for i in range(9):
        value = int(sys.stdin.readline())
        if value > max :
            max = value
            max_idx = i + 1
    print(max)
    print(max_idx)