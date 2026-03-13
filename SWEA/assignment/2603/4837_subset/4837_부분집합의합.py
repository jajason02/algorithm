import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

def comb(cnt, selected, start):
    global count

    if cnt == N:
        if sum(selected) == K:
            count += 1
        return
    
    for i in range(start, 12):
        comb(cnt + 1, selected + [A[i]], i + 1)



for tc in range(1, T+1):
    N, K = map(int, input().split())

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    count = 0

    comb(0, [], 0)
    
    print(f"#{tc} {count}")
