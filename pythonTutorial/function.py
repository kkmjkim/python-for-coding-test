###########################################################################################
def subtract(a, b):
    print("함수릐 결과:", a - b)

subtract(b = 3, a = 5)  # 순서 바뀌어도 상관은 없음

###########################################################################################
# global variable
a = 0
b = 10
def func():
    a = 1  # local
    global b  # global
    b = 11  #

func()
print(a, b)  # 0, 11

###########################################################################################
# lambda express
print((lambda a, b: a+b)(3, 7))

# lambda랑 def는 정확히 같은 일
# use it when you want to use a function without assigning it (ch06)
result = lambda a, b: a + b
print(result(3, 7))
###########################################################################################


