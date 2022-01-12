import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    
    for i in range(T):

        V, E = list(map(int, sys.stdin.readline().split()))
        graph = [[]for i in range(V)]

        for j in range(E):
            start, end = list(map(int, sys.stdin.readline().split()))

            graph[start - 1].append(end)
            graph[end - 1].append(start)

        flag = 0
        stack = []
        value = []
        visited = [0 for i in range(V)]
        visited_val = [None for i in range(V)]
        
        stack.append(1)
        value.append(False)

        while stack:
            current = stack.pop()
            current_val = value.pop()
            
            visited[current - 1] = 2
            visited_val[current - 1] = current_val

            for i in graph[current - 1]:

                if visited[i - 1] == 2:
                    if visited_val[i - 1] == current_val:
                        print("NO")
                        flag = 1
                        break

                if not visited[i - 1]:
                    stack.append(i)
                    value.append(not current_val)

                    visited[i - 1] = 1

            if flag == 1:
                break
            
        if flag != 1:
            print("YES")  
