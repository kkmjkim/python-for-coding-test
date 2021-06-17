###########################################################################################
# list는 기본적으로 가장 뒷쪽 원소를 기준으로 append()나 pop()함
# 따라서 가장 앞 원소를 다룰 때에는 시간 복잡도가 높아질 수 있음
# ex) 리스트 가장 앞쪽 원소 추가 O(n)
# 하지만 deque로는 O(1); 왜냐하면 deque는 양방향;
# "덱"이라고 발음

from collections import deque, Counter

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
print(data)  # deque([1, 2, 3, 4, 5])
print(list(data))  # [1, 2, 3, 4, 5]
data.reverse()
print(data)  # deque([5, 4, 3, 2, 1])

data.pop()
print(list(data))  # [5, 4, 3, 2]
data.popleft()
print(list(data))  # [4, 3, 2]


counter = Counter(['red', 'blue', 'red', 'green'])
print(counter['red'])  # 2
print(counter['blue'])  # 1
print(counter['green'])  # 1
print(dict(counter))  # {'red': 2, 'blue': 1, 'green': 1}
###########################################################################################