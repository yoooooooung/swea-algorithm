# 당근 포장하기
import sys
sys.stdin = open("16811_carrot_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()

    min_c_dif = 30000

    # 같은 크기의 당근은 같은 상자에 들어 있다.
    # 한 상자에 담긴 당근의 갯수는 N//2를 초과할 수 없다
    # 각 상자에 든 당근의 개수 차이가 최소가 되도록 포장해야 한다

    for i in range(N - 2):  # A박스
        for j in range(i + 1, N - 1):  # B박스, C박스
            if carrots[i] != carrots[i + 1] and carrots[j] != carrots[j + 1] and i + 1 <= N // 2 and j - i <= N // 2 and N - j - 1 <= N // 2:
                A = i + 1  # A박스 개수
                B = j - i
                C = N - 1 - j
                if min_c_dif > max(A, B, C) - min(A, B, C):
                    min_c_dif = max(A, B, C) - min(A, B, C)

    if min_c_dif == 30000:
        min_c_dif = -1

    print(f'#{tc} {min_c_dif}')
