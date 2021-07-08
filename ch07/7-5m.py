# 부품 찾기
import sys

N = int(input("Enter N: "))
inv = sys.stdin.readline().strip().split()
M = int(input("Enter M: "))
req = sys.stdin.readline().strip().split()

inv = sorted(inv)  # 계속 str 기준으로 정렬 -> "3" > "11

for i in req:
    start = 0
    end = len(inv) - 1
    while start <= end:
        mid = (start + end) // 2
        if inv[mid] == i:
            print("yes")
            break
        elif inv[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
    else:
        print("no")


