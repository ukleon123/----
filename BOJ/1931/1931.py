import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    meetings = []
    for _ in range(N):
        S, T = tuple(map(int, sys.stdin.readline().split()))
        meetings.append((S,T))
    
    meetings.sort(key = lambda x: (x[1], x[0]))

    result = 0
    last = 0
    for meeting in meetings:
        if meeting[0] >= last:
            result += 1
            last = meeting[1]
    print(result)