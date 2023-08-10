# 그래프 경로 (제출용)
import sys
sys.stdin = open("10682_input.txt")

# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     route = [[]]*E
#     visited = ['F']*(V+1)
#     stack = []
#     for i in range(E):
#         From, To = map(int, input().split())
#         route[i] = [From, To]
#     S, G = map(int, input().split())
#     print(route)
#     def find_route(start):
#         for r in route:
#             if r[0] == start:   # 시작점에서 출발
#                 visited[start] = 'T'    # 방문기록
#                 stack.append(start)     # 스택
#                 print(f'{r[0]}에서 {r[1]}로 이동 가능')
#                 if r[1] == G: return 1
#                 else: return find_route(r[1])
#         return 0
#
#     print(f'#{tc} {find_route(S)}')
#


def find_route(s, g):
    visited[s] = 1
    for w in range(1, V + 1):
        if adj_m[s][w] == 1 and visited[w] == 0:
            visited[w] = 1
            find_route(w, g)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선

    # 표(adj_m)를 그려서 한방향 간선에 1 채우기
    adj_m = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        v1, v2 = map(int, input().split())
        adj_m[v1][v2] = 1

    # 시작, 끝점
    S, G = map(int, input().split())

    # 방문 여부(0,1), 방문기록
    visited = [0] * (V+1)
    visited[S] = 1

    find_route(S, G)
    print(f'#{tc} {1 if visited[G] == 1 else 0}')