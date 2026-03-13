import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

def check_way():
    if (location + K) <= N - 1 :
        for n in range(location + K, location, -1):
            if pond_lst[n] == 1:
                return 1
    return 0

for tc in range (1, T + 1):
    N, K = map(int, input().split())
    pond_lst = list(map(int, input().split()))

    location = -1

    while check_way():
        for i in range(location + K, location, -1):
            if pond_lst[i] == 1:
                location = i
                break
        else:
            if i + K <= N - 1:
                location = i + K
            else:
                location = N
    if i + K <= N - 1:
        location = i + K + 1
    else:
        location = N

    print(f"#{tc} {location}")

    