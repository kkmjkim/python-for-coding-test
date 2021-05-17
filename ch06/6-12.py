n, k = map(int, input().split())

a = list(map(int, input().split()))  # n개 제한 안 두면 뒤에서 문제되지 않나?
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
