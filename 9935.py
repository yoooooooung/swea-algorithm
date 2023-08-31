# 화물 도크
import sys
sys.stdin = open("9935_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    apply = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
    apply.sort(key=lambda x: x[1])
    # print(apply)

    S = []
    j = 0

    for i in range(1, N+1):
        if apply[i][0] >= j:
            S.append(apply[i])
            j = apply[i][1]
    print(f'#{tc} {len(S)}')