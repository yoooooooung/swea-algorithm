import sys
sys.stdin = open("10685_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    line = str(input())

    # def cut(words):
    #     if len(words) == 1:
    #         return words
    #     else:
    #         for i in range(len(words)-1):       # 파라미터의 길이 -1 까지 검사
    #             if words[i] and words[i+1] and words[i] == words[i+1]:
    #                 words = words.replace(f'{words[i]+words[i]}', "")
    #                 return cut(words)  # 재귀함수
    #             elif i == len(words) -2:
    #                 return words
    #
    # word_len = len(cut(line))
    #
    # print(f'#{tc} {word_len}')

    # stack을 사용하는 방법

    def solutions(s):
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            else:
                if s[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])
        if stack : return len(stack)
        else : return 0


    print(f'#{tc} {solutions(line)}')