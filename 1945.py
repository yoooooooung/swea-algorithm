# 간단한 소인수분해

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = [2, 3, 5, 7, 11]
    # 지수 리스트
    answer = []
    for num in numbers:
        cnt = 0
        # N이 num(2, 3, 5, 7, 11) 로 나눈뒤 0이 될 때 까지 반복
        while N % num == 0:
            # N은 몫으로 변경
            N = N//num
            cnt += 1
        # 지수 저장
        answer.append(cnt)
    print(f'#{tc}', *answer)
