# 암호 생성기

import sys
sys.stdin = open("1225_input.txt")

for _ in range(10):
    tc = int(input())
    pw = list(map(int, input().split()))
    keep = True


    while keep:
        for i in range(1, 6):
            if pw[0] - i <= 0:
                pw.append(pw[0] - pw.pop(0))
                keep = False
                break
            else:
                pw.append(pw.pop(0)-i)

    print(f'#{tc}', *pw)