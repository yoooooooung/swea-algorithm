# 버블 정렬 알고리즘
def bubbleSort (a, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

arr = [100, 5, 3, 66, 7, 10]
print(bubbleSort(arr, len(arr)))