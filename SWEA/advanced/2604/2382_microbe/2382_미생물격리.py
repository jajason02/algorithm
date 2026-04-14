# import sys
# sys.stdin = open("sample_input.txt", "r")

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 입력값 방향(1~4)을 우리가 정한 인덱스(0~3)로 변환
d_map = {1: 0, 2: 2, 3: 3, 4: 1}

T = int(input())

for tc in range(1, T + 1):
    # N: 격자 크기, M: 격리 시간, K: 미생물 군집 수
    N, M, K = map(int, input().split())
    
    # micros 리스트: [r, c, count, dir]
    micros = []
    for _ in range(K):
        r, c, cnt, d = map(int, input().split())
        micros.append([r, c, cnt, d_map[d]])

    # M시간 동안 시뮬레이션 진행
    for _ in range(M):
        grid = {} # (r, c)를 키로 하고 [미생물 정보들]을 값으로 갖는 딕셔너리
        
        # 모든 군집 이동
        for i in range(len(micros)):
            r, c, cnt, d = micros[i]
            if cnt == 0: continue # 이미 소멸한 군집은 건너뜀
            
            nr, nc = r + di[d], c + dj[d]
            
            # 약품 구역(경계선)에 도달했는지 확인
            if nr == 0 or nr == N - 1 or nc == 0 or nc == N - 1:
                cnt //= 2
                d = (d + 2) % 4 # 방향 반대로 전환
            
            # 이동 후 미생물이 살아있다면 grid에 기록
            if cnt > 0:
                if (nr, nc) not in grid:
                    grid[(nr, nc)] = []
                grid[(nr, nc)].append([cnt, d])
            
            # 현재 군집 정보 일단 업데이트
            micros[i] = [nr, nc, cnt, d]

        # 같은 위치에 모인 군집들 병합 처리
        new_micros = []
        for pos, group in grid.items():
            if len(group) > 1:
                # 내림차순 정렬하여 0번째의 방향을 선택
                group.sort(key=lambda x: x[0], reverse=True)
                total_sum = sum(g[0] for g in group)
                final_dir = group[0][1]
                new_micros.append([pos[0], pos[1], total_sum, final_dir])
            else:
                # 군집이 하나뿐이면 그대로 유지
                new_micros.append([pos[0], pos[1], group[0][0], group[0][1]])
        
        # 다음 턴을 위해 리스트 교체
        micros = new_micros

    # 남은 모든 미생물의 합
    ans = sum(m[2] for m in micros)
    print(f"#{tc} {ans}")