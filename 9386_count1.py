T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = input()
    count = 0
    for k in range(1, N+1):
        if numbers.find('1'*k) > 0:
            if k > count:
                count = k
        # print('1이 몇개', '1'*k)
    print(f'#{tc} {count}')

