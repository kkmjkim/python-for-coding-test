# quick sort (python-ish)
# 코드는 파이썬스럽고 깔끔하지만 조금 더 비효율적

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]

    left_side = [x for x in array[1:] if x <= pivot]
    right_side = [x for x in array[1:] if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
