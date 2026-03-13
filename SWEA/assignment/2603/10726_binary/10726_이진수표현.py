T = int(input())

for tc in range(1, T + 1):
    N , M = map(int, input().split())

    for n in range(N):
        if M & (1 << n) == 0:
            answer = "OFF"
            break
    else:
        answer = "ON"

    print(f"#{tc} {answer}")