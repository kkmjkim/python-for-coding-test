#### 얕은 복사 #############################################################################

# list의 얕은 복사 (mutable)
a = [0, 1, 2, 3]
b = a  # 같은 메모리 가리키는 상황
print(id(a), id(b))  # same
print(id(a[0]), id(b[0]))  # same - 당연히 값이 같으니까
b[0] = 5  # 같은 주소 가리키는 상황이었기 때문에 a도 수정됨
print(a, b)  # same
print(id(a), id(b))  # same
b = [5, 1, 2, 3]  # 새로운 리스트 객체 생성한 것임
print(id(a), id(b))  # diff


# str의 얕은 복사 (immutable)
a = "abc"
b = a  # 같은 메모리 가리키는 상황
print(id(a), id(b))  # same
b = 'def'  # 원래 같은 주소였지만 string은 immutable이라서 따로 할당됨
print(a, b)  # abc def
print(id(a), id(b))  # diff


# list의 얕은 복사 (mutable) - advanced
a = [1, 2, 3]
b = a[:]  # 이것도 얕은 복사 (내용만 복사해옴 -> 객체는 다른 주소)
print(id(a), id(b))  # diff
print(id(a[0]), id(b[0]))  # same -> 당연히 값이 같으니까
b[0] = 5  # 애초에 a랑 전혀 무관하던 사이
print(a, b)  # [1, 2, 3] [5, 2, 3]

a = [[1, 2], [3, 4]]
b = a[:]  # 얕은 복사 (내용만 복사해옴 -> 다른 주소)
print(id(a), id(b))  # diff
print(id(a[0]), id(b[0]))  # same -> 당연히 값이 같으니까
a[0] = [8, 9]
print(a, b)  # diff
print(id(a[0]), id(b[0]))  # diff -> 당연히 값이 다르니까
# 이 상태에서 a[1].append(5) 하면 b[1]에도 영향이 갈까?
# 당연히 yes. a[1]과 b[1]의 메모리 주소는 같았을 것이고 list는 mutable이니까 다른 주소가 할당되지 않음
print(id(a[1]), id(b[1]))  # same
a[1].append(5)
print(b)  # [[1, 2], [3, 4, 5]]

import copy
a = [[1, 2], [3, 4]]
b = copy.copy(a)  # 얘도 얕은 복사 (값만 복사)
print(id(a), id(b))  # diff
print(id(a[0]), id(b[0]))  # same
a[0][1] = 9  # a[0], b[0] 주소는 같아서
print(a, b)  # same
a[0] = [5, 6]  # a, b 주소는 달라서
print(a, b)  # diff


#### 깊은 복사 #############################################################################
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)  # 깊은 복사: 내부 객체들까지 모두 "새롭게" copy됨
print(id(a), id(b))  # diff
print(id(a[0]), id(b[0]))  # diff
print(id(a[0][0]), id(b[0][0]))  # same -> 값이 같으니까
a[0][0] = 5
print(a, b)  # diff -> 위에서 뭘 하든 다 diff


#### 참고 #############################################################################
a = [[0] * 3] * 4
print(id(a[0]), id(a[1]))  # same
a = [[0] * 3 for _ in range(4)]
print(id(a[0]), id(a[1]))  # diff
