###########################################################################################
# built-in functions
# no need to "import"

result = sum([1, 2, 3, 4])  # iterable
print(result)

minimum = min(5, 2, 4, 1)
maximum = max(5, 2, 4, 1)
print(minimum, maximum)

result = eval("(3 + 5) * 7")  # math in string
# result = eval("3 plus 4")  # error
print(result)

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

