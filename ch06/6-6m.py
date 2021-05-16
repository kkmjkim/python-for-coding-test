# counting sort

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

minimum = min(array)

count = [0] * (max(array) - minimum + 1)  # 공간 낭비 없음

for i in array:
    count[i - minimum] += 1
print("count:", count)

for i in range(len(count)):
    for j in range(count[i]):
        print(minimum + i, end=' ')
