# 피보나치 수 - 점화식 (naive)
# 1 1 2 3 5 8 ..

def fibo(x):
    print(x, end=' ')
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)


print("fibo(5):", fibo(5))  # 5 4 3 2 1 2 3 2 1
