T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    number_list = list(map(int, input().split()))
    max_sum = 0
    min_sum = M * 10000
    for i in range(N - M + 1):
        current_sum = 0
        for j in range(M):
            current_sum += number_list[i + j]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < min_sum:
            min_sum = current_sum
    result = max_sum - min_sum
    print(f'#{tc} {result}')