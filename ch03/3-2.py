import time

# # 사용자로부터 input 받기
# n, m, k = map(int, input("Enter N, M, K: ").split())
# data = list(map(int, input("Enter N elements: ").split()))

n = 1000
m = 10000
k = 5000
data = list(range(n))

tic = time.time()

data.sort()
first = data[n - 1]
second = data[n - 2]

###########################################################################################
# 1 (my shorter version)
count = int(m / (k + 1))
result = count * second
result += (m-count) * first

toc = time.time()

print(result, toc - tic)

###########################################################################################
# # or 2
# count = int(m / (k + 1)) * k
# count += m % (k + 1)
# result = count * first
# result += (m-count) * second
#
# toc = time.time()
#
# print(result, toc - tic)
#
###########################################################################################
