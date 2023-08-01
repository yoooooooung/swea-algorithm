'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.


'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = str(input())
    max_num = 0
    max_count = 0

    for i in range(10):
        current_num = i
        current_count = cards.count(f'{i}')

        # 반복문을 나가기전, current_count와 max_count를 비교하며, current_count가 더 크다면
        if current_count > max_count:
            # 최대값, 숫자에 값을 넣어주기
            max_num = current_num
            max_count = current_count
        # 만약 그 값이 같다면, 더 큰 숫자를 넣어주기
        elif current_count == max_count:
            if current_num > max_num:
                max_num = current_num

    print(f'#{tc} {max_num} {max_count}')