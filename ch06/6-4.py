# quick sort

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:  # if 0 or 1 element
        return
    pivot = start
    left = start + 1
    right = end

    while left < right:
        while left <= end and array[left] <= array[pivot]:
            # left가 end 넘어가도 직접 쓰이지 않아서 괜찮음
            left += 1
        while right > start and array[right] >= array[pivot]:
            # right이 pivot이 된 채로 끝나도 다음 loop에서 막혀서 괜찮음
            right -= 1
        if left > right:  # 엇갈릴 경우
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)

print(array)

# 평균적으로 O(NlogN)
# 최악의 경우(정렬 + 호어분할): O(N^2)
# 실제 대부분 언어의 기본 라이브러리는 피벗값을 설정하는 로직을 따로 더함
