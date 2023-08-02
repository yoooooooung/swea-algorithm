'''
다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

다음과 같은 5X5 배열에서 최댓값은 29이다.
'''
for tc in range(1, 11):
    N = int(input())
    arr = []
    max_v = 0
    cross1_summary = 0
    cross2_summary = 0
    row_summary = 0
    col_summary = 0

    for _ in range(100):
        arr.append(list(map(int, input().split())))

    for i in range(100):
        row_summary = sum(arr[i])  # 행 합
        col_summary = 0

        cross1_summary += arr[i][i]          # 대각선의 합1
        cross2_summary += arr[99 - i][i]     # 대각선의 합2

        for j in range(100):
            col_summary += arr[j][i]    # 열 합

        # 최댓값
        for v in [row_summary, col_summary, cross1_summary, cross2_summary]:
            if v > max_v:
                max_v = v

    print(f'#{tc} {max_v}')