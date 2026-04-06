# import sys
# sys.stdin = open("sample_input.txt", "r")
from collections import deque


T = int(input())


def bfs():
    dq = deque()
    dq.append((N, 1))
    visited = [0] * 1000000
    visited[N] = 1
    while dq:
        n, t = dq.popleft()
        if n + 1 == M:
            return t
        else:
            if 0 < n + 1 < 1000000 and not visited[n + 1]:
                visited[n + 1] = 1
                dq.append((n + 1, t + 1))
        if n - 1 == M:
            return t
        else:
            if 1000000 > n - 1 > 0 and not visited[n - 1]:
                visited[n - 1] = 1    
                dq.append((n - 1, t + 1))
        if n * 2 == M:
            return t
        else:
            if 0 < n * 2 < 1000000 and not visited[n * 2] :
                visited[n * 2] = 1
                dq.append((n * 2, t + 1))
        if n - 10 == M:
            return t
        else:
            if 1000000> n - 10 > 0 and not visited[n - 10]:
                visited[n - 10] = 1
                dq.append((n - 10, t + 1))


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    answer = bfs()
    print(f"#{tc} {answer}")
