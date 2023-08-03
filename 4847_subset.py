T = int(input())
A = range(1, 13)
for tc in range(1, T+1):
    N, K = map(int, input().split())
    count = 0
    for i in range(1 << len(A)):            # 1<<N : 부분 집합의 개수
        num_arr = []
        for j in range(len(A)):              # 원소의 수만큼 비트를 비교함
            if i & (1 << j):             # i의 j번 비트가 1인 경우
                num_arr.append(A[j])     # A[j]는 부분집합에 포함되어 있는 원소
        if len(num_arr) == N and sum(num_arr) == K:
            count += 1
    print(f'#{tc} {count}')


'''arr = [1, 2, 3]
N = 3
for i in range(1 << N):     # 부분집합의 개수만큼 i를 돌리기
    for j in range(N)'''