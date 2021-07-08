# 부품 찾기 - 집합 자료형으로 구현

n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print("yes", end=' ')
    else:
        print("no", end=' ')

# search는 list보다 set이 더 빠름 (hash)
