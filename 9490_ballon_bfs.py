# 풍선팡1 (bfs로 풀기)

import sys
sys.stdin = open("9490_ballon_bfs_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # NxM
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)