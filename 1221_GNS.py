import sys
sys.stdin = open("GNS_test_input.txt")

T = int(input())
for tc in range(1, T+1):
    t, length = input().split()
    length = int(length)
    alien_num_list = list(map(str, input().split()))
    new_list = []
    result_list  = []

    num_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

    # 문자열 -> 숫자 변환 작업
    for alien_num in alien_num_list:
        new_list.append(num_dict[alien_num])

    # 정렬 작업
    new_list.sort()
    # print(new_list)

    # 숫자 -> 문자열 변환 작업
    for i in new_list:
        for k, v in num_dict.items():
            if i == v:
                result_list.append(k)

    print(f'#{tc}')
    print(*result_list)