# 이진수2

import sys
sys.stdin = open("5186_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    result = 0
    a = N % 2
    print(f'#{tc} {a}')