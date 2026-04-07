# import sys
# sys.stdin = open("sample.txt", "r")

T = int(input())

def make_set(x):
    p[x] = x

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    king_x = find_set(x)
    king_y = find_set(y)

    if rank[king_x] > rank[king_y]:
        p[king_y] = king_x
    else:
        p[king_x] = king_y

        if rank[king_x] == rank[king_y]:
            rank[king_y] += 1


for tc in range(1, T+1):
    N , M = map(int, input().split())
    lst = list(map(int, input().split()))
    
    p = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    for i in range(0, len(lst), 2):
        a, b = lst[i], lst[i + 1]
        union(a, b)
    
    group_count = 0
    for i in range(1, N + 1):
        if p[i] == i:
            group_count += 1

    print(f"#{tc} {group_count}")