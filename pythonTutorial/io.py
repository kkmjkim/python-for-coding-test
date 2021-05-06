###########################################################################################
a = input("Enter a: ")
b = input("Enter b: ")
print(a, b)

a = int(input())  # string -> int; error if float input
print(a)
###########################################################################################
# 여러 개의 입력 받기 (띄어쓰기로 구분)
data = input().split()
print(data)

a, b = input().split()  # 딱 2개 입력해야함
print(a + b)  # string concat

# 정수 여러개 리스트로 받기 (자주 쓰이니까 알아두기)
data = list(map(int, input().split()))
data.sort(reverse=True)  # 내림차순
print(data)

# 정수 여러개 변수로 받기
a, b = map(int, input().split())  # 딱 2개 입력해야함
print(a, b)  # string concat
###########################################################################################
# 동작 속도가 빨라야 하거나 입력 데이터가 많으면 이렇게
import sys

data = sys.stdin.readline().rstrip()  # <class 'str'>
print(type(data), data[0])  # 12 3 4 -> 1

data = sys.stdin.readline().rstrip().split()  # <class 'list'>
print(type(data), data[0])  # 12 3 4 -> 12

data = input().split()  # <class 'list'>
print(type(data), data[0])  # 12 3 4 -> 12

# rstip(), lstrip(), strip()
data = sys.stdin.readline()
print(data, "<end>")
# 2 3
#  <end>
data = sys.stdin.readline().rstrip()
print(data, "<end>")
# 2 3 <end>

data = sys.stdin.readline()  # if starts with space, ' abc'
print("index 0:", data[0])  # prints space ' '
data = sys.stdin.readline().lstrip()  # strips spaces on the left ' abc' -> 'abc'
print("index 0:", data[0])  # 'a'

###########################################################################################
# output
answer = 7
# print("정답은 " + answer + "입니다.")  # error
print("정답은 " + str(answer) + "입니다.")
print("정답은", answer, "입니다.")  # 사이에 공백 출력됨 주의
print(f"정답은 {answer}입니다.")  # python 3.6 부터
###########################################################################################