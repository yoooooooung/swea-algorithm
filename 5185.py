# 이진수

import sys
sys.stdin = open("5185_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, num = input().split()
    trans = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    result = ''
    for x in num:
        if x.isalpha():
            trans[x]%2
            pass
        else:
            # ten += int(x)
            pass
    print(f'ten:: ')