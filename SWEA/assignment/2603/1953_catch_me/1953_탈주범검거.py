import sys
from collections import deque
sys.stdin = open("sample_input.txt", "r")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

types = 

def bfs(R, C):
    q = deque([R, C])
    visited[R][C] = 1

    while q:
        now_y, now_x = q.popleft()
        dirs = types[graph[now_y][now_x]]

        for dir in range(4):
            
            if dirs[dir] == 0:
                continue
            
            ny = now_y + dy[dir]
            nx = now_x + dx[dir]

            if ny < 0 or ny >= N or nx < 0 or nx > M:
                continue

            if visited[ny][nx] == 0:
                continue

            if graph[ny][nx] == 0:
                continue

            next_dirs = types[graph[ny][nx]]

            if dir % 2 == 0 and next_dirs[dir + 1] == 0:
                continue
            
            if dir % 2 == 1 and next_dirs[dir - 1] == 0:
                continue

            if visited[ny][nx] + 1 > L:
                continue

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

