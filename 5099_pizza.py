# 피자 굽기
import sys
sys.stdin = open("5099_input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    waitlist = list(map(int, input().split()))
    pizza_list = [i for i in range(M)]
    oven = []
    round = M            # 다음에 들어가려고 대기중인 피자 번호

    # 화덕에 피자 준비
    for i in range(N):
        # new_pizza = waitlist.pop(0)
        oven.append(waitlist[i])

    while pizza_list.count(1) != 1:



        # 한 번 돌 고 난 뒤, 치즈 상태
        for i in range(N):
            oven[i] = oven[i]//2
            # 근데 화덕에 i 번째 피즈의 치즈 상태가 0이고 waitlist에 남은 피자가 있다면
            if oven[i] == 0 and waitlist:
                pizza_list[i] = 0   #
                M += 1
                oven[i] = waitlist.pop(0)
            # 화덕에 i 번째 피자의 치즈 상태가 0 이고 waitlist에 남은 피자가 없다면
            elif oven[i] == 0:
                pizza_list[i] = 0
                oven[i] = 100


    print(f'#{tc} {pizza_list.index(1)+1}')

    print(oven, waitlist, pizza_list)