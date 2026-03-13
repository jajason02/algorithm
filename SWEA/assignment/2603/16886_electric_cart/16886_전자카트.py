T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    E = [list(map(int, input().split())) for _ in range(N)]
    # 에너지 사용 최솟값

    min_e = float("inf")
    # 방문배열

    visited = [0] * N
    visited[0] = 1

    # now_room: 현재 위치한 방 번호
    # e: 현재까지 사용한 에너지 양
    def patrol(now_room, e):
        global min_e

        # 가지치기
        if e > min_e:
            return

        # 종료 조건
        # 방문 배열에 0이 없으면 최솟값 계산
        if 0 not in visited:
            e += E[now_room][0]
            min_e = min(e, min_e)
            return

        # 재귀
        for next_room in range(N):
            if not visited[next_room]:
                visited[next_room] = 1
                e_sum = E[now_room][next_room]
                patrol(next_room, e + e_sum)
                visited[next_room] = 0

    patrol(0, 0)

    print(f"#{tc} {min_e}")
