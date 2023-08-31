# 컨테이너 운반
import sys
sys.stdin = open("9934_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 컨테이너 수 , M : 트럭 수
    W = list(map(int, input().split()))     # N개의 화물의 무게
    T = list(map(int, input().split()))     # M개 트럭의 적재용량
    W.sort()
    T.sort()
    S = 0       # 건너간 총 화물 무게
    i = N-1       # 남은 것 중 제일 큰 컨테이너 index

    for j in range(M-1, -1, -1):
        if i < 0:
            break
        else:
            while W[i] > T[j]:
                i -= 1
                if i < 0:
                    break
            if W[i] <= T[j]:
                S += W[i]
                i -= 1

    print(f'#{tc} {S}')