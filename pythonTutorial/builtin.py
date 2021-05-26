###########################################################################################
# built-in functions
# no need to "import"

# sum()
result = sum([1, 2, 3, 4])  # iterable
print(result)

# min()
minimum = min(5, 2, 4, 1)
maximum = max(5, 2, 4, 1)
print(minimum, maximum)

# eval()
result = eval("(3 + 5) * 7")  # math in string
# result = eval("3 plus 4")  # error
print(result)

# sorted()
result = sorted([3, 7, 6, 4, 1, 1])  # iterable
print(result)
result = sorted([3, 7, 6, 4, 1, 1], reverse=True)
print(result)

result = sorted([('홍길동, 35'), ('이순신, 75'), ('아무개, 50')], key=lambda x: x[1])
print(result)
result = sorted([('홍길동, 35'), ('이순신, 75'), ('아무개, 50')], key=lambda x: x[1], reverse=True)
print(result)

# 근데 사실 list는 sort() 내장
data = [9, 5, 2, 8, 3]
data.sort()
print(data)

###########################################################################################
# map()
# 리스트의 요소를 지정된 함수로 처리해줌 (새 리스트를 생성)
array = [1.2, 3.33, 4.0, 6.43]
array2 = map(int, array)  # map object (iterator)
print(array2)

# iterator 라서 unpacking 가능
a, b, c, d = array2
print(a, b, c, d)
toList = list(map(int, array))
print(toList)

# with lambda
print(list(map(lambda i: i + 2, toList)))


# zip()
# aggregates elements from each of the iterables
list1 = [1, 2, 3]
list2 = ['aa', 'bb', 'cc']
list3 = [150, 160, 158, 188]
print(zip(list1, list2, list3))  # zip object
toList = list(zip(list1, list2, list3))
print(toList)  # [(1, 'aa', 150), (2, 'bb', 160), (3, 'cc', 158)]

# with for loop
for id, name in zip(list1, list2):
    id += 10
    print(id, name)

# dictionary 에 사용하기 좋음
dict = {id:name for id, name in zip(list1, list2)}
print(dict)

# transpose 2d array(matrix)
mat = [[1, 2, 3],
       [4, 5, 6]]
mat_t = list(zip(*mat))  # b/c list of lists
print(mat_t)  # [(1, 4), (2, 5), (3, 6)]


# iter(), next()
# returns an iterator object
import random
it = iter(lambda : random.randint(0, 5), 4)
print(next(it, 999))  # X raise StopIteration
print(next(it, 999))
print(next(it, 999))

for i in iter(lambda : random.randint(0, 5), 4):
    print(i, end=' ')  # 3 1 2 2 0 3 5

###########################################################################################

