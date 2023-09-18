# 이진 탐색
import sys
sys.stdin = open("5207_input.txt")

T = int(input())


def binary_search(arr, num):
    l = 0
    r = N - 1
    search_dir = '0'
    global cnt
    # if arr[m] == num:
    #     # 번갈아 선택했는지 확인하는 로직
    #     return 1
    # elif num > arr[m]:
    #     # 오른쪽 탐색
    #     binary_search(m+1, r, num)
    # else:
    #     # 왼쪽 탐색
    #     binary_search(l, m-1, num)

    while l <= r:
        m = (l+r) // 2
        print(f'l, r, m :: {l, r, m}')
        if num == arr[m]:
            cnt += 1
            break
        if num > arr[m]:
            # 오른쪽 탐색
            print('오른쪽 탐색')
            if search_dir == 'r':
                break
            else:
                search_dir = 'r'
                l = m+1
                continue
        elif num < arr[m]:
            # 왼쪽 탐색
            print('왼쪽 탐색')
            if search_dir == 'l':
                break
            else:
                search_dir = 'l'
                r = m-1
                continue
        # else:
        #     return 1
    else:
        print('while 끝')
        return 1


for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_arr = sorted(list(map(int, input().split())))
    M_arr = list(map(int, input().split()))
    cnt = 0
    # M개의 정수가 들어있는 배열 요소를 다 돌려보기
    for i in M_arr:
        # 해당 숫자가 N_arr에 있으면 이진탐색 함수돌리기
        if i in N_arr:
            # 이진탐색 조건에 해당하면 1을 반환, 없으면 0을 반환
            binary_search(N_arr, i)

    print(f'#{tc} {cnt}')