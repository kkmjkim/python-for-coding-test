n = int(input("Enter N: "))

array = [int(input()) for _ in range(n)]
print(array)

# for lists, faster than sorted() b/c X create copy
array.sort(reverse=True)

for i in array:
    print(i, end=' ')
# print(" ".join(map(str, array)))
