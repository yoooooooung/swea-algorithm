# 병합 정렬
import sys
sys.stdin = open("5204_input.txt")


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    left_2 = merge_sort(left)
    right_2 = merge_sort(right)
    return merge(left_2, right_2)


def merge(left, right):
    global cnt
    i, j = 0, 0
    sorted_list = []
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우를 세기
    if left[-1] > right[-1]:
        cnt += 1
    # 작은 수부터 차례로 sorted_list에 넣기
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    # left나 right 리스트만 남았을 때 없어질때까지 추가해주기~
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    unsorted_list = list(map(int, input().split()))
    cnt = 0

    print(f'#{tc} {merge_sort(unsorted_list)[N // 2]} {cnt}')