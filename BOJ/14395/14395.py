import sys
from collections import deque

def operation(value, op):
    result = 0
    match(op):
        case 0:
            result = value ** 2
        case 1:
            result = value + value
        case 2:
            result = 0
        case 3:
            result = 1
    return result if result < 10e9 else False

def print_state(state, op):
    
    for o in state:
        print(dictionary[o], end = '')
    print(dictionary[op])

if __name__ == "__main__":
    s,t = map(int, sys.stdin.readline().split())
    
    result = 0
    if s != t:
        result = -1
        queue = deque()
        visited = set()
        queue.append((s, []))
        dictionary = ['*', '+', '-', '/']

        while queue :
            value, state = queue.popleft() 
            visited.add(value)
            for op in range(4):
                next_value = operation(value, op)
                if next_value and next_value not in visited:
                    if next_value != t:
                        queue.append((next_value, state + [op]))
                    else:
                        print_state(state, op)
                        exit()
    print(result)