# Activity-selection Problem
# 회의실 배정하기

N = 10
a = [1, 4, 1, 6, 6, 10, 5, 7, 3, 8, 5, 9, 3, 5, 8, 11, 2, 13, 12, 14]
# 두개씩 짝을 지어 다시 저장
meet = [[0, 0]]
for i in range(N):
    meet.append([a[i*2], a[i*2+1]])
meet.sort(key=lambda x:x[1])     # 끝나는 시간 기준 오름차순 정렬

S = []  # 선택된 리스트
j = 0   # 활동의 종료시간이 필요

for i in range(1, N+1):
    if meet[i][0] >= meet[j][1]:    # 시작시간이 이전의 종료시간의 이후일때만 계산
        S.append(i)
        j = i                       # 
print(S)