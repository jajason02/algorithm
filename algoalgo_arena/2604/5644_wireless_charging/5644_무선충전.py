import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

dy = [0, -1, 0, 1, 0]
dx = [0, 0, 1, 0, -1]

def is_charge(x, y, charger_num):
    cx, cy, C, P = charger[charger_num]
    D = abs(x - cx) + abs(y - cy)
    if D <= C:
        return 1
    return 0

for tc in range(1, T+1):
    M, A = map(int, input().split())

    a_route = list(map(int, input().split()))
    b_route = list(map(int, input().split()))
    charger = []
    for _ in range(A):
        charger.append(list(map(int, input().split())))
    print(charger)
    a_grid = [1,1]
    b_grid = [10, 10]
    sum_charge = 0

    

    
        
    # M번 반복
    for m in range(M+1):
        a_charger = []
        b_charger = []
        # 충전 확인
        for ch_num in range(A):
            ax, ay = a_grid
            if is_charge(ax, ay, ch_num):
                a_charger.append(ch_num)
            bx, by = b_grid
            if is_charge(bx, by, ch_num):
                b_charger.append(ch_num)
        # 충전 안하면 continue
        if not a_charger and not b_charger:
            continue
        # 하나만 충전 되면 하나만 충전
        if a_charger and not b_charger:
            # 연결된 충전기가 1개 이상일 때 최대 충전량
            if len(a_charger) > 1:
                max_p = 0
                for i in range(len(a_charger)):
                    max_p=max(charger[a_charger[i]][3], max_p)
                sum_charge += max_p
            else:
                sum_charge += charger[a_charger[0]][3]

        if b_charger and not a_charger:
            # 연결된 충전기가 1개 이상일 때 최대 충전량
            if len(b_charger) > 1:
                max_p = 0
                for i in range(len(b_charger)):
                    max_p=max(charger[b_charger[i]][3], max_p)
                sum_charge += max_p
            else:
                sum_charge += charger[a_charger[0]][3]

        # 둘다 충전 될 때
        # 둘 다 같은 충전기
        if len(a_charger) == 1 and len(b_charger) == 1 and a_charger[0] == b_charger[0]:
            sum_charge += charger[a_charger][3]
        # 둘 다 다른 충전기
            # 연결된 충전기가 1개 이상일 때 최대 충전량
        if len(a_charger) > 1:
            max_p = 0
            for i in range(len(a_charger)):
                max(charger[a_charger[i]][3], max_p)
            sum_charge += max_p
        else:
            sum_charge += charger[a_charger[0]][3]
            # 연결된 충전기가 1개 이상일 때 최대 충전량
        if len(b_charger) > 1:
            max_p = 0
            for i in range(len(b_charger)):
                max(charger[b_charger[i]][3], max_p)
            sum_charge += max_p
        else:
            sum_charge += charger[a_charger[0]][3]
        # 겹치는칸 충전기 쓰면 둘 다 쓰게 하기

        # 델타 이동하기
        if m < M + 1:
            a_grid[0] = a_grid[0] + dx[a_route[m]]
            a_grid[1] = a_grid[1] + dy[a_route[m]]
            b_grid[0] = b_grid[0] + dx[b_route[m]]
            b_grid[1] = b_grid[1] + dy[b_route[m]]
        
            