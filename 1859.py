# 백만장자 프로젝트
import sys
sys.stdin = open("1859_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stock = list(map(int, input().split()))
    answer = 0
    max_stock = 0
    for i in range(N-1, -1, -1):
        if stock[i] > max_stock:
            max_stock = stock[i]
        else:
            answer += max_stock - stock[i]

    print(f'#{tc} {answer}')