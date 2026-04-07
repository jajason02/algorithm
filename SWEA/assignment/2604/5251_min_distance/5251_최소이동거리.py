import heapq  # 우선순위 큐를 위한 모듈 (가장 거리가 짧은 노드를 효율적으로 추출)
import sys

def dijkstra(n, graph):
    # 1. 출발점에서 각 지점까지의 최단 거리를 저장할 배열 (Distance Array)
    # 초기값은 INF(Infinite)로 설정하여 갱신 여부를 판별
    inf = float('inf')
    D = [inf] * (n + 1)
    
    # 2. 시작점(0번 지점) 초기화
    D[0] = 0
    # 우선순위 큐 (Heap) 생성: (거리, 지점) 형태로 저장하여 거리가 짧은 순으로 정렬
    pq = [(0, 0)]

    while pq:
        # 3. 현재 가장 누적 거리가 짧은 노드 정보를 꺼냄
        cur_dist, cur_node = heapq.heappop(pq)

        # 4. 가지치기(Optimization): 
        # 이미 처리된 적이 있고, 현재 꺼낸 거리보다 더 짧은 경로를 알고 있다면 스킵
        if D[cur_node] < cur_dist:
            continue

        # 5. 인접한 노드들을 확인하며 거리 갱신 (Relaxation)
        for neighbor, weight in graph[cur_node]:
            distance = cur_dist + weight
            
            # 현재 노드를 거쳐서 인접 노드로 가는 게 더 빠르다면 갱신 후 큐에 삽입
            if distance < D[neighbor]:
                D[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return D[n]

T = int(input())
for tc in range(1, T + 1):
    # N: 마지막 지점 번호, E: 도로의 개수
    N, E = map(int, input().split())
    
    # 지점이 0부터 N까지이므로 N+1개의 빈 리스트 생성
    adj_list = [[] for _ in range(N + 1)]
    
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj_list[u].append((v, w))  # 유향 그래프(단방향)이므로 한쪽만 추가
        
    result = dijkstra(N, adj_list)
    print(f"#{tc} {result}")