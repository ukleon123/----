import sys
from queue import PriorityQueue

if __name__ == "__main__":
    lecture = PriorityQueue()
    N = int(sys.stdin.readline())
    
    for i in range(N):
        n, s, e = map(int, sys.stdin.readline().split())
        lecture.put((s, e))
    
    room = PriorityQueue()
    while not lecture.empty():
        i = lecture.get()
        if room.empty():
            room.put(i[1])
        else:
            if room.queue[0] <= i[0]:
                room.get()
                room.put(i[1])
            else:
                room.put(i[1])
    print(room.qsize())
      