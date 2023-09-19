# 5208 전기버스2
import sys
sys.stdin = open("5208_input.txt")
#
# T = int(input())
#
#
#
# for tc in range(1, T+1):
#     bus_stop = list(map(int, input().split()))
#     N = bus_stop[0]
#     bus_stop[0] = 0
#     battery, change = 0, 0

'''
T = int(input())
 
def f(i, end, cnt, charge) :
 
    global min_v
 
    if i == end :
 
        if min_v > cnt :
 
            min_v = cnt
 
    elif min_v <= cnt :
 
        return
 
    else :
 
        f(i+1, end, cnt+1, bus_stop[i]-1)
 
        if charge > 0 :
 
            f(i+1, end, cnt, charge-1)
 
for tc in range(1,T+1) :
 
    bus_stop = list(map(int, input().split()))
    min_v = bus_stop[0]
    cnt = 0
 
    f(2,bus_stop[0],0,bus_stop[1]-1)
 
    print(f"#{tc} {min_v}")

'''

T = int(input())


def f(i):
    global cnt, min_v
    print('f(', i, ')번쨰 함수의 cnt값 : ', cnt, 'min_v', min_v)
    if cnt >= min_v:
        return
    if i >= len(arr):
        if min_v > cnt:
            min_v = cnt
        return

    s = arr[i]
    print('s', s)
    for j in range(1, s + 1):
        cnt += 1
        f(i + j)
        cnt -= 1


for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    cnt = 0
    min_v = N
    f(0)
    print(f'#{tc} {min_v - 1}')
