# 3개 노드, 인접 리스
graph = [[] for _ in range(3)]

# 노드에 연결된 (노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))
graph[1].append((0, 7))
graph[2].append((0, 5))

print(graph)
