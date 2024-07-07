from sys import stdin


if __name__ == "__main__":
    N = 0
    data = [0, 1, 3]
    while True:
        try:
            N = int(stdin.readline())
        except ValueError:
            break;

        for i in range(len(data), N + 1):
            data.append(data[i - 1] + data[i - 2] * 2)

        print(data[N])

