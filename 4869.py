# 종이 붙이기
'''
3
30
50
70

'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = N//10
    fibo = [0]*(n + 1)
    for i in range(1, n + 1):
        fibo[1] = 1
        fibo[2] = 3
        if i > 2:
            fibo[i] = fibo[i-1] + 2 * fibo[i-2]
    print(f'#{tc} {fibo[n]}')