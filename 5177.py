# 이진 합
import sys
sys.stdin = open("5177_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    print(arr)
    # 부모가 자식보다 작은 수 여야함. (부모 인덱스 = n//2)
