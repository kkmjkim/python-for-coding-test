###########################################################################################
# list는 기본적으로 가장 뒷쪽 우너소를 기준으로 append()나 pop()함
# 따라서 가장 앞 우너소를 다룰 때에는 시간 복잡도가 높아질 수 있음
# ex) 리스트 가장 앞쪽 원소 추가 O(n); deque로는 O(1)
from collections import deque, Counter

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
print(data)
print(list(data))  # -> list

counter = Counter(['red', 'blue', 'red', 'green'])
print(counter['red'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))  # -> dict


###########################################################################################



###########################################################################################