# import sys
# import math

# class vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__ (self, vec):
#         return vector(self.x + vec.x, self.y + vec.y)
#     def __sub__ (self, vec):
#         return vector(self.x - vec.x, self.y - vec.y)
#     def __len__ (self):
#         return math.sqrt(self.x ** 2 + self.y ** 2)
#     def __eq__ (self, vec):
#         if vec.x == self.x and vec.y == self.y:
#             return True
#         else:
#             return False
#     def __repr__(self):
#         return '({x}, {y})'.format(x=str(self.x), y =str(self.y))
#     def unit(self):
#         size = self.__len__()
#         return vector(self.x / size, self.y / size)



# def is_ccw (p1, p2, p3):
#     result = False
#     vec1 = p2 - p1
#     vec2 = p3 - p1
#     if vec1.x * vec2.y - vec1.y * vec2.x <= 0:
#         result = True
#     return result

# def key(p1, p2):
#     vec = p2 - p1
#     try:
#         return round(vec.x / vec.__len__(), 2)
#     except:
#         return float('-inf')
# if __name__ == "__main__":
#     N = int(sys.stdin.readline())
    
#     data = []
#     x0, y0 = 0, float('inf')
#     for _ in range(N):
#         x, y = map(int, sys.stdin.readline().split())
#         if y < y0:
#             x0, y0 = x, y
#         elif y == y0 and x < x0:
#             x0, y0 = x, y
#         data.append(vector(x, y))
    
#     removed = dict()
#     p0 = vector(x0, y0)
#     for point in data:
#         value = key(p0, point)
#         try:
#             if (point - p0).__len__() > (removed[value] - p0).__len__():
#                 removed[value] = point
#         except :
#             removed[value] = point
    
#     data = list(removed.values())
#     data.sort(key = lambda x : key(p0, x), reverse=True)

#     stack = []
#     stack.append(p0)
#     for point in data:
#         while stack.__len__() > 1 and point != p0 and is_ccw(stack[-2], stack[-1], point):
#             stack.pop()
#         stack.append(point)
#     stack.pop()
#     print(stack.__len__())



import sys


def ccw (p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
if __name__ == "__main__":
    N = int(sys.stdin.readline())

    points = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        points.append((x, y))
    points.sort()
    
    U = []
    L = []
    for point in points:
        while len(L) > 1 and ccw(L[-2], L[-1], point) <= 0:
            L.pop()
        L.append(point)
    for point in reversed(points):
        while U.__len__() > 1 and ccw(U[-2], U[-1], point) <= 0:
            U.pop()
        U.append(point)

    result = L.__len__() - 1
    result += U.__len__() - 1

    print(result)
