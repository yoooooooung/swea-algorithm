# 숫자 배열 회전

import sys
sys.stdin = open("1961_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    print(numbers)