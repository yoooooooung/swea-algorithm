# 5102. 노드의 거리

import sys
sys.stdin = open("5102_input.txt")

def connact(S, G):
    # 노드 방문을 기록
    visited = [0]*(V+1)
    visited[S] = 1
    Q = list()
    Q.append(S)
    # print(Q)

    while Q:
        now = Q.pop(0)

        # [끝점]을 만난 경우 종료
        if node_map[now][G] == 1:
            # print('도챡!')
            return visited[now]

        for i in range(1, V+1):
            # now와 i사이에 간선이 있고, i에 방문한 적이 없을 때
            if node_map[now][i] == 1 and visited[i] == 0:
                visited[i] = visited[now] + 1
                Q.append(i)
                # print(f'{S}에서 {i}로 이동')
    else:
        return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())    # 노드수, 간선수
    # 간선 정보
    line = [map(int, input().split()) for _ in range(E)]
    node_map = [[0]*(V+1) for _ in range(V+1)]
    # 간선 정보로 노드 행렬 생성
    for f, t in line:
        node_map[f][t] = 1
        node_map[t][f] = 1

    S, G = map(int, input().split())    # 출발 노드, 도착 노드

    print(f'#{tc} {connact(S, G)}')