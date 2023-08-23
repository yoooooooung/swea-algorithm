# 이진 힙
import sys
sys.stdin = open("5177_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 노드의 수
    tree = [0] + list(map(int, input().split()))
    # print(tree)
    last = N//2    # 마지막 노드의 부모 번호
    result = 0


    # tree -> 완전 이진 트리 만들기
    for i in range(1, N+1):
        while tree[i] < tree[i//2]:        # 내가 부모 노드보다 작으면
            tree[i], tree[i//2] = tree[i//2], tree[i]   # 자리 바꾸기
            i //= 2              # while 내부에서 i를 변경 -> 다음 조상 계속 검토

    # 조상 노드에 저장된 정수의 합을 알아내기
    while last > 0:
        result += tree[last]
        last //= 2


    # print(f'정리한 tree:: {tree}')
    print(f'#{tc} {result}')

    '''
    
            7
        2       5
      3   4    6
    ---------------------
            2
        5       7
      3   4    6

    
    '''

