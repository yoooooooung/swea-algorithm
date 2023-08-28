# 기지국
import sys
sys.stdin = open("12733_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sell = [list(input()) for _ in range(N)]
    print(sell)
    H_count = 0
    for y in range(N):
        for x in range(N):
            if sell[y][x] == 'H':
                H_count += 1
    
    print(f'집 수 :: {H_count}')