T = int(input())

def dfs(current, goal):                     # dfs 구현
    if current == goal:                     # 다 확인 시 종료
        return 1
    stack[current] = True
    for next in graph.get(current, []):     # 다음 노드 탐색
        if not stack[next]:                 # stack에 없을 때 다음 노드에서 dfs 실시
            if dfs(next, goal):             # 재귀. 다음 노드의 값을 return
                return 1
    return 0

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = {}                              # 노드가 이어진 정보를 딕셔너리에 저장

    for _ in range(E):                      # 딕셔너리에 노드 정보 입력
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

    S, G = map(int, input().split())
    stack = [0] * (V + 1)                   # stack 정의
    answer = dfs(S,G)                       # 함수 실행

    print(f'#{tc} {answer}')