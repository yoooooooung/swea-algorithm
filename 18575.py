# 풍선팡 보너스 게임
import sys
sys.stdin = open("18575_input.txt")
# TODO 머야이게

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pan = [list(map(int, input().split())) for _ in range(N)]
    max_b = 0
    min_b = N*N*9

    for y in range(N):
        for x in range(N):
            # 지금 점수 !
            score = -pan[y][x]      # 중복해서 계산되는걸 미리 빼주기
            for i in range(N):
                score += pan[y][i]  # 가로 한 줄 다 더하기
                score += pan[i][x]  # 세로 한 줄 다 더하기
            if score > max_b:
                max_b = score
            if score < min_b:
                min_b = score

    print(f'#{tc} {max_b - min_b}')


