def traversal(n):
    global cnt
    if n:   # 정점이 있으면
        cnt += 1            # cnt 를 1 올려주기
        # print(n)
        traversal(ch1[n])   # 왼쪽 서브트리로 이동
        traversal(ch2[n])   # 오른쪽 서브트리로 이동


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E+1
    arr = list(map(int, input().split()))
    # 부모를 인덱스로 연결된 자식 노드 번호 저장
    ch1 = [0] * (V+1)   # 왼쪽 자식 노드
    ch2 = [0] * (V+1)   # 오른쪽 자식 노드
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    cnt = 0
    traversal(N)
    print(f'#{tc} {cnt}')