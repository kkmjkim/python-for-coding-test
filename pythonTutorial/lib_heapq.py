###########################################################################################
# PriorityQueue 라이브러리도 있지만 이게 더 빠름
# python의 heap은 기본적으로 min heap으로 구성되어 있음 -> 정렬 O(nlogn)밖에 안 됨
import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))  # heappop(list) -> pops the min
    return result

result = heapsort([4, 7, 5, 1, 3, 9])
print(result)

# max heap을 구현하고 싶다면 음수화 시켜서 하는 팁
def heapsort2(iterable):
    h = []
    result2 = []
    for value in iterable:
        heapq.heappush(h, -value)
    for _ in range(len(h)):
        result2.append(-heapq.heappop(h))
    return result2

result2 = heapsort2([4, 7, 5, 1, 3, 9])
print(result2)

###########################################################################################



