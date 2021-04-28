###########################################################################################
# 이진탐색 - 시간 복잡도 O(logn)
# 정렬된 리스트에서 특정 원소 찾아야 할 때 유용
from bisect import bisect_left, bisect_right, bisect

a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))  # 순서 유지, 가능한 가장 왼쪽 인덱스
print(bisect_right(a, x))  # 순서 유지, 가능한 가장 왼쪽 인덱스 (bisect()와 동)
print(bisect(a, x))


def count_by_range(a, left_value, right_value):
    left_idx = bisect_left(a, left_value)
    right_idx = bisect_right(a, right_value)
    return right_idx - left_idx if right_idx - left_idx > 0 else 0

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 3, 4))  # 6개
print(count_by_range(a, 3, -1))  # 0

###########################################################################################