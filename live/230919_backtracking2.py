# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 부붅비합중 원소 합이 10인 부분집합을 모두 출력하시오

arr = [i for i in range(1, 11)]
path = []

def backtracking(cnt):
    if sum(path) > 10:
        return
    elif sum(path) == 10:
        print(*path)
    else:
        for num in arr:
            if num in path:
                continue
            path.append(num)
            backtracking(cnt+1)
            path.pop()

backtracking(0)