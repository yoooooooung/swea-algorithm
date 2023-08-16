# Forth
# 후위 표기법 => 중위 표기법
# icp (in-coming priority)  스택 밖의 우선순위
# isp (in-stack priority)   스택 안의 우선순위

import sys
sys.stdin = open("4874_forth_input.txt")

T = int(input())
for tc in range(1, T+1):
    susik = list(input().split())
    stack = []
    # print(susik)
    answer = ''
    for char in susik:

        if char.isnumeric():
            stack.append(int(char))

        elif char == '.':
            if len(stack) != 1:
                answer = 'error'
            else:
                # 결과 꺼내
                answer = stack.pop()

        elif len(stack) >= 2 and char in '-+*/':
            n2 = stack.pop()
            n1 = stack.pop()
            if char == '-':
                stack.append(n1 - n2)
            elif char == '+':
                stack.append(n1 + n2)
            elif char == '*':
                stack.append(n1 * n2)
            elif char == '/':
                stack.append(n1 // n2)

        elif len(stack) < 2:
            answer = 'error'
            break

    print(f'#{tc} {answer}')

