
T = int(input())

di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

def border_check(i, j):
    if 0 <= i < N and 0 <= j < N:        return True
    return False

def dfs(ci, cj, d, cnt, lst):
    global max_cnt, si, sj

    if d == 3 and (ci, cj) == (si, sj):
        max_cnt = max(max_cnt, cnt)
        return
    
    for k in range(2):
        if d + k < 4:
            ni = ci + di[d + k]
            nj = cj + dj[d + k]
            if border_check(ni, nj) and not visited[ni][nj] and matrix[ni][nj] not in lst:
                visited[ni][nj] = 1
                lst.append(matrix[ni][nj])
                dfs(ni, nj, d + k, cnt + 1, lst + [matrix[ni][nj]])
                visited[ni][nj] = 0
                lst.remove(matrix[ni][nj])
        else: return


for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0]*N for _ in range (N)]
    max_cnt = -1

    for i in range(N-1):
        for j in range(1, N):
            si, sj = i, j
            dfs(si,sj, 0, 0, [])

    print(f"#{tc} {max_cnt}")


