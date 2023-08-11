# 길찾기
import sys
sys.stdin = open("1219_input.txt", "r")

def dfs(start, end):
    stack = [start]         # 출발지점 stack에 등록
    # visited[start] = True   # visited에 출발지점 기록

    while stack:                        # stack이 채워져 있는 한 = 빠꾸 안되니까 항상 채워져 있음
        last = stack.pop()              # stack에 가장 마지막 요소를 빼고 last 할당
        # print(f'여기로 간다 : {last}')
        if last == end:                 # 만약 마지막 요소가 도착지점이라면
            return 1                    # 1을 return
        if visited[last] == False:    # 마지막 요소에 방문한 적 없다면
            visited[last] = True        # 마지막 요소 방문 기록 남기기
            for dep in graph[last]:       # last에서 출발했을 때 도착할 수 있는 지점 dep 훑기
                if not visited[dep]:      # dep에 방문한 적 없다면
                    stack.append(dep)     # stack에 추가하기
    return 0                              # 도착 지점을 못만나고 다 돌아버린다면 0


#dfs 사용
for _ in range(10):
    tc, length = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [False for _ in range(100)]

    graph = [[] for _ in range(100)]


    for i in range(0, length*2, 2):
        start, end = arr[i], arr[i+1]
        graph[start].append(end)

    # print(graph)
    print(f'#{tc} {dfs(0, 99)}')
