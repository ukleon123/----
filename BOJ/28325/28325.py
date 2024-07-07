import sys
from collections import deque


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    C = deque(map(int, sys.stdin.readline().split()))
    for i in range(N):
        if C[0] == 0:
            C.rotate(-1)
        else:
            break

    result = C.popleft()
    if result != 0:
        count = 0
        while C:
            current = C.pop()
            match current:
                case 0:
                    count += 1
                case _:
                    result += (count + 1) // 2 + current
                    count = 0
        result += (count + 1) // 2
    else:
        result = N // 2
    print(result)
