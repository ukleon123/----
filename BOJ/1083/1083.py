import sys

def sort(num, data, swap_num):
    for i in range(num):
        for j in range(1, num):
            if swap_num == 0:
                return data
            if data[j - 1] < data[j]:
                tmp = data[j - 1]
                data[j - 1] = data[j]
                data[j] = tmp
                swap_num = swap_num - 1
    return data

if __name__ == "__main__":
    num = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    swap_num = int(sys.stdin.readline())

    print (" ".join(map(str, sort(num, data, swap_num))))