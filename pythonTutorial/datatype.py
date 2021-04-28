a = 5
print(a, type(a))
a = -5
print(a, type(a))
a = 5.
print(a, type(a))
a = 5.3
print(a, type(a))
a = 1e-3
print(a, type(a))
a = 1E-3
print(a, type(a))
a = 2.43e4
print(a, type(a))

###########################################################################################
# 현대 컴퓨터 대부분 IEEE754 표준으로 부동소수점 방식 표현
a = 0.3 + 0.6
print(a) # == 0.89999999..
print(round(a, 1))

# 보통 코테에서는 4번째 자리로 반올림한 결과로 정답 인정
if round(a, 4) == 0.9:
    print(True)
    print("True")
else:
    print(False)

###########################################################################################
print(6 / 3) # '/' 연산은 기본적으로 실수형
print(7 // 3)
print(7 % 3)
print(2 ** 3)
###########################################################################################
# 리스트
# 파이썬에서 내부적으로 연결 리스트 -> append, remove 등등 가능
a = []
# a = list()
a.append(1) # returns None
a.append(2)
a.append("hello")
print(a)
print(a[2])
a.remove(2)
print(a)
a.remove(a[0])
print(a)

# a = [3, 5, 2, 4]
a = ["aaa", "fff", "ccc"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a = [3, 5, 2, 4]
a.reverse()
print(a)
a.insert(2, "hi")
print(a)

a = [0, 0, 1, 0, 1, 0, 1, 1]
num_ones = a.count(1) # returns int
print(num_ones)

# 다른 언어와 다르게 특정 원소 삭제 함수 없음. 그래서 이렇게
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} # set
result = [i for i in a if i not in remove_set]
print(result)

# n차원 리스트 초기화
n = 5
a = [0] * n
print(a)

# 인덱싱 & 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[1:3])
print(a[3:])
print(a[-4:-2])
print(a[3:1]) # []

a[1:3] = [0, 0, 0, 0]
print(a)

# 리스트 comprehension
array = [i for i in range(20) if i % 2 == 1]
print(array)
array = [i ** 2 for i in range(1, 10)]
print(array)

# n * m의 2차원 리스트 초기화 (반드시 comprehension 또는 일일이 할 것)
n = 3
m = 4
array = [[0] * m for _ in range(n)] # _ : 의미 없을 때 사용
print(array)
# array = [[i] * m for i in range(n)]
# print(array)

# 그렇지 않으면
array = [[0] * m] * n # 동일한 객체에 대한 m개 / n개 레퍼런스
print(array)

array[1][1] = 5
print(array)

array = [[0] * m for _ in range(n)]
# array = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
array[1][1] = 5
print(array)

###########################################################################################
# 문자열
data = "Don't you know \"Python?\""
print(data)
data = "Don't you know 'Python?'"
print(data)

a = "hello"
b = "world"
print(a + " " + b)
print(a, b)
print(a * 3)
print(a[0])
# a[0] = 'b' # error; not support assignment
print(a[:3])

###########################################################################################
# 튜플
# 원소 변경 불가하길 원할 때 사용 ex) 다익스트라 - 우선순위
# 리스트보다 공간 효율적
a = (1, 2, 3, 4)
print(a)
print(a[2])
# a[2] = 7 # error; no assignment

###########################################################################################
# 사전 자료형 (dictionary)
# 내부적으로 해시 테이블 사용 -> 검색, 수정 O(1)
data = dict()
data['사과'] = "apple"
data['바나나'] = "banana"
data['코코넛'] = "coconut"
print(data)
if '사과' in data:  # in은 iterable 자료형에 모두 사용 가능
    print("'사과'를 키로 가지는 데이터가 존재합니다.")
key_list = data.keys()
print(key_list)
value_list = data.values()
print(value_list)
for key in key_list:
    print(data[key])

###########################################################################################
# 집합 자료형 (set)
# data = {1, 1, 2, 3, 4, 4, 5}
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)
data = set("aabbccdef")
print(data)

a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
print(a | b)  # 합; 파이썬은 || 아님; "a or b" 안 됨
print(a & b)  # 교;
print(a - b)  # 차

a.add(5)
print(a)  # {1, 2, 3, 4, 5}
a.update({5, 6})
print(a)  # {1, 2, 3, 4, 5, 6}
a.update([6, 6, 7])
print(a)  # {1, 2, 3, 4, 5, 6, 7}
a.remove(3)  # multiple 불가
print(a)  # {1, 2, 4, 5, 6, 7}

###########################################################################################

