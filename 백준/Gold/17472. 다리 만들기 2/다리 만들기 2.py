"""
나의 생각: 일단 델타는 써서 해보자. 다음 위치에 닿을 때 까지 while을 써서 구현
dfs로 시작해봐야지. 간접 연결은 리스트에 connected를 만들어서 해봐야겠다
ai 아이디어: 최소 신장 트리(MST)와 대표 알고리즘 Kruskal을 사용해봐라
MST에서 내 set을 이용한 find로직은 1,2 연결 후 3,4 연결 시 2, 3연결을 무시해버린다.
다른로직을 사용해볼것
"""
# import pprint

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 델타 배열 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]



# 섬 별로 숫자 바꾸기
visited = [[0] * M for _ in range(N)]
island_num = 1

# 행렬 범위 체크 함수
def check_size(i, j):
    if 0 <= i < N and 0 <= j < M:
        return 1
    return 0

# dfs로 섬 별로 숫자 바꾸는 함수
def dfs(ci, cj, n):
    visited[ci][cj] = 1
    matrix[ci][cj] = n   
    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]
        if check_size(ni, nj) and not visited[ni][nj] and matrix[ni][nj] == 1:
            dfs(ni, nj, n)
# 만든 다리의 정보를 저장하는 리스트
bridge = [] 
# 완전 탐색으로 섬에 번호 지정   
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and not visited[i][j]:
            dfs(i, j, island_num)
            island_num += 1
            
# 놓을 수 있는 다리 완전 탐색
for i in range(N):
    for j in range(M):
        if matrix[i][j] != 0:
            start_idx = matrix[i][j]
            # 델타 탐색
            for d in range(4):
                length = 0
                ni, nj = i + di[d], j + dj[d]
                # matrix[ni][nj]가 다른 섬에 닿을 때까지 다리 생성
                while check_size(ni, nj) and matrix[ni][nj] == 0:
                    length += 1
                    ni, nj = ni + di[d], nj + dj[d]
                    if not check_size(ni, nj):
                        break
                if length >= 2 and check_size(ni, nj) and matrix[ni][nj] != start_idx:
                    bridge.append((length, start_idx, matrix[ni][nj]))
bridge.sort()
"""
내가 구현한 코드
connected = set()
min_len = 0

def find(a, b):
    if a in connected and b in connected:
        return 1
    return 0

while len(connected) < island_num-1:
    l, u, v = bridge.pop(0)
    if not find(u, v):
        connected = connected.union((u, v))
        min_len += l
print(min_len)
"""
# ai 로직
# 1. parent 리스트 초기화 (섬의 개수만큼)
# island_num이 섬의 개수 + 1이므로 range(island_num) 사용
parent = [i for i in range(island_num)]

# 2. Find 함수: 섬 x의 대장(Root)을 찾음
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 3. Union 함수: 두 섬 u, v를 하나의 그룹으로 합침
def union_parent(parent, u, v):
    root_u = find_parent(parent, u)
    root_v = find_parent(parent, v)
    if root_u < root_v:
        parent[root_v] = root_u
    else:
        parent[root_u] = root_v

# 4. MST 실행
total_len = 0
edges_count = 0 # 실제 선택된 다리의 개수

for l, u, v in bridge:
    # 두 섬의 대장이 다르면 (다른 그룹이면) 연결!
    if find_parent(parent, u) != find_parent(parent, v):
        union_parent(parent, u, v)
        total_len += l
        edges_count += 1

# 5. 최종 확인: 선택된 다리가 (섬 개수 - 1)개여야 모두 연결됨
# 섬의 실제 개수는 island_num - 1 임
actual_island_count = island_num - 1
if edges_count == actual_island_count - 1 and total_len != 0:
    print(total_len)
else:
    print(-1) # 모두 연결할 수 없는 경우

