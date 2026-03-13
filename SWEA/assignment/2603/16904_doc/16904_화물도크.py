import sys

sys.stdin = open("sample_input(1).txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    work_list = [list(map(int, input().split())) for _ in range(N)]

    work_list.sort(key=lambda x: x[1])
    print(work_list)
    count = 0

    last_end = 0

    for start, end in work_list:
        if start >= last_end:
            count += 1
            last_end = end

    print(f"#{tc} {count}")