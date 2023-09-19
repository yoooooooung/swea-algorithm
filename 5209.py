# 5209 최소생산비용
# 강사님 풀이
import sys
sys.stdin = open("5209_input.txt")

def f(i, N, s):
    global min_v
    if i==N:
        if min_v > s:
            min_v = s
    elif min_v <= s:
        # 더적기
        return
    else:
        for j in range(N):
            if u[j] == 0:   # j번 공장이 아직 결정 전이면
                p[i] = j    # i번 물건을 j번 공장에서 생산
                u[j] = 1    # j번 공장 가동
                f(i+1, N, s+cost[i][j])     # 누적 생산 비용이 계산됨
                u[j] = 0    # 초기화 (j번 공장에서 다른 물건을 생산하는 경우)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    min_v = 1500    # 최소 생산 비용
    p = [0] * N     # p[i] : i번 물건을 생산하는 공장 번호
    u = [0] * N     # 생산물품이 결정된 공장 표시
    f(0, N, 0)
    print(f'#{tc} {min_v}')