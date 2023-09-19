# 1865 동철이의 일 분배
# 지원이 코드

import sys
sys.stdin = open("1865_input.txt")

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    p = [0] * n
    max_v = 0


    def find(i, s):
        global max_v
        if s <= max_v:
            return
        if i == n:
            if max_v <= s:
                max_v = s
            return
        else:
            for j in range(n):
                if p[j] == 0:
                    p[j] = 1
                    find(i + 1, s * (arr[i][j] * 0.01))
                    p[j] = 0


    find(0, 1)
    print(f'#{tc} {max_v * 100:6f}')