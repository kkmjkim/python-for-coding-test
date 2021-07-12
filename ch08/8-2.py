# # 피보나치 수 - 동적계획법 (memoization, 탑다운)
# # 1 1 2 3 5 8 ..

def fibo(x):
    d = [0] * 100

    if x == 1 or x == 2:
        return 1

    # 이미 계산된 적이 있다면
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x - 1) + fibo(x - 2)

    return d[x]

print(fibo(99))
