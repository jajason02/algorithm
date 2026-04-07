import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    houses = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:              
                houses.append((i, j))

    max_house = 0

    for i in range(N):
        for j in range(N):
            for k in range(1, N + 2):
                service_house = 0
                security_charge = k * k + (k - 1) * (k - 1)
                for hi, hj in houses:
                    if abs(hi - i) + abs(hj - j) < k:
                        service_house += 1
                if security_charge <= M * service_house:
                    max_house = max(max_house, service_house)

    print(f"#{tc} {max_house}")
