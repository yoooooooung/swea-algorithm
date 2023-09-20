# DFS
# 재귀 버전

graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]


visited = [0] * 5
path = []   # 방문 순서 기록


def dfs(now):
    visited[now] = 1    # 방문 체크
    # print(now, end=' ')
    path.append(now)

    # 인접한 노드들을 방문
    for next in range(5):
        if graph[now][next] == 0:
            continue
        if visited[next]:
            continue

        dfs(next)

print("dfs 재귀 = ", end="")
dfs(0)
print(*path)
# 재귀 사용시,
    # 기저 조건
    # 들어가기 전
    # 함수 호출
    # 돌아와서