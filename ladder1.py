for tc in range(1, 11):
    N = int(input())
    ladder = []

    for line in range(100):
        ladder_input = '0 ' + input() + '0'         # 양 옆에 0 한 열씩 삽입
        ladder.append(list(map(int, ladder_input.split())))

    x_row, x_col = 99, ladder[99].index(2)
    # print('위치 :', x_row, x_col)

    while x_row > 0:
        if ladder[x_row][x_col - 1] == 1:           # 왼쪽에 1이 있다면
            while ladder[x_row][x_col - 1] == 1:    # 1이 있을 때까지
                x_col -= 1                          # 왼쪽으로 이동
            x_row -= 1                              # 끝나고 위로 이동
        elif ladder[x_row][x_col + 1] == 1:         # 오른쪽에 1이 잇다면
            while ladder[x_row][x_col + 1] == 1:    # 1이 있을 때 까지
                x_col += 1                          # 오른쪽으로 이동
            x_row -= 1                              # 끝나고 위로 이동
        else:                                       # 왼/오에 1이 없으면
            x_row -= 1                              # 위로 이동
    print(f'#{tc} {x_col - 1}')
