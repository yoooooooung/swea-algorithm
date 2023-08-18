'''
인접 4칸의 합 중 최대값 구하기
3
1 2 3
4 5 6
7 8 9

'''
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]  # 오 위 왼 하 순서

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)

max_v = 0 # 모든 원소가 0 이상이라는 전제 하에
for i in range(N):  # 모든 원소 arr[i][j]에 대해...
    for j in range(N):
        s = arr[i][j]
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N:  # 배열을 벗어나지 않으면 (인접 4칸이 모두 존재할 때)
                s += arr[ni][nj]

        # 여기까지 주변 원소를 포함한 합
        if max_v < s:
            max_v = s



