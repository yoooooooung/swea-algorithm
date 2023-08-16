# 토너먼트 카드 게임
import sys
sys.stdin = open("4880_cardgame_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    # final_winner = ''

    # for i in range(0, N, 2):
    #     winner = 0
    #     if i == N-1:
    #         if final_winner != '':  # final_winner 가 나왔을 때
    #             if cards[i] - cards[final_winner] == 1 or cards[i] - cards[final_winner] == -2 or cards[i] == cards[final_winner]:
    #                 final_winner = i
    #         else:
    #             final_winner = winner
    #     else:
    #         # 큰 수가 이기거나, i가 1, i+1이 3일 때
    #         if cards[i] - cards[i+1] == 1 or cards[i] - cards[i+1] == -2 or cards[i] == cards[i+1] :
    #             winner = i
    #         else:
    #             winner = i+1
    #
    #     if final_winner != '':    # final_winner 가 나왔을 때
    #         if cards[winner] - cards[final_winner] == 1 or cards[winner] - cards[final_winner] == -2 or cards[winner] == cards[final_winner]:
    #             final_winner = winner
    #     else:
    #         final_winner = winner

    def tournament(i, j):       # 대진 짜기
        if i == j:              # 한 명 남았을 때
            return i
        else:
            left = tournament(i, (i+j)//2)
            right = tournament((i+j)//2 + 1, j)
            return win(left, right)

    def win(i, j):                 # 가위바위보 게임
        if cards[i] == cards[j]:    # 비겼을 때
            return i
        elif cards[i] - cards[j] == 1 or cards[i] - cards[j] == -2: # 이겼을 때
            return i
        else:                       # 그 외에
            return j

    print(f'#{tc} {tournament(0, N-1)+1}')