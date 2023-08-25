# 진기의 최고급 붕어빵

import sys
sys.stdin = open("1860_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())     # N명, M초동안 K개 생산
    # N명이 각각 도착하는 시간
    time = list(map(int, input().split()))
    time.sort()      # 도착시간이 빠른 사람 순으로 정렬
    result = 'Possible'

    # 하나를 만들기도 전에 첫 손님이 도착한다면 바로 Impossible
    if time[0] < M:
        result = 'Impossible'

    else:
        for i in range(N):
            if i+1 > time[i]//M*K:     # arr[i]//M*K : i+1 번째 손님이 왔을 때 생산량
                result = 'Impossible'
                break
    # 하나를 만들기도 전에 첫 손님이 도착한다면 바로 Impossible
    # if time[0] < M:
    #     result = 'Impossible'


    print(f'#{tc} {result}')