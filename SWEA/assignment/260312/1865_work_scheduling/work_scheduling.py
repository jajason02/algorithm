# import sys

# sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 최댓값을 저장하는 변수 max_prob
    # 이미 작업을 한 직원의 인덱스를 selected에 저장
    max_prob = 0
    selected = [0] * N

    # 백트래킹 함수
    def backtracking(idx, prob):
        global max_prob

        # 이미 확률이 최댓값보다 작으면 가지치기
        if prob < max_prob:
            return

        # 종료조건, 최댓값 갱신
        if idx == N:
            max_prob = max(max_prob, prob)

        # 아직 작업을 하지 않은 작업자를 찾아 재귀, 백트래킹 실시
        for j in range(N):
            if not selected[j] and matrix[idx][j] != 0:
                selected[j] = 1
                backtracking(idx + 1, prob * matrix[idx][j] / 100)
                selected[j] = 0

    # 최초값이 왜 100이여 샹
    backtracking(0, 100)
    print(f"#{tc} {max_prob:.6f}")