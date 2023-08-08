# 회문
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    words = []
    for _ in range(N):
        words.append(list(input()))
    answer = ''

    for _ in range(2): # 가로 찾고 zip으로 옆으로 뒤집어서 세로 찾기
        for i in range(N):
            for j in range(N-M+1):
                same = 0
                word = []
                check_word = words[i][j:j+M+1]

                for k in range(M):
                    if check_word[k] != check_word[-k - 1]:
                        break
                    same += 1
                    word.append(check_word[k])

                if len(word) == M:
                    answer = word
        words = list(map(list, zip(*words)))

    last_answer = ''.join(answer)
    print(f'#{tc} {last_answer}')
