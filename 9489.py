#고대 유적

import sys
sys.stdin = open("9489_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    photo = [list(map(int, input().split())) for n in range(N)]
    max_len = 0
    for i in range(N):
        h_length = 0

        for j in range(M):
            # 가로 검사
            if photo[i][j]:
                h_length += 1
                # print(f'가로검사 ({i}, {j}) => {h_length}')
                if h_length > max_len:
                    max_len = h_length
            else:
                h_length = 0

    for j in range(M):
        v_length = 0
        for i in range(N):
            # 세로 검사
            if photo[i][j]:
                v_length += 1
                # print(f'세로검사 ({j}, {i}) => {v_length}')
                if v_length > max_len:
                    max_len = v_length
            else:
                v_length = 0
    print(f'#{tc} {max_len}')
