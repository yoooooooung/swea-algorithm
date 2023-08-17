# 회전
import sys
sys.stdin = open("5097_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    front, reat = 0, 0

    for _ in range(M):
        arr.append(arr.pop(0))

    print(f'#{tc} {arr[0]}')