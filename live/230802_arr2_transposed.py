# 전치 행렬 & 대각선 방향 합치기

'''
전치 행렬
NxN의 행렬에서 ↘ 방향 전치 행렬
3
1 2 3
4 5 6
7 8 9
'''


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
	for j in range(3):
		if i < j:  # 대각선을 기준으로 오른쪽 위에 있는 요소들만 대치 가능해야 하는 조건
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]




# 대각선 방향 합치기
'''
NxN의 행렬에서 ↘ 방향값 합치기 (1, 5, 9)
NxN의 행렬에서 ↙ 방향값 합치기 (3, 5, 7)
3
1 2 3
4 5 6
7 8 9
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total1 = 0     # NxN의 행렬에서 ↘ 방향값 합치기 (1, 5, 9)
total2 = 0     # NxN의 행렬에서 ↙ 방향값 합치기 (3, 5, 7)
for p in range(N):
    total1 += arr[p][p]
    total2 += arr[p][N - 1 - p]