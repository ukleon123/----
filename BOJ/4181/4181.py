import sys


def ccw (p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
if __name__ == "__main__":
    N = int(sys.stdin.readline())

    points = []
    for _ in range(N):
        x, y, c = sys.stdin.readline().split()
        x, y = map(int, (x, y))
        points.append((x, y))
    points = sorted(points)
    
    U = []
    L = []
    for point in points:
        while len(L) > 1 and ccw(L[-2], L[-1], point) < 0:
            L.pop()
        L.append(point)
    for point in reversed(points):
        while U.__len__() > 1 and ccw(U[-2], U[-1], point) < 0:
            U.pop()
        U.append(point)

    result = L[:-1] + U[:-1]

    print(result.__len__())
    for point in result:
        print(point[0], point[1])