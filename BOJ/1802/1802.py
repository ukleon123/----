import sys

def solve(bent):
    result = 1
    length = len(bent) // 2
    for i in range(length):
        if bent[i] != bent[-(i + 1)]:
            continue
        else:
            return 0
    if length > 1:
        result = solve(bent[:length])
        result = solve(bent[-length:])
    return result

    

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for i in range(T):
        origami = list(map(int, sys.stdin.readline()[:-1]))
        print("YES" if solve(origami) else "NO")
            

# 접힌 것이기 때문에 역순, 역방향으로 생각하여야 조건에 성립한다.
# 프랙탈 구조이기 때문에 재귀적으로 전부 검사하는 것도 옳은 해답이 될 것
