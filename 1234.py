import sys
sys.stdin = open("1234_input.txt", "r")

for tc in range(1, 11):
    N, numbers = map(str, input().split())
    stack = ['']*int(N)
    top = -1
    for char in numbers:
        if top >= 0 and char == stack[top]:
            stack[top] = ''
            top -= 1
            # print(f'빼고 난 뒤 : {stack}')
        else:
            top += 1
            stack[top] = char
            # print(f'넣고 난 뒤 : {stack}')

    result =''.join(stack)
    print(f'#{tc} {result}')
