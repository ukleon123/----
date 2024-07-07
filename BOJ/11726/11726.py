import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    state, p_state = 1, 1
    for i in range(N - 1):
        state, p_state = state + p_state, state
    print(state % 10007)