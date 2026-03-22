import sys
from collections import deque

sys.stdin = open("sample.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    # N: 접수 창구 수, M: 정비 창구 수, K: 고객 수
    # A: 찾고자 하는 접수 창구 번호, B: 찾고자 하는 정비 창구 번호
    N, M, K, A, B = map(int, input().split())
    
    # ai: 각 접수 창구별 처리 소요 시간 (List)
    ai = list(map(int, input().split()))
    # bj: 각 정비 창구별 처리 소요 시간 (List)
    bj = list(map(int, input().split()))
    # tk: 각 고객별 정비소 도착 시간 (List)
    tk = list(map(int, input().split()))
    
    # 각 창구의 현재 상태를 저장하는 리스트 (구조: [잔여시간, 고객번호])
    reception_status = [[0, -1] for _ in range(N)]
    repair_status = [[0, -1] for _ in range(M)]
    
    # 고객들의 이용 창구 기록 (1번 고객부터 K번 고객까지)
    # customer_log[고객번호] = [이용한 접수창구 번호, 이용한 정비창구 번호]
    customer_log = [[0, 0] for _ in range(K + 1)]
    
    wait_reception = deque() # 접수 대기열
    wait_repair = deque()    # 정비 대기열
    
    current_time = 0
    finished_customers = 0
    arrived_idx = 0
    
    # 모든 고객의 정비가 완료될 때까지 반복 시행
    while finished_customers < K:
        # 1. 고객 도착 처리: 현재 시간(current_time)에 도착한 고객을 접수 대기열에 추가
        while arrived_idx < K and tk[arrived_idx] <= current_time:
            wait_reception.append(arrived_idx + 1) # 고객 번호는 1부터 시작
            arrived_idx += 1
        
        # 2. 접수 창구 시뮬레이션
        for i in range(N):
            # 작업 중인 창구의 잔여 시간 감소
            if reception_status[i][0] > 0:
                reception_status[i][0] -= 1
            
            # 작업이 완료된 경우
            if reception_status[i][0] == 0:
                # 완료된 고객이 있다면 정비 대기열로 인계
                if reception_status[i][1] != -1:
                    wait_repair.append(reception_status[i][1])
                    reception_status[i][1] = -1
                
                # 대기 고객이 있다면 빈 창구에 배치
                if wait_reception:
                    target_customer = wait_reception.popleft()
                    reception_status[i] = [ai[i], target_customer]
                    customer_log[target_customer][0] = i + 1 # 창구 번호 기록
        
        # 3. 정비 창구 시뮬레이션
        for j in range(M):
            # 작업 중인 창구의 잔여 시간 감소
            if repair_status[j][0] > 0:
                repair_status[j][0] -= 1
            
            # 작업이 완료된 경우
            if repair_status[j][0] == 0:
                # 정비 완료 처리
                if repair_status[j][1] != -1:
                    finished_customers += 1
                    repair_status[j][1] = -1
                
                # 정비 대기 고객 배치 (접수 완료 순서대로 wait_repair에 삽입됨)
                if wait_repair:
                    target_customer = wait_repair.popleft()
                    repair_status[j] = [bj[j], target_customer]
                    customer_log[target_customer][1] = j + 1 # 창구 번호 기록
        
        current_time += 1
        
    # 결과 산출: 지정된 A번 접수 창구와 B번 정비 창구를 모두 이용한 고객 번호 합산
    ans = 0
    for p in range(1, K + 1):
        if customer_log[p][0] == A and customer_log[p][1] == B:
            ans += p
    
    print(f"#{tc} {ans if ans != 0 else -1}")