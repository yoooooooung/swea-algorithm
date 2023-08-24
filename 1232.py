# 사칙연산
import sys
sys.stdin = open("1232_input.txt")

for tc in range(1, 11):
    N = int(input())
    tree = [0]*(N+1)
    connect = [0]*(N+1)

    # print(f'#{tc}번째 케이스')

    for _ in range(N):
        # n은 정점 번호, node는 정점내 값, V는 연결된 간선
        n, node,  *V = input().split()
        n = int(n)
        # if tc == 1:
            # print(f'n:: {n}')
            # print(f'node:: {node}')
            # print(f'V:: {V}')
        # 연결된 간선 리스트
        if V:
            connect[n] = list(map(int, V))
        # print(f'connect:: {connect}')

        # tree 완성 (정점 위치에 값 넣기)
        if node in '+-/*':
            tree[n] = node
        else:
            # tree[n] = int(node)
            tree[n] = int(node)

    # print(f'tree:: {tree}')

    for i in range(N, 0, -1):
        if connect[i]:
            # print(f'{i}번째 정점은 연산자 :: {tree[i]}')
            if tree[i] == '+':
                tree[i] = tree[connect[i][0]] + tree[connect[i][1]]
            elif tree[i] == '-':
                tree[i] = tree[connect[i][0]] - tree[connect[i][1]]
            elif tree[i] == '/':
                # print(f'now:: {now} tree[now]::{tree[now]}')
                tree[i] = tree[connect[i][0]] / tree[connect[i][1]]
            elif tree[i] == '*':
                tree[i] = tree[connect[i][0]] * tree[connect[i][1]]



            # if tree[i] == '+':
            #     tree[i] = tree[connect[i][0]] + tree[connect[i][1]]
            # elif tree[i] == '-':
            #     tree[i] = tree[connect[i][0]] - tree[connect[i][1]]
            # elif tree[i] == '/':
            #     # print(f'now:: {now} tree[now]::{tree[now]}')
            #     tree[i] = tree[connect[i][0]] / tree[connect[i][1]]
            # elif tree[i] == '*':
            #     tree[i] = tree[connect[i][0]] * tree[connect[i][1]]


    print(f'#{tc} {int(tree[1])}')
