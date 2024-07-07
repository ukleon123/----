import sys


def divide(x, y, size):
    count = 0
    white, blue = 0, 0
    for i in range(x, x + size):
        for j in range(y, y + size):
            if B[i][j]:
                count += 1
    if count == 0:
        white += 1
    elif count == size ** 2:
        blue += 1
    else:
        offset = size >> 1
        w_tmp, b_tmp = divide(x, y, offset); white += w_tmp; blue += b_tmp
        w_tmp, b_tmp = divide(x, y + offset, offset); white += w_tmp; blue += b_tmp
        w_tmp, b_tmp = divide(x + offset, y, offset); white += w_tmp; blue += b_tmp
        w_tmp, b_tmp = divide(x + offset, y + offset, offset); white += w_tmp; blue += b_tmp
    return white, blue

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    B = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    white, blue = divide(0, 0, N)
    print(white)
    print(blue)