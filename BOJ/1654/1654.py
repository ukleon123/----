import sys

def binarySearch(end, li, target):
    start = 1
    end = max(li)
    current = 0
    while start <= end :
        current = 0
        mid = (start + end) // 2
        for i in li:
            current += (i // mid)

        if current < target:
            end = mid  - 1
        else:
            start = mid + 1
    return end
        

if __name__ == "__main__":
    N, K = list(map(int,sys.stdin.readline().split()))
    length = []
    
    for i in range(N):
        length.append(int(sys.stdin.readline()))

    result = binarySearch(max(length), length, K)
    print(result)
    