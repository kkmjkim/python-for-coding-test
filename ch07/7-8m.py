n, m = map(int, input().split())
q = list(map(int, input().split()))
q.sort(reverse=True)  # max -> min

h = q[0]  # init H
total = 0  # current total length
while total < m:
    h -= 1
    j = 0
    while h < q[j]:
        total += 1
        j += 1
print(h)
