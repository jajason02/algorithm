"""
나의 아이디어: 일단 움직이는 방향과 같게 델타 배열을 생성한다.
재귀를 사용하는 문제는 아니라 판단하고 구현을 시작했다.
M만큼 반복하는 for문을 생성해 문제를 해결해보자.

AI 아이디어: 10x10 행렬을 만들지 말고 시간별로 문제에서 주어진
거리를 구하는 식을 사용해 충전을 할 수 있는지를 판단하라는 아이디어를 얻음.
각 time마다 a, b에서 갈 수 있는 충전소를 리스트에 저장하는 방식으로
충전소가 겹치는 경우에서 최적을 찾는 방법을 도움받았다.
충전소를 찾지 못한 경우 충전 가능 리스트에 -1을 넣는 아이디어를 받았다.
"""

T = int(input())

di = [0, -1, 0, 1, 0]                               # 델타 행렬
dj = [0, 0, 1, 0, -1]

for tc in range(1, T + 1):
    M, A = map(int, input().split())
    a_route = list(map(int, input().split()))
    b_route = list(map(int, input().split()))
    bc_info = []
    for _ in range(A):
        lst = list(map(int, input().split()))
        bc_info.append(lst)
    a_location = [1, 1]                             # a 시작 위치
    b_location = [10, 10]                           # b 시작 위치
    charge_sum = 0

    for time in range(M + 1):                       # M만큼 반복(시작 위치부터 충전 가능 여부 파악)
        a_possible = []                             # time 별로 a, b 위치에서 가능한 충전기 파악
        b_possible = []
        max_current = 0                             # 이번 time에서 할 수 있는 최대 충전량
        for n in range(A):                          # 문제에서 주어진 거리 공식을 사용해 가능한 충전기 번호 탐색
            if (
                abs(a_location[0] - bc_info[n][0]) + abs(a_location[1] - bc_info[n][1])
                <= bc_info[n][2]
            ):
                a_possible.append(n)                # 가능한 충전기가 있으면 그 충전기 번호를 리스트에 추가
            if (
                abs(b_location[0] - bc_info[n][0]) + abs(b_location[1] - bc_info[n][1])
                <= bc_info[n][2]
            ):
                b_possible.append(n)                # 가능한 충전기가 있으면 그 충전기 번호를 리스트에 추가
        if not a_possible:                          # 가능한 충전기가 없으면 리스트에 -1 입력
            a_possible.append(-1)                 
        if not b_possible:
            b_possible.append(-1)
        for a_idx in a_possible:                    # 가능한 충전기 숫자 리스트 이중 for문으로 경우의 수 파악
            for b_idx in b_possible:
                total = 0
                if a_idx == b_idx:                  # 둘이 같은 충전기를 사용하면 그 충전기 하나의 충전량만 total에 저장
                    if a_idx != -1:
                        total = bc_info[a_idx][3]
                else:
                    if a_idx != -1:                 # 둘이 다른 충전기를 사용하면 각각의 충전량을 total에 저장
                        total += bc_info[a_idx][3]
                    if b_idx != -1:
                        total += bc_info[b_idx][3]
                max_current = max(max_current, total)   # 최댓값 찾기 비교
        charge_sum += max_current

        if time < M:                                # 다음 time으로 이동. 좌표 변경
            a_location[0] += dj[a_route[time]]
            a_location[1] += di[a_route[time]]
            b_location[0] += dj[b_route[time]]
            b_location[1] += di[b_route[time]]

    print(f"#{tc} {charge_sum}")
