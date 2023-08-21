# 트리

'''
V
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

'''

# 전위 순회
def preorder(n):
    if n:                   # n이 0 이 아니면 = 자식과 연결되어 있으면
        print(n)            # n을 방문
        preorder(c1[n])     # 왼쪽 서브트리로 이동
        preorder(c2[n])     # 오른쪽 서브트리로 이동


V = int(input())    # 정점 개수
E = V - 1           # 간선 수
arr = list(map(int, input().split()))

# 방법1 부모를 인덱스로 자식을 저장
c1 = [0] * (V+1)
c2 = [0] * (V+1)

# 방법2 자식을 인덱스로 부모를 저장
par = [0] * (V+1)

# arr에 있는 간선 정보 -> c1, c2에 정리
for i in range(E):
    p, c = arr[2*i], arr[2*i+1]
    # 방법1
    if c1[p] == 0:
        c1[p] = c
    else:
        c2[p] = c
    # 방법2
    par[c] = p
# 루트 찾기
root = 1
while par[root] != 0:
    root += 1

preorder(1)
