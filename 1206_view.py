T = 10
for tc in range (1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    for i in range(2, N-2):
        left_v2 = arr[i] - arr[i-2]
        left_v1 = arr[i] - arr[i-1]
        right_v1 = arr[i] - arr[i+1]
        right_v2 = arr[i] - arr[i+2]
        if left_v2 > 0 and left_v1 > 0 and right_v2 > 0 and right_v1 > 0:
            answer += min(left_v2, left_v1, right_v1, right_v2)
    print(f'#{tc} {answer}')
