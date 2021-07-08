# 부품 찾기 - 계수 정렬로 구현

n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    # 각 부품은 고유한 번호가 있음
    if array[i] == 1:
        print("yes", end=' ')
    else:
        print("no", end=' ')