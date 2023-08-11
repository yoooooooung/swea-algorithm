# 백만장자 프로젝트
import sys
sys.stdin = open("1859_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stock = list(map(int, input().split()))
    buy = 0
    answer = 0

    for i in range(N-1):
        # answer = 0
        max_stock = max(stock)
        where = stock.index(max_stock)
        if i < where:
            answer += max_stock - stock[i]
            print(f'#{tc} {i}번째 계산 중 : {answer} ')
            # buy += stock[i]
        else:
            max_stock = max(stock[i:])
            where = stock.index(max_stock)


        answer += max(stock)*where - buy

    print(f'#{tc} {answer}')
    # print(f'buy : {buy}')
    # print(f'where : {where}')