import time

n = int(input("거스름돈 금액: "))  # 총 거스름돈 (10의 배수)
count = 0  # 총 동전 개수

tic = time.time()

if n >= 500:
    count += n // 500
    n %= 500
if n >= 100:
    count += n // 100
    n %= 100
if n >= 50:
    count += n // 50
    n %= 50
if n > 0:
    count += n // 10

toc = time.time()

print(count)
print("time:", toc - tic)