# 선택 정렬 알고리즘
def selectionSort(a, N):
    for i in range(N-1):    # 마지막 바로 앞 원소까지
        min_idx = i
        for j in range(i+1, N):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
