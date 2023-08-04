# 풍선팡
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    balloon_list = []
    flower_max = 0

    for i in range(N):
        balloon_list.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(M):
            flower_now = balloon_list[i][j]
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                for k in range(1, balloon_list[i][j] + 1):
                    ni, nj = i+di*k, j+dj*k
                    if 0 <= ni < N and 0 <= nj < M:
                        flower_now += balloon_list[ni][nj]
            # 최댓값
            if flower_now > flower_max:
                flower_max = flower_now

    print(f'#{tc} {flower_max}')