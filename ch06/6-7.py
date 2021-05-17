array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array = {3:"three", 6:"six", 1:"one"}
# array = {1, 4, 3, 2}
# array = "bdeac"

result = sorted(array)  # list, dictionary, set, string 모두 가능
# result = sorted(array.values())  # dictionary의 "value들을" 정렬 (기준으로 전체 정렬 X)

print(result)

# sorted(): 병렬 + 삽입 -> 최악: O(NlogN) 보장
