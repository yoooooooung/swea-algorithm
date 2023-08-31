# 조합 재귀 (부분집합 합 문제 구현)
# 합이 0 인 부분집합을 만나면 계산이 멈추도록

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
bit = [0] * N


def subset(i, N, s):
    if i == N:
        for j in range(N):
            if bit[j]:
                s += arr[j]
        if s == 0:              # 합(s)이 0이라면 !
            for j in range(N):  # 안에 있는 원소를 다 print 하기
                if bit[j]:
                    print(arr[j], end = ' ')
            print()
        return   # 생략가능
    else:
        bit[i]= 1
        subset(i+1, N, s+arr[i])
        bit[i] = 0
        subset(i+1, N, s)
    return


subset(0, N)