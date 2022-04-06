import sys

if __name__ == "__main__":
    number = int(sys.stdin.readline())
    result = 0
    while number:
        if number < 0 :
            result = -1
            break
        if number % 5 :
            result += 1
            number -= 3
        else:
            result += number // 5 
            number = 0
    print(result)
    pass
"""
3으로 빼내고 5로 나누어서 확인
"""