# 파리퇴치3
import sys
sys.stdin = open("12712_fly3_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    # print(fly)
    max_catch = 0
    for y in range(N):
        for x in range(N):
            catch = fly[y][x]
            # 가로세로
            for i in range(1, M):
                if y+i < N: catch += fly[y+i][x]
                if y-i >= 0: catch += fly[y-i][x]
                if x+i < N: catch += fly[y][x+i]
                if x-i >= 0: catch += fly[y][x-i]
                # print(f'y,x,i:: {y},{x},{i} => catch:: {catch}')
            if catch > max_catch:
                max_catch = catch
            catch = fly[y][x]
            # 대각선
            for i in range(1, M):
                if y-i >= 0 and x-i >= 0: catch += fly[y-i][x-i]
                if y+i < N and x-i >= 0: catch += fly[y+i][x-i]
                if y-i >=0 and x+i < N: catch += fly[y-i][x+i]
                if y+i < N and x+i < N: catch += fly[y+i][x+i]
            if catch > max_catch:
                max_catch = catch

    print(f'#{tc} {max_catch}')
