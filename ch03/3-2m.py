import time

# # 사용자로부터 input 받기
# n, m, k = map(int, input("Enter N, M, K: ").split())
# data = list(map(int, input("Enter N elements: ").split()))

n = 1000
m = 10000
k = 5000
data = list(range(n))

tic = time.time()

# 가장 큰 수 2개 구하기 (연속만 아니면 되니까 2개를 적절히 번갈아가며 연산)
first = max(data)
data.remove(first)
second = max(data)

i = 0
result = 0
while i < m:
    if i % (k + 1) == k:
        result += second
    else:
        result += first
    i += 1

toc = time.time()

print(result, toc - tic)

# max() or sort()? -> https://stackoverflow.com/questions/35014951/why-is-max-slower-than-sort

###########################################################################################
# # 1
# first = data.pop(data.index(max(data)))
# second = max(data)

# # 2
# data.sort()
# first = data[n - 1]
# second = data[n - 2]

# # 3
# import heapq
# h = []
# for i in data:
#     heapq.heappush(h, -i)
# first = -heapq.heappop(h)
# second = -heapq.heappop(h)
###########################################################################################
