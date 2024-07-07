import sys

if __name__ == "__main__":

    N, M = map(int, sys.stdin.readline().split())
    gems = [int(sys.stdin.readline()) for _ in range(M)]
        
    start = 1
    end = max(gems)

    result = 0

    while start <= end:
        sum = 0
        mid = (start + end) // 2
        for i in range(gems.__len__()):
            sum += gems[i]//mid
            if gems[i] % mid != 0:
                sum += 1
    
        if sum > N:
            start = mid + 1
        else:
            end = mid - 1
            result = mid
    print(result)