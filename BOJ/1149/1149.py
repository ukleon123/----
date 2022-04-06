import sys
def select(color, past, current):
    list = [0,1,2]
    del list[color]
    first, second = list

    current[color] = past[first] if past[first] < past[second] else past[second]

if __name__ == "__main__":
    cost = list()
    number = int(sys.stdin.readline())
    
    #0 = red 1 = green 2 = blue
    for i in range(number):
        cost.append(list(map(int, sys.stdin.readline().split()))) #O(N)
    
    past = cost[0]
    current = [0, 0, 0] 
    #각 인덱스에 해당하는 이전 최소값에 다음 최소값을 더하면 된다.
    for i in range(1, number):
        select(0, past, current)
        current[0] += cost[i][0]
        select(1, past, current)
        current[1] += cost[i][1]
        select(2, past, current)
        current[2] += cost[i][2]

        #for shallow copy
        past = current[:]
        pass 
    print(min(current))
    pass