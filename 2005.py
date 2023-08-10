import sys
sys.stdin = open("2005_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    # 빈 행렬
    for n in range(N):
        arr.append([0]*(n+1))
        if n == 0:
            arr[n][0] = 1
        else:
            for k in range(n):
                arr[n][0] = 1
                arr[n][-1] = 1
                if 0 < k < n:
                    arr[n][k] = arr[n-1][k-1] + arr[n-1][k]     # DP 사용

    print(f'#{tc}')
    for num in arr:
        print(*num)