import sys
sys.stdin = open("1974_input.txt", "r")

T = int(input())

def sudoku_f(arr):
    for i in range(9):
        cnt = [0]*10
        # print(tc, cnt)
        for j in range(9):
            cnt[arr[i][j]] += 1
        for k in range(1, 10):
            if cnt[k] == 0:
                return 0
        if sum(cnt) == 9:
            return 1


for tc in range(1, T+1):
    sudoku = []
    # 스도쿠 배열 완성
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))

    print(f'#{tc} {sudoku_f(sudoku)}')

