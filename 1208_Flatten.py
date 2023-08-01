T = 10
for tc in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input().split()))
    count = 0
    for i in range (N):
        # 평탄화 작업
        boxes[boxes.index(max(boxes))] = max(boxes) - 1
        boxes[boxes.index(min(boxes))] = min(boxes) + 1

    result = max(boxes) - min(boxes)

    print(f'#{tc} {result}')