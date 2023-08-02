'''
[최대값과 최소값]

N개의 양의 정수가 첫번째부터 N번째까지 주어진다. 최대값의 위치와 최소값의 위치의 차이를 절대값으로 출력 하시오. 단, 가장 작은 수가 여러 개이면 먼저 나오는 위치로 하고 가장 큰 수가 여러 개이면 마지막으로 나오는 위치로 한다.
예를 들어, {1, 1, 2, 3, 3} 가 주어지면 최대값의 위치는 5이고, 최소값의 위치는 1이다. 따라서 두 값 차이의 절대값은 4이다.
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    min_num = 10
    max_num = 0
    min_i = 0
    max_i = 0
    for i, num in enumerate(num_list):
        if num < min_num:
            min_num = num
            min_i = i + 1
        if num >= max_num:
            max_num = num
            max_i = i + 1

    print(f'#{tc} {abs(max_i - min_i)}')