# bfs.py

import sys
sys.stdin = open("230818_bfs_input.txt")


def bfs(s, V):              # 인접 리스트를 사용한 bfs
    visited = [0]*(V+1)     # 1. visited 생성
    Q = list()              # 2. 큐 생성
    Q.append(s)             # 3. 시작점 인큐
    visited[s] = 1          # 4. 시작점에 방문 표시
    cnt = 1

    while Q:                # 5. 큐에 정점이 남아있으면 (front != rear)
        now = Q.pop(0)      # 5-1. 디큐
        print(now)
        for i in adj_l[now]:            # 6. 인접한 정점을 탐색
            if visited[i] == 0:         # 6-1. 그 중 방문하지 않은 정점이 있다면
                Q.append(i)             # 6-2. 인큐
                visited[i] = visited[now] + 1   # 6-3. 방문기록 표시. (1에 의해 방문되는 애들은 2로 표시)
                # 정점에서 할 일



V, E = map(int, input().split())
arr = list(map(int, input().split())) # 간선 리스트

# 간선 리스트를 통해 인접 리스트 생성
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)    # 방향이 없는 경우 양방향으로 인접 리스트 생성

# 간선 리스트를 통해 인접 행렬 생성 (인접 리스트 or 인접 행렬 둘 중 하나로 이용하면 됨)
adj_m = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1       # 방향이 없는 경우


print(f'adj_l:: {adj_l}')
print('방문순서')
bfs(1, 7)
