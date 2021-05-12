hour = int(input("Enter hour: "))
count = 0
MIN, SEC = 60, 60

for i in range(int(hour) + 1):  # 0 ~ H
    for j in range(MIN):  # 0 ~ 59
        for k in range(SEC):  # 0 ~ 59
            if '3' in str(i) or '3' in str(j) or '3' in str(k):  # str concat으로 개선
                count += 1

print(count)
