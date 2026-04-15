# 서로소 집합(Union-Find)

* **두 원소가 같은 집합에 속해 있는지 확인하기 위한 자료구조.**

> 처음엔 전부 개인  
> 
> 1번, 2번, 3번, 4번, 5번 → 각자 혼자  
> 
> "1번이랑 2번 같은 반"  → union(1, 2)  
> "2번이랑 3번 같은 반"  → union(2, 3)  
>  
> 그럼 1,2,3은 전부 같은 반  
> 
> "1번이랑 3번 같은 반이야?" → find(1) == find(3) → YES  
> "1번이랑 4번 같은 반이야?" → find(1) != find(4) → NO  

## 코드 구현
```python
# 처음 세팅. 모두 자기 자신이 대표
p = [i for i in range(N + 1)]

# 내 대표를 찾는 함수(경로 압축)
def find_set(x):
    # 자기자신의 인덱스와 대표가 같은 수를 찾을 때 까지 반복
    if x != p[x]:
        return find_set(p[x])
    return x


# 두 집합 합치기 (랭크 사용)
rank = [0] * (N+1)

def union(x, y):
    king_x = find_set(x)
    king_y = find_set(y)

    # 합칠때 작은 집합(깊이가 작음)을 큰 집합에 합친다.
    if rank[king_x] > rank[king-y]:
        p[king-y] = king_x
    else:
        p[king_x] = king_y
        if rank[king_x] == rank[king_y]:
            rank[king_y] += 1
```    
    

# 최소신장트리(MST)

* 신장 트리: N개의 정점으로 이루어진 무방향 그래프에서 N개의 정점과 N-1개의 간선으로 이루어진 트리.
* **최소 신장 트리(MST, Minimum Spanning Tree)**: 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치 합이 최소인 신장트리.


## Prim 알고리즘

```python
import heapq
import sys
input = sys.stdin.readline

# 정점, 간선 수 입력
V, E = map(int, input().split())

# 인접 리스트 구성 (양방향)
graph = [[] for _ in range(V + 1)]
# u, v: 정점
# w: 가중치(가중치 기준으로 정렬하기 위해 앞에 둠)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

def prim(start):
    visited = [False] * (V + 1)
    
    # 우선순위 큐 (가중치, 노드)
    pq = [(0, start)]
    # 가중치의 합
    mst_cost = 0

    # pq가 빌 때 까지
    while pq:
        w, node = heapq.heappop(pq)  # 가장 싼 간선 꺼냄

        if visited[node]:  # 이미 방문한 노드 스킵
            continue

        visited[node] = True
        mst_cost += w

        # 현재 노드에서 뻗어나갈 수 있는 간선 추가
        for next_w, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(pq, (next_w, next_node))

    return mst_cost

print(prim(1))
```

## Kruskal 알고리즘

```python
import sys
input = sys.stdin.readline

V, E = map(int, input().split())

# 간선 정보 저장 (가중치, 출발, 도착)
edges = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

# 핵심 1: 가중치 기준 오름차순 정렬
edges.sort()

# Union-Find 초기화
p = [i for i in range(V + 1)]
rank = [0] * (V + 1)

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])  # 경로 압축
    return p[x]

def union(x, y):
    king_x = find_set(x)
    king_y = find_set(y)

    if king_x == king_y:  # 사이클 감지 → 스킵
        return False

    # 랭크 기반 union
    if rank[king_x] > rank[king_y]:
        p[king_y] = king_x
    else:
        p[king_x] = king_y
        if rank[king_x] == rank[king_y]:
            rank[king_y] += 1
    return True

# MST 구성
mst_cost = 0
edge_count = 0

for w, u, v in edges:
    if union(u, v):          # 사이클 없으면 추가
        mst_cost += w
        edge_count += 1
    if edge_count == V - 1:  # 간선 V-1개 완성
        break

print(mst_cost)
```


## Dijkstra 알고리즘