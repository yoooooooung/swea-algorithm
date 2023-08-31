# 최대 상금
import sys
sys.stdin = open("1244_input.txt")


def prize(p, t):
    if t == 0:
        print(num)
        return
    # while t != 0:
    for i in range(t, len(num)):
        # if p != i:
        num[i], num[p] = num[p], num[i]
        prize(p+1, t-1)
        # print(num)
        num[i], num[p] = num[p], num[i]


T = int(input())
for tc in range(1, T+1):
    num, time = input().split()
    num = list(map(int,num))
    time = int(time)
    print(f'#{tc}')

    i = 0               # 자리인덱스
    time_size_ = []     # 자리수 크기 순서대로

    prize(0, time)

