import sys
sys.stdin = open('sample2.txt')

T = int(input())
for tc in range(1, T+1):
    strings = input()
    stack = []
    for i in strings:
        if not stack :
            if i == '{' or i == '(':
                stack.append(i)
            elif i == '}' or i == ')':
                stack.append(i)
                break
        else :
            temp = stack[-1]
            if temp == '{':
                if i == '}':
                    stack.pop()
                elif i == ')':
                    break
                elif i == '{' or i == '(':
                    stack.append(i)
            elif temp == '(':
                if i == ')':
                    stack.pop()
                elif i == '}':
                    break
                elif i == '{' or i == '(':
                    stack.append(i)
    print('#{} {}'.format(tc, 0 if stack else 1))
