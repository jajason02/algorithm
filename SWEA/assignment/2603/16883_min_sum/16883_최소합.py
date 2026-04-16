"""
AI도움: 델타 값 자체가 왔던 길을 다시 돌아갈 수 없기 때문에 백트래킹, visited
배열을 사용 할 필요가 없다.
"""

T = int(input())

# 델타함수 정의
di = [1, 0]
dj = [0, 1]


# 행렬 범위 체크 함수
def border_check(i, j):
    if 0 <= i < N and 0 <= j < N:
        return 1
    return 0


# ci, cj: 현재 위치
# cur_sum: 현재까지의 합
def search(ci, cj, cur_sum):
    global min_sum

    # 가지치기
    if cur_sum > min_sum:
        return

    # 반대 꼭지점에 도착하면 최솟값 설정, 함수 리턴
    if (ci, cj) == (N - 1, N - 1):
        min_sum = min(cur_sum, min_sum)
        return

    # 델타 탐색, 재귀
    for d in range(2):
        ni = ci + di[d]
        nj = cj + dj[d]
        if border_check(ni, nj):
            search(ni, nj, cur_sum + matrix[ni][nj])


for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float("inf")

    # 최초 합을 matrix[0][0]으로 설정
    search(0, 0, matrix[0][0])

    print(f"#{tc} {min_sum}")
