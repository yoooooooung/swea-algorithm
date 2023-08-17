# 미로
import sys
sys.stdin = open("4875_input.txt")

def find_way():
    while stack:
        y, x = stack.pop()
        miro[y][x] = 5  # 지나간길 5로 표시
        for i in range(4):
            ni = y + di[i]
            nj = x + dj[i]
            if 0 <= ni < N and 0 <= nj < N:
                # 도착점을 찾으면
                if miro[ni][nj] == 3:
                    return 1
                # 못찾으면 갈 수 있는 곳을 전부 stack에 담음
                elif miro[ni][nj] == 0:
                    stack.append([ni, nj])
    # 도착점을 못 찾으면 0
    return 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    # print(miro)
    # start_i, start_j = '', ''
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    stack = []

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                stack.append([i, j])
                break
        # i 반복문도 멈추기
        if stack:
            break
    print(f'#{tc} {find_way()}')