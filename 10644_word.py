T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = input()
    # print(str1)
    max_count = 0

    for alp in str1:
        cnt = 0
        for i in range(len(str2)):
            if alp == str2[i]:
                cnt += 1
        if cnt > max_count:
            max_count = cnt
    print(f'#{tc} {max_count}')