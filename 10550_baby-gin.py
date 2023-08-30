# Baby-gin (완전검색 그리디)

import sys
sys.stdin = open("10550_baby-gin_input.txt")

'''
Baby gin?
숫자 6개를 임의로 뽑았을 때,
연속된 숫자 3개나, 동일한 숫자 3개로 구성되어 있는 경우

완전 검색 (그리디)
=> 순열, 조합, 부분 집합과 같은 조합적 문제들과 연관됨
완전 검색은 조합적 문제에 대한 brute-force 방법이다.
(가능한 모든 방법을 모두 탐색해보는!)
'''

# baby-gin
def babygin(arr):
    if arr[0] == arr[1] == arr[2] and arr[3]+2 == arr[4]+1 == arr[5] :
        return 1
    elif arr[0] == arr[1] == arr[2] and  arr[3] == arr[4] == arr[5]:
        return 1
    elif arr[0]+2 == arr[1]+1 == arr[2] and arr[3]+2 == arr[4]+1 == arr[5] :
        return 1
    else:
        return 0

    # r = tri = 0
    # if p[0] == p[1] == p[2]:
    #     tri += 1
    # if p[3] == p[4] == p[5]:
    #     tri += 1
    # if p[0] + 2 == p[1] + 1 == p[2]:
    #     r += 1
    # if p[3] + 2 == p[4] + 1 == p[5]:
    #     r += 1
    # if r + tri == 2:
    #     return 1
    # else:
    #     return 0

# 순열의 모든 경우를 만드는 함수
def f(i, N, K):
    if i == K:
        return babygin(p)
    else:
        for j in range(N):  # 6가지 카드
            if used[j] == 0:    # 아직 사용되기 전이면
                p[i] = card[j]  # i번째 자리에 card[j]를 넣기
                used[j] = 1     # 사용함 표시 1
                if f(i + 1, N, K):  # 다음으로 넘어가기
                    return 1    # (하나라도 조건에 맞는 순열을 찾았으면 1을 리턴)
                used[j] = 0     # 다음 순열 다녀오면 원래대로 복구해놓기
        return 0


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input()))
    N = 6
    K = 6
    used = [0] * K  # card를 사용했는가? (1/0)
    p = [0] * K     # 여섯자리를 순서대로 채울 곳 (순열 결과값)

    r = f(0, 6, K)
    if r:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')