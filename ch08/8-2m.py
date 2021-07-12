# # 피보나치 수 - 동적계획법 (memoization, 탑다운)
# # 1 1 2 3 5 8 ..

def fibo(x):
    d = [0] * 100

    if x == 1 or x == 2:
        d[x - 1] = 1

    # 얘가 먼저 나와버리면 fibo(0), fibo(-1)을 호출하게 돼서
    if d[x - 1] == 0:
        d[x-1] = fibo(x-1) + fibo(x-2)

    # 세팅 위에서 다 하고 밑에서 반환
    return d[x - 1]


print(fibo(50))
