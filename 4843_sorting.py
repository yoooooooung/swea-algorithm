T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    new_list = []
    for i in range(N-1):
        if num_list and len(new_list) < 9:
            new_list.append(max(num_list))
            num_list.remove(max(num_list))
            new_list.append(min(num_list))
            num_list.remove(min(num_list))
    result = ' '.join(map(str, new_list))
    print(f'#{tc} {result}')

# 선택 정렬로 다시 풀기