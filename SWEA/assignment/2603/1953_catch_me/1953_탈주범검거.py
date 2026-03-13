import sys

sys.stdin = open("sample_input.txt", "r")

from collections import deque

# 델타배열(상하좌우)
# 상하좌우로 델타배열을 쓰면 2로 나눈 나머지를 사용해 (상, 하), (좌, 우)를 묶기 편하네
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 터널의 종류에 따른 이동 가능 여부
types = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0],
}


# 너비기반 탐색
def bfs(R, C):
    # 시작위치 지정
    q = deque([(R, C)])
    visited[R][C] = 1

    while q:
        now_y, now_x = q.popleft()
        dirs = types[graph[now_y][now_x]]

        # 현재 좌표로부터 갈 수 있는 모든 노드 확인
        # 이동이 가능한 다음 좌표만 q에 추가
        for dir in range(4):
            # dir 방향이 막히면 continue
            if dirs[dir] == 0:
                continue

            # dir 방향으로 다음 좌표 확인
            ny = now_y + dy[dir]
            nx = now_x + dx[dir]

            # 행렬 범위 체크
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            # 방문여부 체크
            if visited[ny][nx]:
                continue

            # 다음 위치의 값이 0이면 못감
            if graph[ny][nx] == 0:
                continue

            # 다음 위치의 입구 확인
            next_dirs = types[graph[ny][nx]]

            # dir이 상, 좌 방향이면 반대쪽이 하, 우가 뚫려야 함
            if dir % 2 == 0 and next_dirs[dir + 1] == 0:
                continue

            # dir이 하, 우 방향이면 반대쪽이 상, 좌가 뚫려야 함
            if dir % 2 == 1 and next_dirs[dir - 1] == 0:
                continue

            # 주어진 시간을 벗어나면 안봄
            if visited[ny][nx] + 1 > L:
                continue

            # 시간을 + 1 누적하면서 갈 수 있는 위치를 큐에 저장
            visited[ny][nx] = visited[now_y][now_x] + 1
            q.append((ny, nx))


T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    bfs(R, C)
    cnt = 0

    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

    print(f"#{tc} {cnt}")
