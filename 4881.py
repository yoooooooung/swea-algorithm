import sys
sys.stdin = open("4881_input.txt")

def f (i, N):
    global min_v
    total = 0
    if i == N:
        # print(p)
        for s in range(N):
            total += sqr[s][p[s]]
        if min_v > total:
            min_v = total
    # 조건 더해서 쓸데 없는 일 안하도록
    elif min_v <= total:
        print('멈췃')
    else:
        for j in range(i, N):   # p[i]와 자리를 바꿀 위치
            p[i], p[j] = p[j], p[i]     # p[i]를 결정
            f(i+1, N)
            p[i], p[j] = p[j], p[i]     # 원상 복구

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sqr = [list(map(int, input().split())) for _ in range(N)]

    p = [i for i in range(N)]*N   # p[i]는 i 행에서 고른 열 번호

    min_v = 100     # 나올 수 있는 최댓값이 default 값

    f(0, N)

    print(f'#{tc} {min_v}')         # p[0]부터 p[N-1]까지 각 행에서 열을 선택하는 함수