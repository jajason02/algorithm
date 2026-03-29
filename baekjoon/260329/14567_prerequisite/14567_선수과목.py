"""
나의 생각: 위상정렬 큐로 풀어버린다 이번엔 절대로 안틀린다.
ai 도움: visited 없애고 while 탐색 안에서 degree가 0이 되는 순간,
바로 queue에 넣어버리기
for neighbor in (node[idx]): 에서 len(node[idx]) 쓰지말고 node[idx]로 실행
리스트 언패킹 print(*(semester[1:]))
"""

from collections import deque

N, M = map(int, input().split())
# 인덱스 별 하위 노드 리스트 각 노드에서 출발하는 간선 인덱스
node = [[] for _ in range(N + 1)]
# 진입 차수 리스트 각 노드로 들어오는 간선 수
degree = [0] * (N + 1)
# 수강한 학기 저장 리스트
semester = [0] * (N + 1)

# visited 리스트 제거 후 큐 저장 알고리즘 수정
# visited = [0] * (N + 1)
# visited[0] = 1

# 입력값 저장
for _ in range(M):
    u, v = map(int, input().split())
    node[u].append(v)
    degree[v] += 1

queue = deque()

# 최초 출발 노드 탐색(degree[i] 진입 차수가 0이면 출발 노드)
for i in range(1, N + 1):
    if degree[i] == 0:
        queue.append(i)

# 학기 인덱스
semester_idx = 1


# queue가 빌 때 까지 반복
while queue:
    for _ in range(len(queue)):
        # queue에서 pop한 subject 과목 수강하기
        subject = queue.popleft()
        # subject 노드로부터 뻗어져 나온 간선의 진입 차수를 1 깎는다
        for neighbor in node[subject]:
            degree[neighbor] -= 1
            # 진입차수가 0이 되면 queue에 해당 노드 push
            if degree[neighbor] == 0:
                queue.append(neighbor)
        # 수강 리스트에 subject 과목 추가
        semester[subject] = semester_idx

    # visited를 사용한 최초 코드
    # for n in range(1, N + 1):
    #     if not visited[n] and degree[n] == 0:
    #         queue.append(n)
    
    # queue 반복 실행 후 학기 인덱스 1 증가
    semester_idx += 1

# 리스트 언패킹 하지 않은 출력
# for neighbor in range(1, N + 1):
#     print(semester[neighbor],end=" ")
print(*(semester[1:]))
