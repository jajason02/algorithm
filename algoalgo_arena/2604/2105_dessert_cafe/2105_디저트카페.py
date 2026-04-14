import sys
sys.stdin = open("sample_input.txt", "r")

# 델타배열(대각선방향)
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

# 가장자리 체크
def border_check(i, j):
    if 0 <= i < N and 0 <= j < N:
        return 1
    return 0
    

# dfs 탐색
# ci, cj: 현재 좌표
# lst: 여태 먹은 디저트 종류
# d: 현재 방향
def dfs(ci, cj, lst, d):
    global si, sj, ans
    # 방향이 3이고, 제자리로 돌아오면 종료
    if d == 3 and (ci, cj) == (si, sj):
        ans = max(ans, len(lst))
        return
    # 같은 종류의 디저트 있으면 가지치기
    # 계속 가거나 방향 전환
    for k in range(2):
        if d + k < 4:
            ni, nj = ci + di[d + k], cj + dj[d + k]
            if border_check(ni, nj) and matrix[ni][nj] not in lst:
                lst.append(matrix[ni][nj])
                dfs(ni, nj, lst, d + k)
                lst.remove(matrix[ni][nj])

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 가장 많은 디저트를 먹는 경우가 정답. 초기값 -1
    ans = -1
    # 모든 좌표에서 시작
    for i in range(N):
        for j in range(N):
            si, sj = i, j
            dfs(si, sj, [], 0)
    print(f'#{tc} {ans}')
    
