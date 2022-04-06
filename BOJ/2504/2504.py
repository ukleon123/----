import sys

if __name__ == "__main__":
    data = list(sys.stdin.readline()[:-1])
    data.reverse()
    expr = ''
    cnt1 = 0; cnt2 = 0
    while data:
        try:
            first = data.pop()
            second = data[-1]
            if first== '(':
                if second == '(':
                    expr = expr + '2*(' 
                elif second == '[':
                    expr = expr + '2*(' 
                elif second == ')':
                    expr = expr + '2'
                elif second == ']':
                    expr = '0'
                    break
                cnt1 += 1
            elif first == '[':
                if second == '(':
                    expr = expr + '3*(' 
                elif second == '[':
                    expr = expr + '3*(' 
                elif second == ']':
                    expr = expr + '3'
                elif second == ')':
                    expr = '0'
                    break
                cnt2 += 1
            elif first == ')':
                if second == '(':
                    expr = expr + '+' 
                elif second == '[':
                    expr = expr + '+' 
                elif second == ')':
                    expr = expr + ')'
                elif second == ']':
                    expr = expr + ')'
                cnt1 -= 1
            elif first == ']':
                if second == '(':
                    expr = expr + '+' 
                elif second == '[':
                    expr = expr + '+' 
                elif second == ')':
                    expr = expr + ')'
                elif second == ']':
                    expr = expr + ')'
                cnt2 -= 1
            if cnt1 < 0 or cnt2 < 0:
                expr = '0'
                break
        except:
            if first == ')':
                cnt1 -= 1
            elif first == ']':
                cnt2 -= 1
            if first == '(':
                cnt1 += 1
            elif first == '[':
                cnt2 += 1
    if cnt1 or cnt2:
        expr = '0'
    print(eval(expr))