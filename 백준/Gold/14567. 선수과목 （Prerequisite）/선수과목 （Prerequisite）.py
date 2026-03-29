"""
나의 생각: 위상정렬 큐로 풀어버린다 이번엔 절대로 안틀린다.
ai 도움: visited 없애고 while 탐색 안에서 degree가 0이 되는 순간,
바로 queue에 넣어버리기
for neighbor in (node[idx]): 에서 len(node[idx]) 쓰지말고 node[idx]로 실행
리스트 언패킹 print(*(semester[1:]))
"""

from collections import deque

N, M = map(int, input().split())
node = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)
semester = [0] * (N + 1)

# visited = [0] * (N + 1)
# visited[0] = 1

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
        # visited[idx] = 1
        for neighbor in (node[idx]):
            degree[neighbor] -= 1
            if degree[neighbor] == 0:
                queue.append(neighbor)
        semester[idx] = semester_idx
    
    # for n in range(1, N + 1):
    #     if not visited[n] and degree[n] == 0:
    #         queue.append(n)
    semester_idx += 1
# for neighbor in range(1, N + 1):
#     print(semester[neighbor],end=" ")
print(*(semester[1:]))
