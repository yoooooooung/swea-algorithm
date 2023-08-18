# 미로1

import sys
sys.stdin = open("1226_miro1_input.txt")


def miro(s_y, s_x):
    visited = [[0]*16 for _ in range(16)]
    visited[s_y][s_x] = 1
    Q = list()
    Q.append((s_y, s_x))

    while Q:
        y, x = Q.pop(0)
        # print(f'({y},{x})로 이동')
        if arr[y][x] == 3:
            return 1

        for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ny = y+dy
            nx = x+dx
            if 0 <= ny < 16 and 0 <= nx < 16 and arr[ny][nx] != 1 and visited[ny][nx] == 0:
                Q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1     # 거리를 재면

    return 0


for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    s_y, s_x = '', ''\
    # 시작점 찾기
    for y in range(16):
        # print('y 계속 돈당')
        for x in range(16):
            if arr[y][x] == 2:
                s_y = y
                s_x = x
                # print('차자따')
                break
        if type(s_y) == int:
            # print('멈춧다')
            break

    print(f'#{tc} {miro(s_y, s_x)}')
