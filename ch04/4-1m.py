n = int(input())
plans = input().split()

DIR = ['L', 'R', 'U', 'D']
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in plans:
    nx = x + dx[DIR.index(i)]
    ny = y + dy[DIR.index(i)]

    if 1 <= nx <= n and 1 <= ny <= n:
        x = nx
        y = ny

print(x, y)
