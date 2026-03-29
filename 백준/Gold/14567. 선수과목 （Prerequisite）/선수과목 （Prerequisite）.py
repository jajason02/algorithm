"""
나의 생각: 위상정렬 큐로 풀어버린다 이번엔 절대로 안틀린다.
"""

from collections import deque

N, M = map(int, input().split())
node = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)
semester = [0] * (N + 1)
visited = [0] * (N + 1)
visited[0] = 1

for _ in range(M):
    u, v = map(int, input().split())
    node[u].append(v)
    degree[v] += 1

queue = deque()

for i in range(1, N + 1):
    if degree[i] == 0:
        queue.append(i)
semester_idx = 1

while queue:
    for _ in range (len(queue)):
        idx = queue.popleft()
        visited[idx] = 1
        for n in range(len(node[idx])):
            degree[node[idx][n]] -= 1
        semester[idx] = semester_idx
    
    for n in range(1, N + 1):
        if not visited[n] and degree[n] == 0:
            queue.append(n)
    semester_idx += 1
for n in range(1, N + 1):
    print(semester[n],end=" ")
