from collections import deque


N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
cnt = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    lst[A].append(B)
    cnt[B] += 1

answer = [0] * (N + 1)

dq = deque()
for t in range(1, N + 1):
    for i in range(N + 1):
        if cnt[i] == 0 and not answer[i]:
            dq.append(i)
    while dq:
        n = dq.popleft()
        answer[n] = t
        for m in lst[n]:
            cnt[m] -= 1
for n in answer[1:]:
    print(n, end=" ")


