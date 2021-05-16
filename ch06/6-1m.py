# selection sort

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array) - 1):
    a = array[i]
    minimum = min(array[i+1:])
    index = array.index(minimum)
    if minimum < a:
        array[i] = minimum
        array[index] = a

print(array)
