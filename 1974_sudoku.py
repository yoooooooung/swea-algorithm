import sys
sys.stdin = open("1974_input.txt", "r")



def sudoku_f(arr):
    # 9줄 검사
    for i in range(9):
        cnt_h = [0]*10
        cnt_v = [0]*10

        for j in range(9):
            # 가로 검사
            cnt_h[arr[i][j]] += 1
            # 세로 검사
            cnt_v[arr[j][i]] += 1
        # 0이 들어가 있는 경우로 수정 ([0]인덱스 제외하고)
        if 0 in cnt_h[1:] or 0 in cnt_v[1:]:
            return 0

    # 3x3 검사
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            pan = [0]*10
            for i in range(3):
                for j in range(3):
                    pan[arr[x+i][y+j]] += 1
                    if pan[arr[x+i][y+j]] == 2:
                        # print(pan)
                        return 0
    return 1


T = int(input())
for tc in range(1, T+1):
    sudoku = []
    # 스도쿠 배열 완성
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))

    print(f'#{tc} {sudoku_f(sudoku)}')

