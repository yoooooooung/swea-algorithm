# 단순 2진 암호코드
import sys
sys.stdin = open("1240_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 암호코드 리스트
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)
    start_y = ''
    start_x = ''

    # 암호코드 시작점 찾기 = 뒤에서부터 1을 찾기
    for y in range(N):
        for x in range(M-1, -1, -1):
            if arr[y][x] == 1:
                start_y = y
                start_x = x - 55
                break
        if type(start_y) == int:
            break


    # 암호코드만 추출하기
    code = [[0]] * 8
    for i in range(8):
        code[i] = arr[start_y][start_x + i*7:start_x + (i+1)*7]

    # print(f'#{tc} start_y:: {start_y}, start_x:: {start_x}')
    #
    # print(f'code:: {code}')
    # print()

    # 암호 해석하기
    answer = 0
    confirm = [0]

    trans = {0: [0, 0, 0, 1, 1, 0, 1], 1: [0, 0, 1, 1, 0, 0, 1], 2: [0, 0, 1, 0, 0, 1, 1], 3: [0, 1, 1, 1, 1, 0, 1], 4: [0, 1, 0, 0, 0, 1, 1], 5: [0, 1, 1, 0, 0, 0, 1], 6: [0, 1, 0, 1, 1, 1, 1], 7: [0, 1, 1, 1, 0, 1, 1], 8: [0, 1, 1, 0, 1, 1, 1], 9: [0, 0, 0, 1, 0, 1, 1] }
    for one in code:
        for k, v in trans.items():
            if one == v:
                answer += k
                confirm.append(k)

    # print(f'#{tc} {answer}')
    # print(confirm)

    # 코드 검증
    confirm_code = 0
    for i in range(1, 8, 2): # 홀수번째 계산
        confirm_code += confirm[i]

    confirm_code *= 3
    for i in range(2, 9, 2):
        confirm_code += confirm[i]


    if confirm_code % 10 == 0:
        print(f'#{tc} {answer}')
    else:
        print(f'#{tc} 0')

