import sys
sys.stdin = open("sample.txt", "r")

from heapq import heappop, heappush

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 초기 세포 정보 힙큐에 저장 분열 시 pop
    pq_cell = []
    # 세포의 위치, 생존력, 생일 저장. 죽으면 pop
    hash_cell = {}
    for i in range(N):
        for j in range(M):
            if matrix[i][j] > 0:
                # 활성화 시간, -생명력(생명력이 큰 순서대로 정렬), 좌표 순으로 정렬
                heappush(pq_cell, [matrix[i][j] + 1, -matrix[i][j], i, j])
                # 딕셔너리에 (좌표) : [생명력, 탄생시간]으로 저장
                hash_cell[(i, j)] = [matrix[i][j],1]
    # print(hash_cell)
    # print(pq_cell)
    # K 시간동안 세포 키우기
    for curr_t in range(1, K + 1):
        # 이번 시간에 분열할 세포 리스트
        culture_lst = []
        # 활성화 된 세포는 분열
        while pq_cell and pq_cell[0][0] == curr_t:
            # activ_t: 활성화 시간    power: 생명력    ci, cj: 세포 위치 
            activ_t, temp, ci, cj = heappop(pq_cell)
            power = -temp            
            # 4방향으로 분열
            for d in range(4):
                # 분열할 세포 먼저 저장
                ni, nj = ci + di[d], cj + dj[d]
                if (ni, nj) not in hash_cell:
                    culture_lst.append((power, ni, nj))
        # 분열하는 세포가 한 칸에 두개인 경우 생명력이 큰 세포가 분열
        culture_lst.sort(reverse=True)
        for x, i, j in culture_lst:
            if (i, j) not in hash_cell:
                hash_cell[(i, j)] = [x, curr_t]
                heappush(pq_cell, [curr_t + x + 1, -x, i, j])
        
    # k시간 후 살아있는 세포 카운팅
    ans = 0
    for lst in hash_cell.values():
        # (세포가 태어난 시간 + 2 * 생명력) 이 지나면 죽는다
        if (lst[0]*2 + lst[1]) > K:
            ans += 1
    print(f'#{tc} {ans}')

