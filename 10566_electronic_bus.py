'''
내풀이
T = int(input())
for tc in range(1, T + 1):
    # K = 한 번 충전으로 최대 이동가능한 정류장 수
    # N = 마지막 정류장 번호 (총 정류장 수 = N + 1)
    # M = 충전기가 있는 정류장 수
    K, N, M = map(int, input().split())
    # bus_charger_list = 충전기가 있는 정류장 번호
    bus_charger_list = list(map(int, input().split()))
    battery = K + 1
    charge_count = 0
    # 정류장을 돌다가,
    for bus_stop in range(N + 1):
        battery -= 1
        # 만약 종점에 도착할 수 없는 경우, 0을 출력
        if battery < 0:
            charge_count = 0
            break

        # 충전기가 있는 정류장 리스트 돌기
        for i in range(M):
            # 현재 충전기 위치
            charger = bus_charger_list[i]
            # 다음 충전기 위치 (현재 위치가 마지막 충전소라면 다음 충전기 위치는 마지막 위치(N)
            next_charger = N if charger == bus_charger_list[-1] else bus_charger_list[i + 1]

            # 충전기가 있는 정류장을 만났을 때
            if bus_stop == charger:
                # 다음 정거장 까지의 거리가 남은 베터리보다 크다면 충전하기
                if next_charger - charger > battery:
                    battery = K
                    charge_count += 1

    print(f'#{tc} {charge_count}')
'''


# 모범답안
T = int(input())
for test_case in range(1, T + 1):
    # K = 한 번 충전으로 최대 이동가능한 정류장 수
    # N = 마지막 정류장 번호 (총 정류장 수 = N + 1)
    # M = 충전기가 있는 정류장 수
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    count = 0
    now = 0

    while now + K < N:  # 현재 위치 + 최대 이동 가능한 정류장수가 총 정류장 수가 되기 전까지
        for i in range(K, 0, -1):   # [K, K-1, ..., 1]
            if (now + i) in charge: # 현재위치 + 최대 이동했을 때 위치가 충전소 리스트에 있으면
                now += i            # 현재위치 + i
                count += 1
                break
        else:   # while 문이 끝날때
            count = 0
            break

    print(f"#{test_case} {count}")


