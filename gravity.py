'''
가로 N 세로 100 크기의 방에 상자들이 쌓여있다. 방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때, 가장 큰 낙차를 구하여라

[제약 사항]
중력은 회전이 완료된 후 적용된다.
상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다.
방의 세로 길이는 항상 100이다. 즉, 상자는 최소 0, 최대 100 높이로 쌓을 수 있다
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box_arr = list(map(int, input().split()))

    max_d = 0
    for i in range(N):
        # 나보다 작은 숫자가 오른쪽에 몇개인지 세기
        count = 0
        for j in range(i+1, N):
            if box_arr[i] > box_arr[j]:
                count += 1
        # 지금 센 값이 max_d보다 크면 값 교체
        if max_d < count:
            max_d = count

    print(f'#{tc} {max_d}')