for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    view_sum = 0
    view = 0
    for x in range(2, N-3):
        max_v = arr[x-2]
        if max_v < arr[x-1]:
            max_v = arr[x-1]
        if max_v < arr[x+1]:
            max_v = arr[x+1]
        if max_v < arr[x+2]:
            max_v = arr[x+2]
        if arr[x] > max_v:
            view = arr[x] - max_v
        view_sum += view
    print(view_sum)
