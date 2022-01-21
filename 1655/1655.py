import sys
import heapq

if __name__ == "__main__":
    front= []
    rear = []
    N = int(sys.stdin.readline())
    
    for i in range(N):
        M = int(sys.stdin.readline())
        
        heapq.heappush(front, -1 * M)
        try:
            if front[0] * -1 > rear[0]:
                tmp = heapq.heappop(front)
                heapq.heappush(rear, tmp * -1)
        except:
            pass

        if abs(len(front) - len(rear)) > 1:
            if len(front) > len(rear):
                tmp = heapq.heappop(front)
                heapq.heappush(rear, tmp * -1)
            else:
                tmp = heapq.heappop(rear)
                heapq.heappush(front, tmp * -1)

        if len(front) >= len(rear):
            print(front[0] * -1)
        else:
            print(rear[0])
