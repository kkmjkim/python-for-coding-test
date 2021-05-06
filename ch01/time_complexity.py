from random import randint
import time

array = []
for _ in range(10000):
    array.append(randint(1, 100))

start_time = time.time()

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    # in python, we swap like this:
    array[i], array[min_index] = array[min_index], array[i]

end_time = time.time()
print("선택 정렬:", end_time - start_time)  # approx. 33s

array = []
for _ in range(10000):
    array.append(randint(1, 100))

start_time = time.time()

array.sort()

end_time = time.time()

print("기본 라이브러리: ", end_time - start_time)  # 0.0012s