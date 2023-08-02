T = int(input())
for tc in range(1, T+1):
    N = int(input())
    color1_list = []
    color2_list = []
    count = 0

    for color in range(N):
        a1i, a1j, a2i, a2j, color1 = list(map(int, input().split()))
        if color1 == 1:
            for i in range(a1i, a2i + 1):
                for j in range(a1j, a2j + 1):
                    if [i, j] not in color1_list:
                        color1_list.append([i, j])
        else:
            for i in range(a1i, a2i + 1):
                for j in range(a1j, a2j + 1):
                    if [i, j] not in color2_list:
                        color2_list.append([i, j])


    for color1_paint in color1_list:
        if color1_paint in color2_list:
            count += 1

    print(f'#{tc} {count}')