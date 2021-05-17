n, k = map(int, input().split())

a = list(map(int, input().split()))[:n]  # 이렇게 안 하면 뒤에서 sort때문에 문제됨. k > n일 때도 그렇고.
b = list(map(int, input().split()))[:n]

# a의 최소를 b의 최대 숫자로 대체
a.sort()
b.sort(reverse=True)

# 이렇게 하면 안됨 (a 원소가 더 클 땐 X 바꿈)
# a[:k], b[:k] = b[:k], a[:k]

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

print(sum(a))
