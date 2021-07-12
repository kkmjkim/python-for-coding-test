# pg. 217 - 1로 만들기

X = int(input("Enter integer X: "))

# X+1개 초기화 (index 편하게)
d = [0] * (X+1)

for i in range(2, X+1):
    # 일단 이렇게 해놓고
    d[i] = d[i-1] + 1
    # 2로 나눠지는 선택지도 있다면
    if i % 2 == 0:
        d[i] = min(d[i-1], d[i//2] + 1)
    # 3으로 나눠지는 선택지도 있다면
    if i % 3 == 0:
        d[i] = min(d[i-1], d[i//3] + 1)
    # 5로 나눠지는 선택지도 있다면
    if i % 5 == 0:
        d[i] = min(d[i-1], d[i//5] + 1)

print(d[X])
