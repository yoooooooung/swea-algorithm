# 노드의 합

import sys
sys.stdin = open("5178_input.txt")


def find_key(s, L): # s는 현재 탐색 노드(마지막 노드부터 시작)/ L은 찾아야 하는 노드 번호
    # L 노드에 값이 들어 있다면 그 값을 출력
    if s < L:
        return heap[L]
    # L 노드에 값이 들어 있지 않다면 = 아직 빈 값이라면
    else:
        if heap[s] == 0:
            if s*2+1 <= N:
                heap[s] = heap[s * 2] + heap[s*2+1]
            else:
                heap[s] = heap[s * 2]
        s -= 1
        return find_key(s, L)




T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    heap = [0] * (N+1)
    for _ in range(M):
        leaf, key = map(int, input().split())
        heap[leaf] = key

    search = N-M

    print(f'#{tc} {find_key(search, L)}')
