# 원 안의 점
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 반지름
    count = 0
    for x in range(-N, N+1):
        for y in range(-N, N+1):
            if x*x + y*y <= N*N:
                count += 1
    print(f'#{tc} {count}')
