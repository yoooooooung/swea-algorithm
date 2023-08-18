# 부분 집합과 부분 집합의 합
arr = [1, 2, 3, 4]
bit = [0, 0, 0, 0]

# 부분 집합
def print_subset(bit, arr, n):
    total = 0
    for i in range(n):
        if bit[i]:
            print(arr[i], end=' ')
            total += arr[i]    # 부분집합의 합을 구하는 식
    print(bit)

# 모든 원소가 돌아가면서 들어가거나 없어지거나(0)
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print_subset(bit, arr, 4)