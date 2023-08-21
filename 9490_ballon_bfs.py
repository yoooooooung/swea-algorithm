# 풍선팡1 (bfs로 풀기)

import sys
sys.stdin = open("9490_ballon_bfs_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # NxM
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    max_flower = 0
    for i in range(N):
        for j in range(M):
            flower = 0
            for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                for k in range(1, arr[i][j]+1):
                    ny = i + dy
                    nx = j + dx
                    if 0 <= ny < N and  0 <= nx < M:
                        flower += arr[ny][nx]
            if max_flower < flower:
                max_flower = flower
    print(f'#{tc} {max_flower}')