# 서로소 집합
# make set 과정 : 집합을 만들어 주는 과정
# 각 요소가 가리키는 값이 부모
parent = [i for i in range(10)]

# find-set 과정
def find_set(x):
    if parent[x] == x:
        return x
    return find_set(parent[x])


# union 과정
def union(x, y):
    # 1. 이미 같은 집합인지 체크
    x = find_set(x)
    y = find_set(y)

    # 대표자가 같으니, 같은 집합이다.
    if x == y:
        print('싸이클이 발생')
        return

    # 2. 다른 집합이라면, 같은 대표자로 수정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

union(0, 1)

union(2, 3)

union(1, 3)     # 이렇게 하면 대표가 바뀜

union(0, 2)     # 싸이클이 발생 (이미 같은 집합에 속해 있는 원소를 한번 더 union)

print(find_set(2))
print(find_set(3))

# 같은 그룹인지 판별

t_x = 0
t_y = 1

if find_set(t_x) == find_set(t_y):
    print(f'{t_x}와 {t_y}는 같은 집합에 속해 있습니다.')
else:
    print(f'{t_x}와 {t_y}는 다른 집합에 속해 있습니다.')
