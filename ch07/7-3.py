# binary search (이진 탐색) - 반복문

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid + 1
        elif array[mid] > target:
            start = mid + 1
        else:
            end = mid - 1
    return None


n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result:
    print(result)
else:
    print("원소가 존재하지 않습니다.")
