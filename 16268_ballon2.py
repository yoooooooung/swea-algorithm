# 풍선팡2
import sys
sys.stdin = open("16268_ballon2_input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ballons = [list(map(int, input().split())) for _ in range(N)]
    print(ballons)

dx = [0, 0, -1, -1, 1]
dy = [0, 1, 0, -1, 0]

