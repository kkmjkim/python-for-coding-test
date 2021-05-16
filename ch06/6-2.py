# insertion sort

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):  # 1, 2, 3.. 9
    for j in range(i, 0, -1):  # 1, 21, 321 ..
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)

# 2중 for문: O(N^2)
# 단, 최선의 경우 (정렬이 거의 되어있을 때): O(N)
