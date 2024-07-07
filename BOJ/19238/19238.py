import sys

from collections import deque, defaultdict


def get_dist(start, ends):
    move = [1, -1]
    queue = deque()
    visited = set()
    visited.add(start)
    queue.append((start, 0))
    result = defaultdict(lambda : 1e9)
    if start in ends: result[start] = 0
    while queue:
        current, dist = queue.popleft()
        for i in range(4):
            h = i // 2
            npos = [0, 0]
            npos[1 - h] = current[1 - h]
            npos[h] = current[h] + move[i % 2]
            npos = tuple(npos)
            if npos not in visited and  0 <= npos[h] < N and field[npos[0]][npos[1]] != 1:
                if npos in ends and result[npos] > dist + 1:
                    result[npos] = dist + 1
                    if not isinstance(ends, set):
                        return result
                queue.append((npos, dist + 1))
                visited.add(npos)
    return result


if __name__ == "__main__":
    N, M, fuel = map(int, sys.stdin.readline().split())
    field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    xt, yt = map(lambda x : int(x) - 1, sys.stdin.readline().split())
    
    guests = []
    for i in range(M):
        sxg, syg, exg, eyg = map(lambda x : int(x) - 1, sys.stdin.readline().split())
        guests.append(((sxg, syg), (exg,eyg)))
    # find minimum distance guest
    while guests:
        dist = get_dist((xt, yt), {guest[0] for guest in guests})
        guests.sort(key = lambda x: (-dist[x[0]], -x[0][0], -x[0][1]))
        start, end = guests[-1]
        fuel -= dist[start]
        if fuel > 0:
            dist = get_dist(start, {end})[end]
            if fuel < dist: 
                break
            else:
                fuel += dist
        else: 
            break

        xt, yt = end
        guests.pop()

    if guests:
        print (-1)
    else:
        print(fuel)