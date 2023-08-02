T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    max_fly = 0
    fly_sum = 0
    fly_stick = []

    for p in range(M):
        for q in range(M):
            fly_stick.append([p, q])

    for k in range(N - M + 1):
        for l in range(N - M + 1):
            fly_sum = 0
            for i, j in fly_stick:
                fly_sum += arr[k+i][l+j]
            if fly_sum > max_fly:
                max_fly = fly_sum

    print(f'#{tc} {max_fly}')