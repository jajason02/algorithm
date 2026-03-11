import sys

sys.stdin = open("sample.txt", "r")

T = int(input())

def mergesort(start, end):

    if start == end - 1:
        return start, end
    mid = (start + end) // 2

    left_s, left_e = mergesort(start, mid)
    right_s, right_e = mergesort(mid, end)

    merge(left_s, left_e, right_s, right_e)

    return start, end

def merge(left_s, left_e, right_s, right_e):
    global count
    l = left_s
    r = right_s
    n = right_e - left_s
    idx = 0
    result = [0] * n

    # if lst[left_e-1] > lst[right_e-1]:
    #     count += 1

    while l < left_e and r < right_e:
        if lst[l] > lst[r]:
            result[idx] = lst[r]
            r += 1
            idx += 1
        else:
            result[idx] = lst[l]
            l += 1
            idx += 1

    while l < left_e:
        result[idx] = lst[l]
        l += 1
        idx += 1

    while r < right_e:
        result[idx] = lst[r]
        r += 1
        idx += 1

    for i in range(n):
        lst[left_s + i] = result[i]
    



for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    count = 0
    mergesort(0, N)

    print(f"#{tc} {lst[N//2]} {count}")