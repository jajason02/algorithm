import sys
import heapq

sys.stdin = open("sample_input.txt", "r")

T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    t = 1
    pq = []
    cell = {}
    for i in range(N):
        for j in range(M):
            if matrix[i][j] > 0:
                heapq.heappush(pq, (matrix[i][j], -matrix[i][j], i, j))
                cell[(i, j)] = (0, matrix[i][j])

    for curr_time in range(1, K+1):
        temp = []

        while pq and pq[0][0] == curr_time:
            time, neg_X, ci, cj = heapq.heappop(pq)
            X = -neg_X
            for d in range(4):
                ni = ci + di[d]
                nj = cj + dj[d]
                if (ni, nj) not in cell:
                    temp.append(( X, ni, nj))

        temp.sort(key=lambda x: x[1], reverse=True)
        for X, ni, nj, in temp:
            if (ni, nj) not in cell:
                cell[(ni, nj)] = (curr_time + X, X)
                heapq.heappush(pq, (curr_time + X + 1, -X, ni, nj))
    
    live_count = 0

    for pos in cell:
        birth_time, X = cell[pos]
        if birth_time + 2 * X > K:
            live_count += 1
    print(live_count)
        
