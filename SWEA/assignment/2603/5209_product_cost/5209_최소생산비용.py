# import sys

# sys.stdin = open("sample.txt", "r")

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    selected = [0] * N
    min_cost = float("inf")

    def backtracking(idx, cost):
        global min_cost

        if cost > min_cost:
            return
        
        if idx == N:
            min_cost = min(min_cost, cost)
            return
        
        for j in range(N):
            if selected[j] == 0:
                selected[j] = 1
                backtracking(idx + 1, cost + matrix[idx][j])
                selected[j] = 0
        
    backtracking(0,0)
    print(f"#{tc} {min_cost}")