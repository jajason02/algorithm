"""
나의 생각: 함수의 인자를 month(달), total_cost(현재 가격 합)으로 놓고 dfs.
종료 조건은 month >= 12로 하고 이 때, 최솟값을 갱신하는 형식으로 해보자.
AI 도움: 이미 최솟값보다 현재 합이 크면 가지치기 하기. global 변수 취하기.(걍 실수임)
"""

# import sys

# sys.stdin = open("sample_input.txt", "r")


# dfs 구현
def dfs(month, total_cost):
    global min_cost

    # 가지치기
    if total_cost > min_cost:
        return
    
    # month가 12보다 커지면 최솟값 비교 후 갱신
    if month >= 12:
        if min_cost > total_cost:
            min_cost = total_cost
        return
    
    # 재귀 함수 구현 이번 달에 수영장 갈 계획이 있을 때.
    if plan_lst[month] != 0:
        # 회원권 고르기 (각각 1일, 1달, 3달)
        for plan in range(3):
            # 1일권이면 한 달 동안 가는 횟수를 곱해서 다음 달로 재귀 실행
            if plan == 0:
                next_cost = total_cost + plan_lst[month] * charge_lst[plan]
                dfs(month + 1, next_cost)
            # 1달권이면 1달 후로 재귀 실행
            elif plan == 1:
                next_cost = total_cost + charge_lst[plan]
                dfs(month + 1, next_cost)
            # 3달권 이면 3달 후로 재귀 실행
            elif plan == 2:
                next_cost = total_cost + charge_lst[plan]
                dfs(month + 3, next_cost)
    # 이번 달 수영장 안가면 month + 1 해서 재귀 실행
    else:
        dfs(month + 1, total_cost)

T = int(input())

for tc in range(1, T+1):
    charge_lst = list(map(int, input().split()))
    plan_lst = list(map(int, input().split()))
    
    # 최솟값을 1년권 가격으로 지정
    min_cost = charge_lst[3]
    dfs(0, 0)
    print(f"#{tc} {min_cost}")