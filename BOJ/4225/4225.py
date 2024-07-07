import sys
import math


def ccw (p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) 

if __name__ == "__main__":
    C = 1
    while True:
        points = []
        N = int(sys.stdin.readline())
        if N == 0:
            break
        for i in range(N):
            x, y = map(int, sys.stdin.readline().split())
            points.append((x, y))
        points = sorted(points)

        L = []
        U = []
        for point in points:
            while L.__len__() > 1 and ccw(L[-2], L[-1], point) <= 0:
                L.pop()
            L.append(point)
        for point in reversed(points):
            while U.__len__() > 1 and ccw(U[-2], U[-1], point) <= 0:
                U.pop()
            U.append(point)
        hull = L[:-1] + U[:-1]


        result = float("inf")
        for i in range(hull.__len__()):
            width = 0
            line = (hull[i - 1], hull[i])
            a = line[1][1] - line[0][1]
            b = line[0][0] - line[1][0]
            c = line[0][1] * line[1][0] - line[0][0] * line[1][1]
            for point in hull:
                tmp = abs(a * point[0] + b * point[1] + c) / (a ** 2 + b ** 2) ** 0.5
                width = max(width, tmp)
            result = min(result, width)
        print("Case %d: %.2f" %(C, math.ceil(result * 100) / 100))
        C += 1