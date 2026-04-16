## 1949. 등산로 조성
> 메모리: 62848 kb  
> 실행 시간: 143 ms

```python
"""
나의 아이디어: K만큼 산을 깎는 것을 고려하는 것 보다
일단 등산로의 최장 루트를 찾는 것을 먼저 구현하기로 했다
당연히 DFS를 써야할 것 같았고 재귀를 통해 구현해볼 것이다.

구현까지는 쉽게 되었고 work라는 함수에 True, False를 넣어서
공사 유무를 넣어볼 것이다.


AI 활용 아이디어: 종료 조건을 어떻게 해야할지 계속 생각했는데
델타 탐색을 모두 완료했는데 재귀가 실행이 되지 않으면
자연스럽게 함수를 종료하면 된다는 힌트를 받을 수 있었다.

백트래킹을 위해 visited 행렬을 ni, nj로 저장하지 않고
ci, cj로 저장하는 아이디어를 얻었다

elif문을 사용해서 공사를 진행할 때 원래의 값을
임시로 temp 변수에 저장해두고 matrix의 값을 바꿔서
문제를 해결하는 아이디어를 얻었다.
공사는 한 번만 진행되기 때문에
temp 변수가 이중 호출 될 가능성이 없다는 것도 확인했다.
"""

T = int(input())

di = [-1, 0, 1, 0]                                                   # 델타탐색
dj = [0, 1, 0, -1]


def dfs(ci, cj, depth, work):
    global max_len

    visited[ci][cj] = 1                                             # 함수 시작 위치 저장

    if max_len < depth:
        max_len = depth

    for d in range(4):
        ni = ci + di[d]                                             # 4방향 탐색
        nj = cj + dj[d]
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:    # 이동 가능 범위, 탐색 여부 확인
            if matrix[ni][nj] < matrix[ci][cj]:
                dfs(ni, nj, depth + 1, work)                        # 재귀 시 깊이 + 1
            elif work and matrix[ni][nj] - K < matrix[ci][cj]:      # 공사를 하지 않았고 공사 시 갈 수 있는 길이면
                temp = matrix[ni][nj]                               # 현 위치 -1 만큼 공사를 진행 후 재귀 실행
                matrix[ni][nj] = matrix[ci][cj] - 1
                dfs(ni, nj, depth + 1, 0)                           # work를 0으로 바꾼다
                matrix[ni][nj] = temp

    visited[ci][cj] = 0                                             # 함수 종료 전 백트래킹


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_len = 0

    start_point = []                                                
    sp = max(max(row) for row in matrix)                            # 2차원 배열에서 최댓값 찾기

    for i in range(N):                                              # 최댓값이 있는 배열의 인덱스 튜플로 리스트에 저장
        for j in range(N):
            if matrix[i][j] == sp:
                start_point.append((i, j))

    for i, j in start_point:                                        # 튜플을 풀어서 함수 반복 실행
        dfs(i, j, 1, 1)
    print(f"#{tc} {max_len}")
```