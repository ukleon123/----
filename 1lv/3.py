import sys

def backtrack(state, current, object):
    chk = 0
    if current == object:
        chk += 1
        return chk
    else: 
        if state[current[0]][current[1] + 1] != 1:
            chk += backtrack(state, (current[0], current[1] + 1))
        if state[current[0] + 1][current[1]] != 1:
            chk += backtrack(state, (current[0], current[1] + 1))
        elif state[current[0]][current[1] + 1] == 0 and state[current[0] + 1][current[1]]:
            return 0
    

if __name__ == "__main__":
