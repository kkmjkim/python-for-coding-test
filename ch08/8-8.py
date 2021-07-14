# pg. 226 - 효율적인 화폐 구성

N, M = map(int, input("Enter N, M: ").split())
values = [int(input()) for _ in range(N)]

d = [10001] * (M + 1)
d[0] = 0  # 이래야 뒤에서 d[2-2] + 1 할 때 1 만들수 있음

for i in range(N):
    for j in range(values[i], M+1):
        d[j] = min(d[j], d[j - values[i]] + 1)

if d[M] >= 10001:
    print(-1)
else:
    print(d[M])
