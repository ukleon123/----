# import sys
# import copy


# class state:
#     def __init__(self, prev, value):
#         self.prev = copy.copy(prev)
#         self.value = value

# if __name__ == "__main__":
#     N = int(sys.stdin.readline())
    
#     query = []
#     query.append(state(None, -1))
#     for i in range(N):
#         command = sys.stdin.readline()
#         command = command.split()
#         match command[0]:
#             case 'a':
#                 n_state = state(query[-1], int(command[1]))
#                 query.append(n_state)
#                 pass   
#             case 't':
#                 next = query[int(command[1]) - 1]
#                 query.append(state(next, None))
#                 pass
#             case 's':
#                 if query.__len__() == 1:
#                     query.append(state(query[0], None))
#                 else:
#                     current = query[-1]
#                     while current.value == None:
#                         if current.prev.value == -1:
#                             break
#                         current = current.prev
#                     query.append(state(current.prev, None))
#         current = query[-1]
#         while current.value == None:
#             current = current.prev
#         print(current.value)


import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    T = set()
    queries = []
    for i in range(N):
        S = input().split()
        queries.append(S)
        if S[0] == 't':
            T.add(int(S[1]) - 1)

    STORE = [[] for _ in range(N + 1)]
    S = [-1]
    STORE[0] = [-1]

    for i, q in enumerate(queries):
        if q[0] == 'a':
            S.append(int(q[1]))
        elif q[0] == 's':
            S.pop()
        else:
            S = STORE[int(q[1]) - 1][:]
        print(S[-1])
    
        if i + 1 in T:
            STORE[i + 1] = S[:]
