T = int(input())


def comb(cnt, sub, start):
    global count

    if cnt == N:
        if sum(sub) == K:
            count += 1
        return
    
    for i in range(start, 12):
        comb(cnt + 1, sub + [a[i]], start + 1)

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    count = 0
    
    comb(0, [], 0)
    print(f"#{tc} {count}")

