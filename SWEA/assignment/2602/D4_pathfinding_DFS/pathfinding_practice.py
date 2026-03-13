import sys

sys.stdin = open("input.txt", "r")

T = 10

def dfs(s):
    if s == 99:
        return 1

    stack = [0] * 100
    stack[s] = 1
    for next in node.get(s, []):
        if not stack[next]:
            if dfs(next):
                return 1
    return 0        


    

for tc in range(1, T+1):

    N, V = map(int, input().split())

    node = {}
    path = list(map(int, input().split()))
    # print(N, V)
    # print(path)

    for n in range(V):
        i, j = path[2 * n], path[2 * n + 1]
        if i not in node:
            node[i] = [j]
        else:
            node[i].append(j)
    # print(node)

    answer = dfs(0)
    print(f'#{tc} {answer}')