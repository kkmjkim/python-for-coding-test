# counting sort

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)  # min이 0이 아닐 때는 메모리 낭비?

for i in range(len(array)):
    count[array[i]] += 1
print("count:", count)

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

# 범위가 제한적인 정수 리스트라면 매우 빠름: O(N+K)
# 특히 데이터가 고르게 분포해 있거나 중복되는 원소가 많을 때
