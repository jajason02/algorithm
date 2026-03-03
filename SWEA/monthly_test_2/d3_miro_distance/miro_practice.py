import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

# 델타 탐색
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


# 범위 체크
def border_check(i, j):
    if 0 <= i < N and 0 <= j < N:
        return 1
    return 0


# 너비 탐색
def bfs(si, sj):

    # 초기 값 큐에 넣기
    queue = [(si, sj, 0)]
    visited[si][sj] = 1
    # 큐가 빌 때 까지 반복
    while queue:
        ci, cj, dist = queue.pop(0)

        # 3을 찾으면 리턴
        if matrix[ci][cj] == 3:
            return dist - 1

        # 델타 탐색
        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]

            # 조건이 맞으면 큐에 다음 값 추가
            if border_check(ni, nj) and matrix[ni][nj] != 1 and not visited[ni][nj]:
                visited[ni][nj] = 1
                queue.append((ni, nj, dist + 1))

    return 0


for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # 시작 값 찾기
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                si, sj = i, j
                break

    print(f"#{tc} {bfs(si, sj)}")
