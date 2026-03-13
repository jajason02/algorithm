import sys
import pprint
from collections import deque

sys.stdin = open("small_sample.txt", "r")

T = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

pipe = {
    0: [],
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2]
}
oppo = {0: 1, 1: 0, 2: 3, 3: 2}

def is_connected(d, next):
    if next == 0:
        return 0
    return oppo[d] in pipe[next]

def bfs(i, j, L):
    queue = deque([(i, j, 1)])
    visited[i][j] = 1
    count = 1

    while queue:
        i, j, curr_time = queue.popleft()

        if curr_time >= L:
            continue

        for d in pipe[tunnel_list[i][j]]:
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if is_connected(d, tunnel_list[ni][nj]):
                    visited[ni][nj] = 1
                    queue.append((ni, nj, curr_time + 1))
                    count += 1
    return count

for tc in range (1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel_list = [list(map(int, input().split())) for _ in range(N)]
    pprint.pprint(tunnel_list)
    
    visited = [[0] * M for _ in range (N)]
    pprint.pprint(visited)
    print(bfs(R, C, L))