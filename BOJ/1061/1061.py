import sys
import math


    #     +---+        
    #     | 3 |        
    # +---+---+---+---+
    # | 4 | 0 | 1 | 5 |
    # +---+---+---+---+
    #     | 2 |        
    #     +---+        

def minCalc(dice: list) -> tuple:
    li_two = [  (0, 1), (0, 2), (0, 3), (0, 4),
                (1, 2), (1, 3), (1, 5),
                (2, 4), (2, 5),
                (3, 4), (3, 5), 
                (4, 5)]
    li_three = [(0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4),
                (1, 3, 5), (1, 2, 5),
                (2, 4, 5),
                (3, 4, 5)]

    one = min(dice)
    two = float(math.inf)
    three = float(math.inf)
    for i in li_two:
        sum = dice[i[0]] + dice[i[1]]
        two = sum if sum < two else two

    for i in li_three:
        sum = dice[i[0]] + dice[i[1]] + dice[i[2]]
        three = sum if sum < three else three

    return one, two, three


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    dice = list(map(int, sys.stdin.readline().split())) #a, b, c, d, e, f
    
    result = 0
    one, two, three = minCalc(dice)

    one_num = ((N - 2) * (N - 2)) * 5 + (N - 2) * 4 if ((N - 2) * (N - 2)) * 5 + (N - 2) * 4 > 0 else 0
    two_num = (8 * N) - 12 if (8 * N) - 12 > 0 else 0
    three_num = 0 if N == 1 else 4 
    
    result += one * one_num
    result += two * two_num
    result += three * three_num

    if N == 1:
        print(sum(dice) - max(dice))
    else:
        print(result)