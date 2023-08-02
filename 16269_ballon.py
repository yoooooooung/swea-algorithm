T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    total = 0
    s = 0

    for i in range(N):
        arr.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(M):
            s = 0
            for di, dt in [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0]]:
                ni, nj = i + di, j + dt
                if 0 <= ni < N and 0 <= nj < M:
                    s += arr[ni][nj]
            if s > total:
                total = s

    print(f'#{tc} {total}')