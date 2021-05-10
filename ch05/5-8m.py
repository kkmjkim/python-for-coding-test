graph = [
    [2, 3, 8],
    [1, 7],
    [4, 5],
    [3, 5],
    [3, 4],
    [7],
    [6, 8],
    [1, 7]
]

visited = [False] * 8  # 상수 크기니까 미리 만들어놓는 게 나중에 search 시에 더 빠름

def dfs(visited, v):
    visited[v - 1] = True
    print(v, end=' ')
    for i in graph[v - 1]:
        if not visited[i - 1]:
            dfs(visited, i)

dfs(visited, 1)
