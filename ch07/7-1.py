# sequential search (순차 탐색)

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1


n, target = input("생성할 원소 개수를 입력한 다음 한 캄 띄고 찾을 문자열을 입력하세요.\n").split()
n = int(n)

array = input("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.\n").split()

sequential_search(n, target, array)
