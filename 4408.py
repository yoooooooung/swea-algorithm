# 자기방으로 돌아가기

import sys
sys.stdin = open("4408_input.txt")

T = int(input())
for tc in range(1, T+1):
    # 돌아가야 할 학생들 수
    N = int(input())
    # 현재방과 돌아갈 방
    arr = [list(map(int, input().split()))for _ in range(N)]
    # 방 사이 공간을 지나는 사람 수
    # 복도 번호 = (방번호+방번호%2)//2
    cnt = [0] * 201
    # a: 현재 방 / b: 돌아갈방
    for a, b in arr:    # 주의할 사항 : a <= b 라는 보장이 없음
        # 이거 왜 함?
        a = (a+a%2)//2
        b = (b+b%2)//2
        for i in range(min(a, b), max(a,b)+1):  # 두 방 번호중 작은 숫자에서 큰 숫자로 가도록 하기
            cnt[i] += 1

    print(f'#{tc} {max(cnt)}')

