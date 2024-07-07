import sys
from itertools import permutations
from abc import abstractmethod


def get_permuted_order():
    for order in permutations(range(1, 9), 8):
        order = order[:3] + (0,) + order[3:]
        yield order

if __name__ == "__main__":
    N : int = int(sys.stdin.readline())
    data : list[list[int]] = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    result = 0
    for order in get_permuted_order():
        point : int = 0
        current : int = 0
        for record in data:
            count : int = 0
            s1, s2, s3  = 0, 0, 0
            while count < 3:
                match record[order[current]]:
                    case 0:
                        count += 1
                    case 1:
                        point += s3
                        s3 = s2
                        s2 = s1
                        s1 = 1
                    case 2:
                        point += s3 + s2
                        s3 = s1
                        s2 = 1
                        s1 = 0
                    case 3:
                        point += s3 + s2 + s1
                        s3 = 1
                        s2 = 0
                        s1 = 0
                    case 4:
                        point += s3 + s2 + s1 + 1
                        s3 = 0
                        s2 = 0
                        s1 = 0
                current = (current + 1) % 9
        if result < point: 
            result = point
        else:
            pass
    print(result)