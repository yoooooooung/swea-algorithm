# 숫자 배열 회전

from pprint import pprint

T = int(input())
for t in range(1, T+1):
    N = int(input())    # 3이상 7이하
    number_list = []
    new_list = [[] * N for _ in range(N)]
    for x in range(N):
        number_list.append(list(map(int, input().split())))

    count = N
    while count > 0:
        # 재귀?
        # def turnning (origin, new):
        #     global count
        #     count -= 1
            # 여기부터
        for i in range(N):
            block = ''
            for j in range(N - 1, -1, -1):
                number_list[j][i]       # number_list[j][i]
                # 문자열 붙이기
                block = block + str(number_list[j][i])
            # print('block::', block)
            new_list[i].append(block)
            # turnning(new, new)

    # turnning(number_list, new_list)

    print(f'#{t}')
    pprint(new_list)
