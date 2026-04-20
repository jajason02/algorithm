"""
union-find로 앉고싶은 쌍을 같은 집합으로 만들어 준다.
"""
import sys
sys.stdin = open("sample.txt", "r")

T = int(input())

def find(x):
    if x != p[x]:
        # p[x]를 모두 갱신
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    root_x, root_y = find(x), find(y)
    if root_x == root_y:
        return False
    elif rank[root_x] > rank[root_y]:
        p[root_y] = root_x
    elif rank[root_y] > rank[root_x]:
        p[root_x] = root_y
    else:
        p[root_y] = root_x
        rank[root_x] += 1

for tc in range(1, T+1):
    # N: 출석번호 수, M: 신청서 수
    N, M = map(int, input().split())
    applications = list(map(int, input().split()))
    # p[x] = x 학생의 뿌리, rank[x]: x학생이 루트인 트리의 높이
    p = [i for i in range(N + 1)]
    rank = [0] * (N + 1)

    # 조 만들기
    for m in range(M):
        union(applications[2*m], applications[2*m + 1])
    # 개선판
    # for i in range(0, M, 2):
    #     union(applications[i], applications[i+1])

    ans = 0
    for x in range(1, N+1):
        if x == p[x]:
            ans += 1
    print(f'#{tc} {ans}')
    
    # 0을 뺀다는 생각으로 했는데 p 리스트는 0이 나올 수 있기 때문에
    # 무조건 0을 제거하면 1이 모자라서 틀리는 경우가 있음
    # set_p = set(p)
    # print(f'#{tc} {len(set(p))-1}')
