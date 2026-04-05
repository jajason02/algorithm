from collections import deque
# import sys
# import pprint

# sys.stdin = open("sample_input.txt", "r")

T = int(input())

# 델타배열 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

tunnel = {
    1:[1, 1, 1, 1],
    2:[1, 0, 1, 0],
    3:[0, 1, 0, 1],
    4:[1, 1, 0, 0],
    5:[0, 1, 1, 0],
    6:[0, 0, 1, 1],
    7:[1, 0, 0, 1]
}


for tc in range (1, T+1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    queue = deque()
    queue.append((R, C))
    visited = [[0]*M for _ in range(N)]
    visited[R][C] = 1
    # 맨홀 뚜껑 위치부터 시작, 시간마다 1 칸씩 이동
    for time in range(1, L+1):
        # 큐에서 값을 팝해서 다음 시간에 이동할 수 있는곳 확인
        temp = []
        while queue:    
            ci, cj = queue.popleft()
            visited[ci][cj] = 1
            
            # 이동할 수 있는지 확인            
            # 다음 칸이 이어져 있지 않으면 이동 불가
            for d in range(4):
                # 길이 안 나있으면 이동 불가
                if tunnel[matrix[ci][cj]][d] == 0:
                    continue
                ni, nj = ci + di[d], cj + dj[d]
                # 맵 밖이면 이동 못함
                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    continue
                # 벽이면 이동 불가
                if matrix[ni][nj] == 0:
                    continue             
                # 방문 했으면 이동 X
                if visited[ni][nj]:
                    continue
                # 터널이 이어져있지 않으면 이동 X (상 <> 하, 좌 <> 우)
                if tunnel[matrix[ni][nj]][(d+2)%4] == 0:
                    continue
                # 이동 가능하면 큐에 추가
                temp.append((ni, nj))
        for i, j in temp:
            queue.append((i, j))
            
    # pprint.pprint(visited)
    # 방문한 칸 개수 세기
    answer = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                answer += 1
    print(f"#{tc} {answer}")