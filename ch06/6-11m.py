n = int(input())

array = []
# 참고로 딕셔너리는 sorted에서 key를 value로 설정 못함

for i in range(n):
    name, score = input().split()
    array.append((name, int(score)))

array = sorted(array, key=lambda data: data[1])

for student in array:
    print(student[0], end=' ')
