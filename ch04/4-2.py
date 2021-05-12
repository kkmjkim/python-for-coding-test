h = int(input("Enter hour: "))

count = 0
for i in range(h + 1):  # 0 ~ h
    for j in range(60):  # 0 ~ 59
        for k in range(60):  # 0 ~ 59
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)