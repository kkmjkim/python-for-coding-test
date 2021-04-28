###########################################################################################
# itertools: deals with iterative data
# most useful classes in coding tests: permutation, combination
from itertools import permutations, combinations, product

data = ['A', 'B', 'C']  # 데이터 준비
result = list(permutations(data, 3))  # 모든 순열 구하기
print(result)

result = list(permutations(data, 2))  # # 2개를 뽑는 모든 순열 구하기 (중복 X)
print(result)
result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)

result = list(combinations(data, 2))  # 2개를 뽑는 모든 조합 구하기
print(result)
###########################################################################################



###########################################################################################



###########################################################################################

