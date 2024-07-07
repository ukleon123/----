import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())

    low = []
    high = []
    for i in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        if i == 0:
            low = line[:]
            high = line[:]
        else:
            current_low = low[:]
            current_high = high[:]
            

            low[0] = min(current_low[:2]) + line[0]
            low[1] = min(current_low) + line[1]
            low[2] = min(current_low[1:]) + line[2]
            high[0] = max(current_high[:2]) + line[0]
            high[1] = max(current_high) + line[1]
            high[2] = max(current_high[1:])+ line[2]
            
    print(max(high), min(low))