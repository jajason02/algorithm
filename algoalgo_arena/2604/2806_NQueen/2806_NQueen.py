T = int(input())

def border_check(i, j):
    if 0 <= i < N and 0 <= j < N:
        return 1
    return 0

def dfs(ci, cj):
    global answer
    # 종료조건
    if ci == N:
        answer += 1
        return
    # 가지치기
    if visited[ci][cj]:
        return
    for i in range(ci):
        if border_check[i][cj-ci+i] and border_check[i][cj+ci-i] and not visited[i][cj-ci+i] and not visited[i][cj+ci-i]:
            continue
    
    for j in range(N):
        for n in range(N):
            visited[n][j] = 1
        dfs(ci + 1, j)
        for n in range(N):
            visited[n][j] = 0



for tc in range(1, T+1):
    N = int(input())
    
    matrix = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    answer = 0
    dfs(0, 0)
    print(f"#{tc} {answer}")
