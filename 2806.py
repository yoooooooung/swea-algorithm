# 2806 N-Queen
# 지원이 코드

def isPromising(x):  # x는 현재 행
    for i in range(x):  # 이전에 놓인 퀸들과 비교
        if queen[x] == queen[i] or abs(queen[x] - queen[i]) == x - i:  # 이전에 놓인 퀸과 열이 같나? or 이전에 놓인 퀸의 대각선에 위치하는가?
            return False
    return True


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    queen = [0] * n  # 인덱스(행)별 퀸을 놓는 열 저장
    cnt = 0


    def dfs(x):
        global cnt

        if x == n:  # 모든 퀸을 다 놓았으면
            cnt += 1  # 경우의 수 하나 증가
            return
        else:
            for i in range(n):
                queen[x] = i  # 퀸 놓기
                if isPromising(x):
                    dfs(x + 1)


    dfs(0)
    print(f'#{tc} {cnt}')