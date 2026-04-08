import sys
sys.stdin = open("sample_input.txt", "r")

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())

def start_point():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == "X":
                return (i, j)
                

def dfs(ci, cj, dir, cut, ctrl):
    global min_ctrl
    # 종료조건
    if matrix[ci][cj] == "Y":
        min_ctrl = min(min_ctrl, ctrl)
        return    
    # 가지치기
    if ctrl > min_ctrl:
        return
    # 재귀
    for d in range(4):
        ni, nj = ci + di[(dir + d) % 4], cj + dj[(dir + d) % 4]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            if matrix[ni][nj] == "T" and cut > 0:
                matrix[ni][nj] = "G"
                visited[ni][nj] = 1
                if d == 0:
                    dfs(ni, nj, (dir + d) % 4, cut-1, ctrl + 1)
                elif d == 2:
                    dfs(ni, nj, (dir + d) % 4, cut-1, ctrl + 3)
                else:
                    dfs(ni, nj, (dir + d) % 4, cut-1, ctrl + 2)
                visited[ni][nj] = 0
                matrix[ni][nj] = "T"
            if matrix[ni][nj] != "T":
                visited[ni][nj] = 1
                if d == 0:
                    dfs(ni, nj, (dir + d) % 4, cut, ctrl + 1)
                elif d == 2:
                    dfs(ni, nj, (dir + d) % 4, cut, ctrl + 3)
                else:
                    dfs(ni, nj, (dir + d) % 4, cut, ctrl + 2)
                visited[ni][nj] = 0
            

for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    # print(visited)
    si, sj = start_point()
    # 정답
    min_ctrl = 1e8
    dfs(si, sj, 0, K, 0)
    if min_ctrl == 1e8:
        min_ctrl = -1
    print(f"#{tc} {min_ctrl}")