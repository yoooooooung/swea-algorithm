# 노드의 합

import sys
sys.stdin = open("5178_input.txt")


# def find_key(s, L): # s는 현재 탐색 노드(마지막 노드부터 시작)/ L은 찾아야 하는 노드 번호
#     s//=2
#     # L 노드에 값이 들어 있다면 그 값을 출력
#     if heap[L]:
#         return heap[L]
#     # L 노드에 값이 들어 있지 않다면 = 아직 빈 값이라면
#     else:
#         if s > 0:
#             if not heap[s] :
#                 heap[s] = heap[s*2] + heap[s*2+1]
#                 find_key(s, L)



T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    heap = [0] * (N+1)
    for _ in range(M):
        leaf, key = map(int, input().split())
        heap[leaf] = key

    search = N//2
    print(heap)
    while True:
        # 탐색하는 search 번호가 L일때 멈춰
        if search == L:
            break
        else:
            pass

    # find_key(N, L)
