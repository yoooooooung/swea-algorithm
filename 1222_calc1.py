# 계산기1
import sys
sys.stdin = open("1222_calc1_input.txt")

for tc in range(1, 11):
    N = int(input())
    S = input()
    stack = []  # +를 닮을 stack
    postfix = ''

    # 후위 표기식으로 바꾸기
    for x in S:
        if x == '+':
            # stack 이 빌 때까지 pop해서 postfix에 붙이기
            while stack:
                postfix += stack.pop()
            # stack 이 비고 나면 stack에 + 삽입
            stack.append(x)
        else:   # 숫자라면 바로 postfix에 붙이기
            postfix += x

    while stack:    # stack이 빌 때까지 postfix에 붙이기 (마지막+를 위해)
        postfix += stack.pop()


    # stack = []

    # 후위 표기식 계산하기
    for i in postfix:
        if i == '+':
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(n1+n2)
        else:
            stack.append(int(i))

    print(f'#{tc} {stack[-1]}')