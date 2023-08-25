# 이진수

import sys
sys.stdin = open("5185_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, num = input().split()
    trans = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    result = ''
    for x in num[::-1]:
        if x.isalpha():
            x = trans[x]
            for _ in range(4):
                result = str(x % 2) + result
                x//=2
        else:
            x = int(x)
            for _ in range(4):
                result = str(x % 2) + result
                x //= 2

    print(f'#{tc} {result}')