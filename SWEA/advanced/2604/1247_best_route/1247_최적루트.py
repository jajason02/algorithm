"""

순열 완전탐색
고객의 방문 순서를 모든 경우의 수로 탐색
회사 고객들(임의 순서) 집(도착) 의 최단 거리 계산
시간복잡도: O(N!)

"""

import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 고객의 수
    coords = list(map(int, input().split()))  # 좌표 입력 (x, y 쌍으로 들어옴)

    # 좌표 파싱: (x, y) 쌍으로 묶기
    # coords = [x1, y1, x2, y2, ..., xN, yN, 회사x, 회사y, 집x, 집y]
    points = [(coords[i], coords[i + 1]) for i in range(0, len(coords), 2)]

    # 고객 좌표, 회사 좌표, 집 좌표 분리
    customers = points[:N]       # 고객들의 좌표 리스트
    company = points[N]          # 출발지: 회사 좌표
    home = points[N + 1]         # 도착지: 집 좌표

    def manhattan(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    min_dist = float('inf')  # 최단 거리 초기값 (무한대)
    visited = [False] * N     # 각 고객 방문 여부 추적
    path = []                 # 현재 탐색 중인 방문 순서

    def dfs(path, visited, dist):
        """
        재귀 백트래킹으로 모든 순열 탐색
        - path   : 현재까지 방문한 고객 순서 리스트
        - visited: 각 고객 방문 여부 (True/False)
        - dist   : 현재까지 누적 이동 거리
        """
        global min_dist  # 외부 변수 min_dist를 재귀 안에서 수정

        # 모든 고객을 방문한 경우 → 마지막 고객에서 집까지 거리 추가
        if len(path) == N:
            total = dist + manhattan(path[-1], home)
            min_dist = min(min_dist, total)
            return

        # 아직 방문하지 않은 고객 탐색
        for i in range(N):
            if not visited[i]:
                visited[i] = True  # 방문 처리

                # 이전 위치 결정: path가 비어있으면 회사, 아니면 마지막 방문 고객
                prev = company if not path else path[-1]
                path.append(customers[i])

                # 다음 고객으로 재귀 호출 (누적 거리 전달)
                dfs(path, visited, dist + manhattan(prev, customers[i]))

                # 백트래킹: 방문 취소 후 다른 경우 탐색
                path.pop()
                visited[i] = False

    dfs(path, visited, 0)
    print(f"#{tc} {min_dist}")