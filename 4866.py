import sys
sys.stdin = open("4866_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    string = input()
    dictionary = {')': '(', '}': '{'}
    stack = []
    for char in string:
        # print('char', char)
        if char in '({)}':
            # print('!')
            if stack and char in ')}' and dictionary[char] == stack[-1]:
                # print('!!')
                stack.pop()
            else:
                stack.append(char)
        # print(stack)
    if stack : print(f'#{tc} 0')
    else : print(f'#{tc} 1')