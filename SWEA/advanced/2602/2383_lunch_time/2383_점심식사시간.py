"""
나의 아이디어: 일단 탐색을 할 필요는 없어보인다.
사람들을 계단 줄을 세우는 방법과 순서를 고려하는 로직으로

AI 아이디어: 탐색 안하면 죽인다고함. 사람들이 각각 어느 계단을 선택하는지,
그 계단을 선택했을 때 계단 입구까지 도착하는 시간을 구해서 최적을 찾아라고 도움받음.
함수 두개를 연계해서 사용할 수 있는 아이디어 받았음. 사실상 내가 한게 거의 없는 것 같다.

"""
T = int(input())


def get_time(arrival_times, stair_len):                     # 완료 시간 구하는 함수
    if not arrival_times:
        return 0
        
    exit_times = []                                         # 계단에 들어간 사람들이 언제 나가는지 기록하는 리스트 (최대 3명 유지)

    for arrival in arrival_times:
        start_time = arrival + 1                            # 계단 입구 도착 후 1분 뒤부터 들어갈 수 있음
        if len(exit_times) >= 3:                            # 만약 계단에 이미 3명이 있으면 나갈 때 까지 기다림
            first_out = exit_times.pop(0)
            if start_time < first_out:
                start_time = first_out
        exit_times.append(start_time + stair_len)           # 내가 계단을 다 내려가는 시간 = 진입 시간 + 계단 길이                               
    return exit_times[-1]                                   # 마지막 사람이 나가는 시간이 이 계단의 최종 완료 시간


def people_div(i):                                          # 사람이 나가는 계단을 설정하는 함수
    global min_ans
    if i == len(people):                                    # 사람 나누기가 끝났을 때 실행
        stair0_arrivals = []                                # 계단별 도착 시간 리스트 생성
        stair1_arrivals = []

        for p_idx in range(len(people)):                    # p_idx번째 사람이 선택한 계단 정보
            s_idx = match[p_idx]                            # 문제에서 준 거리 구하기 공식에 대입
            dist = abs(people[p_idx][0] - stair[s_idx][0]) + abs(people[p_idx][1] - stair[s_idx][1])
            if s_idx == 0:                                  # 계단까지의 거리 값을 계단별 도착 시간 리스트에 삽입
                stair0_arrivals.append(dist)
            else:
                stair1_arrivals.append(dist)

        stair0_arrivals.sort()                              # 도착 시간을 오름차순으로 정렬
        stair1_arrivals.sort()

        time0 = get_time(stair0_arrivals, stair[0][2])      # 다 내려가는 시간을 계산하는 함수
        time1 = get_time(stair1_arrivals, stair[1][2])

        min_ans = min(min_ans, max(time0, time1))           # 두 계단을 모두 내려가는 최솟값 찾기
        return
    match[i] = 0                                            # 재귀를 통해 사람을 계단에 배치
    people_div(i + 1)

    match[i] = 1
    people_div(i + 1)


for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    people = []                                             # 사람의 좌표 리스트
    stair = []                                              # 계단의 좌표 리스트
    for i in range(N):                                      # 사람의 좌표 구하는 반복문
        for j in range(N):
            if matrix[i][j] == 1:
                people.append([i, j])
            elif matrix[i][j] != 0:
                stair.append([i, j, matrix[i][j]])
    match = [0] * len(people)                               # 사람 별로 선택한 계단 리스트
    min_ans = float("inf")                                  
    people_div(0)                                   

    print(f"#{tc} {min_ans}")
