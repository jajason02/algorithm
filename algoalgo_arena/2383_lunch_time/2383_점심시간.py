"""
나의 생각: 각각의 계단으로 들어가는 사람들을 재귀로 조합을 나누고, 
각 조합마다 계단을 모두 내려가는 경우를 구현하여 시뮬레이션을 돌린다
AI 도움: 계단을 내려가는데 걸리는 시간만 있으면 구현할 수 있다.
사람의 개인의 인덱스는 넣을 필요가 없다.
while 탈출 조건은 다 내려온 사람 수를 세어 리스트 길이와 같아질 때
"""



import sys
from collections import deque

sys.stdin = open("small.txt", "r")

T = int(input())


def stair_select(idx):
    if idx == len(people):
        solve()
        return
    for n in range(2):
        selected[idx] = n
        stair_select(idx + 1)


def move_time(tup, idx):
    return abs(tup[0] - stair[idx][0]) + abs(tup[1] - stair[idx][1])


def solve():
    global ans

    stair_1 = []
    stair_2 = []
    # 계단 별로 사람들이 도착하는데 걸리는 시간 리스트에 넣고 오름차순 정렬
    # 사람이 누구인지에 대한 인덱스 필요없음
    for n in range(len(people)):
        if selected[n] == 0:
            stair_1.append((move_time(people[n], 0)))
        elif selected[n] == 1:
            stair_2.append((move_time(people[n], 1)))

    stair_1.sort()
    stair_2.sort()
    print(stair_1)
    
    def finish_time(arrival, stair_length):
        if not arrival:
            return 0

        # 지금이순간
        time = 0
        # 다 내려온 새끼 대갈수
        complete_cnt = 0
        # 계단 내부 인원의 완료 예정 시간
        on_stair = deque()
        # 대기중인 사람 인덱스(도착 시간 오름차순이라 순서대로 계단에 넣으면 됨)
        wait_idx = 0

        while complete_cnt < len(arrival):
            time += 1

            # 탈출 조건. 큐에 값이 있고 그 값이 현재 시간과 같으면 팝
            while on_stair and on_stair[0] == time:
                on_stair.popleft()
                complete_cnt += 1

            # 대기 인원 진입 처리(계단 안에 3명 이하)
            while len(on_stair) < 3 and wait_idx < len(arrival):
                if time >= arrival[wait_idx] + 1:
                    # 계단 큐에 사람 집어넣기
                    on_stair.append(time + stair_length)
                    wait_idx += 1
                else:
                    break

        return time

    time_1 = finish_time(stair_1, stair[0][2])
    time_2 = finish_time(stair_2, stair[1][2])

    current_max = max(time_1, time_2)

    if current_max < ans:
        ans = current_max


for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stair = []

    ans = float("inf")

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                people.append((i, j))
            elif matrix[i][j] > 1:
                stair.append((i, j, matrix[i][j]))
    selected = [0] * len(people)

    stair_select(0)

    print(f"#{tc} {ans}")
