array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

# sorted(key)
result = sorted(array, key=setting)
# result = sorted(array, key=lambda data : data[1])
print(result)

# sort(key)
array.sort(key=setting)
# array.sort(key=lambda data : data[1])
print(array)
