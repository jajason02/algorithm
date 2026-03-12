# import sys

# sys.stdin = open("sample_input.txt", "r")

T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def border_check(i, j):
    if 0 <= i < N and 0 <= j < N:
        return True
    return False

def dfs(ci, cj, route, worked):
    global max_route
    visited[ci][cj] = 1

    if max_route < route:
        max_route = route

    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]        

        if border_check(ni, nj) and not visited[ni][nj]:
            if matrix[ni][nj] < matrix[ci][cj]:
                dfs(ni, nj, route + 1, worked)

            elif worked == 0 and matrix_copy[ni][nj]-K < matrix_copy[ci][cj]:
                temp = matrix[ni][nj]                              
                matrix[ni][nj] = matrix[ci][cj] - 1
                dfs(ni, nj, route + 1, worked + 1)                           
                matrix[ni][nj] = temp

    
    visited[ci][cj] = 0

for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    matrix_copy = matrix
    visited = [[0] * N for _ in range(N)]
    max_route = 0

    max_height = 0
    for i in range(N):
        for j in range(N):
            max_height = max(max_height, matrix[i][j])
    start = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == max_height:
                start.append((i, j))

    for i, j in start:
        dfs(i, j, 1, 0)
    
    print(f"#{tc} {max_route}")
        