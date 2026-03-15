"""
나의 생각: A형 시험 날 풀었던 코드가 왜 안되었는지 집중적으로 질문하고자 했다
dfs와 백트래킹으로 구현하고자 했고 전선이 가는 길을 넣고 빼는 부분에서
실수가 났을 가능성이 높을 것 같다
AI 도움: 진짜 다 구현했는데 완료조건이랑 연결이 되지 않았을 때 다음 재귀 실행
부분에서 틀렸음 하 ㅅㅂ
전선을 깔고 지우는 과정에서 while문을 사용하는 것도 좋은 방법인 것 같다
"""


# import sys

# sys.stdin = open("sample_input.txt", "r")

T = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 코어의 위치 저장
    cores = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if matrix[i][j] == 1:
                cores.append((i, j))

    # max_cnt: 전원이 연결된 코어의 수 최댓값
    # min_wire: 전선의 길이 최솟값
    # cnt_cores: 코어의 갯수
    max_cnt = 0
    min_wire = float('inf')
    cnt_cores = len(cores)

    def dfs(core_idx, connected_cnt, curr_len):
        """
        :param core_idx: 현재 탐색 중인 코어의 인덱스
        :param connected_cnt: 현재까지 연결된 코어의 수
        :param current_len: 현재까지 가설된 전선의 총 길이
        """
        global max_cnt, min_wire

        # Pruning (가지치기): 남은 코어를 다 연결해도 현재 최댓값보다 작으면 중단
        if connected_cnt + (cnt_cores - core_idx) < max_cnt:
            return

        # 모든 코어 탐색 완료 시 결과 갱신
        if core_idx == cnt_cores:
            # 연결된 코어의 수가 max보다 클 때 전선의 길이, 코어의 수갱신
            if connected_cnt > max_cnt:
                max_cnt = connected_cnt
                min_wire = curr_len
            # 연결된 코어의 수가 같을 때 전선의 길이 최솟값 갱신
            # 여기 elif 넣는 것도 틀림
            elif connected_cnt == max_cnt:
                min_wire = min(min_wire, curr_len)
            return

        ci, cj = cores[core_idx]

        # 델타탐색
        for d in range(4):
            can_connect = True
            wire_len = 0
            
            # 1. 전선을 깔 수 있는지 검증 (Check)
            ni, nj = ci + di[d], cj + dj[d]
            while 0 <= ni < N and 0 <= nj < N:
                if matrix[ni][nj] != 0:
                    can_connect = False
                    break
                # 벽에 닿을 때 까지 반복
                ni += di[d]
                nj += dj[d]
                wire_len += 1

            # 2. 연결 가능하다면 전선 배치 후 다음 단계로 진행
            if can_connect:
                # 전선 가설 (2로 표시)
                ri, rj = ci + di[d], cj + dj[d]
                for _ in range(wire_len):
                    matrix[ri][rj] = 2
                    ri += di[d]
                    rj += dj[d]
                
                # 재귀 실행(코어 인덱스 + 1, 연결된 코어 수 + 1, 전선 길이 + 추가 길이)
                dfs(core_idx + 1, connected_cnt + 1, curr_len + wire_len)
                
                # 3. 백트래킹: 가설했던 전선 제거 (Rollback)
                ri, rj = ci + di[d], cj + dj[d]
                for _ in range(wire_len):
                    matrix[ri][rj] = 0
                    ri += di[d]
                    rj += dj[d]
            
        # 4. 해당 코어를 연결하지 않고 넘어가는 경우도 탐색
        # 이 새끼 위치땜에 틀린듯
        dfs(core_idx + 1, connected_cnt, curr_len)

    dfs(0, 0, 0)
    print(f"#{tc} {min_wire}")