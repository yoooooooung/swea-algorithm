# 이진 검색
def binarySearch(a, N, key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end)//2
        if a[middle] == key :   # 검색 성공시
            return True
        elif a[middle] > key :  # 중간값이 찾으려는 값보다 큰 경우
            end = middle - 1    # end를 중간값-1 로 설정 -> 다시 탐색
        else:                   # 중간값이 찾으려는 값보다 작은 경우
            start = middle + 1  # start를 중간값+1로 설정 -> 다시 탐색

    return False   # 위에서 return 을 못만나고 끝난다면 검색 실패