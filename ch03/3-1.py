import time

n = int(input("거스름돈 금액:"))
count = 0

coins = [500, 100, 50, 10]

tic = time.time()

for coin in coins:
    count += n // coin
    n %= coin

toc = time.time()

print(count)
print("time:", toc - tic)  # faster && readable

# time complexity: O(k) where k = number of coin types
