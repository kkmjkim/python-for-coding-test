n, m = map(int, input("Enter N, M: ").split())

graph = []
for i in range(n):
    graph.append(list(int(j) for j in input()))
result = 0

def dfs(graph, x, y):
    if (0 <= x <= n - 1) and (0 <= y <= m - 1):
        if not graph[x][y]:
            graph[x][y] = 1
            dfs(graph, x - 1, y)  # 상
            dfs(graph, x + 1, y)  # 하
            dfs(graph, x, y - 1)  # 좌
            dfs(graph, x, y + 1)  # 우
            return True
    return False

# walk through each element
for i in range(n):
    for j in range(m):
        if dfs(graph, i, j):
            result += 1

print(result)
