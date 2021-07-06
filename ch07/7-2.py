# binary search (이진 탐색) - 재귀 함수

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid+1
    elif array[mid] > target:
        end = mid - 1
        return binary_search(array, target, start, end)
    else:
        start = mid + 1
        return binary_search(array, target, start, end)


n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result:
    print(result)
else:
    print("원소가 존재하지 않습니다.")
