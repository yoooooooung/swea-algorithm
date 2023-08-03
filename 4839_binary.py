T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    book = range(1, P+1)
    a_start, a_end = 0, P - 1
    b_start, b_end = 0, P - 1

    def win(page, start, end):
        in_count = 0
        while start <= end:
            in_count += 1
            middle = int((start + end)/2)
            if book[middle] == page:
                return in_count
            elif book[middle] > page:
                end = middle
            else:
                start = middle
        return 0

    a_count = win(Pa, a_start, a_end)
    b_count = win(Pb, b_start, b_end)

    winner = 'A' if a_count < b_count else 'B' if a_count > b_count else 0

    print(f'#{tc} {winner}')
