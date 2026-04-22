"""
섬을 잇는 모든 간선을 연결하는 경우와 그 때의 환경 부담금을 가중치로
그래프를 생성.
이후 최소 신장 트리를 사용해서 최소 부담금을 구한다.
프림도 ㄱㄱ
"""
# import sys
# sys.stdin = open("small.txt")

T = int(input())

"""크루스칼 풀이
def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    rx, ry = find_set(x), find_set(y)
    if rx == ry:
        return False
    p[rx] = ry
    return True
    
for tc in range(1, T+1):
    N = int(input())  # N: 섬의 개수
    x_island = list(map(int, input().split()))  # 섬들의 x 좌표
    y_island = list(map(int, input().split()))  # 섬들의 y 좌표
    E = float(input())  # E: 환경 부담 세율

    connection = []
    node = []
    for i in range(N):
        for j in range(i + 1, N):
            tax = E * ((x_island[i]-x_island[j])**2 + (y_island[i]-y_island[j])**2)
            node.append([i, j, tax])

    node.sort(key=lambda x:x[2])
    p = [i for i in range(N)]
    cnt_node = 0
    sum_tax  = 0   

    for x, y, w in node:
        if union(x, y):
            cnt_node += 1
            sum_tax += w
            if cnt_node == N - 1:
                break
    print(f'#{tc} {round(sum_tax)}')
    """

# 프림 풀이
from heapq import heappush, heappop

for tc in range(1, T+1):
    N = int(input())  # N: 섬의 개수
    x_island = list(map(int, input().split()))  # 섬들의 x 좌표
    y_island = list(map(int, input().split()))  # 섬들의 y 좌표
    E = float(input())  # E: 환경 부담 세율

    node_lst = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            # tax = E * ((x_island[i]-x_island[j])**2 + (y_island[i]-y_island[j])**2)
            node_lst[i].append( j)
            node_lst[j].append( i)
    # print(node_lst)
    pq = []
    # 방문 배열
    visited = [0] * N
    # 정점 선택 횟수
    v_cnt = 0
    # 비용
    sum_tax = 0
    heappush(pq, (0, 0))
    # 선택한 정점의 개수가 섬의 개수와 같으면 탈출.
    while v_cnt < N and pq:
        w, v = heappop(pq)
        # v를 방문한 적 있으면 스킵
        if visited[v] != 0:
            continue
        # 방문처리
        visited[v] = 1
        # 선택횟수 + 1
        v_cnt += 1
        # 가중치 합
        sum_tax += w
        # v에서 갈 수 있는 정점들의 정보도 힙에 추가
        for nv in node_lst[v]:
            # 다음 정점이 간 적이 없어야 함
            if visited[nv] == 0:
                nw = E * ((x_island[v]-x_island[nv])**2 + (y_island[v]-y_island[nv])**2)
                heappush(pq, (nw, nv))
    print(f'#{tc} {round(sum_tax)}')