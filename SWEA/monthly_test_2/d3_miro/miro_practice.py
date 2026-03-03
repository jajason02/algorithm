import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


# 범위 체크
def border_check(i, j):
    if 0 <= i < N and 0 <= j < N:
        return 1
    return 0


# dfs 재귀탐색
def dfs(ci, cj):
    # 방문한 자리 표시
    visited[ci][cj] = 1
    # 3을 찾으면 1을 리턴
    if matrix[ci][cj] == 3:
        return 1
    
    # 델타 탐색
    for d in range(4):
        ni = ci + di[d]
        nj = cj + dj[d]
        # 범위 체크, 갈 수 있는지 체크
        if border_check(ni, nj) and matrix[ni][nj] != 1 and not visited[ni][nj]:
            # dfs가 3을 찾았으면 계속 1을 리턴
            if dfs(ni, nj):
                return 1
    return 0


for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    # 출발지점 찾기
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                si, sj = i, j
    # 방문 배열
    visited = [[0] * N for _ in range(N)]

    print(f"#{tc} {dfs(si, sj)}")
