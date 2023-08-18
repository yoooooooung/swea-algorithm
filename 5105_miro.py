# 5105.미로의 거리

import sys
sys.stdin = open("5105_miro_input.txt")

T = int(input())

def bfs(r, c):
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1   # 시작점 방문 표시
    Q = list()
    Q.append((r, c))    # 시작점을 인큐

    while Q:
        i, j = Q.pop(0) # Q에 들어있는 가장 앞 정점 정점을 디큐
        if miro[i][j] == 3: # 도착점을 찾으면
            return visited[i][j]-2  # 지나온 칸 수를 리턴 (시작점과 정점을 뺀 나머지)

        # 인접하고 인큐된 적이 없으면
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:   # 이동 방향
            ni, nj = i+di, j+dj
            # 미로 범위내에서 그리고 벽에 부딪히지 않는 선에서 방문한적 없는 칸이라면
            if 0 <= ni < N and 0 <= nj < N and miro[ni][nj] != 1 and visited[ni][nj] == 0:
                Q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    return 0    # 3인칸에 도달할 수 없는 경우


for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    # print(miro)
    s_row, s_col = '', ''

    # 시작점(2) 찾기
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                s_row, s_col = i, j
                break
        if type(s_row) == int:
            break

    print(f'#{tc} {bfs(s_row, s_col)}')
