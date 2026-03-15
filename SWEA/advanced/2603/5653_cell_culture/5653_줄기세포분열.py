"""
나의 생각: 일단 시간개념이 있으니까 bfs로 가고싶은데...
AI 아이디어: 디지기 싫으면 힙으로 풀어라.
힙을 써야하는 이유: 배열의 크기가 무제한임.
아오 ㅈㄴ 어렵네
비활성 상태: 현재 시간 < 탄생 시간 + X(생명력)
활성 상태: 탄생시간 + X <= 현재시간 < 탄생 시간 + 2X
번식 타이밍: 현재 시간 == 탄생 시간 + X + 1
죽은 상태: 현재 시간 >= 탄생 시간 + 2X

"""


import heapq
# import sys

# sys.stdin = open("sample_input.txt", "r")

T = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    # pq: (발생시간, -생명력, r, c)
    # 초기 세포는 0초에 입력되지만, 활성화 및 번식은 생명력(X)에 의존함
    pq = []
    # cells: {(r, c): [생명력, 탄생시간]} -> 좌표 중복 체크 및 생존 계산용
    cells = {}

    # 행렬 입력 받기
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(M):
            if row[j] > 0:
                X = row[j]
                # 초기 상태: 0초에 존재, 생명력 X
                # (활성화 시간, -생명력, r, c) 순서로 힙에 삽입
                heapq.heappush(pq, (X, -X, i, j))
                cells[(i, j)] = [X, 0]

    # K시간 동안의 시뮬레이션 수행
    # 1초부터 K초까지 흐름에 따른 세포의 거동을 제어함
    for current_time in range(1, K + 1):
        # 이번 시간에 번식할 후보들 (동시간대 생명력 높은 놈 우선순위 때문)
        culture_cell = []

        # 현재 시간에 활성화되어 번식을 시작해야 하는 세포 추출
        while pq and pq[0][0] == current_time:
            time, neg_X, r, c = heapq.heappop(pq)
            X = -neg_X
            
            # 4방향 탐색 및 번식 시도
            for d in range(4):
                ni, nj = r + di[d], c + dj[d]
                if (ni, nj) not in cells:
                    # 번식 시점의 생명력 정보를 임시 저장하여 동시간대 충돌 방지
                    # 같은 좌표에 여러 세포가 올 수 있으므로 리스트로 관리 후 최댓값 선택
                    culture_cell.append((ni, nj, X))

        # 동시간대 번식 충돌 해결 (생명력 높은 순으로 정렬하여 점유)
        # 임마 이거 절대 내가 못만드는 로직
        culture_cell.sort(key=lambda x: x[2], reverse=True)
        
        for ni, nj, X in culture_cell:
            if (ni, nj) not in cells:
                # 새로운 세포 탄생 (탄생시간: current_time)
                cells[(ni, nj)] = [X, current_time]
                # 이 자식 세포가 활성화될 시간(현재시간 + X)을 예약
                # 단, K시간 이후에 활성화되는 놈은 굳이 힙에 넣을 필요 없음 (가지치기)
                if current_time + X < K:
                    heapq.heappush(pq, (current_time + X, -X, ni, nj))

    # 최종 생존 세포 카운트 (비활성 + 활성)
    live_count = 0
    for pos in cells:
        X, birth_time = cells[pos]
        # 세포의 총 수명: 비활성(X) + 활성(X) = 2X
        # 현재 시간(K)이 (탄생시간 + 2X)보다 작으면 아직 죽지 않은 상태임
        if birth_time + 2 * X > K:
            live_count += 1

    print(f"#{tc} {live_count}")