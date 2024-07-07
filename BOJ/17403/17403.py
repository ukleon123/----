import sys


def ccw (p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    points = []
    result = dict()
    for _ in range(N):
        x, y = sys.stdin.readline().split()
        x, y = map(int, (x, y))
        points.append((x, y))
        result[(x,y)] = 0
    
    count = 1
    while points.__len__() > 2:
        U = []
        L = []
        points = sorted(points) 
        for point in points:
            while len(L) > 1 and ccw(L[-2], L[-1], point) <= 0:
                L.pop()
            L.append(point)
        for point in points:
            while U.__len__() > 1 and ccw(U[-2], U[-1], point) >= 0:
                U.pop()
            U.append(point)
        
        if U == L:
            break

        convex_hull = set(U) | set(L)
        for p in convex_hull:
            result[p] = count
        
        points = list(set(points) - convex_hull)
        count += 1
    print(*result.values())