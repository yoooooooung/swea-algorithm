import sys
sys.stdin = open('1979_input.txt')

# 연속하는 1*K의 개수를 구한다. 그 이상은 카운트 X

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [[] for _ in range(N)]
    count = 0

    for i in range(N):
        puzzle[i] = list(map(int, input().split()))

    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == N-1:
                if cnt == K:
                    count += 1
                cnt = 0

        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == N-1:
                if cnt == K:
                    count += 1
                cnt = 0

    print(f'#{tc} {count}')