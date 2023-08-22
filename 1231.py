# 중위 순회
import sys
sys.stdin = open("1231_input.txt")

def inorder(p):  # p : 루트 정점 / N : 완전 이진 트리의 마지막 정점
    if p <= N:
        inorder(p*2)            # 왼쪽 자식으로 이동
        print(tree[p], end='')  # 중위순회
        inorder(p*2+1)          # 오른쪽 자식으로 이동동


for tc in range(1, 11):
    N = int(input())    # 정점 개수
    tree = [0] * (N+1)  # N번 노드까지 있는 완전 이진 트리
    # ch1 = [0] * (N+1)
    # ch2 = [0] * (N+1)
    # 트리 완성하기
    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]

    # 중위 순회
    print(f'#{tc} ', end='')
    inorder(1)
    print()
