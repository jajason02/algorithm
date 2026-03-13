# import sys

# sys.stdin = open("sample_input.txt", "r")

T = int(input())


def backtracking(idx, score, cal):
    global max_score

    if cal >= L:
        return
    if idx == N:
        max_score = max(score, max_score)
        return
    for n in range(2):
        if n == 0:
            backtracking(idx + 1, score + layer[idx][0], cal + layer[idx][1])
        else:
            backtracking(idx + 1, score, cal)


for tc in range(1, T + 1):
    N, L = map(int, input().split())
    layer = []
    for i in range(N):
        layer.append(list(map(int, input().split())))

    max_score = 0
    backtracking(0, 0, 0)
    print(f"#{tc} {max_score}")
