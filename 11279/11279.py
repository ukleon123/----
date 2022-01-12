import sys

if __name__ == "__main__" :
    N = int(sys.stdin.readline())
    heap = [float("inf")]
    for i in range(N) :
        val = (int(sys.stdin.readline()))
        if val :
            idx = len(heap)
            heap.append(val)
            while val > heap[idx//2] :
                heap[idx] = heap[idx // 2]
                heap[idx // 2] = val
                idx = idx // 2
            pass
        else:
            try: 
                print(heap[1])
                idx = 1
                child = 2 
                heap[idx] = heap[len(heap) - 1]
                del heap[len(heap) - 1]
                while child <= len(heap) - 1:
                    if child <= (len(heap) - 2) and heap[child] < heap[child + 1]:
                        child += 1
                    if heap[child] > heap[idx]:
                        tmp = heap[idx]
                        heap[idx] = heap[child]
                        heap[child] = tmp
                        idx = child
                        child *= 2
                        
                    else: 
                        break
                    pass
                print(end="")
            except:
                print(0)
    pass