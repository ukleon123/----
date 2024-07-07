import sys
from collections import deque

def search(initial, terminal):
    queue = deque()
    checked = [[-1 for _ in range(1001)] for _ in range(1001)]

    queue.append(initial)
    
    checked[initial[0]][initial[1]] = 0
    while queue:
        window, clipboard = queue.popleft()
        time = checked[window][clipboard]
        if window == terminal:
            return time
        
        clipboard_copied = window
        window_erased = window - 1
        window_pasted = window + clipboard
        if window_pasted < 1001 and checked[window_pasted][clipboard] < 0:
            checked[window_pasted][clipboard] = time + 1
            queue.append((window_pasted, clipboard))  

        if window_erased > 0 and checked[window_erased][clipboard] < 0:
            queue.append((window_erased, clipboard))
            checked[window_erased][clipboard] = time + 1
        
        if checked[window][clipboard_copied] < 0:
            queue.append((window, clipboard_copied))
            checked[window][clipboard_copied] = time + 1
if __name__ == "__main__":
    S = int(sys.stdin.readline())
    print(search((1, 0), S))