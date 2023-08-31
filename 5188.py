# 최소합

def f(i, j, s, N):  # i, j 현재위치 / s 지나온 칸의 숫자 합계

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    y, x = 0, 0
    hop = arr[y][x]

    def f():

        for dy, dx in [[0, 1], [1, 0]]:
            y, x = y+dy, x+dx
            hop += arr[y][x]