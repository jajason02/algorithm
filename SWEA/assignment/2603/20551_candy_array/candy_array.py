import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    A, B, C = map(int, input().split())

    if B < 2 or C < 3:
        print(f"#{tc} -1")
        continue

    eat_count = 0

    if B >= C:
        eat_count += B - (C - 1)
        B = C - 1

    if A >= B:
        eat_count += A - (B - 1)
        A = B - 1

    print(f"#{tc} {eat_count}")
