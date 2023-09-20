# 5247 연산
# 지원이 코드

import sys
sys.stdin = open("5247_input.txt")


def bfs(s):
    q = [s]
    while q:
        t = q.pop(0)
        if t == M:
            return visited[t]
        for w in [t+1, t-1, t*2, t-10]:
            if 0 < w <= 1000000 and not visited[w]:
                visited[w] = visited[t] + 1
                q.append(w)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    result = bfs(N)
    print(f'#{tc} {result}')

